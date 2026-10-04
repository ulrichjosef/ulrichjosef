# Arc de Triomphe 2026 : analyse pré-course (pipeline v0.3)

**Course** : Qatar Prix de l'Arc de Triomphe, ParisLongchamp, R1C5, dimanche 4 octobre 2026, 16h05. 2 400 m, Grande Piste, corde à droite. 16 partants.
**Statut** : **premier test réellement à l'aveugle.** Cette course est postérieure à mes connaissances. Je n'ai fait aucune recherche web, pour ne pas risquer de tomber sur le résultat. Seul le dossier fourni a été utilisé.
**Méthode** : [PIPELINE.md](../PIPELINE.md) v0.3, appliqué **sans modifier aucune pondération**. Les points où la méthode montre une faiblesse sont signalés et non corrigés (section 13).
**Horodatage** : ce document est commité dans git avant le départ. Le commit sert de preuve.

Légende des niveaux de soutien : **[D]** donnée du dossier · **[E]** extrapolation d'un pattern historique (niveau indiqué) · **[H]** hypothèse.

---

## Étape 1 : Compréhension de la course

| Élément | Valeur | Conséquence pour le pipeline |
|---|---|---|
| Terrain | Bon souple, pénétromètre 3,4 [D] ; sec depuis 72 h, soleil, 24 °C | **Classe T1** (< 3,5), avec tendance à sécher pendant la réunion |
| Échelle de poids | Mâles 4 ans+ 59,5 · juments 58 · mâles 3 ans 56,5 · pouliches 3 ans 55 [D] | Conforme au règlement. Les pouliches de 3 ans reçoivent 4,5 kg des mâles d'âge. |
| Partants | 16, aucun non-partant [D] | Peloton moyen |
| Open stretch | Oui, couloir d'environ 6 m [D] | La corde peut payer (axe A3) |
| Lice | 0 m, à confirmer [D] | — |
| Réunion | 5e course, 4 courses avant sur la même piste [D] | Piste un peu usée à la corde ; elle continue de sécher |

**Pattern dominant pour ce terrain** [E, **robuste**] : sous un pénétromètre de 4,2, **les 12 vainqueurs exploitables (2008–2025) étaient des 3 ans ou des femelles**. Aucun mâle de 4 ans ou plus n'a gagné dans ces conditions. Le favori Daryz est un **mâle de 4 ans**.

## Étape 2 : Normalisation et fiabilité

- **Données utilisées** : le dossier, qui tient un journal de 30 corrections. Il signale comme non tranchés : l'heure du pénétromètre, le conflit sur les Nassau Stakes (Friendly Soul et Diamond Necklace toutes deux données 2es), deux courses douteuses de Bay City Roller, la 2e course de Thundering On, le terrain du Derby d'Epsom.
- **Écarté** : la « lecture » de la carte de rythme du dossier. C'est une interprétation, et la règle de purge de l'étape 2 l'exclut. Je refais ma propre lecture à l'étape 6.
- **Stalles** : tirées du « tableau officiel des partants » cité par le dossier. Je les accepte [D], avec une confiance moyenne.
- **Normalisation de la valeur** : la valeur officielle (en kg) est ramenée au poids porté, en ajoutant la décharge reçue par rapport à un mâle d'âge. C'est la conversion des ratings sur une même échelle prévue à l'étape 2.

| Cheval | Valeur | Décharge | **Valeur ajustée au poids** |
|---|---|---|---|
| Maltese Cross (3 ans) | 56,0 | +3 | **59,0** |
| Diamond Necklace (pouliche 3 ans) | 54,5 | +4,5 | **59,0** |
| Benvenuto Cellini (3 ans) | 55,5 | +3 | **58,5** |
| Kalpana (jument) | 56,5 | +1,5 | **58,0** |
| Daryz (4 ans) | 57,5 | 0 | **57,5** |
| Thundering On (pouliche 3 ans) | 53,0 | +4,5 | **57,5** |
| Minnie Hauk (jument) | 54,5 | +1,5 | 56,0 |
| Varandir (3 ans) | 53,0 | +3 | 56,0 |
| Bay City Roller | 56,0 | 0 | 56,0 |
| Meisho Tabaru | 55,5 | 0 | 55,5 |
| Bright Light (3 ans) | 51,5 | +3 | 54,5 |
| Saddadd | 53,5 | 0 | 53,5 |
| Friendly Soul (jument) | 52,0 | +1,5 | 53,5 |
| Admire Terra | 52,0 | 0 | 52,0 |
| Arrow Eagle | 51,5 | 0 | 51,5 |
| Chestnut Rocket | 51,0 | 0 | 51,0 |

**Lecture** [D] : une fois le poids pris en compte, le meilleur cheval sur le papier, Daryz, se retrouve au **5e rang, ex aequo avec Thundering On**. La valeur d'un 3 ans est moins éprouvée que celle d'un cheval d'âge : c'est une donnée à pondérer, pas une vérité.

**Confiance globale : moyenne.** Les données sont riches mais pas toutes vérifiées, et le pipeline n'a jamais été testé à l'aveugle.

## Étapes 3 et 4 : Fiches individuelles et indice de compatibilité (IC)

Notes de 0 à 3. **IC = V + Vp/2 + F + D + T + bonus de poids.** En T1, le bonus vaut +2 pour une pouliche de 3 ans et +1 pour un mâle de 3 ans ou une jument d'âge.

| N° | Cheval | V | Vp | F | D | T | Bonus | **IC** | Style · stalle | Drapeaux / risques |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Daryz** (M4) | 3 | 3 | 3 | 3 | 3 | 0 | **13,5** | Placé · 5 | A gagné l'Arc 2025, l'Ispahan, le Ganay et le Foy [D]. Fiévreux en juin, revenu en forme. **Mâle d'âge sous 4,2 : 0 vainqueur sur 12 [E robuste]** |
| 9 | **Kalpana** (F5) | 3 | 3 | 3 | 3 | 2 | +1 | **13,5** | Milieu, peut se placer · 6 | A gagné le King George et les Yorkshire Oaks devant Benvenuto Cellini, Minnie Hauk et Thundering On [D]. 7e de l'Arc 2025 sur un terrain trop lourd [D] |
| 15 | **Thundering On** (F3) | 2 | 2 | 3 | 3 | 2 | +2 | **13,0** | Attentiste · 3 | A gagné les Oaks d'Epsom (2 420 m) et le Blandford il y a 21 jours [D]. **Battue de 4 longueurs par Kalpana et derrière Minnie Hauk à York [D]**. Changement de jockey |
| 14 | **Maltese Cross** (M3) | 2 | 3 | 3 | 3 | 2 | +1 | **12,5** | Milieu, placé · 11 | A gagné le Grand Prix de Paris sur le parcours et le Voltigeur par 4 longueurs ; 2e du Derby [D]. **N'a jamais affronté de chevaux d'âge** (V plafonnée) |
| 10 | **Friendly Soul** (F5) | 2 | 1 | 3 | 3 | 3 | +1 | **12,5** | **Mène** · 7 | A gagné le Vermeille en menant [D] ; valeur basse (52) ; arrêtée en juin [D] |
| 11 | **Varandir** (M3) | 2 | 2 | 3 | 2 | 3 | +1 | **12,0** | Milieu · 4 | **Drapeau « Niel »** (R3, 0 gagnant de l'Arc sur 13) · battu par Maltese Cross dans le Grand Prix de Paris · jamais face à des chevaux d'âge · même écurie que Daryz |
| 2 | **Saddadd** (M4) | 2 | 2 | 3 | 3 | 3 | 0 | **12,0** | Placé · 9 | A gagné le Grosser Preis von Baden sur 2 400 m en bon souple [D] (Groupe 1 allemand) |
| 8 | Minnie Hauk (F4) | 2 | 3 | 1 | 3 | 2 | +1 | **10,5** | Placée · 10 | 2e de l'Arc 2025 [D] ; forme en baisse (8e du King George, 3e à York) ; changement de jockey |
| 12 | Benvenuto Cellini (M3) | 2 | 3 | 1 | 3 | 2 | +1 | **10,5** | Attentiste · **1** | A gagné l'Irish Derby, 3e du King George [D] ; décevant dans le Niel ; choisi par R. Moore [D] |
| 16 | Diamond Necklace (F3) | 2 | 2 | 2 | 1 | 2 | +2 | **10,0** | Milieu · **16** | A gagné le Diane et la Poule d'Essai [D] ; **n'a jamais couru 2 400 m** ; 66 jours sans courir |
| 7 | Bay City Roller (M4) | 1 | 2 | 3 | 2 | 3 | 0 | **10,0** | **Mène** · 15 | 2e du Foy derrière Daryz [D] ; deux courses douteuses dans son palmarès |
| 13 | Bright Light (M3) | 1 | 1 | 2 | 3 | 2 | +1 | **9,5** | Attentiste · 8 | 2e du Grosser Preis von Berlin, 3e à Baden à 4 longueurs de Saddadd [D] |
| 5 | Meisho Tabaru (M5) | 2 | 2 | 2 | 1 | 2 | 0 | **8,0** | **Mène** · 13 | A gagné le Takarazuka [D] ; 112 jours sans courir ; Japonais : 0 victoire en 18 ans [E anecdotique] |
| 3 | Chestnut Rocket (M4) | 1 | 1 | 2 | 2 | 2 | 0 | **7,5** | Placé · 2 | Meilleure référence : 2e d'un Groupe 2 |
| 6 | Arrow Eagle (M5) | 1 | 1 | 2 | 2 | 1 | 0 | **6,5** | Attentiste · 14 | Aime le terrain lourd, ce qui n'est pas le cas aujourd'hui |
| 4 | Admire Terra (M5) | 1 | 1 | 1 | 2 | 1 | 0 | **5,5** | Milieu · 12 | 154 jours sans courir ; est tombé en octobre 2025 ; découvre la France |

**Autres signaux historiques** [E] :
- **R9**, déjà dans le top 5 de l'Arc l'année précédente (+1 cran pour les places) : Daryz et Minnie Hauk.
- **Gagnant du Grand Prix de Paris dans l'Arc** (vérifié sur 10 cas) : 0 victoire, 6 fois dans le top 5. Cela concerne Maltese Cross (pattern faible à prometteur, nouveau).
- **Ancien vainqueur de 4 ans qui revient** : Treve 2014 et Enable 2018 ont regagné, mais c'étaient des femelles. **Aucun précédent pour un mâle.**

## Étape 5 : Analyse tactique

- **Corde (stalles 1 à 6)** : Benvenuto Cellini (1), Chestnut Rocket (2), Thundering On (3), Varandir (4), Daryz (5), Kalpana (6).
- **À l'extérieur (13 et au-delà)** : Meisho Tabaru (13, meneur), Arrow Eagle (14), Bay City Roller (15, meneur), Diamond Necklace (16).
- **Écuries** :
  - Coolmore et A. O'Brien alignent 3 partants (Minnie Hauk, Benvenuto Cellini, Diamond Necklace), plus Thundering On via J. O'Brien. Aucun lièvre déclaré.
  - L'Aga Khan aligne Daryz et Varandir : un rôle d'équipier est possible pour Varandir [H].

## Étape 6 : Rythme probable

- **Leaders réels** : Friendly Soul (a mené dans le Vermeille [D]), Bay City Roller et Meisho Tabaru (profil « mène » [D]). **Il y en a trois**, donc le rythme sera **plutôt soutenu**.
- **Hypothèse inverse (au moins 20 %)** : les deux meneurs partis de l'extérieur (13 et 15) se calent derrière, et Friendly Soul mène seule sur un **rythme modéré** (règle R5).

## Étape 7 : Génération dynamique des scénarios (module 4 bis)

### Axes examinés
| Axe | État | Ouvert ? | Raison |
|---|---|---|---|
| A1, rythme | soutenu ou modéré | **Ouvert** | Trois meneurs, dont deux en dehors [D]. Friendly Soul entre dans le top 4 ou en sort selon le rythme. |
| A2, terrain | sèche (bon) ou reste bon souple | Fermé | Les deux états restent en T1 ou T2 : même bonus de poids, presque aucun effet sur le top 4 |
| A3, corde | la corde paie ou trajectoire neutre | **Ouvert** | Open stretch, 16 partants [D] ; Varandir entre dans le top 4 et Maltese Cross en sort |
| A4, le favori | Daryz confirme ou est battu | **Ouvert** | Pattern robuste contraire (mâle d'âge sous 4,2), fièvre en juin, et 4 chevaux plus haut que lui en valeur ajustée au poids [D/E] |
| A5, moment de l'effort | — | Absorbé par A1 | Dépend directement du rythme |
| A6, écurie | — | Absorbé par A1 | Un éventuel travail d'équipier ne change que le rythme |
| A7, incident | — | Risque général | Pas d'antécédent spécifique ; traité à l'étape 9 |

### Candidates, fusions et résultat
2 × 2 × 2 = **8 candidates**. Les scores combinent l'IC et les ajustements de l'étape 8 :
- rythme soutenu : grille S1 ;
- rythme modéré : grille S2 ;
- la corde paie : grille S4.

| Candidate | Groupe de tête (score) | Décision |
|---|---|---|
| C1 soutenu · neutre · Daryz OK | Daryz 15,5 · Kalpana 14,5 · Thundering On 14 · Maltese Cross 13,5 | Fusionnée → **SA** |
| C2 soutenu · corde · Daryz OK | Daryz 16,5 · Thundering On 16 · Kalpana 15,5 · Varandir 15 | Fusionnée → **SA** |
| C3 modéré · neutre · Daryz OK | Daryz 14,5 · Friendly Soul 14,5 · Kalpana 13,5 · Maltese Cross 13,5 | Fusionnée → **SA** |
| C4 modéré · corde · Daryz OK | Daryz 15,5 · Friendly Soul 15,5 · Kalpana 14,5 · Varandir 14 | Fusionnée → **SA** |
| C5 soutenu · neutre · Daryz battu | Kalpana 14,5 · Thundering On 14 · Maltese Cross 13,5 · Varandir 13 | Fusionnée → **SB** |
| C6 soutenu · corde · Daryz battu | Thundering On 16 · Kalpana 15,5 · Varandir 15 · Benvenuto Cellini 13,5 | Fusionnée → **SB** |
| C7 modéré · neutre · Daryz battu | Friendly Soul 14,5 · Kalpana 13,5 · Maltese Cross 13,5 · Saddadd 13 | Fusionnée → **SC** |
| C8 modéré · corde · Daryz battu | Friendly Soul 15,5 · Kalpana 14,5 · Varandir 14 · Saddadd 13 | Fusionnée → **SC** |

**Application de la règle de fusion** (même tête, au moins 3 chevaux communs sur 4 ; deux chevaux à ≤ 0,5 point d'écart sont traités comme co-têtes) :
- C1 à C4 gardent Daryz en tête avec Kalpana derrière : **1 scénario**.
- C5 et C6 ont pour co-têtes Kalpana et Thundering On : **1 scénario**.
- C7 et C8 ont Friendly Soul seule en tête : **1 scénario**.

➡️ **Résultat : 3 scénarios distincts.** Les axes rythme et corde ne créent pas de scénarios à eux seuls : ils déplacent Friendly Soul, Varandir et Maltese Cross **à l'intérieur** des scénarios. C'est l'axe « Daryz » qui renverse la hiérarchie.

---

## Les 3 scénarios

### SB : « Course sélective sans domination de Daryz »  ·  *Forte concordance*
1. **Déroulement** : Bay City Roller et Meisho Tabaru, partis de l'extérieur, viennent disputer la tête à Friendly Soul. Le rythme est soutenu dès la montée [D/E]. Le peloton s'étire. Dans la ligne droite, Daryz, sous 59,5 kg, ne fait pas la différence. Les chevaux qui reçoivent du poids et tiennent la distance finissent le mieux, en particulier ceux qui ont économisé du terrain à la corde.
2. **Conditions** : au moins deux meneurs se battent ; Daryz ne reproduit pas son niveau ou est simplement battu.
3. **Facteurs historiques** :
   - [E robuste] 12 vainqueurs sur 12 étaient des 3 ans ou des femelles sous 4,2 ;
   - [E robuste] le favori n'a gagné que 5 fois sur 16 ;
   - [E retenu] règle rythme × style : les meneurs ne se placent pas sur un rythme rapide.
4. **Favorisés** : **Kalpana**, **Thundering On**, Varandir (si la corde paie), Maltese Cross.
5. **Vulnérables** : les meneurs (Friendly Soul, Bay City Roller, Meisho Tabaru) ; Daryz, qui reste placé possible (R9).
6. **Progressent** par rapport au marché : Kalpana, Thundering On, Varandir.
7. **Régressent** : Daryz, Friendly Soul, Diamond Necklace (stalle 16, distance inconnue).
8. **Outsiders compatibles** : Saddadd (terrain et distance prouvés, R7) et Benvenuto Cellini (stalle 1, 3e du King George).
9. **Impact** : la hiérarchie se renverse en tête. Daryz passe du 1er rang à environ 6e.
10. **Ordre plausible** : Kalpana, Thundering On, Varandir, Maltese Cross, Saddadd.
11. **Arguments du pipeline** : R1 et R10, interaction rythme × style, valeur ajustée au poids (Kalpana 58 contre Daryz 57,5), S4 pour les stalles 3, 4 et 6.
12. **Pourquoi « forte concordance »** :
    - le rythme soutenu est annoncé par les données, avec trois meneurs dont deux en dehors ;
    - la victoire d'un cheval avantagé au poids repose sur le pattern le plus robuste de l'historique ;
    - contre : Daryz est le meilleur cheval sur le papier, a battu ces adversaires en 2025 et vient de gagner le Foy.

### SA : « Daryz confirme »  ·  *Concordance partielle*
1. **Déroulement** : Daryz, placé derrière les meneurs depuis la stalle 5, déboîte à 400 m et répète son succès de 2025, quel que soit le rythme.
2. **Conditions** : Daryz est au niveau de son Foy, et la fièvre de juin est oubliée.
3. **Facteurs historiques** :
   - [D] il a gagné l'Arc 2025 sur ce parcours, ainsi que l'Ispahan, le Ganay et le Foy ; il est 2 sur 2 sur 2 400 m ; il a la meilleure valeur brute ;
   - [E prometteur] R9 ;
   - **contre** : [E robuste] aucun mâle d'âge n'a gagné sous 4,2, et [E robuste] R10.
4. **Favorisés** : **Daryz**, puis Kalpana.
5. **Vulnérables** : tous les autres pour la victoire.
6. **Progressent** : Friendly Soul, si le rythme est modéré.
7. **Régressent** : Varandir et Maltese Cross (selon la corde).
8. **Outsiders compatibles** : Friendly Soul (R5, meneuse seule sur un rythme modéré).
9. **Impact** : la hiérarchie du marché est confirmée.
10. **Ordre plausible** : Daryz, Kalpana, Thundering On, Friendly Soul, Varandir.
11. **Arguments du pipeline** : IC de 13,5 (le plus haut, ex aequo), grille S1 (V = 3 et placé : +2), stalle 5.
12. **Pourquoi « partielle »** : les données propres au cheval sont excellentes, mais **aucun pattern robuste ne soutient la victoire d'un mâle d'âge dans ces conditions**, et un pattern robuste la contredit. Limite de ce raisonnement : l'échantillon de 12 courses ne contient **aucun ancien vainqueur de l'Arc revenu à 4 ans chez les mâles**, cas qui pourrait être l'exception.

### SC : « Friendly Soul contrôle un rythme modéré »  ·  *Hypothèse*
1. **Déroulement** : les deux meneurs de l'extérieur se calent derrière. Friendly Soul, partie de la stalle 7, mène seule et règle le rythme. Le peloton reste groupé et la course se joue au sprint à partir de 500 m, sans que Daryz ne domine.
2. **Conditions** : Bay City Roller et Meisho Tabaru renoncent à mener, et Daryz est en dessous de son niveau.
3. **Facteurs historiques** :
   - [E retenu] R5 et l'interaction rythme × style : un meneur non contesté sur un rythme lent se place (Persian King 2020, Los Angeles 2024) ;
   - [D] elle a gagné le Vermeille en menant sur ce parcours.
4. **Favorisés** : **Friendly Soul**, Kalpana, Maltese Cross, Saddadd.
5. **Vulnérables** : les attentistes extrêmes (Thundering On, Bright Light, Arrow Eagle).
6. **Progressent** : Friendly Soul, Saddadd.
7. **Régressent** : Thundering On, Daryz.
8. **Outsiders compatibles** : Friendly Soul (27–31/1), Saddadd (31–49/1).
9. **Impact** : un outsider gagne. Kalpana reste 2e.
10. **Ordre plausible** : Friendly Soul, Kalpana, Maltese Cross, Saddadd, Varandir.
11. **Arguments du pipeline** : grille S2 (meneur non contesté : +2 ; attentiste extrême : −2), R5.
12. **Pourquoi « hypothèse »** : il faut que deux meneurs renoncent, ce que rien n'annonce ; et la valeur de Friendly Soul (52) est l'une des plus basses.

---

## Étape 10 : Synthèse

**Poids indicatifs**, tirés des fourchettes du module 4b.6 puis normalisés : SB 35, SA 25, SC 8, soit **51 % / 37 % / 12 %**.
*Dans SB et SC, Daryz est placé conventionnellement au 6e rang. C'est un « placé possible », pas un effondrement.*

| Cheval | Rang SA | Rang SB | Rang SC | **Rang attendu** | Top 3 dans |
|---|---|---|---|---|---|
| **Kalpana** | 2 | 1 | 2 | **1,5** | 3 scénarios sur 3 |
| **Thundering On** | 3 | 2 | 7 | **3,0** | 2 sur 3 |
| **Varandir** | 5 | 3 | 5 | **4,0** | 1 sur 3 |
| **Daryz** | 1 | 6 | 6 | **4,2** | 1 sur 3 |
| **Maltese Cross** | 6 | 4 | 3 | **4,6** | 1 sur 3 |
| Saddadd | 7 | 5 | 4 | 5,6 | 0 |
| Friendly Soul | 4 | 8 | 1 | 5,7 | 1 sur 3 |
| Benvenuto Cellini | 8 | 7 | 9 | 7,6 | 0 |
| Minnie Hauk | 9 | 10 | 8 | 9,4 | 0 |
| Bay City Roller, Bright Light, Diamond Necklace, Chestnut Rocket | 10–13 | 9–13 | 10–14 | 10 à 13 | 0 |
| Meisho Tabaru, Arrow Eagle, Admire Terra | 14–16 | 14–16 | 13–16 | 14 à 16 | 0 |

**Contrôle de cohérence** : les chevaux favorisés par un scénario à 20 % ou plus (Daryz dans SA ; Kalpana et Thundering On dans SB) sont bien dans les 6 premiers ✅.

### Synthèse croisée (4b.7)
| Rubrique | Chevaux |
|---|---|
| Présents dans plusieurs scénarios (top 4 dans au moins 2 sur 3) | **Kalpana** (3/3), Thundering On, Maltese Cross, Friendly Soul |
| Chevaux de configuration (top 4 dans un seul scénario) | **Daryz** (SA), **Varandir** (SB), **Saddadd** (SC) |
| Très dépendants du déroulement (écart de rang ≥ 4) | Friendly Soul (du 1er au 8e), Daryz (du 1er au 6e), Thundering On (du 2e au 7e) |
| Profitent d'une défaillance du favori | Kalpana (2e → 1re), Thundering On (3e → 2e), Varandir (5e → 3e), Maltese Cross |
| Outsiders récurrents (≥ 20/1 et top 5 dans au moins 2 scénarios) | **Saddadd**, **Friendly Soul** |
| Soutenus par plusieurs familles d'arguments indépendants | **Kalpana** (valeur, poids, position, écart entre cote et valeur ; 4 familles) · Daryz (valeur, terrain, position, historique dans l'Arc ; 4 familles, mais un pattern robuste contre) · Maltese Cross (valeur ajustée, parcours, forme, poids ; 4 familles) |
| **Convergences** | Kalpana est toujours dans les 2 premiers. Admire Terra, Arrow Eagle, Meisho Tabaru et Chestnut Rocket ne sont jamais dans les 8 premiers. |
| **Divergences** | L'axe Daryz décide du vainqueur. Le rythme décide du sort de Friendly Soul et de Thundering On. La corde décide de Varandir contre Maltese Cross. |

## Étape 9 : Risques et confrontation avec le marché

| Cheval | Modèle (victoire) | Marché à 12h, sans marge | Écart | Explication à chercher |
|---|---|---|---|---|
| Kalpana | **~28 %** | 9,7 % | Modèle bien plus optimiste | Pourquoi le marché la boude-t-il ? Son 7e rang de 2025 tient au terrain. Il **manque peut-être une information** (santé, travail du matin). |
| Daryz | **~20 %** | 35,8 % | Modèle plus pessimiste | Cet écart repose sur **un seul pattern**, robuste mais jamais testé sur un ancien vainqueur. C'est le pari le plus risqué de l'analyse. |
| Thundering On | ~18 % | 6,6 % | Plus optimiste | ⚠️ **Contradiction avec les confrontations directes** : elle a été battue de 4 longueurs par Kalpana et a fini derrière Minnie Hauk à York [D]. Le pipeline ne contrôle pas encore ce point (voir la section 13). |
| Varandir | ~8 % | 8,7 % | Proche | — |
| Maltese Cross | ~7 % | 9,5 % | Proche | — |
| Diamond Necklace | < 3 % | 8,8 % | Plus pessimiste | Pénalisée par la distance inconnue et la stalle 16 : ces raisons ne sont pas des variables trompeuses. Soumillon est un atout non modélisé. |
| Friendly Soul / Saddadd | ~5 % / ~3 % | 3,0 % / 2,6 % | Proche | — |

**Risques individuels** :
- Daryz : fièvre en juin ;
- Thundering On : un seul cheval, sa forme dans les courses de juin à août n'est pas sûre (2e course à vérifier) ;
- Varandir : changement de jockey probable ;
- Minnie Hauk : changement de jockey, forme en baisse ;
- Diamond Necklace : distance inconnue.

## Étape 11 : Groupes (seuils relatifs à 3 scénarios)
- **G1, solides** : **Kalpana** (top 3 dans les 3 scénarios, 4 familles d'arguments). Selon la règle, **Thundering On** entre aussi en G1 (top 3 dans 2 scénarios sur 3) ⚠️, mais elle porte le drapeau « confrontation directe défavorable ».
- **G2** : aucun autre cheval.
- **G3, dépendants du scénario** :
  - **Daryz** (dans SA) ;
  - Varandir (SB) ;
  - Maltese Cross (SC) ;
  - Friendly Soul (SC).
- **G4, à risque pour la victoire** : Saddadd (mais outsider récurrent pour les places), Benvenuto Cellini, Minnie Hauk, Diamond Necklace, Bay City Roller, Bright Light, Meisho Tabaru, Chestnut Rocket, Arrow Eagle, Admire Terra.

## Étape 12 : Ordres d'arrivée possibles

| Ordre | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| **Synthétique** (rang attendu) | Kalpana | Thundering On | Varandir | Daryz | Maltese Cross |
| **SB** : course sélective sans domination de Daryz (51 %) | Kalpana | Thundering On | Varandir | Maltese Cross | Saddadd |
| **SA** : Daryz confirme (37 %) | Daryz | Kalpana | Thundering On | Friendly Soul | Varandir |
| **SC** : Friendly Soul contrôle (12 %) | Friendly Soul | Kalpana | Maltese Cross | Saddadd | Varandir |
| Outsider (signaux R5 et R7 : Friendly Soul, Saddadd) | *identique à SC, non dupliqué (règle de l'étape 12)* | | | | |

**Probabilités indicatives de victoire** :
- Kalpana environ 28 % (plafond R10 respecté) ;
- Daryz environ 20 % ;
- Thundering On environ 18 % ;
- Varandir environ 8 % ;
- Maltese Cross environ 7 % ;
- Friendly Soul environ 5 % ;
- les autres environ 14 % au total.

*Ces chiffres découlent des poids de scénarios et de parts de victoire supposées dans chaque scénario. Ils servent à comparer, pas à parier.*

## Mises à jour avant 16h05 (si de nouvelles données arrivent)
- **Pénétromètre officiel ≥ 3,8** (pluie imprévue) : refaire l'étape 7. L'axe terrain s'ouvrirait, et Arrow Eagle comme Saddadd remonteraient.
- **Non-partant** Bay City Roller ou Meisho Tabaru : SC devient bien plus probable (Friendly Soul seule en tête).
- **Changement de jockey confirmé ou équipement déclaré** (œillères pour la première fois) : à noter, sans effet attendu (variable faible).

## 13. Faiblesses du pipeline révélées par ce test (non corrigées, à évaluer à l'audit)
1. **Pas de contrôle des confrontations directes** : Thundering On sort 2e alors qu'elle a été battue par Kalpana et Minnie Hauk il y a six semaines. Proposition à tester : une étape 9 bis où une confrontation récente à poids comparables limite l'écart de rang autorisé.
2. **Le rang attendu pénalise les chevaux à issue binaire** : Daryz, 1er ou environ 6e, finit 4e de la synthèse alors que sa probabilité de victoire est la 2e. Il faut donc toujours lire les deux indicateurs ensemble.
3. **Le pattern « mâle d'âge sous 4,2 » n'a jamais été testé sur un ancien vainqueur.** Si Daryz gagne, il faudra l'ajouter comme condition d'échec du pattern R1.
4. **Précision apportée à la règle de fusion** : deux chevaux à ≤ 0,5 point d'écart sont traités comme co-têtes. C'est une clarification d'application, pas un changement de pondération.

## Registre pré-course
- **Course** : Arc 2026 ; **date** : 4 octobre 2026.
- **Ordre synthétique** : 1 Kalpana, 2 Thundering On, 3 Varandir, 4 Daryz, 5 Maltese Cross, 6 Saddadd, 7 Friendly Soul, 8 Benvenuto Cellini.
- **Scénarios retenus (3)** :
  - SB, course sélective sans domination de Daryz (forte concordance, 51 %) ;
  - SA, Daryz confirme (concordance partielle, 37 %) ;
  - SC, Friendly Soul contrôle (hypothèse, 12 %).
- **Axes ouverts** : rythme, corde, Daryz. **Axe fermé** : terrain. **Candidates** : 8, **fusions** : 8 → 3.
- **Très solides** : Kalpana. **Dangereux** : Daryz, Thundering On. **Dépendants du scénario** : Friendly Soul, Varandir, Maltese Cross.
- **Potentiellement sous-évalués** : Kalpana (9,7 % au marché), Saddadd. **Potentiellement surévalués** : Daryz (pour la victoire), Diamond Necklace.
- **Principales hypothèses** :
  - l'avantage de poids reste décisif en bon souple ;
  - trois meneurs, donc un rythme soutenu.
- **Principaux risques d'erreur** :
  - Daryz est l'exception au pattern R1 ;
  - les confrontations directes de Thundering On ;
  - une information de marché manquante sur Kalpana.
- **Variables déterminantes** : statut d'âge et poids, valeur ajustée, rythme.
- **Variables incertaines** : la corde (stalles non vérifiées par une source officielle), le rôle d'équipier de Varandir, la forme réelle de Minnie Hauk.
- **À observer après la course** :
  - quel scénario s'est réalisé, ou lequel manquait ;
  - qui a mené et le rythme réel ;
  - les positions à 600 m ;
  - la trajectoire de Daryz ;
  - si Kalpana a été placée ou attentiste.
