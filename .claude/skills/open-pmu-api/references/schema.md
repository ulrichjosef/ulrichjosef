# Schéma d'une course (élément de `message`)

| Champ | Type | Description |
|---|---|---|
| `type` | string | Discipline : Plat, Trot attelé, Trot monté, Haies, Steeple-chase, Cross… |
| `montant` | number | Allocation en € |
| `distance` | number | Mètres |
| `prix` | string | Nom du prix |
| `lieu` | string | Hippodrome |
| `heure_depart` | string | `HH:MM:SS` |
| `details` | string | Conditions de course (texte libre) |
| `partants` | number | Nombre de partants |
| `non_partants` | number[] | Numéros non-partants |
| `arrivee` | number[] | Numéros dans l'ordre d'arrivée |
| `r/c` | string | Réunion/course, ex. `R1/C3` |
| `date` | string | `YYYY-MM-DD` |
| `arrivee_details` | object | Clé = numéro (string) → cheval |
| `statistiques` | object | Agrégats calculés (voir ci-dessous) |

## Cheval (`arrivee_details[num]`)

`nom_cheval`, `sexe` (H/F/M), `annee_de_naissance`, `nom_jockey`, `nom_entraineur`, `position`,
et selon disponibilité : `poids_cheval`, `musique`, `cotes` (number[]), `gains`, `corde`, `discipline`, `distance`.

## `statistiques`

`nombre_partants`, `nombre_arrivants`, `nombre_non_partants`, `cote_min`, `cote_max`, `cote_moyenne`, `cote_mediane`,
`favori {numero, nom_cheval, cote, position}`, `gagnant {numero, nom_cheval, cote}`,
`repartition_positions`, `taux_favori_gagnant` (0/100), `taux_favori_place` (0/100),
`ecart_cote_gagnant` (cote gagnant − cote favori), `ecart_cote_favori` (cote moyenne − cote favori).

## Exemple (31/10/2026, extrait)

```json
{"error": false, "total": 1, "params": {"date": "10/31/2026"},
 "message": [{"type": "Plat", "montant": 52800, "distance": 1900, "prix": "PRIX DU PAYS DE BRAY",
   "lieu": "Deauville", "heure_depart": "15:15:00", "partants": 16, "non_partants": [],
   "arrivee": [9, 11, 3, 1, 5, 7, 12], "r/c": "R1/C3", "date": "2026-10-31",
   "arrivee_details": {"9": {"nom_cheval": "AMIE AMOUR", "nom_jockey": "GUYON M.",
     "musique": "2p 1p 2p 4p 3p 5p 2p (25) 13p", "cotes": [5.7, 6.5, 5.2], "position": 1}},
   "statistiques": {"favori": {"numero": 9, "cote": 5.2, "position": 1},
     "gagnant": {"numero": 9, "nom_cheval": "AMIE AMOUR", "cote": 5.2},
     "taux_favori_gagnant": 100, "taux_favori_place": 100}}]}
```
