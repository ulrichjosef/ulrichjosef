#!/usr/bin/env python3
"""
SGC_PLAT-CPL v1.0 - Moteur de fusion bayesienne + Plackett-Luce contextuel
Course: Mont-de-Marsan R1C3 "Le Veinard", 26/07/2026, Plat Handicap 2000m, Classe 2.

ADAPTATION MAJEURE (voir audit E0) : aucun chronometre (temps final ni
intermediaires) n'est fourni pour AUCUNE sortie d'AUCUN cheval. La formule
officielle S_ik = S_ref + k_echelle*[T_par - (T_ik+V_t)] est donc inapplicable
telle quelle. Conformement a la regle du protocole ("Si [C] est absent pour
tout le peloton -> dis-le et bascule en mode 'contextuel seul' avec un
avertissement de fiabilite degradee"), l'indice historique Ŝ_hist est
reconstruit a partir des donnees reellement fournies (classement, ecart a
l'arrivee, classe/allocation, poids porte) plutot que d'un chrono invente.
alpha_i est en consequence plafonne a 0.30 pour TOUS les chevaux (extension
de la regle "< 3 courses exploitables -> alpha <= 0.30" au cas totalement
degrade), et le poids du modele bascule vers le vecteur contextuel X_i.
"""
import json
import math
import numpy as np

RNG_SEED = 20260726
rng = np.random.default_rng(RNG_SEED)

with open("data/race_r1c3_20260726.json", encoding="utf-8") as f:
    DATA = json.load(f)

RACE = DATA["informations_course"]
RACE_DATE = np.datetime64("2026-07-26")

# ---------------------------------------------------------------------------
# PARAMETRES (priors du protocole, non recalibres sauf tau -- voir E6)
# ---------------------------------------------------------------------------
BETA_W = 0.166          # s/kg
K_ECHELLE = 5.0         # pts SF / seconde
SEUIL_CW_BW = 0.131
PHI = 2.5
HALFLIFE_DAYS = 90.0
LAMBDA_TEMP = math.log(2) / HALFLIFE_DAYS
GAMMA_GOWER = 3.0
ETA = 0.08
PSI = 0.0015
K0 = 3.0
ALPHA_MIN, ALPHA_MAX = 0.15, 0.80
ALPHA_MAX_DEGRADED = 0.30   # cap force : chrono absent pour tout le peloton
BETA_DRAW = 0.035
KAPPA_SUREFFORT = 1.6
TAU_PRIOR = 0.65
M_MC = 100_000
KELLY_FRACTION = 0.25
KELLY_CAP = 0.02

TERRAIN_PENETRO = {
    "Bon": 2.8, "Bon/Souple": 3.1, "Bon/PSF": 3.0, "Souple": 3.6,
    "PSF": 5.5,           # sable fibre : surface differente du gazon -> forte distance
    "Lourd": 4.6, "Lourd/PSF": 4.9, "Tr.Souple": 4.2, "Collant": 3.8,
}
PENETRO_JOUR = RACE["penetrometre_jour"]  # 3.35 (Bon a souple)
SEUIL_STALLE = 5  # ligne droite avant 1er tournant ~375m < 400m -> seuil bas (1-5)


def days_between(date_str):
    d = np.datetime64(date_str)
    return float((RACE_DATE - d) / np.timedelta64(1, "D"))


def run_score(run, horse):
    """Score de performance par sortie, construit SANS chrono (position,
    ecart, classe/allocation -- toutes donnees fournies, aucune invention).
    Echelle ~0-100 points, homogene a un 'score de forme'."""
    n = run["partants"]
    place = run["place"]
    if place is None or n is None or n < 2:
        return None
    rank_score = (n - place) / (n - 1)  # 1=victoire, 0=dernier
    ecart = run.get("ecart")
    if ecart is None:
        lengths_score = rank_score  # pas d'info d'ecart -> retombe sur le rang
    else:
        lengths_score = max(0.0, 1.0 - ecart / 8.0)
    alloc = run.get("allocation", 15000)
    class_norm = min(1.0, math.log(max(alloc, 1000) / 8000) / math.log(60000 / 8000))
    class_norm = max(0.0, class_norm)
    score01 = 0.55 * rank_score + 0.30 * lengths_score + 0.15 * class_norm
    score = 100.0 * score01

    # correction de surcharge (E1) : CW/BW avec BW = masse actuelle (proxy, ESTIME)
    bw = horse["masse_corporelle"]
    cw = run["poids_porte"]
    ratio = cw / bw
    if ratio > SEUIL_CW_BW:
        score -= math.exp(PHI * (ratio - SEUIL_CW_BW))
    return score


def gower_distance(run, horse):
    """Distance de Gower normalisee sur distance, terrain(penetro proxy),
    classe(allocation), charge du jour. Simplifiee (cf audit) : sens de
    corde et profil de rythme par course non disponibles -> composantes
    omises et signalees."""
    d_dist = abs(run["distance"] - RACE["distance_m"]) / 800.0
    pen_k = TERRAIN_PENETRO.get(run["terrain"], 3.3)
    d_terrain = abs(pen_k - PENETRO_JOUR) / 2.5
    alloc_k = run.get("allocation", 15000)
    alloc_today = 50900
    d_classe = abs(math.log(max(alloc_k, 1000)) - math.log(alloc_today)) / math.log(60000 / 8000)
    d_charge = abs(run["poids_porte"] - horse["poids_porte"]) / 10.0
    comps = [min(d_dist, 1.0), min(d_terrain, 1.0), min(d_classe, 1.0), min(d_charge, 1.0)]
    return sum(comps) / len(comps)


def compute_historical(horse):
    runs = horse["historique"]
    scored = []
    for r in runs:
        s = run_score(r, horse)
        if s is None:
            continue
        dt = days_between(r["date"])
        w_temp = math.exp(-LAMBDA_TEMP * dt)
        dg = gower_distance(r, horse)
        w_ctx = math.exp(-GAMMA_GOWER * dg ** 2)
        W = w_temp * w_ctx
        scored.append({"score": s, "W": W, "dt": dt})
    n_exploitable = len(scored)
    if n_exploitable == 0:
        return {"s_hist": 50.0, "n_eff": 0.0, "alpha": ALPHA_MIN, "var": 0.0,
                "dt_last": 9999.0, "n_exploitable": 0}
    W_sum = sum(x["W"] for x in scored)
    s_hist = sum(x["W"] * x["score"] for x in scored) / W_sum
    n_eff = W_sum
    # variance ponderee
    var = sum(x["W"] * (x["score"] - s_hist) ** 2 for x in scored) / W_sum
    dt_last = min(x["dt"] for x in scored)
    alpha_raw = 0.80 * (n_eff / (n_eff + K0)) / (1 + ETA * (var / 400.0) + PSI * dt_last)
    alpha = min(max(alpha_raw, ALPHA_MIN), ALPHA_MAX)
    alpha = min(alpha, ALPHA_MAX_DEGRADED)  # bascule "contextuel seul"
    return {"s_hist": s_hist, "n_eff": n_eff, "alpha": alpha, "var": var,
            "dt_last": dt_last, "n_exploitable": n_exploitable}


def parse_forme(forme_str):
    """'1p-1p-1p-1p-4p' -> indice de forme recente base sur 1/position,
    ponderee decroissante (course la plus recente = premier terme)."""
    parts = forme_str.replace("p", "").split("-")
    vals = []
    for i, p in enumerate(parts):
        try:
            pos = int(p)
        except ValueError:
            continue
        if pos == 0:
            pos = 12  # "0p" = non classe (hors places) -> proxy position mediocre
        w = 0.7 ** i
        vals.append(w / pos)
    if not vals:
        return 0.0
    return sum(vals) / sum(0.7 ** i for i in range(len(vals)))


def build_context_vector(horse, field_mean_weight, field_jockey_mean, field_form_mean):
    x = {}
    # a) biais de corde
    corde = horse["corde"]
    rythme = horse["rythme"]
    if corde <= SEUIL_STALLE:
        pen_stalle = 0.0
    else:
        excess = corde - SEUIL_STALLE
        pen_stalle = -BETA_DRAW * excess if rythme == "attentiste" else -BETA_DRAW * KAPPA_SUREFFORT * excess
    x["corde"] = pen_stalle

    # b) terrain -- penetrometre prefere estime par moyenne ponderee (par run_score) des terrains passes
    runs = horse["historique"]
    weighted_pen, wsum = 0.0, 0.0
    for r in runs:
        s = run_score(r, horse)
        if s is None:
            continue
        pen_k = TERRAIN_PENETRO.get(r["terrain"], 3.3)
        weighted_pen += s * pen_k
        wsum += s
    pen_pref = weighted_pen / wsum if wsum > 0 else PENETRO_JOUR
    s_terrain = 1.0 - min(abs(PENETRO_JOUR - pen_pref) / 2.5, 1.0)
    x["terrain"] = (s_terrain - 0.5) * 0.5  # recentre, echelle moderee +-0.25

    # c) aero / drafting (vent 20.5 km/h O/OSO)
    wind_factor = (RACE["vent_kmh"] / 20.0) ** 2
    if rythme == "animateur":
        x["aero"] = -0.15 * wind_factor
    else:
        x["aero"] = 0.08 * wind_factor

    # d) equipement (variables muettes, effet borne +-0.15)
    eq = horse.get("equipement", {})
    eq_score = 0.0
    premiere_fois = eq.get("premiere_fois", [])
    if "oeilleres_australiennes" in premiere_fois:
        eq_score += 0.08
    if "oeilleres" in premiere_fois:
        eq_score += 0.08
    if eq.get("attache_langue"):
        eq_score += 0.03
    if eq.get("rentree_longue_absence_mois"):
        eq_score -= 0.10  # manque de course, incertitude fitness
    if eq.get("raccourci_distance"):
        eq_score += 0.03
    if eq.get("retour_gazon"):
        eq_score += 0.0  # neutre, deja pris en compte via Gower terrain historique
    x["equipement"] = max(-0.15, min(0.15, eq_score))

    # e) charge du jour
    delta_w = horse["poids_porte"] - field_mean_weight
    x["charge"] = -BETA_W * K_ECHELLE * delta_w / 100.0  # ramene a une echelle ~z (points/100)

    # f) age x sexe, jockey, ecurie
    age = horse["age"]
    age_bonus = {4: 0.03, 5: 0.03, 6: 0.0, 7: -0.03}.get(age, 0.0)
    x["age"] = age_bonus

    js = horse["jockey_stats"]
    jwin = js.get("taux_victoire") or field_jockey_mean
    x["jockey"] = (jwin - field_jockey_mean) * 1.5

    forme_idx = parse_forme(horse["entraineur_forme"])
    x["ecurie"] = (forme_idx - field_form_mean) * 0.6

    total = sum(x.values())
    return total, x


def build_pace_map(chevaux):
    animateurs = [h for h in chevaux if h["rythme"] == "animateur"]
    return animateurs


def compute_J(chevaux, animateurs):
    n_anim = len(animateurs)
    J = {h["numero"]: 0.0 for h in chevaux}
    details = {h["numero"]: [] for h in chevaux}
    if n_anim >= 4:
        for h in animateurs:
            # penalite plus forte si tire large (corde exterieure)
            base = -0.15 - 0.05 * min(1.0, (h["corde"] - SEUIL_STALLE) / 10.0 if h["corde"] > SEUIL_STALLE else 0.0)
            base = max(-0.30, base)
            J[h["numero"]] += base
            details[h["numero"]].append(f"Train rapide probable ({n_anim} animateurs) : usure en tete, {base:+.2f}")
        finisseurs = [h for h in chevaux if h["rythme"] == "attentiste" and h["corde"] <= SEUIL_STALLE]
        for h in finisseurs:
            bonus = 0.15
            J[h["numero"]] += bonus
            details[h["numero"]].append(f"Beneficie d'un train rapide devant, place a l'interieur, {bonus:+.2f}")
    elif n_anim <= 1:
        for h in animateurs:
            bonus = 0.25
            J[h["numero"]] += bonus
            details[h["numero"]].append(f"Seul (ou quasi) animateur : prend la tete sans lutte, {bonus:+.2f}")
    else:
        for h in animateurs:
            malus = -0.10
            J[h["numero"]] += malus
            details[h["numero"]].append(f"Lutte tactique moderee entre {n_anim} animateurs, {malus:+.2f}")

    # animateur tire large degrade les chevaux a l'interieur qu'il va rabattre
    for h in animateurs:
        if h["corde"] > SEUIL_STALLE:
            excess = h["corde"] - SEUIL_STALLE
            self_pen = -BETA_DRAW * KAPPA_SUREFFORT * excess * 0.3
            J[h["numero"]] += self_pen
            details[h["numero"]].append(f"Tire large (corde {h['corde']}) et devra ratisser large, {self_pen:+.2f}")
            for h2 in chevaux:
                if h2["corde"] < h["corde"] and h2["numero"] != h["numero"]:
                    pass  # effet diffus deja capture par la penalite de stalle individuelle ; pas de double comptage

    # borne |sum J| <= 0.40
    for num in J:
        if J[num] > 0.40:
            J[num] = 0.40
        if J[num] < -0.40:
            J[num] = -0.40
    return J, details


def gamma_vulnerabilite(horse, field_mean_weight):
    score = 0.0
    if horse["corde"] >= 13:
        score += 0.4
    ratio = horse["poids_porte"] / horse["masse_corporelle"]
    if ratio > 0.125:
        score += 0.3
    if horse["masse_corporelle"] < 470:
        score += 0.3
    return min(1.0, score)


def penalites_extremes(horse):
    pen = 0.0
    if horse["corde"] >= 14:
        pen += 0.10
    if horse.get("equipement", {}).get("rentree_longue_absence_mois"):
        pen += 0.05
    return pen


def main():
    chevaux = DATA["chevaux"]
    field_mean_weight = float(np.mean([h["poids_porte"] for h in chevaux]))
    jockey_wins = [h["jockey_stats"].get("taux_victoire") for h in chevaux if h["jockey_stats"].get("taux_victoire")]
    field_jockey_mean = float(np.mean(jockey_wins))
    field_form_mean = float(np.mean([parse_forme(h["entraineur_forme"]) for h in chevaux]))

    hist_results = {}
    for h in chevaux:
        hist_results[h["numero"]] = compute_historical(h)

    s_hist_vals = np.array([hist_results[h["numero"]]["s_hist"] for h in chevaux])
    mean_s, std_s = s_hist_vals.mean(), s_hist_vals.std(ddof=0)
    if std_s == 0:
        std_s = 1.0

    context_results = {}
    for h in chevaux:
        total, detail = build_context_vector(h, field_mean_weight, field_jockey_mean, field_form_mean)
        context_results[h["numero"]] = {"total": total, "detail": detail}

    animateurs = build_pace_map(chevaux)
    J, J_details = compute_J(chevaux, animateurs)

    rows = []
    for h in chevaux:
        num = h["numero"]
        hr = hist_results[num]
        z_i = (hr["s_hist"] - mean_s) / std_s
        alpha_i = hr["alpha"]
        bx_i = context_results[num]["total"]
        j_i = J[num]
        gamma_i = gamma_vulnerabilite(h, field_mean_weight)
        pen_extreme = penalites_extremes(h)
        theta_i = alpha_i * z_i + (1 - alpha_i) * bx_i + j_i - gamma_i * pen_extreme
        rows.append({
            "numero": num, "nom": h["nom"], "z": z_i, "alpha": alpha_i, "bx": bx_i,
            "J": j_i, "gamma": gamma_i, "pen_extreme": pen_extreme, "theta": theta_i,
            "n_exploitable": hr["n_exploitable"], "n_eff": hr["n_eff"],
            "cote_pmu": h["cote_pmu"], "cote_zeturf": h["cote_zeturf"], "cote_genybet": h["cote_genybet"],
        })

    # ---- E6 : calibration de tau ----
    thetas = np.array([r["theta"] for r in rows])

    def favorite_prob(tau):
        w = np.exp(thetas / tau)
        p = w / w.sum()
        return p.max(), p

    tau = TAU_PRIOR
    p_fav, p_all = favorite_prob(tau)
    lo, hi = 0.05, 5.0
    iterations = 0
    while not (0.18 <= p_fav <= 0.28) and iterations < 200:
        if p_fav > 0.28:
            lo = tau
        else:
            hi = tau
        tau = (lo + hi) / 2
        p_fav, p_all = favorite_prob(tau)
        iterations += 1

    for r, p in zip(rows, p_all):
        r["p_gagne_theorique"] = p

    # ---- E7 : Monte-Carlo Plackett-Luce (course d'exponentielles) ----
    w = np.exp(thetas / tau)  # taux, coherent avec le softmax de E6
    n = len(rows)
    U = rng.random((M_MC, n))
    T = -np.log(U) / w[None, :]
    order = np.argsort(T, axis=1)  # indices tries par T croissant = ordre d'arrivee

    p1 = np.zeros(n)
    ptop2 = np.zeros(n)
    ptop3 = np.zeros(n)
    ptop5 = np.zeros(n)
    for pos in range(n):
        idx = order[:, pos]
        if pos == 0:
            np.add.at(p1, idx, 1)
        if pos < 2:
            np.add.at(ptop2, idx, 1)
        if pos < 3:
            np.add.at(ptop3, idx, 1)
        if pos < 5:
            np.add.at(ptop5, idx, 1)
    p1 /= M_MC
    ptop2 /= M_MC
    ptop3 /= M_MC
    ptop5 /= M_MC

    for i, r in enumerate(rows):
        r["p1_mc"] = p1[i]
        r["ptop2_mc"] = ptop2[i]
        r["ptop3_mc"] = ptop3[i]
        r["ptop5_mc"] = ptop5[i]

    # couples / trio les plus probables (empirique)
    first_two = order[:, :2]
    couple_counts = {}
    for a, b in first_two:
        key = tuple(sorted((int(a), int(b))))
        couple_counts[key] = couple_counts.get(key, 0) + 1
    top_couples = sorted(couple_counts.items(), key=lambda x: -x[1])[:8]

    first_three = order[:, :3]
    trio_counts = {}
    for a, b, c in first_three:
        key = tuple(sorted((int(a), int(b), int(c))))
        trio_counts[key] = trio_counts.get(key, 0) + 1
    top_trios = sorted(trio_counts.items(), key=lambda x: -x[1])[:8]

    num_by_idx = {i: rows[i]["numero"] for i in range(n)}

    # ---- E8 : devigging (methode par puissance) + Kelly ----
    def devig_power(odds_list):
        raw_p = np.array([1.0 / o for o in odds_list])
        overround = raw_p.sum()

        def f(k):
            return np.sum(raw_p ** k) - 1.0
        klo, khi = 0.3, 3.0
        for _ in range(100):
            kmid = (klo + khi) / 2
            if f(kmid) > 0:
                klo = kmid
            else:
                khi = kmid
        k = (klo + khi) / 2
        p_dev = raw_p ** k
        p_dev /= p_dev.sum()
        return p_dev, overround, k

    odds_pmu = [r["cote_pmu"] for r in rows]
    p_market, overround, k_devig = devig_power(odds_pmu)
    for r, pm in zip(rows, p_market):
        r["p_marche_devig"] = pm
        edge = r["p1_mc"] - pm
        r["edge"] = edge
        cote_decimale = r["cote_pmu"] + 1.0
        if edge >= 0.03:
            b = cote_decimale - 1.0
            p = r["p1_mc"]
            fstar = (p * (b) - (1 - p)) / b
            fstar = max(fstar, 0.0)
            mise = min(KELLY_FRACTION * fstar, KELLY_CAP)
        else:
            fstar = 0.0
            mise = 0.0
        r["fstar"] = fstar
        r["mise_kelly"] = mise

    rows_sorted = sorted(rows, key=lambda r: -r["theta"])

    output = {
        "tau": tau,
        "iterations_tau": iterations,
        "overround_pmu": overround,
        "k_devig": k_devig,
        "field_mean_weight": field_mean_weight,
        "field_jockey_mean": field_jockey_mean,
        "field_form_mean": field_form_mean,
        "rows": rows_sorted,
        "J_details": J_details,
        "context_details": {k: v["detail"] for k, v in context_results.items()},
        "hist_results": hist_results,
        "animateurs": [h["numero"] for h in animateurs],
        "top_couples": [(num_by_idx[a], num_by_idx[b], c / M_MC) for (a, b), c in top_couples],
        "top_trios": [(num_by_idx[a], num_by_idx[b], num_by_idx[c], cnt / M_MC) for (a, b, c), cnt in top_trios],
    }
    return output


if __name__ == "__main__":
    out = main()
    with open("output/pipeline_results.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2, default=float)
    print(f"tau calibre = {out['tau']:.4f} (iterations={out['iterations_tau']})")
    print(f"overround PMU = {out['overround_pmu']:.4f}, k_devig = {out['k_devig']:.4f}")
    print()
    print(f"{'n':>3} {'nom':<16} {'z':>6} {'a':>5} {'bx':>6} {'J':>6} {'theta':>7} {'P1':>6} {'Ptop3':>6} {'cote':>6} {'p_mkt':>6} {'edge':>6} {'mise':>6}")
    for r in out["rows"]:
        print(f"{r['numero']:>3} {r['nom']:<16} {r['z']:>6.2f} {r['alpha']:>5.2f} {r['bx']:>6.2f} {r['J']:>6.2f} "
              f"{r['theta']:>7.3f} {r['p1_mc']*100:>5.1f}% {r['ptop3_mc']*100:>5.1f}% {r['cote_pmu']:>6.1f} "
              f"{r['p_marche_devig']*100:>5.1f}% {r['edge']*100:>+5.1f} {r['mise_kelly']*100:>5.2f}%")
    print()
    print("Top couples (P1+2, ordre indifferent):")
    for a, b, p in out["top_couples"][:5]:
        print(f"  {a}-{b}: {p*100:.2f}%")
    print("Top trios:")
    for a, b, c, p in out["top_trios"][:5]:
        print(f"  {a}-{b}-{c}: {p*100:.2f}%")
