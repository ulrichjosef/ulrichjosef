# Confrontation aux résultats réels — apprentissage et scénarios (Prompt 2)

**Base :** mes 14 classements prévisionnels figés (`analyse_retro_aveugle_v1.md`, non modifiés) et les arrivées officielles de `Courses_APRES.docx`.
**Méthode de calcul :** tous les chiffres viennent d'un script qui croise les deux fichiers. Aucun chiffre n'est estimé à la main.
**Convention :** écart = rang réel − rang prédit. Positif = le cheval a fini moins bien que prévu ; négatif = mieux que prévu.

---

## 0. Contrôles préalables

- **Correspondance numéros / noms :** vérifiée automatiquement pour les 14 courses. Chaque numéro du classement prédit existe dans l'arrivée (classé, DA ou NC), avec le même nom. Aucune ambiguïté.
- **Anomalies de la source des résultats** (signalées, pas corrigées) :
  - Thémis 2018 : pas de 8e place, Toohotforyou est donné 9e. Le tracking classe Choriste du Trio 3e alors qu'il est DA. Je retiens l'arrivée officielle.
  - Thémis 2023 : Last Winner et Devs Definitif sont 6es ex æquo.
  - Thémis 2015, 2021, 2022, 2023, 2024, 2025 et Vosges 2024 : les non-classés (NC) ont fini 10e ou plus loin, sans ordre connu. Je ne leur attribue pas de rang chiffré.
  - Thémis 2019 : une source indique « petite piste » pour cette édition.
  - Thémis 2022 : valeurs aberrantes dans le tracking de Firello.
- **Abréviations :** DA = disqualifié pour allure irrégulière. NC = non classé (10e ou plus).
- **Règle :** un DA ou un NC n'a pas d'écart chiffré. Il est compté à part.

---

## A. Comparaison des résultats

Pour chaque course : le tableau cheval par cheval, puis le diagnostic des écarts importants. Chaque diagnostic indique **si le facteur était connu avant le départ** et le range dans l'une des trois catégories :
- **Évitable** : l'information était dans les données, je l'ai mal pondérée.
- **Indisponible** : l'information n'existait pas avant le départ.
- **Incertitude de course** : l'écart ne prouve pas à lui seul une faiblesse du raisonnement.

### A1. Prix Thémis 2015
**Prédit :** 15-9-4 · **Réel :** 9-7-15 · Gagnant prédit 2e · Podium : 2 chevaux sur 3, ordre faux · Top 5 : 2 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 15 – Tropic du Hetre | 1 | 3 | +2 | Bien classé |
| 9 – Viking Blue | 2 | 1 | -1 | Bien classé |
| 4 – Vulcania de Godrel | 3 | 8 | +5 | Surestimé |
| 6 – Vasco de Viette | 4 | NC (10e ou plus) | — | Surestimé (non classé) |
| 12 – Prince Di Poggio | 5 | 7 | +2 | Bien classé |
| 5 – Vella Blue | 6 | DA | — | Disqualifié |
| 18 – Sergent du Rib | 7 | 4 | -3 | Sous-estimé |
| 8 – Farmer’s Julia | 8 | DA | — | Disqualifié |
| 14 – Tip Top Nelliere | 9 | 6 | -3 | Sous-estimé |
| 1 – Okay Dei Ronchi | 10 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 7 – Quick Fix | 11 | 2 | -9 | Sous-estimé |
| 16 – Tafaiko Sax | 12 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 3 – Head Line | 13 | 5 | -8 | Sous-estimé |
| 11 – Theo d’Erah | 14 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 17 – Tina Jolie | 15 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 2 – Pingus Vang | 16 | 9 | -7 | Sous-estimé |
| 13 – Team Job | 17 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 10 – Velinotte du Derby | 18 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |

- **Viking Blue gagne (prédit 2e)** — *Évitable (pondération)*. Je l'ai placé derrière Tropic du Hêtre à cause de son record lent (1'14"10). Il gagne en 1'12"9, plus vite que ce record. Sa série de 5 victoires était dans les données ; j'ai surpondéré le record.
- **Quick Fix 2e (prédit 11e)** — *Indisponible en partie*. Aucune musique française. Mais trois indices existaient : D4, entraîneur-driver Kolgjini, 165 912 € de gains (haut du premier échelon). Je l'ai mis au milieu par défaut : ce choix par défaut était trop bas.
- **Vulcania de Godrel 8e (prédite 3e), Vasco de Viette NC (prédit 4e)** — *Incertitude de course*. Rien dans les données ne l'annonçait.
- **Vella Blue et Farmer's Julia DA** — avaient chacune un D dans leurs 5 dernières : risque connu, mais impossible à trancher.

### A2. Prix Le Parisien (Thémis) 2018
**Prédit :** 10-6-11 · **Réel :** 12-4-3 · Gagnant prédit 4e · Podium : 0 sur 3 · Top 5 : 4 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 10 – Lover Face | 1 | 5 | +4 | Surestimé |
| 6 – Visitor | 2 | DA | — | Disqualifié |
| 11 – Tripolini V P | 3 | 4 | +1 | Bien classé |
| 12 – Ange de Lune | 4 | 1 | -3 | Sous-estimé |
| 4 – Cristal du Lupin | 5 | 2 | -3 | Sous-estimé |
| 7 – Buzz de Carel | 6 | 6 | 0 | Bien classé |
| 9 – Babylone Seven | 7 | DA | — | Disqualifié |
| 8 – Onceforall Face | 8 | DA | — | Disqualifié |
| 3 – Valokaja Hindo | 9 | 3 | -6 | Sous-estimé |
| 15 – Venezia de Mai | 10 | 7 | -3 | Sous-estimé |
| 1 – Toohotforyou | 11 | 9 | -2 | Bien classé |
| 13 – Beaute de Bailly | 12 | DA | — | Disqualifié |
| 2 – Choriste du Trio | 13 | DA | — | Disqualifié |
| 5 – Artiste de Tillard | 14 | DA | — | Disqualifié |
| 16 – Astral Viretaute | 15 | DA | — | Disqualifié |
| 14 – Uppercut Orange | 16 | DA | — | Disqualifié |

- **Course hors norme : 8 disqualifiés sur 16.** Mon top 5 contient 4 des 5 premiers, mais aucun de mes trois premiers n'est sur le podium.
- **Ange de Lune gagne (prédit 4e)** — *Incertitude de course*. Même profil que Lover Face (record 1'11"20, D4, recul). Je les avais départagés sur la régularité ; l'écart à l'arrivée ne prouve pas que ce choix était faux.
- **Valokaja Hindo 3e (prédit 9e)** — *Indisponible en partie*. Aucune musique, mais D4 et entourage Bazire / A. Abrivard. Même erreur de classement par défaut que Quick Fix en 2015.
- **Visitor DA (prédit 2e)** — *Incertitude* (un seul D dans ses 5 dernières).
- **Lover Face 5e (prédit 1er)** — *Évitable en partie*. Profil de placeur : aucune victoire dans ses 5 dernières courses. Je l'ai mis 1er sur sa vitesse et sa régularité.

### A3. Prix Thémis 2019
**Prédit :** 9-3-11 · **Réel :** 9-1-6 · **Gagnant trouvé** · Podium : 1 sur 3 · Top 5 : 3 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 9 – Douceur du Chêne | 1 | 1 | 0 | Bien classé |
| 3 – Delmonica | 2 | DA | — | Disqualifié |
| 11 – Aron The Baron | 3 | 7 | +4 | Surestimé |
| 2 – Partizan Face | 4 | 5 | +1 | Bien classé |
| 6 – Donuts Deladou | 5 | 3 | -2 | Bien classé |
| 15 – Dreambreaker | 6 | 13 | +7 | Surestimé |
| 7 – Dona Viva | 7 | DA | — | Disqualifié |
| 1 – Dream | 8 | 2 | -6 | Sous-estimé |
| 5 – Desperado | 9 | 12 | +3 | Surestimé |
| 14 – Tinamo Jet | 10 | 8 | -2 | Bien classé |
| 12 – Bauloise Haufor | 11 | 11 | 0 | Bien classé |
| 4 – Cuba Libre | 12 | 10 | -2 | Bien classé |
| 10 – Danseur Baroque | 13 | 4 | -9 | Sous-estimé |
| 8 – Dastavia de Guez | 14 | 9 | -5 | Sous-estimé |
| 16 – Be Bop Haufor | 15 | 6 | -9 | Sous-estimé |
| 13 – Codie de Beaulieu | 16 | 14 | -2 | Bien classé |

- **Douceur du Chêne gagne, comme prévu.**
- **Les cinq premiers sont tous partis du premier échelon (2 850 m).** C'était mon scénario principal. Pourtant j'ai classé Aron The Baron (reculé) 3e ; il finit 7e, avec la fin de course la plus rapide (1'08"00 sur les 500 derniers mètres), mais 15 m trop loin. *Évitable* : je n'ai pas tiré la conséquence de mon propre scénario dans le classement.
- **Delmonica DA (prédite 2e)** — *Incertitude* (un D ancien).
- **Dream 2e (prédit 8e)** — *Évitable en partie* : il avait gagné sa dernière course ; j'ai jugé cette victoire « isolée ».
- **Danseur Baroque 4e (prédit 13e)** — *Incertitude* : sa musique était faible.

### A4. Prix Thémis 2020
**Prédit :** 9-10-5 · **Réel :** 10-8-7 · Gagnant prédit 2e · Podium : 1 sur 3 · Top 5 : 3 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 9 – Django du Bocage | 1 | 6 | +5 | Surestimé |
| 10 – Calle Crown | 2 | 1 | -1 | Bien classé |
| 5 – Helena di Quattro | 3 | DA | — | Disqualifié |
| 8 – Dollar Soyer | 4 | 2 | -2 | Bien classé |
| 2 – Etenclin | 5 | 5 | 0 | Bien classé |
| 4 – Niky Flax | 6 | 7 | +1 | Bien classé |
| 12 – Christo | 7 | 8 | +1 | Bien classé |
| 3 – Catch My Love | 8 | 9 | +1 | Bien classé |
| 1 – Eberton | 9 | 4 | -5 | Sous-estimé |
| 13 – Epic Julry | 10 | DA | — | Disqualifié |
| 7 – Defi Pierji | 11 | 3 | -8 | Sous-estimé |
| 6 – Darling Berry | 12 | DA | — | Disqualifié |
| 11 – Daelia de Vandel | 13 | DA | — | Disqualifié |

- **Les trois premiers sont tous des reculés (2 875 m).**
- **Calle Crown gagne (prédit 2e)** — sa classe (11 211 € par course) l'a emporté. Mon hésitation avec Django du Bocage était un choix serré.
- **Django du Bocage 6e (prédit 1er)** — *Incertitude de course*. Le tracking le montre en tête sur les deux premiers tronçons (1er et 1er), puis 10e sur les derniers : effort trop tôt. Ce n'était pas prévisible avec les données.
- **Defi Pierji 3e (prédit 11e)** — *Incertitude* : musique 9-9-2-0-7, rien ne l'annonçait.
- **Helena di Quattro DA (prédite 3e)** — *Incertitude* (aucun D récent).

### A5. Prix Thémis 2021
**Prédit :** 12-2-10 · **Réel :** 7-4-2 · Gagnant prédit 7e · Podium : 1 sur 3 · Top 5 : 4 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 12 – Equinoxe Jiel | 1 | DA | — | Disqualifié |
| 2 – Payet D.E. | 2 | 3 | +1 | Bien classé |
| 10 – Freyja du Pont | 3 | 5 | +2 | Bien classé |
| 4 – Falco Berry | 4 | 2 | -2 | Bien classé |
| 9 – Valzer di Poggio | 5 | 4 | -1 | Bien classé |
| 14 – For You Madrik | 6 | NC (10e ou plus) | — | Surestimé (non classé) |
| 7 – Victor Ferm | 7 | 1 | -6 | Sous-estimé |
| 11 – Baron Daidou | 8 | 6 | -2 | Bien classé |
| 6 – Firello | 9 | 8 | -1 | Bien classé |
| 5 – Dreamer de Chenu | 10 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 8 – Datcha | 11 | DA | — | Disqualifié |
| 1 – Colvert d’Herfraie | 12 | 9 | -3 | Sous-estimé |
| 3 – Ready Ribb | 13 | 7 | -6 | Sous-estimé |
| 13 – Decoloration | 14 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |

- **Victor Ferm gagne (prédit 7e)** — *Évitable en partie*. Sa forme était mauvaise (0-9-0-3-D), mais il avait le 2e meilleur record du lot (1'11"00), le D4, l'écurie Bazire, 8 268 € par course, et le marché le plaçait 5e (8,5). J'ai donné trop de poids à la forme récente face à la classe et à la ferrure. D'après le commentaire, il fait une faute au départ, est vite remis, puis est envoyé en tête. Une partie de l'issue relève donc de la course.
- **Equinoxe Jiel DA (prédit 1er)** — *Incertitude* (aucun D récent).
- **Falco Berry 2e (prédit 4e)** — ma pénalité pour ses 3 D consécutifs était trop forte : il trotte et finit 2e. Voir la tendance D5 : les chevaux à 3 D ou plus ne sont pas plus souvent disqualifiés dans ce corpus.
- **Course lente (gagnant en 1'14"3).** Payet D.E. (record lent) finit 3e en passant à la corde.

### A6. Prix Thémis 2022
**Prédit :** 3-7-2 · **Réel :** 3-7-1 · **Gagnant trouvé, et 1er-2e dans l'ordre exact** · Podium : 2 sur 3 · Top 5 : 4 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 3 – Grace du Digeon | 1 | 1 | 0 | Bien classé |
| 7 – Cyrano de B. | 2 | 2 | 0 | Bien classé |
| 2 – Ghost des Charrons | 3 | 4 | +1 | Bien classé |
| 14 – Eileen | 4 | 7 | +3 | Surestimé |
| 1 – Gardner Shaw | 5 | 3 | -2 | Bien classé |
| 11 – Deesse Noire | 6 | 6 | 0 | Bien classé |
| 4 – Vicki Laksmy | 7 | 5 | -2 | Bien classé |
| 9 – Zerozerosette Gar | 8 | NC (10e ou plus) | — | Surestimé (non classé) |
| 13 – Fly Speed | 9 | NC (10e ou plus) | — | Surestimé (non classé) |
| 10 – Gently de Muze | 10 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 15 – Digne et Droit | 11 | 8 | -3 | Sous-estimé |
| 5 – Expert Delta | 12 | DA | — | Disqualifié |
| 16 – Firello | 13 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 6 – Diable Ludois | 14 | 9 | -5 | Sous-estimé |
| 12 – Charly de l’Aunay | 15 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 8 – Deus Ex Machina | 16 | DA | — | Disqualifié |

- **Meilleure prédiction du corpus.** Le raisonnement (Grace du Digeon avantagée par sa forme et son échelon, Cyrano de B. par sa régularité malgré le recul) correspond au déroulement décrit : Grace prend la tête dans la descente et répond à toutes les attaques ; Cyrano trouve le passage trop tard.
- **Gardner Shaw 3e (prédit 5e)** — trouve un trou depuis le 4e rideau : *incertitude* favorable.
- **Eileen 7e (prédite 4e)** — sa vitesse ne s'est pas exprimée : *incertitude*.

### A7. Prix Thémis 2023
**Prédit :** 16-6-13 · **Réel :** 16-4-12 · **Gagnant trouvé** · Podium : 1 sur 3 · Top 5 : 3 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 16 – Harlem de Bucy | 1 | 1 | 0 | Bien classé |
| 6 – Brand Roc | 2 | 9 | +7 | Surestimé |
| 13 – Galileo Bello | 3 | DA | — | Disqualifié |
| 7 – Hidden Texas | 4 | 4 | 0 | Bien classé |
| 12 – He And Me | 5 | 3 | -2 | Bien classé |
| 9 – Bordeaux S. | 6 | NC (10e ou plus) | — | Surestimé (non classé) |
| 10 – Face Time | 7 | DA | — | Disqualifié |
| 4 – Chandelles | 8 | 2 | -6 | Sous-estimé |
| 8 – Devs Definitif | 9 | 6 (ex æquo) | -3 | Sous-estimé |
| 2 – Digital Dominance | 10 | 8 | -2 | Bien classé |
| 1 – Hostia | 11 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 3 – Last Winner (BEL) | 12 | 6 (ex æquo) | -6 | Sous-estimé |
| 11 – Flower By Magalou | 13 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 14 – Eberton | 14 | 5 | -9 | Sous-estimé |
| 5 – Follow Me Flash | 15 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 15 – Fougue du Dollar | 16 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |

- **Harlem de Bucy gagne, comme prévu.** Ma réserve sur sa cote de 1,8 n'était pas fondée : il gagne « sans opposition ».
- **Chandelles 2e (prédite 8e)** — *Évitable*. Je l'avais désignée comme « surestimée par le marché » parce que sa musique était vide. Mais J.-M. Bazire la drivait lui-même, elle était D4, et le marché la plaçait 3e (8,9). Elle mène la course après un relais et résiste. Même erreur qu'avec Imoko Jibelau (A12).
- **Brand Roc 9e (prédit 2e)** — *Incertitude* : le tracking le place 14e dès le premier tronçon mesuré, jamais dans la course.
- **Galileo Bello DA (prédit 3e)** — *Incertitude* (un D ancien).
- **Eberton 5e (prédit 14e)** — *Incertitude* (musique Dm-8-D-1-9).

### A8. Prix Thémis 2024
**Prédit :** 5-14-9 · **Réel :** 9-14-4 · Gagnant prédit 3e · Podium : 2 sur 3 · Top 5 : 4 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 5 – Icare de Phyt’s | 1 | 4 | +3 | Surestimé |
| 14 – Hedic Gema | 2 | 2 | 0 | Bien classé |
| 9 – Isofou du Chêne | 3 | 1 | -2 | Bien classé |
| 3 – Lucky Guy Boko | 4 | 6 | +2 | Bien classé |
| 4 – In En Vrie | 5 | 3 | -2 | Bien classé |
| 8 – Indien de Fontaine | 6 | 7 | +1 | Bien classé |
| 11 – Ibiscus Man | 7 | DA | — | Disqualifié |
| 7 – If You Can | 8 | 5 | -3 | Sous-estimé |
| 6 – Illico des Baux | 9 | DA | — | Disqualifié |
| 1 – Caligola Laser | 10 | 9 | -1 | Bien classé |
| 10 – Here We Go | 11 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 13 – Grindelwald | 12 | 8 | -4 | Sous-estimé |
| 2 – Irina d’Atout | 13 | DA | — | Disqualifié |
| 12 – Gabiano | 14 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |

- **Bonne identification du lot de tête** : 4 des 5 premiers.
- **Icare de Phyt's 4e (prédit 1er)** — *Incertitude de course*. Il prend la tête dans le tournant de la plaine et cède sous une triple attaque à mi-ligne droite. Sa série de 4 victoires ne le protégeait pas d'un parcours exposé.
- **Isofou du Chêne gagne et Hedic Gema finit 2e (prédits 3e et 2e)** : deux reculés D4 en forme. Cela confirme que le recul ne pénalise pas un cheval en forme (tendance D4).
- **In En Vrie 3e (prédit 5e)** — le placeur régulier fait sa course, à l'abri à la corde.

### A9. Prix Thémis 2025 (données lacunaires)
**Prédit :** 2-1-4 · **Réel :** 6-14-1 · Gagnant prédit 4e · Podium : 1 sur 3 · Top 5 : 3 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 2 – Dada del Ronco | 1 | 8 | +7 | Surestimé |
| 1 – Dayak (ITY) | 2 | 3 | +1 | Bien classé |
| 4 – Junkie (SWE) | 3 | 6 | +3 | Surestimé |
| 6 – Power Doc | 4 | 1 | -3 | Sous-estimé |
| 14 – Eros Zola | 5 | 2 | -3 | Sous-estimé |
| 10 – Gims du Plessis | 6 | DA | — | Disqualifié |
| 12 – Harison du Plessis | 7 | 4 | -3 | Sous-estimé |
| 8 – Dea Sprint Bar | 8 | NC (10e ou plus) | — | Surestimé (non classé) |
| 13 – Iznogoud Am | 9 | 5 | -4 | Sous-estimé |
| 9 – Headscott | 10 | 9 | -1 | Bien classé |
| 7 – Jolie Surprise | 11 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 3 – Lucky Guy Boko | 12 | 7 | -5 | Sous-estimé |
| 5 – Iron du Gers | 13 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 11 – Jewelcandle Fac | 14 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |

- **Power Doc gagne (prédit 4e)** — meilleur record du lot (1'10"4, ex æquo), D4, Ouvrie. Je l'ai pénalisé pour son D récent. *Évitable en partie.*
- **Dada del Ronco 8e (prédite 1re)** — *Incertitude de course*. Elle est la plus rapide du tronçon 1 500-1 000 m (1'09"7), puis 11e sur la fin : effort trop tôt. C'était aussi **mon choix contre le marché** (Dayak, favori, finit 3e).
- **Eros Zola 2e, Harison du Plessis 4e, Iznogoud Am 5e** — *Indisponible* : aucune donnée sportive. Leur ordre dans le marché, que j'avais repris faute de mieux, était à peu près juste.

### A10. Prix Case IH (Jacques Andrieu) 2020 — monté
**Prédit :** 8-1-4 · **Réel :** 2-1-4 · Gagnant prédit 4e · Podium : 2 sur 3 · Top 5 : 4 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 8 – Evangelina Blue | 1 | 4 | +3 | Surestimé |
| 1 – Emir de Rebomard | 2 | 2 | 0 | Bien classé |
| 4 – Gross Weight | 3 | 3 | 0 | Bien classé |
| 2 – Caban Prior | 4 | 1 | -3 | Sous-estimé |
| 9 – Coach Franbleu | 5 | 9 | +4 | Surestimé |
| 3 – Evidence Roc | 6 | NC (10e ou plus) | — | Surestimé (non classé) |
| 10 – Vertige de Chenu | 7 | 5 | -2 | Bien classé |
| 6 – Accord Marjacq | 8 | 6 | -2 | Bien classé |
| 7 – Volcan de Bellande | 9 | 7 | -2 | Bien classé |
| 5 – Aribo Mix | 10 | 8 | -2 | Bien classé |

- **Emir de Rebomard 2e et Gross Weight 3e : placés exactement.**
- **Caban Prior gagne (prédit 4e)** — *Incertitude*. Spécialiste du monté, mais ferré et avec un D.
- **Evidence Roc NC (prédit 6e)** — je l'avais signalé comme « surestimable » malgré son gain moyen record : **avertissement confirmé**.
- **Evangelina Blue 4e (prédite 1re)** — placeuse sans victoire récente : fidèle à son profil, pas gagnante.

### A11. Prix des Vosges 2024
**Prédit :** 12-5-10 · **Réel :** 12-5-1 · **Gagnant trouvé, et 1er-2e dans l'ordre exact** · Podium : 2 sur 3 · Top 5 : 3 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 12 – Hymne du Gers | 1 | 1 | 0 | Bien classé |
| 5 – Harry Cohiais | 2 | 2 | 0 | Bien classé |
| 10 – Harley Gema | 3 | DA | — | Disqualifié |
| 7 – Garibaldi | 4 | DA | — | Disqualifié |
| 1 – Hermes Smart | 5 | 3 | -2 | Bien classé |
| 9 – Hubble du Vivier | 6 | 9 | +3 | Surestimé |
| 15 – Gabelou Carisaie | 7 | 4 | -3 | Sous-estimé |
| 4 – Hold Up Ranais | 8 | 7 | -1 | Bien classé |
| 11 – Gybor Well | 9 | 8 | -1 | Bien classé |
| 13 – Editeur la Ravelle | 10 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 8 – Filou Smiling | 11 | DA | — | Disqualifié |
| 2 – Hold Up du Saptel | 12 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 14 – Eternel Amour | 13 | 6 | -7 | Sous-estimé |
| 3 – Go Away Bird | 14 | 5 | -9 | Sous-estimé |
| 6 – Help Me Win | 15 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 16 – Excel d’Amour | 16 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |

- **Hymne du Gers et Harry Cohiais : 1er et 2e exacts.**
- **Harley Gema DA (prédite 3e) et Garibaldi DA (prédit 4e)** — *Incertitude*. Le marché (96) se méfiait de Garibaldi ; sa disqualification ne permet pas de savoir s'il avait raison sur le niveau.
- **Hermes Smart 3e (prédit 5e)** — je l'avais jugé surestimé à cause de ses 2 D ; il a trotté.
- **Go Away Bird 5e (prédit 14e), Eternel Amour 6e (prédit 13e)** — *Incertitude* : musiques faibles.

### A12. Prix de la Camargue 2024
**Prédit :** 6-13-11 · **Réel :** 6-10-13 · **Gagnant trouvé** · Podium : 2 sur 3 · Top 5 : 3 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 6 – Cobra Killer Gar | 1 | 1 | 0 | Bien classé |
| 13 – Iacynthe Didjeap | 2 | 3 | +1 | Bien classé |
| 11 – Instructor | 3 | 6 | +3 | Surestimé |
| 9 – Ixora | 4 | 7 | +3 | Surestimé |
| 10 – Imoko Jibelau | 5 | 2 | -3 | Sous-estimé |
| 5 – Island Love | 6 | 4 | -2 | Bien classé |
| 2 – Indien de Fontaine | 7 | 5 | -2 | Bien classé |
| 7 – Imperial Mabon | 8 | NC (10e ou plus) | — | Surestimé (non classé) |
| 3 – Ivoire Prestance | 9 | 8 | -1 | Bien classé |
| 1 – Bottnas Idol | 10 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 4 – Igo Clea | 11 | NC (10e ou plus) | — | Cohérent (classé bas, non classé) |
| 12 – Irina de Bailly | 12 | DA | — | Disqualifié |
| 8 – Intello de Chenu | 13 | 9 | -4 | Sous-estimé |

- **Cobra Killer Gar gagne, comme prévu.**
- **Imoko Jibelau 2e (prédit 5e)** — *Évitable en partie*. Je l'avais déclassé avec la même formule que Chandelles (« joué pour son driver plus que pour sa musique »). J.-M. Bazire le drivait. C'est la 2e fois.
- **Iacynthe Didjeap 3e (prédit 2e)** — profil de régularité bien lu.

### A13. Prix de Vic sur Cère 2025
**Prédit :** 8-10-12 · **Réel :** 11-4-12 · Gagnant prédit 5e · Podium : 1 sur 3 · Top 5 : 3 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 8 – Just de l'Oison | 1 | DA | — | Disqualifié |
| 10 – Just a Boy d'Alesa | 2 | 5 | +3 | Surestimé |
| 12 – Jilord Viva | 3 | 3 | 0 | Bien classé |
| 5 – Destino D.J. | 4 | 6 | +2 | Bien classé |
| 11 – Jingle du Pont | 5 | 1 | -4 | Sous-estimé |
| 13 – Je Reve du Bois | 6 | DA | — | Disqualifié |
| 4 – Yahoo Diamant | 7 | 2 | -5 | Sous-estimé |
| 3 – Dragowski | 8 | 7 | -1 | Bien classé |
| 1 – Dutchess Sun | 9 | 9 | 0 | Bien classé |
| 7 – Jolie Surprise | 10 | 4 | -6 | Sous-estimé |
| 2 – H.C.'s Crazy Horse | 11 | DA | — | Disqualifié |
| 9 – Hnokki Speed | 12 | DA | — | Disqualifié |
| 6 – Janzibar | 13 | 8 | -5 | Sous-estimé |

- **Just de l'Oison DA « à 1 m » du poteau (prédit 1er)** — *Incertitude de course pure*. Le tracking le place 2e sur l'avant-dernier tronçon : il était aux premières places.
- **Jingle du Pont gagne (prédit 5e)** — *Évitable en partie*. Meilleur record du lot de loin (1'09"8) dans une course **sans recul**. J'avais choisi la régularité contre la vitesse ; ici la vitesse l'a emporté. Dans les deux courses sans recul du corpus, le meilleur record a gagné (voir D3).
- **Yahoo Diamant 2e (prédit 7e)** — le meilleur dernier 1 000 m de la course (1'10"6).

### A14. Prix Jacques Andrieu 2025 — monté
**Prédit :** 10-3-1 · **Réel :** 1-5-8 · Gagnant prédit 3e · Podium : 1 sur 3 · Top 5 : 2 sur 5

| Cheval | Rang prédit | Rang réel | Écart | Diagnostic |
|---|---|---|---|---|
| 10 – Filwell | 1 | 4 | +3 | Surestimé |
| 3 – Impala de Val | 2 | DA | — | Disqualifié |
| 1 – Heuristique | 3 | 1 | -2 | Bien classé |
| 6 – Halfa | 4 | 6 | +2 | Bien classé |
| 11 – Edition Gema | 5 | 7 | +2 | Bien classé |
| 5 – Go Or Not | 6 | 2 | -4 | Sous-estimé |
| 8 – Hannibal Tuilerie | 7 | 3 | -4 | Sous-estimé |
| 4 – Good Girl Marceaux | 8 | DA | — | Disqualifié |
| 9 – Hidalgo des Noes | 9 | 8 | -1 | Bien classé |
| 2 – Gadget du Gade | 10 | 5 | -5 | Sous-estimé |
| 7 – Fougue du Dollar | 11 | 9 | -2 | Bien classé |

- **Filwell 4e (prédit 1er)** — *Incertitude de course*. Le tracking le place 1er sur les tronçons 2 000-1 500 et 1 500-1 000 m (1'08"8), puis 8e sur la fin : il a remonté ses 25 m de recul trop vite.
- **Impala de Val DA (prédit 2e)** — *Incertitude* (aucun D en monté récemment).
- **Hannibal Tuilerie 3e (prédit 7e)** — je l'avais jugé surestimé par le marché (9,2) parce que ses meilleures courses récentes étaient attelées. *Erreur de lecture* : il a couru en monté à son niveau.
- **Heuristique gagne (prédite 3e)** : forme montée bien lue, mais placée derrière Filwell et Impala de Val.

---
## B. Bilan des performances du modèle

### B1. Indicateurs globaux (14 courses, 200 partants)

| Indicateur | Résultat | Repère « au hasard » | Lecture |
|---|---|---|---|
| Gagnant = mon 1er | **5 / 14** (36 %) | ≈ 1,0 / 14 | Nettement mieux que le hasard |
| Gagnant dans mon top 3 | **9 / 14** | ≈ 3,0 / 14 | Bon |
| Chevaux du podium dans mon top 3 | **19 / 42** (45 %) | ≈ 9 / 42 | Correct |
| Podium dans l'ordre exact | **0 / 14** | — | Faible |
| 1er et 2e dans l'ordre exact | **2 / 14** (Thémis 2022, Vosges 2024) | — | — |
| Chevaux des 5 premiers dans mon top 5 | **45 / 70** (64 %) | — | Bon |
| Rang prédit du gagnant | 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 7 (médiane 2,5) | — | Le gagnant n'a jamais été classé au-delà de mon 7e |
| Écart moyen (en valeur absolue) sur les chevaux classés | 2,9 places | — | Mesure partielle : DA et NC exclus |

*Le repère « au hasard » est l'espérance d'un classement tiré au sort (1/partants pour le gagnant, 3/partants pour un top 3).*

### B2. Le classement sépare bien le haut et le bas, moins bien l'intérieur du haut

| Mon rang prédit | Partants | Victoires | Podiums | Taux de podium |
|---|---|---|---|---|
| 1 à 3 | 42 | 9 | 19 | 45 % |
| 4 à 6 | 42 | 4 | 15 | 36 % |
| 7 et au-delà | 116 | 1 | 8 | 7 % |

Le bas du classement est fiable : une seule victoire (Victor Ferm, 2021) et 8 podiums sur 116 chevaux. L'ordre entre les 6 premiers est beaucoup moins sûr.

### B3. Comparaison avec le marché (9 courses avec cotes complètes)

| Mesure | Marché | Moi |
|---|---|---|
| Victoires du 1er choix | 4 / 9 | 4 / 9 |
| Chevaux du podium dans le top 3 | **18 / 27** | 13 / 27 |
| Courses où je fais mieux que le marché sur le podium | — | **0** (égalité 4, moins bien 5) |

- Mon 1er choix était le favori du marché dans 7 courses sur 9. **Les deux fois où je m'en suis écarté (2021, 2025), mon choix a fini plus loin que le favori.**
- Chevaux classés 7e ou au-delà dans le marché : **0 victoire, 2 podiums sur 73.**
- **Conclusion :** sur ce corpus, mon analyse indépendante n'apporte pas d'information supplémentaire par rapport au marché. Elle fait moins bien sur les places.

### B4. Mes niveaux de confiance étaient informatifs

| Confiance annoncée | Courses | Gagnant trouvé |
|---|---|---|
| Élevée / moyenne à bonne | 6 (2019, 2022, Vosges, Camargue, Vic, Andrieu) | 4 |
| Moyenne | 6 (2015, 2018, 2021, 2023, 2024, Case IH) | 1 |
| Faible | 2 (2020, 2025) | 0 |

Échantillon très réduit, mais le sens est cohérent.

### B5. Thémis contre autres courses

| | Thémis (9) | Autres (5) |
|---|---|---|
| Gagnant trouvé | 3 / 9 | 2 / 5 |
| Chevaux du podium dans mon top 3 | 11 / 27 | 8 / 15 |

---

## C. Diagnostic des erreurs

### C1. Les familles d'erreurs

| Famille | Cas | Connu avant le départ ? | Catégorie | Certitude du diagnostic |
|---|---|---|---|---|
| **1. Chevaux sans données classés au milieu par défaut** | Quick Fix 2e (prédit 11e), Valokaja Hindo 3e (9e), chevaux sans données de 2025 | Partiellement : gains élevés, D4, entourage | Évitable en partie | Moyenne |
| **2. Forme récente surpondérée face à la classe + D4** | Victor Ferm 1er (prédit 7e), Power Doc 1er (4e) | Oui : record, gain moyen, D4, cote | Évitable en partie | Moyenne |
| **3. Divergences avec le marché sans argument fort** | Chandelles 2e (8e), Imoko Jibelau 2e (5e), Dada del Ronco 8e (1re), Equinoxe Jiel DA (1er) | Oui : cote, J.-M. Bazire au sulky | Évitable | Moyenne |
| **4. Mauvais usage du record** | Viking Blue pénalisé pour un record lent (gagne) ; Jingle du Pont pas assez valorisé pour le meilleur record (gagne) | Oui | Évitable | Moyenne |
| **5. Pénalité excessive pour 3 D ou plus** | Falco Berry 2e (prédit 4e) | Oui | Évitable en partie | Faible (n = 8) |
| **6. Scénario non reporté dans le classement** | Aron The Baron 7e (prédit 3e) alors que mon scénario donnait l'avantage au 1er échelon | Oui | Évitable | Élevée |
| **7. Disqualification d'un cheval fiable** | 8 de mes 42 « top 3 » sont DA (Visitor, Delmonica, Helena di Quattro, Equinoxe Jiel, Galileo Bello, Harley Gema, Just de l'Oison, Impala de Val), dont 4 sans aucun D récent | Non | Incertitude de course | Élevée |
| **8. Effort trop tôt / exposé** | Django du Bocage, Icare de Phyt's, Dada del Ronco, Filwell | Non (le tracking est postérieur) | Incertitude de course | Élevée |
| **9. Données absentes** | 5 chevaux sans aucune donnée en 2025 | Non | Indisponible | Élevée |

### C2. Ce qui n'était pas une erreur

- **Les disqualifications** : 36 DA sur 200 partants (18 %). Mes « top 3 » sont DA à 19 %, soit la moyenne. Mon filtre de fiabilité ne les a pas protégés, mais 4 des 8 n'avaient aucun D récent : rien ne permettait de l'anticiper.
- **Les efforts trop tôt** : ils se voient dans le tracking, après la course. Le contre-exemple existe (Victor Ferm, Jingle du Pont et Grace du Digeon ont mené et gagné). Je n'en tire pas de règle.
- **Thémis 2018 (8 DA sur 16)** : le top 5 était correct (4 sur 5) ; l'hécatombe a redistribué l'ordre.

---

## D. Tendances répétées

Chaque tendance est mesurée séparément sur les Thémis (9 courses) et sur les autres courses (5). **Une tendance n'est retenue que si elle va dans le même sens dans les deux sous-ensembles.** Ces deux groupes ne constituent pas une vraie validation : j'ai vu toutes les arrivées. C'est seulement un contrôle de cohérence.

*Repère : taux de podium moyen = 42 / 200 = 21 %.*

| # | Tendance | Thémis | Autres | Exceptions | Confiance |
|---|---|---|---|---|---|
| D1 | **Déferré des 4 (D4) ≫ ferré ou partiel** | D4 : 23 podiums / 63 (37 %) · F4 : 2 / 38 · partiel : 1 / 26 | D4 : 12 / 42 (29 %) · F4 : 1 / 5 · partiel : 2 / 16 | Gagnants non D4 : Viking Blue (F4), Caban Prior (F4), Jingle du Pont (DP) | **Moyenne à bonne** (association forte et stable ; mais la ferrure accompagne souvent la classe et l'ambition de l'entourage) |
| D2 | **Le D4 n'augmente pas le risque de DA** | DA : D4 13 %, F4 21 %, partiel 29 % (tous groupes) | — | — | Moyenne |
| D3 | **Forme gagnante (≥ 2 victoires dans les 5 dernières)** | 10 podiums / 23 (43 %) | 6 / 13 (46 %) | Icare de Phyt's (4 victoires, 4e), Delmonica (DA) | Moyenne |
| D4 | **A gagné sa dernière course** | 6 / 14 (43 %) | 5 / 12 (42 %) | — | Moyenne |
| D5 | **Le recul de 25 m n'est pas un handicap mesurable** | Victoires : 6 / 74 reculés contre 3 / 63 ; podium 18 % contre 22 % | Trop peu de reculés | Thémis 2019 : les 5 premiers sont du 1er échelon | Moyenne |
| D6 | **Le nombre de D récents prédit le risque de DA** | 0 D : 9 % · 1 D : 25 % · 2 D : 50 % · 3 D ou plus : 1 / 6 | 0 D : 9 % · 1 D : 31 % · 2 D : 1 / 2 · 3 D ou plus : 0 / 2 | **3 D ou plus : 1 DA sur 8** (Falco Berry, Pingus Vang, Etenclin, Eberton, Tinamo Jet, Intello de Chenu, Vertige de Chenu ont trotté) | Bonne pour 0 à 2 D ; **non concluant à 3 ou plus** |
| D7 | **Le record ne prédit pas les places** | Podium : record ≥ 1'13"0 = 22 %, comparable aux autres catégories | — | — | Moyenne |
| D8 | **Un des 3 meilleurs records du lot gagne plus souvent** | 5 victoires / 27 contre 4 / 102 | 2 / 15 contre 3 / 45 | Viking Blue gagne avec le pire record (17e / 17) | Faible à moyenne |
| D9 | **Les placeurs réguliers sans victoire finissent placés, rarement 1ers** | Lover Face 5e, Dayak 3e, In En Vrie 3e, Gardner Shaw 3e, Ghost des Charrons 4e, Hidden Texas 4e, Tip Top Nelliere 6e | Evangelina Blue 4e, Yahoo Diamant 2e, Destino D.J. 6e, Hold Up Ranais 7e | Aucun n'a gagné ; Okay Dei Ronchi NC, Hubble du Vivier 9e | Moyenne (13 cas, aucune victoire) |
| D10 | **Le marché hiérarchise mieux que moi les places** | Voir B3 : 18 / 27 contre 13 / 27 | — | Andrieu 2025 (marché 1 / 3) | Moyenne |
| D11 | **Les chevaux sans données, soutenus par leur entourage ou le marché, réussissent** | Quick Fix 2e, Valokaja Hindo 3e, Partizan Face 5e, Eros Zola 2e, Harison du Plessis 4e, Iznogoud Am 5e | Les inconnus peu joués (cote ≥ 32) échouent : Bottnas Idol NC, Dutchess Sun 9e, H.C.'s Crazy Horse DA | Gims du Plessis (5,4) DA | Faible à moyenne |
| D12 | **J.-M. Bazire au sulky : toujours sur le podium** | Tropic du Hêtre 3e, Chandelles 2e | Imoko Jibelau 2e | Aucune, mais **n = 3** | **Faible** (hypothèse) |
| D13 | **Sans recul, le meilleur record gagne** | — | Cobra Killer Gar, Jingle du Pont : 2 / 2 | — | **Faible** (n = 2) |

**Tendance cherchée mais non retenue :** « une course pleine de chevaux à D récents finira en hécatombe ». Faux ici : Thémis 2018 (8 chevaux avec D, 8 DA) contre Thémis 2023 (10 chevaux avec D, 2 DA). Le nombre de DA d'une course n'est pas prévisible avec ces données.

---

## E. Consensus entre modèle et réalité

Les classements initiaux ne sont pas modifiés. Les ajustements concernent la méthode pour les courses futures.

| Principe de la V1 | Verdict | Raison | Ajustement pour la V2 |
|---|---|---|---|
| Pénaliser fortement les D/A répétés | **Conservé sous conditions** | 1 et 2 D : taux de DA multiplié par 3 à 5 (D6) | Pénaliser 1 à 2 D. **Pour 3 D ou plus : mis en attente** (1 DA sur 8). Ne pas utiliser l'absence de D pour départager les premiers : environ 9 % de DA restent incompressibles. |
| Avantage du cheval le plus riche du 1er échelon | **Révisé (abandonné)** | Le plus riche sans recul : 0 victoire sur 12 courses, 2 deuxièmes | Ne plus utiliser la position dans l'échelon comme argument. |
| Un record lent limite une série de victoires | **Révisé** | Le record ne prédit pas les places (D7) ; Viking Blue gagne en courant plus vite que son record | Le record sert à départager **pour la victoire**, pas pour les places. |
| Le recul de 25 m se rattrape | **Conservé** | 6 gagnants de Thémis sur 9 sont des reculés (D5) | Ne pas pénaliser le recul par défaut. Exception possible quand le 2e échelon est petit et irrégulier (2019, cas unique : hypothèse). |
| D4 = bonus modéré, jamais décisif seul | **Révisé à la hausse** | Association la plus forte du corpus (D1) ; pas plus de DA (D2) | Un ferré ou un partiel doit avoir des arguments nettement supérieurs pour être classé devant un D4 comparable. Risque de confusion avec la classe : à confirmer. |
| La forme récente prime | **Conservé sous conditions** | ≥ 2 victoires ou une victoire à la dernière : environ 43 % de podium (D3, D4) | Mais ne pas l'opposer à la classe : Victor Ferm et Power Doc gagnent avec une forme moyenne, un excellent record, le D4 et un entourage fort. |
| Les régularités départagent les premiers | **Conservé pour les places seulement** | Placeurs : aucune victoire sur 13 (D9) | Classer les placeurs réguliers dans les places (2e à 5e), pas en 1er. |
| La cote sert uniquement de contrôle | **Révisé** | Le marché fait mieux que moi sur les places et n'a jamais fait pire (D10) | La cote devient le **point de départ**. Je ne m'en écarte qu'avec un argument nommé et vérifiable, et je note chaque écart pour en mesurer la valeur. |
| Un cheval inconnu se classe au milieu | **Révisé** | Les inconnus avec gains élevés et entourage fort finissent souvent placés (D11) | Classer un inconnu d'après ses gains, sa ferrure, son entourage et sa cote ; bas seulement si le marché le délaisse. |
| Effet J.-M. Bazire au sulky | **Hypothèse à tester** | 3 sur 3 (D12) | Ne plus déclasser un cheval drivé par J.-M. Bazire sur sa seule musique. Mesurer sur de nouvelles courses. |
| Sans recul, la vitesse prime | **Hypothèse à tester** | 2 sur 2 (D13) | À vérifier sur d'autres courses de 6 ans sans recul. |
| Cohérence scénario → classement | **Nouvelle règle de procédure** | Thémis 2019 : bon scénario, classement incohérent | Contrôler, avant de figer un classement, qu'il respecte le scénario principal annoncé. |

---

## F. Scénarios de course

Le corpus soutient **cinq** configurations. Je n'en invente pas de sixième : l'« hécatombe de DA » n'est pas reconnaissable avant le départ (voir D).

### Scénario 1 — Le dominant identifié
1. **Mécanisme :** un cheval cumule classe, forme et entourage, et le marché le désigne nettement.
2. **Indices pré-course :** favori à **2,1 ou moins** ; D4 ; gain moyen parmi les plus élevés ; pas de D à la dernière course.
3. **Profils favorisés :** le dominant pour la victoire ; les réguliers pour les places.
4. **Profils pénalisés :** les outsiders qui ont besoin d'une course sélective.
5. **Observations :** favoris à 2,1 ou moins : Cobra Killer Gar (1,4), Harlem de Bucy (1,8), Grace du Digeon (2,1) → **3 victoires sur 3**.
6. **Exceptions :** favoris entre 2,5 et 3,9 : 1 victoire sur 6 (Hymne du Gers gagne ; Falco Berry 2e, Just de l'Oison DA, Filwell 4e, Icare de Phyt's 4e, Dayak 3e).
7. **Confiance :** faible (n = 3). Le seuil exact est une hypothèse.
8. **Utilisation future :** si la configuration est remplie, garder le dominant 1er et consacrer l'analyse à l'ordre des places. Entre 2,5 et 3,9, le favori n'est pas un dominant : garder plusieurs hypothèses pour la victoire.

### Scénario 2 — Le second échelon impose sa classe (attelé, recul de 25 m)
1. **Mécanisme :** les reculés, plus riches et souvent D4, comblent les 25 m dans une course au train.
2. **Indices pré-course :** 2e échelon fourni (8 reculés ou plus) contenant des chevaux en forme, D4, avec de bons records.
3. **Profils favorisés :** reculés D4 en forme ou de classe (Calle Crown, Isofou du Chêne, Hedic Gema, Power Doc, Harlem de Bucy).
4. **Profils pénalisés :** chevaux du 1er échelon qui font l'effort trop tôt (Icare de Phyt's, Django du Bocage — dont le parcours n'était pas prévisible).
5. **Observations :** Thémis 2018, 2020 (podium 100 % reculé), 2021, 2023, 2024, 2025 : 6 gagnants reculés sur 9 Thémis.
6. **Exceptions :** Thémis 2019 (6 reculés irréguliers, aucun sur le podium) ; Thémis 2015 et 2022 (gagnant du 1er échelon en forme).
7. **Confiance :** moyenne.
8. **Utilisation future :** par défaut, ne pas pénaliser le recul. Basculer vers le 1er échelon seulement si le 2e est petit et sans forme (hypothèse fondée sur 2019 seul).

### Scénario 3 — La vitesse pure sans recul
1. **Mécanisme :** tous les partants à la même distance ; la vitesse de pointe décide de la victoire.
2. **Indices pré-course :** pas de recul (courses réservées à une génération, ici des 6 ans) ; un cheval au record nettement meilleur.
3. **Profils favorisés :** le meilleur record du lot, même irrégulier (Jingle du Pont).
4. **Profils pénalisés :** les réguliers lents, pour la victoire seulement.
5. **Observations :** Camargue 2024, Vic sur Cère 2025 : le meilleur record gagne 2 fois sur 2.
6. **Exceptions :** aucune observée, mais seulement 2 courses.
7. **Confiance :** faible.
8. **Utilisation future :** hypothèse prioritaire à tester. Dans ces courses, remonter le meilleur record dans les 3 premiers.

### Scénario 4 — La course à inconnues
1. **Mécanisme :** plusieurs chevaux sans données exploitables (étrangers, retours, fiches vides) ; l'analyse sportive ne couvre qu'une partie du lot.
2. **Indices pré-course :** musique française vide ou absente ; gains connus élevés ; course européenne ; records de qualification.
3. **Profils favorisés :** inconnus riches, D4, avec un entourage fort ou soutenus par le marché.
4. **Profils pénalisés :** inconnus délaissés par le marché (cote ≥ 30 environ).
5. **Observations :** Thémis 2015, 2018, 2025 (6 inconnus soutenus sur le podium ou dans les 5) ; courses de 6 ans (3 inconnus peu joués, tous loin).
6. **Exceptions :** Gims du Plessis (5,4) DA.
7. **Confiance :** faible à moyenne.
8. **Utilisation future :** ne jamais classer un inconnu au milieu par défaut. L'ordonner d'après ses gains, son entourage et sa cote, puis baisser la confiance globale du classement.

### Scénario 5 — Le trot monté
1. **Mécanisme :** discipline à part, où la spécialisation au monté compte d'abord.
2. **Indices pré-course :** musiques en « m » ; jockeys ; peu de reculés (2 sur 10 et 2 sur 11 ici).
3. **Profils favorisés :** spécialistes en forme au monté, sans recul (Caban Prior, Emir de Rebomard, Heuristique, Go Or Not).
4. **Profils pénalisés :** reculés qui doivent produire un long effort (Filwell 4e après avoir été le plus rapide en milieu de course ; Coach Franbleu 9e) ; chevaux à la classe passée (Evidence Roc NC).
5. **Observations :** les deux gagnants partaient à 2 850 m ; aucun reculé sur les 6 places de podium.
6. **Exceptions :** Hannibal Tuilerie (plutôt attelé) 3e.
7. **Confiance :** faible (2 courses).
8. **Utilisation future :** traiter le monté séparément et ne pas lui appliquer les conclusions attelé, en particulier sur le recul.

---

## G. Matrice de décision (pour les prochaines analyses)

| Indices observables avant le départ | Scénario privilégié | Facteurs à revaloriser | Risques à surveiller | Solidité |
|---|---|---|---|---|
| Favori à 2,1 ou moins, D4, gain moyen parmi les plus élevés, pas de D à la dernière | 1. Dominant | Le favori pour la victoire ; les placeurs réguliers pour 2e-5e | DA (environ 9 % même sans D) | Faible (n = 3) |
| Favori entre 2,5 et 4 | Plusieurs hypothèses | Les 3 premiers du marché, D4 et forme gagnante | Forcer un vainqueur unique | Faible |
| Attelé, recul de 25 m, 8 reculés ou plus dont des D4 en forme | 2. Second échelon | Reculés D4 en forme ou de classe ; ne pas pénaliser le recul | 1er échelon trop bien classé par réflexe | Moyenne |
| Attelé, recul de 25 m, 2e échelon petit (6 environ) et irrégulier | 1er échelon (variante du 2) | Chevaux du 1er échelon en forme | Hypothèse issue d'une seule course | Faible |
| Pas de recul (courses d'une génération) | 3. Vitesse pure | Meilleur record du lot, même irrégulier | Le record peut avoir été établi en autostart | Faible (n = 2) |
| Fiches vides, étrangers, course européenne, records de qualification | 4. Inconnues | Gains, entourage, ferrure, cote des inconnus | Confiance surévaluée | Faible à moyenne |
| Trot monté | 5. Monté | Spécialistes en forme sans recul | Long effort des reculés ; classe passée | Faible |
| **Dans toutes les configurations** | — | D4 (D1) ; ≥ 2 victoires récentes ou victoire à la dernière (D3, D4) ; marché comme point de départ (D10) | Placeur classé 1er (D9) ; 1 à 2 D récents (D6) | Moyenne |
| Mon classement s'écarte du favori du marché | — | Nommer l'argument précis de l'écart | Les deux écarts de ce corpus ont échoué | Moyenne |

---

## H. Synthèse finale

### Les conclusions les plus solides
1. **Le classement V1 sépare bien le haut et le bas** (45 % de podium pour mes 3 premiers, 7 % au-delà du 7e), **mais n'a pas battu le marché** sur les places (13 contre 18 sur 27).
2. **La ferrure D4 est l'indicateur le plus fortement associé au podium** dans les deux sous-ensembles, sans hausse du risque de DA. Elle était sous-pondérée.
3. **Le recul de 25 m n'est pas un handicap mesurable** dans les Thémis.
4. **Les placeurs réguliers sans victoire restent des placeurs.**
5. **Les DA de chevaux fiables et les efforts trop tôt ne sont pas des erreurs de modèle** : ils relèvent de l'incertitude de course.

### Les principales incertitudes
- **14 courses, dont 9 comparables** (Thémis). Les échantillons de chaque tendance vont de 2 à 105 chevaux : aucune tendance n'est validée.
- **Corrélations non causales :** le D4 accompagne souvent la classe et l'ambition de l'entourage.
- **Données manquantes :** dates des courses passées, terrain, type de DA (départ ou en course), tracking des courses précédentes. Thémis 2025 reste à compléter. Les musiques contaminées entre courses (voir l'audit V1) ont été écartées, mais elles devront être nettoyées avant tout nouvel essai sur ces mêmes courses.

### Améliorations à tester (sans les déclarer validées)
1. **Figer la méthode V2** (matrice G) **avant** d'analyser de nouvelles courses.
2. **Tester sur 15 à 20 nouvelles courses qui n'ont pas servi à construire la V2**, en priorité des 2 850 m de Vincennes. Pour chaque course, noter avant le départ : le classement V2, le favori du marché, et chaque écart volontaire au marché avec son argument.
3. **Mesurer** : gagnant trouvé, chevaux du podium dans le top 3, comparaison au marché, et taux de réussite des écarts volontaires au marché.
4. **Hypothèses à surveiller en priorité :** J.-M. Bazire au sulky (D12), meilleur record sans recul (D13), seuil de 2,1 pour le dominant (S1), 3 D ou plus (D6).
5. **Ajouter aux futurs jeux de données :** dates des 5 dernières courses, terrain, nature des D, tracking des courses précédentes (pour repérer les chevaux qui partent trop tôt).
