---
name: open-pmu-api
description: Interroge l'API publique Open PMU (open-pmu-api.vercel.app) pour récupérer les arrivées officielles de courses hippiques françaises (PMU) depuis 2004 — par date, hippodrome ou nom de prix — avec partants, non-partants, cotes, musique, jockeys, entraîneurs et statistiques (favori, gagnant, écarts de cote). À utiliser dès qu'il faut des résultats/arrivées PMU, vérifier un pronostic après course, ou constituer un historique pour analyser des courses, des chevaux, des hippodromes ou la réussite des favoris.
---

# Open PMU API

API REST publique, sans clé, en lecture seule : `GET https://open-pmu-api.vercel.app/api/arrivees`

Un seul paramètre par requête (priorité si plusieurs : `prix` > `hippo` > `date`) :

| Paramètre | Format | Exemple |
|---|---|---|
| `date` | `MM/DD/YYYY` (format US !) | `10/31/2026` |
| `hippo` | nom de l'hippodrome | `Chantilly` |
| `prix` | nom du prix (majuscules) | `PRIX DE LA CHAMBRE DU DUC` |

Données : du 22/01/2004 à ~fin du mois précédent (mise à jour mensuelle, pas de résultats du jour).
Pas de pagination ni de limite publiée : préférer `date`; `hippo`/`prix` peuvent renvoyer de très grosses réponses.

## Utilisation

Script fourni (Python stdlib, aucune dépendance) :

```bash
python3 scripts/pmu.py --date 2026-10-31            # accepte aussi 31/10/2026 ou 10/31/2026 (--us)
python3 scripts/pmu.py --hippo Chantilly --limit 20
python3 scripts/pmu.py --prix "PRIX DU PAYS DE BRAY"
python3 scripts/pmu.py --date 2026-10-31 --json     # JSON brut de l'API
python3 scripts/pmu.py --from 2026-10-01 --to 2026-10-07 --summary   # plage de dates + stats favoris
```

Le script convertit les dates françaises (JJ/MM/AAAA) et ISO vers le format US attendu, imprime un résumé lisible par course (R/C, lieu, prix, discipline, distance, partants, arrivée, gagnant et cote, favori) et peut agréger une plage de dates (`--summary` : taux de victoire / place du favori, cote moyenne du gagnant).

Sans le script : `curl -s "https://open-pmu-api.vercel.app/api/arrivees?date=10%2F31%2F2026"` (encoder `/` en `%2F` et les espaces en `%20`).

## Réponse

`{ error, total, params, message }` — `message` est un tableau de courses si `error` est `false`, sinon une chaîne d'explication (ex. aucune course trouvée). Détail des champs : `references/schema.md`.

Points d'attention :
- `arrivee` = liste ordonnée des numéros ; `arrivee_details` est indexé par numéro de cheval (chaîne) et peut être partiel.
- `cotes` = plusieurs relevés ; la cote « effective » retenue par l'API est la plus basse valide.
- `musique` : chiffres = places, `D/T/A/R` = disqualifié/tombé/arrêté/rétrogradé, `(25)` = séparateur d'année.
- Les champs varient selon les courses : toujours tester la présence avant usage.

## Bonnes pratiques

- Pour un historique, boucler jour par jour sur `date` plutôt que de lancer des requêtes larges répétées ; espacer les appels (le script attend 0,5 s entre jours).
- Ne pas présenter les statistiques passées comme une garantie : ce sont des données historiques pour l'analyse.
- Si l'hôte est bloqué (erreur proxy 403), le signaler : l'accès réseau à `open-pmu-api.vercel.app` doit être autorisé dans l'environnement.

Source : projet open source MIT https://github.com/nanaelie/open-pmu-api (la licence couvre le code, pas les données de course).
