# Prix Héra — Vincennes R1C4, ven. 09/10/2026, 20h15 — Analyse value

## 1. Cadre
Trot attelé, course C, départ volté, Grande Piste corde à gauche, 2 850 m (n°1-9) / 2 875 m (n°10-15, recul de 25 m), 15 partants, cendrée souple et légèrement collante, 13-14 °C, risque de pluie fine.

**Données manquantes (critique)** : pas de musique ni de 5 dernières courses, pas de réduction kilométrique, pas de taux de disqualification, pas de références à Vincennes GP / 2 850 m / départ volté. Le modèle tourne donc en **mode « marché + ajustements »** : le point de départ est la probabilité PMU dévigée (méthode power, k = 1,085, marché à 119,4 %) et les corrections restent modestes.

**Points douteux dans la fiche fournie** : n°8 et n°9 ont des gains identiques à l'euro près (168 605 €), possible erreur de copie. « Pelham complet » ne veut rien dire ici. Il n'existe pas de disqualification « pour l'épaule gauche dans les virages ». L'effet du vent sud-ouest dans la montée n'est pas vérifiable. Avant de jouer, vérifiez partants, ferrures et cotes sur le site PMU.

## 2. Variables retenues / écartées
| Variable | Traitement | Poids (log-force) |
|---|---|---|
| Cote PMU dévigée | prior : elle contient forme, classe et recul | base |
| Ferrure sur sol souple | D4 +0,06 · DP +0,03 · Pa/Dp +0,02 · Pa 0 · P4 −0,04 | faible |
| Âge | 7 ans +0,05 · 8 ans 0 · 9 ans −0,04 | faible |
| Driver de premier plan | +0,03 | faible |
| 2d échelon en départ volté | −0,03 (risque de faute en remontant le lot) | faible |

**Écartées** :
- gains et classe : déjà dans la cote et dans le recul, donc colinéaires ;
- météo et vent : identiques pour tout le champ, pas de signal différentiel ;
- tracé de la Grande Piste : aucune donnée d'aptitude par cheval.

## 3. Probabilités du modèle (Plackett-Luce, 200 000 simulations)
| N° | Cheval | Cote | p marché | p modèle | Top 3 | Top 5 | Edge | Rôle |
|---|---|---|---|---|---|---|---|---|
| 10 | Irish Nice Elgé | 3,3 | 27,4 % | 27,8 % | 67 % | 88 % | +0,4 | **Base** |
| 13 | I Still Loving You | 5,1 | 17,1 % | 16,8 % | 49 % | 74 % | −0,3 | Associé |
| 14 | Indien de Fontaine | 7,8 | 10,8 % | 10,5 % | 33 % | 57 % | −0,3 | Associé |
| 5 | Jytrace de Houelle | 8,7 | 9,6 % | 10,2 % | 33 % | 56 % | +0,6 | Associé (meilleur du 1er échelon) |
| 6 | Jannig d'Erevan | 10 | 8,2 % | 8,4 % | 28 % | 49 % | +0,2 | Associé |
| 15 | Ileo Pierji | 12 | 6,8 % | 6,9 % | 23 % | 42 % | +0,1 | Associé |
| 2 | Heaven d'Ecajeul | 16 | 4,9 % | 4,7 % | 16 % | 31 % | −0,3 | Outsider |
| 12 | Inherit | 18 | 4,3 % | 4,1 % | 14 % | 28 % | −0,2 | Outsider |
| 8 | Horizon du Thay | 28 | 2,7 % | 2,6 % | 9 % | 18 % | −0,1 | — |
| 3 | Horacio de Cerisy | 30 | 2,5 % | 2,4 % | 9 % | 17 % | −0,1 | — |
| 7, 9, 4, 11, 1 | autres | 45–99 | ≤ 1,6 % | ≤ 1,6 % | ≤ 6 % | ≤ 12 % | ≈ 0 | écartés |

Ordre du modèle : **10 – 13 – 14 – 5 – 6** (15 en 6e).
Probabilité que le couplé gagnant 10-13 sorte : 12,1 %. Couplé 10-14 : 7,4 %. Couplé 10-5 : 7,1 %.

## 4. Value bets
**Aucun.** Les edges ne dépassent jamais +0,6 point, donc ils restent sous le bruit d'estimation. Après le tassement habituel des rapports au départ (≈ −15 %), le Kelly est nul partout. C'est logique : sans données de forme, le modèle ne peut pas contredire le marché. Les seuls légers écarts positifs sont **5 Jytrace de Houelle** (7 ans, déferré des 4, le plus solide du premier échelon) et **10 Irish Nice Elgé**.

## 5. Tickets proposés (jeu « plaisir », pas de value démontrée)
- **Quinté+ champ réduit** : base **10**, avec 13, 14, 5, 6, 15 et 12. Cela donne 15 combinaisons, soit 30 € à 2 € la combinaison. Variante plus large, en ajoutant le 2 : 35 combinaisons, soit 70 €.
- **2sur4** : 10 – 13 (pari annexe le plus cohérent).
- **Simple placé 10** : 67 % de top 3 estimé, mais le rapport sera faible et la value négative après la marge.
- Mise totale conseillée : **≤ 1 % de la bankroll**, puisque l'edge est nul.

## 6. Confiance & réserves
- La confiance est **faible à modérée**. Le modèle reproduit le marché, faute de forme récente. Il ne peut pas trouver de value que le marché aurait ratée.
- Le départ volté sur 2 850 m garde un risque de faute réel pour chacun, favoris compris. Un favori à 28 % perd plus de 7 fois sur 10.
- Pour transformer cette lecture en vraie analyse value, fournissez les **musiques (5-6 dernières courses), les réductions kilométriques et les résultats sur la Grande Piste et en départ volté**. Je relancerai alors le pipeline.

`resultat` est à compléter après la course dans `journal_pronostics.jsonl`.
