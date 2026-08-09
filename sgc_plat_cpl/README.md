# SGC_PLAT-CPL v1.0 — Fusion bayésienne + Plackett-Luce contextuel

Moteur d'analyse quantitative pour le plat handicap (référence 2000 m,
adaptable 1600–2400 m), implémentant le pipeline É0–É8 : normalisation des
performances passées, pondération temporelle/contextuelle (Gower), fusion
bayésienne historique + contextuelle, interactions tactiques (pace map),
softmax calibré, simulation Monte-Carlo Plackett-Luce, devigging et
détection de value (Kelly fractionné).

## Contenu

- `data/race_r1c3_20260726.json` — Données structurées de la course
  (Mont-de-Marsan R1C3, 26/07/2026, Prix Le Journal "Le Veinard").
- `pipeline.py` — Implémentation complète du pipeline en Python/numpy.
- `output/pipeline_results.json` — Résultats bruts du calcul (theta, P(1er),
  P(top3), edge, mises, détails des composantes).
- `output/rapport_R1C3_MontDeMarsan_20260726.md` — Rapport final au format
  requis (audit, scénario, tableau, ordre d'arrivée, tickets, exclusions,
  CALCULÉ vs ESTIMÉ, ligne JSONL).
- `output/journal_pronostics.jsonl` — Journal d'apprentissage (une ligne par
  course analysée, à compléter après course avec résultat/brier/roi).

## Point d'attention majeur

**Aucune donnée de chronométrage n'était disponible** pour aucun cheval,
dans aucune course de l'historique fourni. Le pipeline a donc basculé en
mode « contextuel seul » conformément à la règle de garde-fou du protocole :
l'indice historique est reconstruit à partir du classement, de l'écart à
l'arrivée et de la classe/allocation plutôt que d'un chrono, et α_i est
plafonné à 0,30 pour l'ensemble du peloton. Voir la section 1 (Audit) du
rapport pour le détail complet des données manquantes et des approximations
déclarées.

## Reproduire l'analyse

```bash
pip install numpy
cd sgc_plat_cpl
python3 pipeline.py
```
