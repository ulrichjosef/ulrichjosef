# Analyse hippique rétrospective à l'aveugle — Prompt maître V1.0

**Source :** `Courses_AVANT.docx` (14 courses, Vincennes, 2 850 m)
**Règle appliquée :** chaque course est analysée uniquement avec son propre tableau, comme si elle n'avait pas encore été courue. Aucune recherche externe, aucun résultat consulté, aucune connaissance personnelle d'arrivée mobilisée.

---

## 0. Audit préalable du jeu de données

### 0.1 Contrôle des fuites (informations post-course)

- **Aucun résultat officiel, rapport PMU ou commentaire d'après-course** dans le document. L'analyse aveugle est possible.
- **Contamination croisée entre courses : à nettoyer.** Plusieurs chevaux apparaissent dans deux courses du dossier. La musique fournie pour la course la plus récente couvre très probablement la course plus ancienne, et révèle donc la place obtenue dans celle-ci :
  - Indien de Fontaine (Thémis 2024 → Camargue 2024)
  - Lucky Guy Boko (Thémis 2024 → Thémis 2025)
  - Jolie Surprise (Vic sur Cère 2025 → Thémis 2025)
  - Cas possibles mais moins nets : Firello (Thémis 2021 → 2022), Eberton (2020 → 2023), Fougue du Dollar (Thémis 2023 → Andrieu 2025)
  
  **Traitement :** je n'ai pas croisé les tableaux. Chaque course a été classée avec ses seules données, et je ne commente aucune place révélée. Pour la phase suivante (comparaison aux arrivées), il faut tronquer ces musiques à la date de chaque course.
- **Cote finale :** selon ta note, c'est la dernière information du marché avant le départ. Elle est donc admissible. Je ne l'utilise pas pour construire le classement (qui repose sur les données sportives). Elle sert seulement, **après coup**, de point de comparaison pour repérer les chevaux que le marché sur- ou sous-estime. Elle sert de seule source **uniquement** pour les chevaux sans aucune donnée sportive (Thémis 2025), et c'est signalé.

### 0.2 Limites communes à toutes les courses

| Donnée | Problème | Conséquence |
|---|---|---|
| Type de départ | Non précisé. Le recul de 25 m implique un **départ volté** (hypothèse) | Le risque de faute au départ pèse plus |
| Terrain / météo | Souvent « non renseigné » | Facteur neutralisé |
| Dates des courses de la musique | Absentes | Fraîcheur et intervalle impossibles à évaluer |
| Record | Sans contexte (autostart, piste, distance) | Utilisé comme indicateur de vitesse, pas comme preuve |
| Colonne « Crack » | Définition inconnue (indice de classement ? plus bas = mieux classé ?) | Poids quasi nul, cité seulement en appoint |
| « Moy. gains » | Gain moyen par course (supposé) | Utilisé comme indicateur de classe |
| Musique | Coquilles probables : « D7 », « D5 », « 7d », « 7ha », « Aia » | Lues au mieux (D = disqualifié, A = arrêté) |
| Chevaux étrangers | Musique française vide (Quick Fix, Partizan Face, Valokaja Hindo, Niky Flax, Bottnas Idol…) | Forte incertitude, ni bonus ni malus automatique |
| Courses montées | Colonne « Driver » = jockey | Pris en compte |

### 0.3 Grille de lecture commune (rappel des conventions)

- **Musique** : du plus récent au plus ancien ; `a` attelé, `m` monté ; `0` = au-delà de la 9e place ; `D` = disqualifié ; `A` = arrêté.
- **Ferrure** : `D4` déferré des quatre pieds ; `DA` antérieurs ; `DP` postérieurs ; `PA` plaqué antérieurs ; `PADP` plaqué antérieurs + déferré postérieurs ; `F4` ferré. Le déferrage est en principe un signe d'objectif, mais **je ne lui attribue pas automatiquement un effet positif** : il augmente aussi le risque de faute.
- **Position dans l'échelon** : sur un 2 850 m avec recul, le cheval aux gains les plus proches de la limite **sans** recul est structurellement le mieux placé (le plus riche de la ligne de 2 850 m). Celui qui dépasse **à peine** le seuil de recul est structurellement le moins bien placé (25 m de handicap face à des chevaux souvent bien plus riches que lui).

### 0.4 Hiérarchie de facteurs (variable selon la course)

1. **Fiabilité** (nombre de D/A récents) : décisive en départ volté sur 2 850 m.
2. **Forme récente et niveau démontré** (musique + gain moyen).
3. **Échelon et position dans l'échelon** (25 m ≈ 1,5 s de handicap théorique).
4. **Vitesse démontrée** (record), avec prudence.
5. **Ferrure et entourage** (driver, entraîneur).
6. **Cote** : contrôle a posteriori uniquement.

Les catégories d'évaluation (Très forte / Forte / Crédible / Secondaire / Fragile) sont **qualitatives**. Je ne donne pas de pourcentages : les données (sans dates, sans temps de course, sans terrain) ne permettent pas une calibration honnête.

---
## Course 1 — Prix Thémis 2015 (R5 C3, vendredi 16/10/2015, 20 h 57)

### A. Identification
Trot attelé (déduit des musiques), course C, 2 850 m, 65 000 €, 6 à 10 ans, gains < 349 000 €, recul de 25 m à 176 000 €. **18 partants** : 10 à 2 850 m, 8 à 2 875 m. Terrain non renseigné. Pas de cotes. Quick Fix sans données françaises exploitables.

### B. Lecture générale
Lot nombreux et hétérogène. Le premier échelon est mené par un cheval en série (Viking Blue, 5 victoires). Le second contient les plus riches et les meilleurs records (Tropic du Hêtre 1'11"60, Sergent du Rib 1'12"10). À 18 partants en volté, la course sera probablement encombrée : risque de trafic et parcours en 2e/3e épaisseur pour les numéros extérieurs de chaque ligne.

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant |
|---|---|---|---|---|
| 1 | Okay Dei Ronchi | Très régulier (4-4-6-4-5), sans faute, record 1'12"00 | Aucune victoire récente, le plus pauvre (117 887 €), ferré | Placeur, pas gagneur |
| 2 | Pingus Vang | Gain moyen élevé (5 166 €) | **3 D consécutifs** | Fiabilité rédhibitoire |
| 3 | Head Line | D4, record 1'12"20 | Irrégulier (0-5m-1-0-7) | Inconstance |
| 4 | Vulcania de Godrel | **Très régulière** (3-2-2-0-2), DP, record 1'12"10 | Pas de victoire récente | Régularité sur le 1er échelon |
| 5 | Vella Blue | D4, Monclin, 4 060 €/course | 0a à sa dernière, un D | Forme en baisse ? |
| 6 | Vasco de Viette | **Meilleur record du 1er échelon (1'11"80)**, 2 victoires sur 5, Gelormini | D à sa dernière, ferré | Vitesse vs fiabilité |
| 7 | Quick Fix | D4, Kolgjini, gains 165 912 € | Une seule ligne (Da), pas de record, données étrangères absentes | **Inconnue majeure** |
| 8 | Farmer's Julia | 2 victoires sur 5, B. Goop | Record lent (1'13"60), un D, irrégulière | Niveau réel incertain |
| 9 | Viking Blue | **5 victoires d'affilée**, 5 763 €/course, 171 708 € (tout en haut du 1er échelon) | **Record lent (1'14"10)** : vitesse non prouvée à ce niveau, ferré | Forme maximale, vitesse à confirmer |
| 10 | Velinotte du Derby | — | 0-7-0-4-6m, record 1'13"80 | Pas d'argument |
| 11 | Theo d'Erah | Régulier dans l'accessit | Recul, record 1'13"40, pas de victoire | Insuffisant avec 25 m |
| 12 | Prince Di Poggio | **Gain moyen le plus élevé (13 046 €)**, indice Crack le plus bas (53), record 1'12"30 | Recul, ferré, 5a à sa dernière | Classe pure |
| 13 | Team Job | 312 480 € de gains | 0-0-2, seulement 3 lignes | Forme absente |
| 14 | Tip Top Nelliere | D4, régulier (2-6-2-6-6), record 1'12"50 | Recul, pas de victoire | Placé possible |
| 15 | Tropic du Hêtre | **Meilleur record du lot (1'11"60)**, D4, J.-M. Bazire, vainqueur à sa dernière | Recul, irrégularité ancienne (0a) | Combinaison vitesse + ferrure + driver |
| 16 | Tafaiko Sax | 2 victoires sur 5, record 1'12"20 | Deux 0a récents, recul, ferré | Forme en baisse |
| 17 | Tina Jolie | 2e deux fois, 5 708 €/course | **2 D sur 5**, recul | Fiabilité |
| 18 | Sergent du Rib | Le plus riche (344 601 €, au plafond), DP, record 1'12"10 | 9-9-0 avant son 2a, recul | Classe, retour en forme ? |

### D. Scénario prévisionnel
- **Principal :** les chevaux du 1er échelon font la course. Viking Blue et Vulcania de Godrel devraient se placer tôt. Vasco de Viette peut accélérer, au risque de la faute. Les reculés (Tropic du Hêtre, Prince Di Poggio, Sergent du Rib) remontent progressivement et ont besoin d'un train soutenu pour combler les 25 m. Avec 18 partants, un rythme soutenu est plausible.
- **Alternative :** un train lent en tête favorise le 1er échelon (Viking Blue, Vulcania, Okay Dei Ronchi) et pénalise les reculés.
- **Risques :** fautes au départ (Pingus Vang, Tina Jolie, Vasco de Viette), trafic pour les numéros extérieurs.

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 15 | Tropic du Hêtre | Très forte | Meilleur record, D4, Bazire, vainqueur à sa dernière : compense le recul |
| 2 | 9 | Viking Blue | Forte | Série de 5 victoires, haut du 1er échelon ; seul doute : sa vitesse |
| 3 | 4 | Vulcania de Godrel | Forte | La plus régulière, sans recul |
| 4 | 6 | Vasco de Viette | Candidat crédible | Meilleur record du 1er échelon, mais D récent |
| 5 | 12 | Prince Di Poggio | Candidat crédible | Classe (gain moyen record) handicapée par le recul et la ferrure |
| 6 | 5 | Vella Blue | Candidat crédible | D4, références correctes, dernière course décevante |
| 7 | 18 | Sergent du Rib | Candidat crédible | Le plus riche, mais forme en dents de scie |
| 8 | 8 | Farmer's Julia | Candidat crédible | Gagneuse, mais record lent |
| 9 | 14 | Tip Top Nelliere | Candidat secondaire | Régulier mais rarement gagnant, recul |
| 10 | 1 | Okay Dei Ronchi | Candidat secondaire | Régulier mais ne gagne pas |
| 11 | 7 | Quick Fix | Candidat secondaire | Inconnue : à classer au milieu faute de données |
| 12 | 16 | Tafaiko Sax | Candidat secondaire | Forme en baisse |
| 13 | 3 | Head Line | Candidat secondaire | Irrégulier |
| 14 | 11 | Theo d'Erah | Candidat fragile | Pas de vitesse suffisante pour le recul |
| 15 | 17 | Tina Jolie | Candidat fragile | 2 D sur 5 |
| 16 | 2 | Pingus Vang | Candidat fragile | 3 D consécutifs |
| 17 | 13 | Team Job | Candidat fragile | Forme absente |
| 18 | 10 | Velinotte du Derby | Candidat fragile | Aucun argument |

### F. Points phares
- **Facteurs déterminants :** (1) l'opposition **forme (Viking Blue) / vitesse et classe (Tropic du Hêtre)** ; (2) la fiabilité en volté (élimine Pingus Vang et Tina Jolie) ; (3) le recul de 25 m face à des records espacés de 2 s/km ; (4) le D4 associé à J.-M. Bazire.
- **Choix le plus difficile :** Tropic du Hêtre 1er devant Viking Blue. Les 25 m de recul (~1,5 s) pèsent moins que les 2,5 s/km d'écart de record. Mais ce record lent peut venir de courses en province ou sur terrain lourd. **Si Viking Blue a la vitesse cachée que sa série suggère, l'ordre s'inverse.**
- **Sous-évalués possibles :** Sergent du Rib (le plus riche, simple retour de forme), Vulcania de Godrel (pas de victoire, mais ne se trompe pas).
- **Surestimables :** Pingus Vang (son gain moyen élevé masque 3 fautes), Prince Di Poggio (classe énorme sur le papier, mais recul + ferré + forme 2-4-7-1-5).
- **Risques de renversement :** une faute de Tropic du Hêtre au départ ; un tempo lent ; la vraie valeur de Quick Fix.

### G. Bilan
- **Faits :** musiques, records, gains, ferrures, échelons.
- **Interprétations :** Viking Blue est en forme ascendante ; Tropic du Hêtre a la meilleure vitesse.
- **Hypothèses :** départ volté ; train soutenu.
- **Incertitudes :** contexte du record de Viking Blue ; Quick Fix ; terrain.
- **Hypothèses qui pèsent le plus :** (1) le record de 1'14"10 reflète une vraie limite de vitesse ; (2) le recul est rattrapable sur 2 850 m pour un cheval à 1'11"60.

---

## Course 2 — Prix Le Parisien (Prix Thémis) 2018 (R1 C2, vendredi 19/10/2018, 20 h 15)

### A. Identification
Trot attelé, course C, 2 850 m, 65 000 €, 6 à 10 ans, gains < 362 000 €, recul à 178 000 €. **16 partants** : 8 + 8. Terrain non renseigné. Pas de cotes. Valokaja Hindo sans musique.

### B. Lecture générale
Second échelon nettement plus rapide (trois records ≤ 1'12"00 : Lover Face, Ange de Lune, Tripolini V P). Premier échelon plus lent (aucun record sous 1'12"90) mais en forme : Visitor, Buzz de Carel. Course de **vitesse au second échelon contre forme au premier**.

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant |
|---|---|---|---|---|
| 1 | Toohotforyou | D4, Ouvrie, 3a à sa dernière | 9-7-Dm avant, record 1'13"00 | Moyen |
| 2 | Choriste du Trio | Record 1'12"90 | Une seule place (3-8-7-5-7), ferré | Faible |
| 3 | Valokaja Hindo | D4, A. Abrivard, entraînement Bazire | **Aucune musique, aucun record** | Inconnue |
| 4 | Cristal du Lupin | D4, 2 victoires sur 5, 5 521 €/course | 8a et 6a intercalés | Crédible au 1er échelon |
| 5 | Artiste de Tillard | D4 | **2 D sur 5** | Fiabilité |
| 6 | Visitor | **Forme (2-1-1)**, D4, Raffin, haut de l'échelon (175 650 €) | Record lent (1'14"10), un D ancien, 9 ans | Forme sans recul |
| 7 | Buzz de Carel | D4, Monclin, haut de l'échelon, en progression (6-3-2-1 lu à rebours) | D ancien, record 1'13"20 | Crédible |
| 8 | Onceforall Face | Vercruysse, 3 places/victoire sur 5 | **2 D sur 5**, alterne faute et place | Fiabilité |
| 9 | Babylone Seven | 7 231 €/course, entraînement Bazire, 2 victoires | 0a à sa dernière, ferrée, la moins riche du 2e échelon (260 330 €) | Mal placée dans l'échelon |
| 10 | Lover Face | **Meilleur record (1'11"20)**, D4, **Nivard**, régulier (4-2-2-9-4) | Recul, 10 ans, ne gagne plus | Vitesse + régularité |
| 11 | Tripolini V P | **Très régulier (2-1-3-2-7)**, 10 996 €/course, record 1'12"00 | Recul, DA seulement | Régularité + classe |
| 12 | Ange de Lune | Record 1'11"20, D4, M. Abrivard, 2e deux fois | 0a ancien, recul | Vitesse |
| 13 | Beaute de Bailly | D4, Mottier | 6-0-D-7-4 | Faible |
| 14 | Uppercut Orange | — | 9-7-Dm-6-9, 10 ans, ferré | Aucun argument |
| 15 | Venezia de Mai | Record 1'11"90, D4, 2a à sa dernière | 0a deux fois, 2 279 €/course | Irrégulière |
| 16 | Astral Viretaute | DP | 8-8-3-0-0 | Faible |

### D. Scénario prévisionnel
- **Principal :** Visitor et Buzz de Carel se positionnent bien au 1er échelon. Les reculés rapides (Lover Face, Tripolini V P, Ange de Lune) viennent au contact au train et dominent la fin de course si le rythme est sélectif.
- **Alternative :** un train modéré profite à Visitor, qui peut garder son avance de 25 m.
- **Risques :** fautes d'Onceforall Face et d'Artiste de Tillard au départ.

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 10 | Lover Face | Forte | Meilleur record, D4, Nivard, très régulier |
| 2 | 6 | Visitor | Forte | Meilleure forme du 1er échelon, sans recul |
| 3 | 11 | Tripolini V P | Forte | Le plus régulier du 2e échelon, gain moyen élevé |
| 4 | 12 | Ange de Lune | Candidat crédible | Vitesse (1'11"20), D4 |
| 5 | 4 | Cristal du Lupin | Candidat crédible | Gagnant récent, D4 |
| 6 | 7 | Buzz de Carel | Candidat crédible | En progression, haut de l'échelon |
| 7 | 9 | Babylone Seven | Candidat crédible | Classe, mais ferrée et mal placée dans l'échelon |
| 8 | 8 | Onceforall Face | Candidat secondaire | Capable d'une place, mais une course sur deux en faute |
| 9 | 3 | Valokaja Hindo | Candidat secondaire | Entourage fort, données nulles |
| 10 | 15 | Venezia de Mai | Candidat secondaire | Vitesse mais irrégulière |
| 11 | 1 | Toohotforyou | Candidat secondaire | Moyenne |
| 12 | 13 | Beaute de Bailly | Candidat fragile | Forme absente |
| 13 | 2 | Choriste du Trio | Candidat fragile | Une place sur 5 |
| 14 | 5 | Artiste de Tillard | Candidat fragile | 2 D sur 5 |
| 15 | 16 | Astral Viretaute | Candidat fragile | Deux 0a récents |
| 16 | 14 | Uppercut Orange | Candidat fragile | Aucun argument |

### F. Points phares
- **Facteurs déterminants :** les records du 2e échelon (1'11"20 ×2) contre le 1'14"10 de Visitor ; la régularité de Lover Face et Tripolini ; la fiabilité.
- **Choix difficile :** Lover Face devant Visitor. Lover Face ne gagne plus (placeur), mais sa vitesse et son driver couvrent le recul. Visitor peut l'emporter si le train est lent.
- **Surestimable :** Babylone Seven (gain moyen élevé, mais 0a à sa dernière, ferrée et mal placée dans l'échelon).
- **Potentiel caché :** Valokaja Hindo (entourage Bazire / Abrivard, D4), sans aucune preuve.

### G. Bilan
- **Hypothèses clés :** (1) train sélectif ; (2) Visitor manque de vitesse de pointe (record lent).
- **Limite principale :** aucune information sur les dates (fraîcheur) ni sur le contexte des records.

---

## Course 3 — Prix Thémis 2019 (R1 C3, vendredi 18/10/2019, 20 h 15)

### A. Identification
Trot attelé, course C, 2 850 m, 58 000 €, 6 à 10 ans, gains < 365 000 €, recul à 181 000 €. Terrain **bon**. **16 partants** : 10 + 6. Cotes partielles : Douceur du Chêne ≈ 4,2 (favorite), Partizan Face ≈ 5,1.

### B. Lecture générale
Premier échelon fourni et déferré presque entièrement (D4 partout sauf Dastavia, DP). Le second est réduit (6) et irrégulier, à l'exception d'Aron The Baron. **L'avantage structurel semble au 1er échelon.**

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant |
|---|---|---|---|---|
| 1 | Dream | Vainqueur à sa dernière, D4, Monclin | 0-5-6-6 avant, record 1'13"30 | Forme récente isolée |
| 2 | Partizan Face | D4, Ouvrie/Kolgjini, cote ≈ 5,1 | **Aucune donnée française** | Inconnue |
| 3 | Delmonica | **2 victoires consécutives**, D4, record 1'12"60 | Un D | Forme |
| 4 | Cuba Libre | Record 1'11"90 | 7-1-6-7-8 | Irrégulier |
| 5 | Desperado | 7 037 €/course (classe), Bazire | 0-9-D-2-0 | Hors de forme |
| 6 | Donuts Deladou | 3-2 récents, record 1'12"10, D4 | 0-0 plus anciens | En reprise de forme |
| 7 | Dona Viva | Gagnante, 2-2, 5 482 €/course | **2 D sur 5 (dont la dernière)** | Fiabilité |
| 8 | Dastavia de Guez | 5 942 €/course | **3 fois 0a consécutifs** | Forme absente |
| 9 | Douceur du Chêne | **Meilleur record du 1er échelon (1'11"20)**, Nivard, 2 victoires, haut de l'échelon (180 440 €) | Un D ancien | Vitesse + forme + position |
| 10 | Danseur Baroque | Haut de l'échelon | « D7 » (coquille ?), 0-4-0-6m | Faible |
| 11 | Aron The Baron | **Régulier (6-2-2-4-1)**, record 1'11"50, Thomain | Recul, DP | Meilleur du 2e échelon |
| 12 | Bauloise Haufor | Record 1'11"60, 6 468 €/course | 7-5-0-9-0 | Irrégulière |
| 13 | Codie de Beaulieu | Record 1'11"50 | 0-0-9-0-9, ferrée | Aucune forme |
| 14 | Tinamo Jet | Record 1'11"40, Raffin, 3-3 | **3 D sur 5** | Fiabilité |
| 15 | Dreambreaker | **13 326 €/course (classe)**, N. Bazire, 2-2 anciens | 0a à sa dernière, ferré | Classe sans forme |
| 16 | Be Bop Haufor | DP | 0-6-5-5-D | Faible |

### D. Scénario prévisionnel
- **Principal :** Douceur du Chêne et Delmonica prennent une bonne place au 1er échelon et contrôlent. Aron The Baron remonte. Les autres reculés manquent de constance pour combler les 25 m.
- **Alternative :** si Partizan Face a le niveau que suggère sa cote, il s'intercale aux premières places.

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 9 | Douceur du Chêne | Très forte | Vitesse, forme, position idéale dans l'échelon |
| 2 | 3 | Delmonica | Forte | Deux victoires consécutives |
| 3 | 11 | Aron The Baron | Forte | Seul reculé régulier |
| 4 | 2 | Partizan Face | Candidat crédible | Entourage et marché favorables, données nulles |
| 5 | 6 | Donuts Deladou | Candidat crédible | En reprise (3-2), record 1'12"10 |
| 6 | 15 | Dreambreaker | Candidat crédible | Classe, mais ferré et hors de forme |
| 7 | 7 | Dona Viva | Candidat secondaire | Valeur réelle, fiabilité douteuse |
| 8 | 1 | Dream | Candidat secondaire | Victoire isolée |
| 9 | 5 | Desperado | Candidat secondaire | Classe sans forme |
| 10 | 14 | Tinamo Jet | Candidat secondaire | Vitesse, mais 3 D sur 5 |
| 11 | 12 | Bauloise Haufor | Candidat fragile | Irrégulière |
| 12 | 4 | Cuba Libre | Candidat fragile | Irrégulier |
| 13 | 10 | Danseur Baroque | Candidat fragile | Forme faible |
| 14 | 8 | Dastavia de Guez | Candidat fragile | 3 fois 0a |
| 15 | 16 | Be Bop Haufor | Candidat fragile | Forme faible |
| 16 | 13 | Codie de Beaulieu | Candidat fragile | Aucune forme |

### F. Points phares
- **Facteurs déterminants :** la position de Douceur du Chêne (la plus riche du 1er échelon et la plus rapide) ; la faiblesse globale du 2e échelon ; la fiabilité (Tinamo Jet, Dona Viva).
- **Surestimable :** Dreambreaker (gain moyen spectaculaire, mais forme et ferrure défavorables).
- **Incertitude majeure :** Partizan Face, classé 4e uniquement à partir de son entourage, sans preuve sportive.

### G. Bilan
- **Hypothèses clés :** (1) le 1er échelon garde l'avantage ; (2) Douceur du Chêne reste sans faute.
- **Limite :** cheval étranger non évaluable.

---
## Course 4 — Prix Thémis 2020 (R1 C2, vendredi 16/10/2020, 19 h 03)

### A. Identification
Trot attelé, course C, 2 850 m, 49 000 €, 6 à 10 ans, gains < 365 000 €, recul à 183 000 €. Terrain non renseigné (« généralement bon » n'est pas une donnée : non exploité). **13 partants** : 5 + 8. Pas de cotes. Niky Flax avec une seule ligne de musique.

### B. Lecture générale
Lot **peu fiable** : une majorité de partants a un D ou un A dans ses cinq dernières sorties. Le second échelon est majoritaire et plus rapide. Course ouverte où **la fiabilité sera aussi décisive que la valeur**.

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant |
|---|---|---|---|---|
| 1 | Eberton | Vainqueur à sa dernière | **3 D sur 5**, le plus pauvre, record 1'13"40 | Fiabilité |
| 2 | Etenclin | Record 1'11"80, D4, 6 261 €/course, A. Abrivard | **3 D sur 4** | Talent non fiable |
| 3 | Catch My Love | D4, Goop, record 1'11"80 | Gain moyen très bas (1 250 €), 0m-3m-0a-D | Faible |
| 4 | Niky Flax | 12 600 €/course, gagnant | Une seule ligne, record 1'15"10, cheval étranger | Inconnue |
| 5 | Helena di Quattro | **Meilleur record du 1er échelon (1'10"80)**, Nivard, D4, proche de la limite | Forme moyenne (7-5-2-9-8) | Vitesse sans forme |
| 6 | Darling Berry | N. Bazire | A, D, 0a récents, ferrée | Fragile |
| 7 | Defi Pierji | D4 | 9-9-2-0-7 | Faible |
| 8 | Dollar Soyer | D4, Barrier, 2a à sa dernière, sans faute | 0a ×2 | Régulier pour ce lot |
| 9 | Django du Bocage | **Vainqueur à sa dernière**, D4, Lebourgeois, record 1'11"80 | Un D (avant-dernière), recul | Meilleure forme |
| 10 | Calle Crown | **11 211 €/course (classe)**, record 1'11"10, Thomain | D à sa dernière, recul | Classe |
| 11 | Daelia de Vandel | — | 0-6-0-0-Dm, ferrée | Aucun argument |
| 12 | Christo | Record 1'11"50 | 2 D, 0a à sa dernière | Fragile |
| 13 | Epic Julry | Record 1'10"90 | D-9-9-6-0 | Vitesse sans forme |

### D. Scénario prévisionnel
Course probablement décousue : fautes au départ attendues. Helena di Quattro et Dollar Soyer peuvent profiter d'un parcours sans histoire. Django du Bocage et Calle Crown, s'ils trottent, ont la vitesse pour s'imposer au second échelon. **Scénario alternatif :** les fautes en série des chevaux rapides laissent la course à des chevaux réguliers mais moins rapides (Dollar Soyer).

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 9 | Django du Bocage | Forte | Meilleure forme (victoire), vitesse, D4 |
| 2 | 10 | Calle Crown | Forte | Classe supérieure, mais D à sa dernière |
| 3 | 5 | Helena di Quattro | Candidat crédible | Vitesse, sans recul, Nivard |
| 4 | 8 | Dollar Soyer | Candidat crédible | Fiable dans un lot qui ne l'est pas |
| 5 | 2 | Etenclin | Candidat secondaire | Talent, mais 3 D sur 4 |
| 6 | 4 | Niky Flax | Candidat secondaire | Inconnue |
| 7 | 12 | Christo | Candidat secondaire | Vitesse, fiabilité moyenne |
| 8 | 3 | Catch My Love | Candidat secondaire | Peu d'arguments |
| 9 | 1 | Eberton | Candidat fragile | 3 D sur 5 |
| 10 | 13 | Epic Julry | Candidat fragile | Vitesse sans forme |
| 11 | 7 | Defi Pierji | Candidat fragile | Forme faible |
| 12 | 6 | Darling Berry | Candidat fragile | Arrêt + D récents |
| 13 | 11 | Daelia de Vandel | Candidat fragile | Aucune forme |

### F. Points phares
- **Facteur n°1 :** la fiabilité. C'est la course du dossier où elle pèse le plus.
- **Choix difficile :** Django du Bocage devant Calle Crown. Forme et victoire récente contre classe (gain moyen deux fois supérieur). Les deux sortent d'un D récent : départage serré.
- **Surestimable :** Etenclin (record et gain moyen flatteurs, mais 3 D sur 4).

### G. Bilan
Confiance **faible** : beaucoup de chevaux non fiables, aucune cote, terrain inconnu. L'hypothèse dominante est qu'une partie des favoris théoriques commettra une faute.

---

## Course 5 — Prix Thémis 2021 (R1 C3, vendredi 22/10/2021, 20 h 15)

### A. Identification
Trot attelé, course C, 2 850 m, 60 000 €, gains < 399 000 €, recul à 189 000 €. **14 partants** : 4 + 10. Cotes disponibles.

### B. Lecture générale
Seulement 4 chevaux sans recul, dont Falco Berry (talent, 3 D consécutifs) et Payet D.E. (régulier). Le 2e échelon est dense et rapide. **Le cœur de la course : le talent non fiable du favori face aux réguliers.**

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant | Cote |
|---|---|---|---|---|---|
| 1 | Colvert d'Herfraie | D4, vainqueur il y a 5 courses | 0-0-7-0, 9 ans | Aucun | 89 |
| 2 | Payet D.E. | **3 victoires + 1 place en 4 courses**, 9 580 €/course, D4, Ouvrie | Record 1'13"00 (lent) | Forme + régularité | 6 |
| 3 | Ready Ribb | — | 9-6-D-4-6, 10 ans, ferré | Aucun | 63 |
| 4 | Falco Berry | Record 1'11"20, 2 victoires, D4, A. Abrivard, haut de l'échelon | **3 D consécutifs** | Talent / fiabilité | 2,7 |
| 5 | Dreamer de Chenu | 3-3 anciens | 0-D-0, ferré | Faible | 13 |
| 6 | Firello | 7 700 €/course | Ferré, 0a à sa dernière | Moyen | 62 |
| 7 | Victor Ferm | Record 1'11"00, 8 268 €/course | 0-9-0-3-D | Hors de forme | 8,5 |
| 8 | Datcha | 2a, 3a | **2 D sur 5**, PA | Fiabilité | 25 |
| 9 | Valzer di Poggio | **11 662 €/course**, 2a ×2, record 1'11"40 | D ancien, DP | Classe | 15 |
| 10 | Freyja du Pont | Régulière (3-0-2-3-1), record 1'11"10, D4, Raffin | Un 0a | Fiable et rapide | 7,5 |
| 11 | Baron Daidou | **Meilleur record (1'10"50)** | 10 ans, 5-3-0-7-1, DA | Vitesse | 34 |
| 12 | Equinoxe Jiel | **Vainqueur à sa dernière, 1-4-1-2-6**, D4, Thomain, record 1'11"40 | Recul | Forme + fiabilité | 7,4 |
| 13 | Decoloration | — | D-7d-D, ferrée | Fragile | 93 |
| 14 | For You Madrik | Record 1'11"10, Nivard, 2-1 | 0a à sa dernière, un D, « 7ha » (coquille) | Irrégulier | 14 |

### D. Scénario prévisionnel
Payet D.E. et Falco Berry partent devant. Si Falco Berry trotte, il a la vitesse pour garder ses 25 m d'avance. Les reculés réguliers (Equinoxe Jiel, Freyja du Pont) remontent au train. **Alternative :** Falco Berry fait une nouvelle faute (scénario probable vu la série) et la course se joue entre Payet D.E. et les reculés.

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 12 | Equinoxe Jiel | Forte | Forme gagnante, fiable, D4, vitesse suffisante |
| 2 | 2 | Payet D.E. | Forte | Régularité exceptionnelle, sans recul |
| 3 | 10 | Freyja du Pont | Forte | Régulière et rapide |
| 4 | 4 | Falco Berry | Candidat crédible | Le plus doué du 1er échelon, mais 3 D consécutifs |
| 5 | 9 | Valzer di Poggio | Candidat crédible | Classe |
| 6 | 14 | For You Madrik | Candidat crédible | Vitesse, Nivard |
| 7 | 7 | Victor Ferm | Candidat secondaire | Vitesse sans forme |
| 8 | 11 | Baron Daidou | Candidat secondaire | Meilleur record, forme irrégulière, 10 ans |
| 9 | 6 | Firello | Candidat secondaire | Moyen |
| 10 | 5 | Dreamer de Chenu | Candidat fragile | Faible |
| 11 | 8 | Datcha | Candidat fragile | 2 D sur 5 |
| 12 | 1 | Colvert d'Herfraie | Candidat fragile | Aucune forme |
| 13 | 3 | Ready Ribb | Candidat fragile | Aucune forme |
| 14 | 13 | Decoloration | Candidat fragile | Fautes |

### F. Points phares
- **Favori rétrogradé :** Falco Berry (2,7 au marché, classé 4e). Trois disqualifications consécutives en volté : son potentiel est supérieur à sa probabilité de le réaliser.
- **Sous-évalué par le marché :** Payet D.E. (cote 6). Probablement à cause de son record lent ; mais sa régularité est la meilleure du lot.
- **Opposition clé :** Equinoxe Jiel / Freyja du Pont, deux reculés fiables et proches. Equinoxe est préféré pour sa victoire récente.

### G. Bilan
- **Hypothèse clé :** les fautes de Falco Berry sont structurelles, pas accidentelles. Si c'est faux, il gagne.
- **Limite :** aucune information sur la nature des disqualifications (départ, en course, matériel).

---

## Course 6 — Prix Thémis 2022 (R1 C3, vendredi 21/10/2022, 20 h 15)

### A. Identification
Trot attelé, course C, 2 850 m, 65 000 €, gains < 399 000 €, recul à 189 000 €. **16 partants** : 6 + 10. Cotes disponibles.

### B. Lecture générale
Le 1er échelon est faible derrière Grace du Digeon. Le 2e échelon a de la vitesse (Eileen 1'10"1, Zerozerosette Gar 1'10"3, Digne et Droit 1'10"4), mais très peu de forme. Seul Cyrano de B. combine régularité et classe. **Course de forme plus que de vitesse.**

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant | Cote |
|---|---|---|---|---|---|
| 1 | Gardner Shaw | Régulier (3-2-6-5), M. Abrivard | Record 1'14"1, seulement 4 courses | Limité en vitesse | 11 |
| 2 | Ghost des Charrons | Régulier (4-3-3-2), D4, Barrier | D ancien, pas de victoire | Placé probable | 9,7 |
| 3 | Grace du Digeon | **2 victoires consécutives**, D4, Raffin, haut de l'échelon (185 890 €) | D ancien, record 1'12"9 | Forme + position | 2,1 |
| 4 | Vicki Laksmy | Record 1'11"5, 5 669 €/course | 5-5-0-0-9 | Moyen | 23 |
| 5 | Expert Delta | PADP | « Aia », D, 0a | Fragile | 45 |
| 6 | Diable Ludois | DP | 9-0-0-9-5 | Aucun | 110 |
| 7 | Cyrano de B. | **2-1-2-2m-2 : le plus régulier du lot**, 10 702 €/course, D4, Ouvrie | Recul, le moins riche du 2e échelon (246 042 €) | Régularité + classe | 4,6 |
| 8 | Deus Ex Machina | — | A, D, D, ferré | Fragile | 56 |
| 9 | Zerozerosette Gar | Record 1'10"3, 9 359 €/course | 10-0 récents, ferré | Vitesse sans forme | 84 |
| 10 | Gently de Muze | 9 469 €/course, Crack 53 | 13-0-3-8-0, ferré | Hors de forme | 78 |
| 11 | Deesse Noire | Record 1'11"2, D4 | 6-8-5-4-D | Moyenne | 15 |
| 12 | Charly de l'Aunay | — | 12-D-D-6-9, 10 ans | Fragile | 75 |
| 13 | Fly Speed | Record 1'11"2 | 11-2m-7m-7-3m | Moyen | 26 |
| 14 | Eileen | **Meilleur record (1'10"1)**, 8 106 €/course, 1-3 anciens | 7-6-5 récents, ferrée | Vitesse, forme en baisse | 26 |
| 15 | Digne et Droit | Record 1'10"4 | 8-0-0-D-0 | Aucune forme | 47 |
| 16 | Firello | 2-1 anciens | 14-0 récents, ferré | Faible | 101 |

### D. Scénario prévisionnel
Grace du Digeon se place en tête du 1er échelon, suivie de Ghost des Charrons. Cyrano de B. remonte au train. Eileen peut finir vite si elle retrouve sa forme. **Alternative :** un train soutenu pourrait remettre en jeu les reculés rapides mais hors de forme (Zerozerosette Gar, Digne et Droit) : peu probable vu leurs musiques.

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 3 | Grace du Digeon | Très forte | Forme + position idéale dans le 1er échelon |
| 2 | 7 | Cyrano de B. | Très forte | Régularité exemplaire, compensée par le recul |
| 3 | 2 | Ghost des Charrons | Forte | Régulier, sans recul |
| 4 | 14 | Eileen | Candidat crédible | Meilleure vitesse du lot |
| 5 | 1 | Gardner Shaw | Candidat crédible | Régulier mais lent |
| 6 | 11 | Deesse Noire | Candidat secondaire | Vitesse, forme moyenne |
| 7 | 4 | Vicki Laksmy | Candidat secondaire | Vitesse, forme moyenne |
| 8 | 9 | Zerozerosette Gar | Candidat secondaire | Vitesse sans forme |
| 9 | 13 | Fly Speed | Candidat secondaire | Moyen |
| 10 | 10 | Gently de Muze | Candidat fragile | Classe passée |
| 11 | 15 | Digne et Droit | Candidat fragile | Aucune forme |
| 12 | 5 | Expert Delta | Candidat fragile | Fautes |
| 13 | 16 | Firello | Candidat fragile | Faible |
| 14 | 6 | Diable Ludois | Candidat fragile | Aucun argument |
| 15 | 12 | Charly de l'Aunay | Candidat fragile | Fautes |
| 16 | 8 | Deus Ex Machina | Candidat fragile | Arrêt + 2 D |

### F. Points phares
- **Choix difficile :** Grace du Digeon contre Cyrano de B. Cyrano est plus régulier et plus riche par course, mais il est le moins riche du 2e échelon (position structurellement la plus défavorable). Grace a l'avantage de l'échelon et de la forme.
- **Peu d'importance :** les records rapides du 2e échelon, contredits par les musiques.
- **Sous-évalué possible :** Ghost des Charrons (9,7) par rapport à sa régularité.

### G. Bilan
Confiance **moyenne à bonne** sur les trois premiers. **Hypothèse clé :** la forme prime sur la vitesse brute dans ce lot.

---

## Course 7 — Prix Thémis 2023 (R1 C3, vendredi 20/10/2023, 20 h 15)

### A. Identification
Trot attelé, course C, 2 850 m (grande piste, corde à gauche), 68 000 €, recul à 189 000 €, terrain **bon (cendrée)**. **16 partants** : 8 + 8. Cotes disponibles.

### B. Lecture générale
Harlem de Bucy domine sur le papier (classe, record, entourage) et est très favori (1,8). Au 1er échelon, Brand Roc combine forme et vitesse. Course à **un favori net**, avec une lutte ouverte pour les places.

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant | Cote |
|---|---|---|---|---|---|
| 1 | Hostia | Gagnante il y a 3 courses | 0a à sa dernière, D, ferrée | Moyenne | 175 |
| 2 | Digital Dominance | Record 1'11"6, D4 | **2 D sur 5** | Fiabilité | 53 |
| 3 | Last Winner | Régulière dans l'accessit, DA | Aucune victoire, 8 ans | Placée au mieux | 48 |
| 4 | Chandelles | J.-M. Bazire (driver-entraîneur), D4 | **7m-9-5m-D-6 : aucune forme attelée** | Entourage > forme | 8,9 |
| 5 | Follow Me Flash | Record 1'11"2 | 0-0-8, ferré | Faible | 177 |
| 6 | Brand Roc | **3 victoires en 5 courses**, record 1'10"8 (meilleur du 1er échelon), D4, N. Bazire, haut de l'échelon | 6a à sa dernière | Forme + vitesse + position | 10 |
| 7 | Hidden Texas | Régulier (5-3-3-3), Gelormini, haut de l'échelon | Un D, PA | Placé | 23 |
| 8 | Devs Definitif | Thomain, D4 | **Musique montée** (5m-9m-1m-3m) puis D attelé | Discipline | 20 |
| 9 | Bordeaux S. | Record 1'10"4, 10 788 €/course, 2 victoires | 0-D récents, ferré | Classe, forme en baisse | 138 |
| 10 | Face Time | **Record 1'10"2 (meilleur)**, 2-1-2 anciens | 0-0 récents, ferré | Vitesse, forme en baisse | 81 |
| 11 | Flower By Magalou | — | 6-8m-6-6-4 | Faible | 146 |
| 12 | He And Me | 2 victoires, 8 136 €/course, Raffin | Record 1'12"2, un D, ferré | Crédible | 12 |
| 13 | Galileo Bello | **Très régulier (2-1-3-1)**, Nivard, record 1'11"4 | Un D ancien, PADP | Régularité | 6,6 |
| 14 | Eberton | — | Dm-8-D-1-9 | Fragile | 91 |
| 15 | Fougue du Dollar | — | Mixte attelé/monté, 0a | Faible | 206 |
| 16 | Harlem de Bucy | **Plafond de gains (394 170 €), 12 317 €/course, Crack 37**, record 1'10"9, D4, A. Abrivard | 0a et D dans ses 5 dernières, recul, n° 16 (extérieur) | Classe | 1,8 |

### D. Scénario prévisionnel
Brand Roc et Hidden Texas en action au 1er échelon. Harlem de Bucy et Galileo Bello remontent ; Harlem a la vitesse pour dominer la fin de course. **Alternative :** une faute de Harlem (il en a une dans sa musique) laisse le duel Brand Roc / Galileo Bello.

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 16 | Harlem de Bucy | Forte | Classe nettement supérieure, D4, vitesse |
| 2 | 6 | Brand Roc | Forte | Forme + vitesse + position dans l'échelon |
| 3 | 13 | Galileo Bello | Forte | Le plus régulier des reculés |
| 4 | 7 | Hidden Texas | Candidat crédible | Régulier, sans recul |
| 5 | 12 | He And Me | Candidat crédible | Gagnant, mais ferré et record moyen |
| 6 | 9 | Bordeaux S. | Candidat secondaire | Classe, forme en baisse |
| 7 | 10 | Face Time | Candidat secondaire | Meilleure vitesse, forme en baisse |
| 8 | 4 | Chandelles | Candidat secondaire | Entourage, aucune forme |
| 9 | 8 | Devs Definitif | Candidat secondaire | Spécialiste du monté |
| 10 | 2 | Digital Dominance | Candidat secondaire | Fiabilité |
| 11 | 1 | Hostia | Candidat fragile | Moyenne |
| 12 | 3 | Last Winner | Candidat fragile | Ne gagne pas |
| 13 | 11 | Flower By Magalou | Candidat fragile | Faible |
| 14 | 14 | Eberton | Candidat fragile | Fautes |
| 15 | 5 | Follow Me Flash | Candidat fragile | Faible |
| 16 | 15 | Fougue du Dollar | Candidat fragile | Aucune forme |

### F. Points phares
- **Je ne classe pas Harlem de Bucy « Très forte » malgré sa cote de 1,8.** Recul, numéro extérieur, 0a et D dans sa musique récente : une cote à 1,8 surestime à mon sens sa probabilité de victoire. Il reste mon 1er.
- **Surestimée par le marché :** Chandelles (8,9). Le nom Bazire masque une musique sans forme.
- **Sous-évalué :** Brand Roc (10), meilleur profil du 1er échelon.

### G. Bilan
**Hypothèse clé :** la classe de Harlem de Bucy l'emporte sur le recul. **Limite :** le contexte du 0a et du D récents est inconnu.

---
## Course 8 — Prix Thémis 2024 (R1 C4, vendredi 18/10/2024, 20 h 15)

### A. Identification
Trot attelé, course C, 2 850 m (grande piste), 68 000 €, 6 à 11 ans, gains < 379 000 €, recul à 174 000 €, terrain **bon**. **14 partants** : 8 + 6. Cotes disponibles ; colonne Crack absente.

### B. Lecture générale
Lot jeune (presque tous des 6 ans) et assez **fiable**. Trois profils en très bonne forme : Icare de Phyt's (4 victoires), Isofou du Chêne et Hedic Gema (reculés). Course ouverte entre ces trois et Lucky Guy Boko, le plus rapide du 1er échelon.

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant | Cote |
|---|---|---|---|---|---|
| 1 | Caligola Laser | Record 1'11"5, régulier, gagnant | Très peu de gains (71 402 €), ferré, « D5 » (coquille ?) | Classe faible | 69 |
| 2 | Irina d'Atout | D4, Thomain | Dm-6-D-0-6 | Fragile | 19 |
| 3 | Lucky Guy Boko | **Record 1'10"6 (meilleur du 1er échelon)**, 2 victoires, 7 220 €/course, D4 | 5a à sa dernière | Vitesse + régularité | 16 |
| 4 | In En Vrie | **Très régulier (6-3-4-3-2)**, D4, Mottier | Pas de victoire, record 1'12"1 | Placé | 10 |
| 5 | Icare de Phyt's | **4 victoires consécutives**, D4, Barrier | Record 1'12"7, un D | Forme | 3,5 |
| 6 | Illico des Baux | Record 1'11"4, Raffin | 9-9-4, 3 courses | Faible | 28 |
| 7 | If You Can | 2 victoires, record 1'11"2 | 0-9 récents, DA | Forme en baisse | 25 |
| 8 | Indien de Fontaine | Record 1'11"0, Nivard, D4 | 7a à sa dernière | Moyen | 18 |
| 9 | Isofou du Chêne | **3 victoires + 1 place sur 5**, D4 | Recul, record 1'12"1, un D | Forme | 4,5 |
| 10 | Here We Go | Record 1'10"6 | 0-5-3-3-9, ferré | Moyen | 91 |
| 11 | Ibiscus Man | Vainqueur à sa dernière, record 1'10"9 | 2 D sur 5 | Fiabilité | 13 |
| 12 | Gabiano | D4 | 7m-D-0-D-5m | Fragile | 72 |
| 13 | Grindelwald | Record 1'10"3 (meilleur du lot), A. Abrivard | **4 fois 0a sur 5** | Hors de forme | 29 |
| 14 | Hedic Gema | **Régulier (3-2-6-1-1)**, 7 003 €/course, D4, le plus riche (plafond) | Recul, record 1'12"1 | Forme + classe | 5,1 |

### D. Scénario prévisionnel
Icare de Phyt's et In En Vrie bien placés au 1er échelon. Lucky Guy Boko peut produire l'effort le plus rapide. Hedic Gema et Isofou du Chêne remontent ; leur record (1'12"1) rend le recul plus coûteux. **Alternative :** un train rapide favorise Lucky Guy Boko et les reculés rapides (Ibiscus Man).

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 5 | Icare de Phyt's | Forte | Série de 4 victoires, sans recul |
| 2 | 14 | Hedic Gema | Forte | Régulier, plus riche, D4 |
| 3 | 9 | Isofou du Chêne | Forte | Forme gagnante |
| 4 | 3 | Lucky Guy Boko | Candidat crédible | Meilleure vitesse sans recul |
| 5 | 4 | In En Vrie | Candidat crédible | Très régulier |
| 6 | 8 | Indien de Fontaine | Candidat crédible | Vitesse, Nivard |
| 7 | 11 | Ibiscus Man | Candidat crédible | Vainqueur récent, 2 D |
| 8 | 7 | If You Can | Candidat secondaire | Forme en baisse |
| 9 | 6 | Illico des Baux | Candidat secondaire | Peu de références |
| 10 | 1 | Caligola Laser | Candidat secondaire | Régulier, classe faible |
| 11 | 10 | Here We Go | Candidat secondaire | Moyen |
| 12 | 13 | Grindelwald | Candidat fragile | Vitesse sans forme |
| 13 | 2 | Irina d'Atout | Candidat fragile | Fautes |
| 14 | 12 | Gabiano | Candidat fragile | Fautes |

### F. Points phares
- **Choix difficile :** Icare de Phyt's (forme, pas de recul, mais vitesse moyenne 1'12"7) devant Lucky Guy Boko (vitesse 1'10"6, moins de victoires). J'ai donné la priorité à la série. **Si le train est rapide, l'ordre peut s'inverser.**
- **Sous-évalué par le marché :** Lucky Guy Boko (16) et In En Vrie (10).
- **Surestimable :** Grindelwald (29 : marché qui respecte un record et un entourage, malgré 4 fois 0a).

### G. Bilan
Confiance **moyenne**. Trois chevaux en forme nette, aucun dominant.

---

## Course 9 — Prix Thémis 2025 (R1 C1, vendredi 17/10/2025, 18 h 24)

### A. Identification
Trot attelé, course C **européenne**, 2 850 m (grande piste), 68 000 €, 6 à 11 ans, gains < 382 000 €, recul à 178 000 €, terrain **bon**. **14 partants** : 4 + 10. Cotes disponibles.

**⚠️ Données très incomplètes :** gains approximatifs (≈) ; ferrure inconnue pour 8 chevaux ; **musique, record et gains absents pour les n° 10 à 14** ; records de qualification (Headscott, Harison du Plessis) qui suggèrent un retour après une longue absence. Cinq des six chevaux les plus joués n'ont **aucune donnée sportive**. **Cette course devrait être re-documentée avant d'en tirer des enseignements.**

### B. Lecture générale
Quatre chevaux sans recul, dont trois en bonne forme. Le 2e échelon est impossible à évaluer sportivement pour 5 chevaux sur 10. Pour ces cinq, **la cote est la seule information disponible** : je l'utilise par défaut et je le signale.

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant | Cote |
|---|---|---|---|---|---|
| 1 | Dayak (ITY) | Très régulier (2-2-0-2-0-3), D4, Gelormini | Ne gagne pas (0 victoire sur 7) | Placeur | 3,9 |
| 2 | Dada del Ronco | **Forme (5-1-1-3-2-3)**, D4, même entraîneur que Dayak | Record 1'11"6 | Forme gagnante | 7,7 |
| 3 | Lucky Guy Boko | Record 1'10"6 | **8-0-0 récents** | Hors de forme | 129 |
| 4 | Junkie (SWE) | **Record 1'10"4**, 7-5-2-1-2, haut de l'échelon (≈ 170 000 €), PA | Deux résultats moyens récents | Vitesse + position | 22 |
| 5 | Iron du Gers | N. Bazire | 0-0 récents, à peine au-dessus du seuil de recul | Mal placé | 86 |
| 6 | Power Doc | Record 1'10"4, D4, Ouvrie, gagnant | D à sa dernière, 9-0 ensuite | Irrégulier | 9,7 |
| 7 | Jolie Surprise | Record 1'10"5 | 9-7-6 récents | Hors de forme | 60 |
| 8 | Dea Sprint Bar | Forme correcte (3-2-9-3-1-1) | Aucun record ni gain renseigné | Incomplet | 60 |
| 9 | Headscott | Régulier en 2024 (2-1-3-2) | Record de qualification : probable retour après absence | Fraîcheur | 57 |
| 10 | Gims du Plessis | — | **Aucune donnée** | Cote seule | 5,4 |
| 11 | Jewelcandle Fac | — | **Aucune donnée** | Cote seule | 94 |
| 12 | Harison du Plessis | — | Record de qualification : retour probable | Cote seule | 8,9 |
| 13 | Iznogoud Am | — | **Aucune donnée** | Cote seule | 15 |
| 14 | Eros Zola | — | **Aucune donnée** | Cote seule | 5 |

### D. Scénario prévisionnel
Dayak, Dada del Ronco et Junkie se disputent le 1er échelon. Le scénario du 2e échelon n'est pas déductible. **Seule hypothèse raisonnable :** les reculés riches et très joués (Eros Zola, Gims du Plessis) ont un niveau supérieur que les données ne montrent pas.

### E. Classement prévisionnel (confiance faible)

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 2 | Dada del Ronco | Forte | Meilleure forme gagnante du 1er échelon |
| 2 | 1 | Dayak (ITY) | Forte | Le plus régulier, mais placeur |
| 3 | 4 | Junkie (SWE) | Candidat crédible | Vitesse + position dans l'échelon |
| 4 | 6 | Power Doc | Candidat crédible | Vitesse, irrégulier |
| 5 | 14 | Eros Zola | Candidat crédible | **Classement fondé uniquement sur la cote** |
| 6 | 10 | Gims du Plessis | Candidat crédible | **Classement fondé uniquement sur la cote** |
| 7 | 12 | Harison du Plessis | Candidat secondaire | Cote seule + risque de retour d'absence |
| 8 | 8 | Dea Sprint Bar | Candidat secondaire | Forme correcte, niveau inconnu |
| 9 | 13 | Iznogoud Am | Candidat secondaire | Cote seule |
| 10 | 9 | Headscott | Candidat secondaire | Retour probable |
| 11 | 7 | Jolie Surprise | Candidat fragile | Hors de forme |
| 12 | 3 | Lucky Guy Boko | Candidat fragile | Hors de forme |
| 13 | 5 | Iron du Gers | Candidat fragile | Hors de forme, mal placé |
| 14 | 11 | Jewelcandle Fac | Candidat fragile | Aucune donnée, cote élevée |

### F. Points phares
- **Le marché préfère Dayak (3,9) à Dada del Ronco (7,7).** Je fais l'inverse : la régularité de Dayak est réelle, mais il ne gagne pas, alors que Dada gagne.
- **Sous-évaluée :** Junkie (22).
- **Classement des n° 10 à 14 :** c'est de l'enregistrement du marché, pas de l'analyse.

### G. Bilan
**Confiance faible.** Cette course ne doit pas peser dans l'évaluation de la méthode tant que les données manquantes ne sont pas complétées.

---

## Course 10 — Prix Case IH (Prix Jacques Andrieu) 2020 (R1 C5, dimanche 26/01/2020, 14 h 50)

### A. Identification
**Trot monté** (musiques en « m » ; la colonne Driver = jockeys). 2 850 m, 100 000 €, 5 à 11 ans, gains ≥ 160 000 €. **Conditions tronquées** (seuil de recul non fourni, déduit : les deux plus riches sont à 2 875 m). **10 partants** : 8 + 2. Terrain non renseigné. Pas de cotes.

### B. Lecture générale
Petit lot de bon niveau (gains de 273 000 à 667 000 €). **En monté, l'aptitude spécifique à la discipline est le premier filtre** : plusieurs partants ont surtout une musique attelée.

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant |
|---|---|---|---|---|
| 1 | Emir de Rebomard | **Spécialiste du monté (1-2-2-7-1 en monté)**, 6 ans, D4, 6 835 €/course | Le moins riche, record 1'13"00 | Forme spécialisée |
| 2 | Caban Prior | Monté (3-1-4-2), record 1'12"10 | Un D, ferré | Crédible |
| 3 | Evidence Roc | **19 928 €/course (classe très élevée)**, DP | **0m-0a-0a-6a-6a** : aucune forme, peu de référence en monté | Classe passée |
| 4 | Gross Weight | Mixte monté/attelé régulier (4-4-1-2-3), record 1'11"40, Thomain, D4 | Pas de victoire récente en monté | Régularité |
| 5 | Aribo Mix | — | Aucune course montée dans la musique, 8-5-6-9-6, 10 ans | Discipline |
| 6 | Accord Marjacq | Monté, M. Abrivard | Dm-0m-5m-5m-6m, 10 ans | Faible |
| 7 | Volcan de Bellande | Spécialiste du monté | 6-8-6-6-8, 11 ans | Faible |
| 8 | Evangelina Blue | **Très régulière en monté (5-4-2-4-3)**, **19 388 €/course**, D4, Mottier, record 1'11"50 | Pas de victoire récente | Classe + régularité |
| 9 | Coach Franbleu | **Meilleur record (1'10"70)**, D4, Lebourgeois, 1m récent | D à sa dernière, recul | Vitesse |
| 10 | Vertige de Chenu | Le plus riche, 2m ×2, Raffin | **3 Dm sur 5**, recul, 11 ans | Fiabilité |

### D. Scénario prévisionnel
En monté, les fautes d'allure sont fréquentes. Evangelina Blue, Emir de Rebomard et Gross Weight devraient courir sans histoire. Coach Franbleu a la vitesse pour combler 25 m sur un parcours propre.

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 8 | Evangelina Blue | Forte | Classe + régularité en monté |
| 2 | 1 | Emir de Rebomard | Forte | Meilleure forme montée |
| 3 | 4 | Gross Weight | Forte | Régulier, vitesse |
| 4 | 2 | Caban Prior | Candidat crédible | Spécialiste, un D |
| 5 | 9 | Coach Franbleu | Candidat crédible | Meilleur record, recul + D récent |
| 6 | 3 | Evidence Roc | Candidat secondaire | Classe sans forme |
| 7 | 10 | Vertige de Chenu | Candidat secondaire | 3 Dm sur 5 |
| 8 | 6 | Accord Marjacq | Candidat fragile | Forme faible |
| 9 | 7 | Volcan de Bellande | Candidat fragile | Forme faible |
| 10 | 5 | Aribo Mix | Candidat fragile | Aucune référence montée |

### F. Points phares
- **Surestimable :** Evidence Roc. Son gain moyen (le plus élevé) vient de son passé ; ni sa forme ni ses références montées ne le justifient ici.
- **Opposition clé :** Evangelina Blue (classe, placée) contre Emir de Rebomard (forme, gagnant, moins riche).

### G. Bilan
**Limite :** conditions tronquées (probables exclusions par placement dans une course précédente) et absence de cotes.

---
## Course 11 — Prix 20 Minutes (Prix des Vosges) 2024 (C5, dimanche 11/02/2024, 16 h 28)

### A. Identification
Trot attelé, 2 850 m, 59 000 €, 7 à 11 ans, gains < 265 000 €, recul à 165 000 €. **16 partants** : 5 + 11. Cotes disponibles.

### B. Lecture générale
Le 1er échelon est court (5) et Harry Cohiais y est le mieux placé (le plus riche, en forme). Le 2e échelon est large, avec un favori clair (Hymne du Gers) et deux profils en forme (Harley Gema, Garibaldi).

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant | Cote |
|---|---|---|---|---|---|
| 1 | Hermes Smart | 2 victoires sur 5, D4, Ploquin | **2 D sur 5 (dont la dernière)**, record 1'13"4 | Fiabilité | 5,5 |
| 2 | Hold Up du Saptel | Régulier dans l'accessit | Ne gagne pas | Moyen | 51 |
| 3 | Go Away Bird | Record 1'11"9 | 0-0 anciens, 9-3-7 | Faible | 76 |
| 4 | Hold Up Ranais | Régulier (5-4-3-8-3), Thomain, record 1'11"5 | Pas de victoire | Placé | 30 |
| 5 | Harry Cohiais | **2-1-2**, record 1'11"1 (meilleur du 1er échelon), haut de l'échelon (163 875 €), D4, Ouvrie | Seulement 3 courses en musique | Forme + position | 7,9 |
| 6 | Help Me Win | — | 6-8-0, PA | Faible | 148 |
| 7 | Garibaldi | **1-1-2-2**, **record 1'10"4 (meilleur du lot)**, 10 455 €/course | Ferré, cote très élevée (96) qui contredit la musique | Forme + vitesse | 96 |
| 8 | Filou Smiling | 4-3 récents | 0-8-7 | Moyen | 66 |
| 9 | Hubble du Vivier | **Très régulier (2-4-2-2-6)** | Ferré, ne gagne pas | Placé | 23 |
| 10 | Harley Gema | 2 victoires, 6 880 €/course, D4, Rochard, record 1'11"1 | Un D, 6a à sa dernière | Crédible+ | 8,3 |
| 11 | Gybor Well | Gagnant récent, M. Abrivard | 0a | Moyen | 36 |
| 12 | Hymne du Gers | **3 victoires sur 5**, 9 869 €/course, D4, N. Bazire, record 1'11"2 | Recul | Forme + classe | 3 |
| 13 | Editeur la Ravelle | 2 victoires | 0-0-7, 10 ans | Irrégulier | 49 |
| 14 | Eternel Amour | Record 1'11"0 | 0-0 récents, 10 ans | Forme en baisse | 123 |
| 15 | Gabelou Carisaie | Vainqueur à sa dernière, Raffin, sans faute | Record 1'12"7 | Fiable | 18 |
| 16 | Excel d'Amour | — | 7-0-7-0-2, 10 ans | Faible | 217 |

### D. Scénario prévisionnel
Harry Cohiais bien placé au 1er échelon. Hymne du Gers et Harley Gema remontent. Garibaldi peut finir le plus vite si sa forme est réelle. **Alternative :** une faute d'Hermes Smart ou de Harley Gema rebat les places.

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 12 | Hymne du Gers | Très forte | Forme gagnante + classe + D4 |
| 2 | 5 | Harry Cohiais | Forte | Forme et position idéale dans le 1er échelon |
| 3 | 10 | Harley Gema | Forte | Gagnante, rapide, D4 |
| 4 | 7 | Garibaldi | Candidat crédible | Musique et record excellents, ferré |
| 5 | 1 | Hermes Smart | Candidat crédible | Gagnant, mais 2 D |
| 6 | 9 | Hubble du Vivier | Candidat crédible | Très régulier |
| 7 | 15 | Gabelou Carisaie | Candidat crédible | Vainqueur récent, fiable |
| 8 | 4 | Hold Up Ranais | Candidat secondaire | Régulier dans l'accessit |
| 9 | 11 | Gybor Well | Candidat secondaire | Irrégulier |
| 10 | 13 | Editeur la Ravelle | Candidat secondaire | Irrégulier |
| 11 | 8 | Filou Smiling | Candidat secondaire | Moyen |
| 12 | 2 | Hold Up du Saptel | Candidat fragile | Ne gagne pas |
| 13 | 14 | Eternel Amour | Candidat fragile | Forme en baisse |
| 14 | 3 | Go Away Bird | Candidat fragile | Faible |
| 15 | 6 | Help Me Win | Candidat fragile | Faible |
| 16 | 16 | Excel d'Amour | Candidat fragile | Faible |

### F. Points phares
- **Écart majeur avec le marché : Garibaldi (96).** Sa musique (1-1-2-2) et son record (le meilleur) en font un candidat crédible, voire fort. Une cote aussi élevée suggère une information que je n'ai pas (niveau des courses gagnées, problème connu). **Je le classe 4e, en le signalant comme le principal point d'incertitude.**
- **Surestimé par le marché :** Hermes Smart (5,5) malgré 2 D sur 5.

### G. Bilan
Confiance **moyenne à bonne** sur le favori. **Hypothèse clé :** la musique de Garibaldi reflète un niveau comparable à celui du lot.

---

## Course 12 — Prix de la Camargue 2024 (R1 C10, lundi 25/11/2024, 19 h 12)

### A. Identification
Trot attelé, course C, 2 850 m, 53 000 €, **6 ans uniquement**, gains < 205 000 €, **pas de recul** (tous à 2 850 m). **13 partants**. Cotes disponibles.

### B. Lecture générale
Course dominée sur le papier par Cobra Killer Gar (5 victoires consécutives, meilleur record, gain moyen record), favori à 1,4. **La vraie question est l'ordre des places.**

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant | Cote |
|---|---|---|---|---|---|
| 1 | Bottnas Idol | — | **Aucune donnée** (étranger), ferré | Inconnue | 32 |
| 2 | Indien de Fontaine | Record 1'11"0, Nivard, D4 | D à sa dernière, 7-7 | Forme en baisse | 93 |
| 3 | Ivoire Prestance | 8 103 €/course, M. Abrivard | 3 courses seulement (4-8-4), PA | Moyen | 58 |
| 4 | Igo Clea | 2m-1m (monté) | 0-9 récents en attelé | Discipline | 135 |
| 5 | Island Love | Vainqueur à sa dernière, Dubois | 0-0-D-2 avant | Irrégulière | 9,7 |
| 6 | Cobra Killer Gar | **1-1-1-1-1, record 1'10"3, 13 064 €/course**, D4, Gelormini | Aucune | Domination | 1,4 |
| 7 | Imperial Mabon | 8 331 €/course | 0-4-2-4-9, ferré | Moyen | 94 |
| 8 | Intello de Chenu | D4 | **5 D consécutifs** | Fiabilité nulle | 87 |
| 9 | Ixora | 1-2 récents, Thomain, D4 | D à sa dernière | Crédible | 22 |
| 10 | Imoko Jibelau | J.-M. Bazire, D4 | 4-5-5-1-8, record 1'12"7 | Moyen | 10 |
| 11 | Instructor | Record 1'11"1, A. Abrivard, 2a à sa dernière | 9-7-5-6 | Moyen | 15 |
| 12 | Irina de Bailly | — | D-0-9-9m-8 | Faible | 145 |
| 13 | Iacynthe Didjeap | **Très régulier (2-4-2-5-1)**, sans faute, Rochard | Record 1'12"0 | Régularité | 13 |

### D. Scénario prévisionnel
Cobra Killer Gar fait la course ou s'impose dans la ligne droite. Derrière, une lutte ouverte entre les réguliers (Iacynthe Didjeap), les rapides (Instructor, Ixora) et les entourages forts (Imoko Jibelau).

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 6 | Cobra Killer Gar | Très forte | Domination totale sur les données |
| 2 | 13 | Iacynthe Didjeap | Forte | Le plus régulier et fiable |
| 3 | 11 | Instructor | Candidat crédible | Vitesse, 2a récent |
| 4 | 9 | Ixora | Candidat crédible | Forme, un D récent |
| 5 | 10 | Imoko Jibelau | Candidat crédible | Entourage, forme moyenne |
| 6 | 5 | Island Love | Candidat secondaire | Gagnante récente mais irrégulière |
| 7 | 2 | Indien de Fontaine | Candidat secondaire | Vitesse, forme en baisse |
| 8 | 7 | Imperial Mabon | Candidat secondaire | Moyen |
| 9 | 3 | Ivoire Prestance | Candidat secondaire | Peu de références |
| 10 | 1 | Bottnas Idol | Candidat secondaire | Inconnue |
| 11 | 4 | Igo Clea | Candidat fragile | Monté plutôt qu'attelé |
| 12 | 12 | Irina de Bailly | Candidat fragile | Faible |
| 13 | 8 | Intello de Chenu | Candidat fragile | 5 D consécutifs |

### F. Points phares
- **Sous-évalué :** Iacynthe Didjeap (13) par rapport à Imoko Jibelau (10), joué pour son driver plus que pour sa musique.
- **Seul risque réel pour le favori :** une faute (aucune dans ses 5 dernières).

### G. Bilan
Confiance **élevée** pour la 1re place, **faible** pour l'ordre des places.

---

## Course 13 — Prix de Vic sur Cère 2025 (C8, samedi 04/01/2025, 17 h 40)

### A. Identification
Trot attelé, **course A**, 2 850 m, 71 000 €, **6 ans** (génération J), gains de 43 000 à 205 000 €, pas de recul. **13 partants**. Cotes disponibles.

### B. Lecture générale
Course de bon niveau pour des 6 ans. Un favori régulier (Just de l'Oison), un cheval très rapide mais irrégulier (Jingle du Pont, 1'09"8), et plusieurs réguliers (Just a Boy d'Alesa, Destino D.J., Jilord Viva).

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant | Cote |
|---|---|---|---|---|---|
| 1 | Dutchess Sun | Ouvrie, D4 | **Aucune donnée** (étrangère) | Inconnue | 54 |
| 2 | H.C.'s Crazy Horse | DP | **Aucune donnée** | Inconnue | 93 |
| 3 | Dragowski | Gagnant il y a 2 courses, record 1'11"4 | 7a à sa dernière | Moyen | 53 |
| 4 | Yahoo Diamant | Régulier dans l'accessit, 6 700 €/course, record 1'11"3 | Pas de victoire | Placé | 22 |
| 5 | Destino D.J. | **Très régulier (3-5-2-2-3)**, 8 090 €/course, D4, Gelormini | Pas de victoire | Placé solide | 17 |
| 6 | Janzibar | Gagnant en monté | Musique surtout montée, 9a ×2 en attelé | Discipline | 135 |
| 7 | Jolie Surprise | Dubois | D-5-9-5-0 | Faible | 31 |
| 8 | Just de l'Oison | **1-3-6-2-2, 11 465 €/course (le plus élevé)**, PADP, Th. Duvaldestin | Record 1'11"8 | Forme + classe | 2,8 |
| 9 | Hnokki Speed | — | 7-7-D-D, 1 063 €/course | Faible | 101 |
| 10 | Just a Boy d'Alesa | **4-2-1-3-1**, 8 539 €/course, D4, Mottier | Record 1'11"8 | Forme + régularité | 6,3 |
| 11 | Jingle du Pont | **Record 1'09"8 (de loin le meilleur)**, N. Bazire, 2a à sa dernière | **9-0-9-0 avant** | Vitesse / irrégularité | 5 |
| 12 | Jilord Viva | 1-2-0-2-4, Raffin, D4 | Un 0a | Forte | 5,4 |
| 13 | Je Reve du Bois | Record 1'10"6, Thomain, 3a | Dm, 9a | Crédible | 11 |

### D. Scénario prévisionnel
Course sans recul : la vitesse pure compte davantage. Just de l'Oison et Just a Boy d'Alesa en bonne place. Jingle du Pont peut tout gagner s'il répète son 2a, ou finir loin.

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 8 | Just de l'Oison | Très forte | Forme + classe, la plus haute moyenne de gains |
| 2 | 10 | Just a Boy d'Alesa | Forte | Forme et régularité |
| 3 | 12 | Jilord Viva | Forte | Forme, D4 |
| 4 | 5 | Destino D.J. | Candidat crédible | Le plus régulier, ne gagne pas |
| 5 | 11 | Jingle du Pont | Candidat crédible | Vitesse exceptionnelle, irrégulier |
| 6 | 13 | Je Reve du Bois | Candidat crédible | Vitesse, irrégulier |
| 7 | 4 | Yahoo Diamant | Candidat secondaire | Placé |
| 8 | 3 | Dragowski | Candidat secondaire | Moyen |
| 9 | 1 | Dutchess Sun | Candidat secondaire | Inconnue |
| 10 | 7 | Jolie Surprise | Candidat fragile | Faible |
| 11 | 2 | H.C.'s Crazy Horse | Candidat fragile | Inconnue |
| 12 | 9 | Hnokki Speed | Candidat fragile | Fautes |
| 13 | 6 | Janzibar | Candidat fragile | Spécialiste du monté |

### F. Points phares
- **Choix difficile :** Jingle du Pont 5e malgré une cote de 5. Son record est le meilleur de 0,8 s/km, mais il alterne mauvaises places et bonnes courses : un « tout ou rien ».
- **Données peu utiles :** l'âge (tous 6 ans), le recul (inexistant).

### G. Bilan
Confiance **moyenne à bonne**. **Hypothèse clé :** la régularité prime sur la vitesse pure de Jingle du Pont.

---

## Course 14 — Prix Jacques Andrieu 2025 (C3, dimanche 26/01/2025, 14 h 15)

### A. Identification
**Trot monté**, 2 850 m, 120 000 €, 5 à 11 ans, gains ≥ 130 000 €. **Conditions tronquées.** **11 partants** : 9 + 2 (Filwell et Edition Gema, les deux plus riches, à 2 875 m). Cotes disponibles.

### B. Lecture générale
Lot de spécialistes du monté. Filwell est le plus riche, le plus régulier en monté et favori malgré le recul. Impala de Val domine le 1er échelon.

### C. Analyse individuelle

| N° | Cheval | Forces | Faiblesses / risques | Discriminant | Cote |
|---|---|---|---|---|---|
| 1 | Heuristique | Monté (2-0-1-1), D4, Ploquin | Un 0m | Crédible+ | 11 |
| 2 | Gadget du Gade | Vainqueur à sa dernière (1m) | 9-0-7-8 avant, 9 ans | Irrégulier | 75 |
| 3 | Impala de Val | **1-4-5-3-1**, 7 851 €/course, D4, Rochard | Record 1'12"0 | Forme spécialisée | 3,5 |
| 4 | Good Girl Marceaux | Record 1'10"5, 2m ×2 | Dm, 0a ×2, 9 ans | Irrégulière | 10 |
| 5 | Go Or Not | 2 victoires en monté | Dm, 9m | Irrégulier | 13 |
| 6 | Halfa | Régulière en monté (4-2-1-8-4) | — | Crédible | 15 |
| 7 | Fougue du Dollar | — | 5-7-5-0-0, 10 ans | Faible | 125 |
| 8 | Hannibal Tuilerie | 6 605 €/course, gagnant (attelé) | Musique mixte, 0a | Moyen | 9,2 |
| 9 | Hidalgo des Noes | Record 1'10"3 | 8-3-7-0, DA | Faible forme | 33 |
| 10 | Filwell | **1m-1m-2m-3m-4m : le plus régulier**, 9 655 €/course, D4, Lamy | Recul, 10 ans | Classe + spécialisation | 2,9 |
| 11 | Edition Gema | **Meilleur record (1'10"2)**, 2m ×2, la plus riche | 8-7-5, recul, 11 ans | Classe, irrégulière | 12 |

### D. Scénario prévisionnel
Impala de Val et Heuristique en bonne place devant. Filwell remonte au train ; sa régularité en monté rend le recul acceptable. Les fautes d'allure, fréquentes en monté, peuvent toucher Good Girl Marceaux et Go Or Not.

### E. Classement prévisionnel

| Rang | N° | Cheval | Évaluation | Justification principale |
|---|---|---|---|---|
| 1 | 10 | Filwell | Très forte | Le plus régulier et le plus riche par course parmi les spécialistes |
| 2 | 3 | Impala de Val | Forte | Meilleure forme du 1er échelon |
| 3 | 1 | Heuristique | Forte | Forme montée, D4 |
| 4 | 6 | Halfa | Candidat crédible | Régulière en monté |
| 5 | 11 | Edition Gema | Candidat crédible | Classe et vitesse, forme moyenne |
| 6 | 5 | Go Or Not | Candidat crédible | Gagnant, irrégulier |
| 7 | 8 | Hannibal Tuilerie | Candidat secondaire | Plus attelé que monté |
| 8 | 4 | Good Girl Marceaux | Candidat secondaire | Vitesse, irrégulière |
| 9 | 9 | Hidalgo des Noes | Candidat secondaire | Vitesse, forme faible |
| 10 | 2 | Gadget du Gade | Candidat fragile | Victoire isolée |
| 11 | 7 | Fougue du Dollar | Candidat fragile | Faible |

### F. Points phares
- **Opposition clé :** Filwell (recul, mais régularité de spécialiste) contre Impala de Val (sans recul, forme).
- **Surestimé par le marché :** Hannibal Tuilerie (9,2), dont les meilleures performances récentes sont attelées.

### G. Bilan
Confiance **moyenne à bonne**. **Limite :** conditions tronquées.

---

## Synthèse transversale (constats de méthode, pas règles universelles)

| Course | Mon 1er | Mon 2e | Mon 3e | Confiance |
|---|---|---|---|---|
| Thémis 2015 | Tropic du Hêtre | Viking Blue | Vulcania de Godrel | Moyenne |
| Thémis 2018 | Lover Face | Visitor | Tripolini V P | Moyenne |
| Thémis 2019 | Douceur du Chêne | Delmonica | Aron The Baron | Moyenne à bonne |
| Thémis 2020 | Django du Bocage | Calle Crown | Helena di Quattro | Faible |
| Thémis 2021 | Equinoxe Jiel | Payet D.E. | Freyja du Pont | Moyenne |
| Thémis 2022 | Grace du Digeon | Cyrano de B. | Ghost des Charrons | Moyenne à bonne |
| Thémis 2023 | Harlem de Bucy | Brand Roc | Galileo Bello | Moyenne |
| Thémis 2024 | Icare de Phyt's | Hedic Gema | Isofou du Chêne | Moyenne |
| Thémis 2025 | Dada del Ronco | Dayak | Junkie | **Faible (données manquantes)** |
| Case IH 2020 (monté) | Evangelina Blue | Emir de Rebomard | Gross Weight | Moyenne |
| Vosges 2024 | Hymne du Gers | Harry Cohiais | Harley Gema | Moyenne à bonne |
| Camargue 2024 | Cobra Killer Gar | Iacynthe Didjeap | Instructor | Élevée (1er) |
| Vic sur Cère 2025 | Just de l'Oison | Just a Boy d'Alesa | Jilord Viva | Moyenne à bonne |
| Andrieu 2025 (monté) | Filwell | Impala de Val | Heuristique | Moyenne à bonne |

**Hypothèses de travail qui ont pesé le plus dans mes classements** (ce sont elles qu'il faudra tester quand tu compareras aux arrivées) :
1. **Les D/A répétés réduisent fortement les chances** (Falco Berry, Etenclin, Pingus Vang rétrogradés).
2. **Le cheval le plus riche du 1er échelon a un avantage structurel** (Douceur du Chêne, Grace du Digeon, Harry Cohiais).
3. **Un record lent (≥ 1'13"5) limite la valeur d'une série de victoires** (Viking Blue, Visitor, Payet D.E.).
4. **Pour un cheval régulier et rapide, le recul de 25 m se rattrape** (Tropic du Hêtre, Lover Face, Harlem de Bucy, Filwell classés 1ers malgré le recul).
5. **Le déferrage (D4) est un bonus modéré, jamais décisif seul.**

**Avant la phase de comparaison :** tronquer les musiques contaminées (voir §0.1) et compléter Thémis 2025.
