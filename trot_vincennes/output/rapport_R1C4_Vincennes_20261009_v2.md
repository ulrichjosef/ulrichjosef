# Prix Héra — Vincennes R1C4, 09/10/2026 — Analyse value v2 (données de forme)

Remplace la v1 (mode « marché seul »). Données : `data/Prix_Hera_R1C4_09-10-2026.docx` (musiques, 5 dernières courses, RK, fautes, ferrures, cotes de 13h24).

## 1. Cadre et qualité des données
Trot attelé, course C, départ volté, Grande Piste, 2 850 m / 2 875 m (n°10-15 à +25 m), 15 partants, piste souple.

**Fiable** : les musiques, les RK courses par course et la ferrure du jour.

**Fragile** :
- les écarts avec le gagnant manquent sur 69 courses sur 75 ;
- les records volté / autostart ne concordent pas d'une source à l'autre, donc ils ne sont pas utilisés ;
- les bilans à Vincennes GP ne viennent que d'une source, donc ils ont un poids faible et sont lissés vers la moyenne ;
- les RK des n°1, 3, 6 et 8 sont **imputés** : ces chevaux n'ont pas de course comparable récente sur la GP ou à Enghien en volté.

## 2. Variables
| Composante | Poids | Mesure |
|---|---|---|
| Vitesse | 0,35 | Moyenne des RK comparables (Vincennes GP ou Enghien, volté, ≥ 2 700 m), + 0,64 s/km pour le recul de 25 m |
| Forme | 0,25 | Points selon la place × classe de la course (C 68 k = 1 ; D ≈ 0,65 ; F ≈ 0,4) × ancienneté. Les courses fautées sont exclues, car comptées dans le risque de faute |
| Écurie / driver 30 j | 0,15 | Moyenne des sources B et D |
| Aptitude GP | 0,10 | (victoires + places) / sorties, lissé vers 28 % |
| Ferrure du jour | 0,10 | +1 si D4 efficace, +0,5 si ferrure optimale connue, −1 si contre-emploi (n°1 en p4, n°11 en pA alors qu'il a besoin du D4) |
| **Risque de faute** | simulé à part | Mélange musique + sources B et D : n°1 45 %, n°5 30 %, n°13 25 %, n°10 22 %, les autres entre 6 et 15 % |

**Écartées** :
- records volté / autostart : incohérents entre les sources ;
- écarts à l'arrivée : quasi absents ;
- météo : identique pour tout le champ ;
- gains : déjà intégrés dans le recul et dans la classe.

**Méthode** : on prend des z-scores, puis un modèle Plackett-Luce avec fautes (200 000 simulations). La température est calée sur la dispersion du marché. On fait ensuite un pooling logarithmique modèle 60 % / marché 40 %, avec dévigging power sur les cotes de 13h24.

## 3. Probabilités
| N° | Cheval | Cote 13h24 | RK effectif | p forme | p marché | **p final** | Top 3 | Top 5 | Edge | Cote juste |
|---|---|---|---|---|---|---|---|---|---|---|
| 10 | Irish Nice Elgé | 4,5 | 1'13"1 | 16,0 % | 20,0 % | **17,8 %** | 46 % | 65 % | −2,2 | 5,6 |
| 13 | I Still Loving You | 5,9 | 1'13"3 | 18,7 % | 14,9 % | **17,7 %** | 46 % | 63 % | +2,7 | 5,6 |
| 14 | Indien de Fontaine | 6,9 | 1'13"5 | 10,3 % | 12,6 % | **11,3 %** | 35 % | 58 % | −1,4 | 8,8 |
| 2 | Heaven d'Ecajeul | 13,6 | **1'12"7** | 14,8 % | 6,1 % | **10,4 %** | 32 % | 54 % | **+4,3** | 9,6 |
| 5 | Jytrace de Houelle | 8,4 | 1'13"3 | 6,3 % | 10,2 % | 7,9 % | 24 % | 41 % | −2,3 | 12,7 |
| 15 | Ileo Pierji | 10,3 | 1'13"6 | 7,3 % | 8,2 % | 7,9 % | 25 % | 45 % | −0,4 | 12,7 |
| 6 | Jannig d'Erevan | 8,9 | 1'13"6* | 5,2 % | 9,6 % | 6,7 % | 22 % | 39 % | −2,9 | 14,9 |
| 12 | Inherit | 15,3 | 1'13"5 | 5,1 % | 5,4 % | 5,5 % | 18 % | 34 % | +0,1 | 18 |
| 7 | Izijal | 19,8 | 1'13"6 | 3,6 % | 4,1 % | 3,9 % | 13 % | 26 % | −0,2 | 26 |
| 8 | Horizon du Thay | 30,3 | 1'13"8* | 4,1 % | 2,6 % | 3,5 % | 12 % | 24 % | +0,9 | 29 |
| 9, 4, 3, 11, 1 | — | 33-91 | — | ≤ 2,8 % | — | ≤ 2,6 % | ≤ 9 % | ≤ 18 % | ≈ 0 | — |

\* RK imputé (pas de course comparable).

**Ordre du modèle : 10 – 13 – 14 – 2 – 15** (10 et 13 quasi à égalité, puis 5 et 6).

## 4. Value bets
- **N°2 Heaven d'Ecajeul : seule value robuste.** Edge de +4,3 points. Il reste **positif dans les 5 variantes de sensibilité testées** (+2,7 à +6,9 points), que l'on change les poids, que l'on renforce le marché ou que l'on retire la forme d'écurie. Pourquoi :
  - meilleur RK comparable du lot (1'12"5 et 1'12"8 sur la GP en C 68 k, 3e et 4e) ;
  - il part du premier échelon, donc avec 25 m d'avance sur les meilleurs ;
  - 1 seule faute sur 9 courses ;
  - Gelormini au sulky, en pA, sa ferrure optimale.

  Cote juste ≈ 9,6, pour une cote réelle de 13,6. **Simple gagnant à ¼ Kelly : 0,5 % de la bankroll** (selon les variantes, entre 0,2 % et 1,3 %). Probabilité de top 3 : 32 %, donc **le simple placé vaut le coup si le rapport placé est ≥ 3,5**.
- **N°13 I Still Loving You** : edge légèrement positif dans toutes les variantes, mais trop mince une fois le tassement pris en compte. Ne jouer que si la cote est ≥ 6,5 au départ.
- **N°10 Irish Nice Elgé** : légèrement **surjoué** (cote juste 5,6 contre 4,5). Il reste une base Quinté logique, mais ce n'est pas un pari gagnant.
- **N°5 et n°6** : surjoués par le marché, à cause du risque de faute pour le 5 et de RK provinciaux non transposables pour le 6.

## 5. Tickets
| Pari | Sélection | Coût | Probabilité estimée |
|---|---|---|---|
| Simple gagnant | **2** | 0,5 % de la bankroll | 10,4 % (cote juste 9,6) |
| Simple placé | **2** (si rapport ≥ 3,5) | 0,5 % de la bankroll | 32 % |
| 2sur4 | 10 – 13 | 3 € | 29 % |
| 2sur4 | 13 – 2 ou 10 – 2 (pour le rapport) | 3 € chacun | ~22 % |
| Quinté+ champ réduit | Base **10** + 13, 14, **2**, 15, 5, 6 | 15 combinaisons, 30 € | 11,7 % que le désordre soit couvert |

Le Quinté+ sert à viser un gros rapport, pas à faire de la value : la probabilité de couvrir le désordre reste faible.

## 6. Confiance & réserves
- **Confiance modérée.** La value sur le n°2 tient à la vitesse brute et au premier échelon, ce qui est robuste. En revanche, les écarts à l'arrivée et une partie des RK manquent.
- **Cotes** : celles de 13h24 bougeront. Si le n°2 descend sous 10, la value disparaît.
- **Risque de faute** : le volté sur 2 850 m garde un risque élevé pour les n°5, 13 et 10 (22 à 30 %). Ces trois-là doivent être des associés de Quinté, pas des bases en couplé gagnant.
- Les données contradictoires sont listées dans le fichier source (⚠).
