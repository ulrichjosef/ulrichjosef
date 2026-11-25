---
name: analyse-pronostics
description: >-
  Analyse quantitative et détection de value pour paris hippiques (PMU/Quinté+ :
  plat handicap, trot attelé avec échelons, autostart, Grande Piste, obstacle),
  football et tennis. À utiliser dès que l'utilisateur demande une analyse de
  course hippique, un pronostic Quinté+, une analyse de match de foot ou de
  tennis, une recherche de "value"/edge contre les cotes, une construction de
  tickets/combinés, un pari "sûr à 90 %", ou parle de scoring composite pondéré
  par SHAP, devigging, Poisson/Dixon-Coles, xG, Elo par surface, staking/Kelly,
  ou de probabilités calibrées sur des événements sportifs. Déclenche cette
  compétence même si l'utilisateur ne dit pas explicitement "value" ou "modèle" —
  toute demande de pronostic structuré ou d'analyse prédictive sur une course ou
  un match relève de cette compétence.
---

# Analyse Pronostics — Value & Probabilités Calibrées

Cette compétence produit, pour une course hippique ou un match (football, tennis),
une **estimation de probabilité la plus fiable possible**, la **détection des value
bets** (là où le marché se trompe) et une **mise disciplinée**. Elle travaille en
français et suit une architecture modulaire réutilisable (Bloc 0 + étapes numérotées).

## Ce que l'outil garantit — et ne garantit pas

À poser explicitement à chaque livrable, pour ne jamais tromper l'utilisateur :

- **Ce qui est livré** : des probabilités calibrées, l'écart de value contre les
  cotes, et une taille de mise proportionnée à l'edge.
- **Ce qui n'est PAS livré** : la certitude. Les résultats sportifs contiennent de
  l'aléa irréductible (chute, cadre du filet, carton, disqualification, incident de
  course). Un événement estimé à 90 % perd encore ~1 fois sur 10, et le marché le
  cote généralement autour de 1.10–1.12 : l'avantage y est mince.
- **La vraie source du gain** : être *mieux calibré que le marché* sur un grand
  nombre de paris. L'edge se compose sur la durée ; il ne se matérialise pas ticket
  par ticket. Ne jamais promettre un pronostic « sûr de passer ».

Traduire toute demande de « prédiction certaine » ou « infaillible » en son
équivalent honnête et opérationnel : **la probabilité la plus fiable + le value +
la mise qui protège le capital**. C'est la version la plus poussée qui existe
réellement, y compris pour les syndicats professionnels.

## Pipeline unifié (à adapter par discipline)

Applique ces étapes dans l'ordre. Les détails propres à chaque discipline sont dans
`references/` — lis le fichier correspondant avant de modéliser.

### Bloc 0 — Cadre & collecte
- Identifier l'épreuve : discipline, format exact (voir routage ci-dessous),
  hippodrome/compétition, distance/surface, conditions du jour, heure.
- Rassembler **toutes** les données disponibles, sans présélection à ce stade :
  historique des épreuves passées, forme récente, cotes de marché (PMU, ou
  bookmaker), et les variables spécifiques listées dans le fichier de discipline.
- Noter les données manquantes ou incertaines : elles élargiront l'intervalle de
  confiance, elles ne doivent pas être remplacées par des suppositions.

### Étape 1 — Ingestion & nettoyage
- Structurer les données en tableau exploitable (une ligne par partant / une ligne
  par match).
- Nettoyer : unités homogènes, gestion des non-partants/forfaits, des cotes
  aberrantes, des valeurs manquantes (imputation explicite et signalée, jamais
  silencieuse).

### Étape 2 — Sélection de variables (éliminer le bruit, garder le signal)
C'est le cœur de la demande « prendre ce qui est très important, jeter ce qui ne
sert à rien ». Procéder rigoureusement :
- **Importance** : classer les variables par pouvoir prédictif (pondération de type
  SHAP sur un modèle de référence, ou à défaut corrélation/gain d'information).
  Construire un score composite pondéré (ex. SGC/SGP/SGV selon la discipline).
- **Multicolinéarité** : calculer le VIF ; écarter ou fusionner les variables
  redondantes (VIF élevé) pour éviter le double comptage.
- **Parcimonie** : conserver le sous-ensemble minimal qui explique l'essentiel de la
  variance. Documenter ce qui a été éliminé et pourquoi — la transparence de la
  chaîne de raisonnement fait partie du livrable.

### Étape 3 — Modèle probabiliste (par discipline)
- Convertir les scores en probabilités selon le modèle adapté :
  - Hippisme → Plackett-Luce ou softmax sur les scores composites (probabilités de
    victoire et de place cohérentes entre elles).
  - Football → Poisson / Dixon-Coles alimenté par des forces attaque/défense
    informées par les xG.
  - Tennis → modèle logistique / Elo par surface, converti en proba de match.
- Voir le fichier de discipline pour la spécification exacte.

### Étape 4 — Calibration & validation
- **Validation temporelle walk-forward** : tester sur des épreuves antérieures dans
  l'ordre chronologique, jamais en mélangeant passé et futur (pas de fuite de
  données).
- Vérifier la **calibration** : sur l'historique, les événements donnés à p % se
  réalisent-ils ~p % du temps ? Ajuster si le modèle est sur- ou sous-confiant.
- Rapporter une mesure honnête de performance (log-loss / Brier **avec intervalle
  de confiance bootstrap 95 %**), pas seulement un taux de réussite brut. Deux
  modèles dont les IC se chevauchent ne sont pas significativement différents.
- Méthode de recalibration selon la taille d'échantillon : **Platt (sigmoïde) si
  n ≤ 500, isotonique au-delà** (l'isotonique sur-apprend sur petit échantillon).
- Pour les marchés à plusieurs issues (1X2, gagnant de course), mesurer l'**ECE par
  classe** : un modèle juste sur 1 et 2 mais faux de 5 points sur le nul peut
  afficher un bon ECE global et perdre de l'argent dès qu'on applique Kelly.
- ECE **non fiable** si moins de 80 % des intervalles (bins) sont remplis : réduire
  le nombre de bins ou attendre plus de données avant de conclure.
- **Geler** les probabilités avant l'épreuve (horodatage + empreinte SHA-256) pour
  pouvoir les évaluer honnêtement après coup.

### Étape 5 — Devigging du marché & edge value
- Retirer la marge du bookmaker/PMU des cotes pour obtenir la **probabilité
  implicite « juste »** du marché. Méthode par défaut : **Shin** (corrige le biais
  favori/outsider, important en hippisme et sur les gros outsiders) ; power ou
  multiplicative en contrôle. Toujours indiquer la marge (overround) observée.
- Calculer l'**edge** : `edge = p_modèle − p_marché_dévigée`. Un value bet existe
  quand l'edge est positif et significatif au-delà du bruit d'estimation.
- Ne retenir comme value QUE les écarts robustes ; un petit edge sur une donnée
  fragile n'est pas un value. Seuil opérationnel par défaut : **EV = p × cote − 1
  ≥ 5 %** (ajustable par marché).

### Étape 6 — Sélection & staking
- Trier les sélections par edge et par fiabilité de l'estimation.
- Dimensionner les mises via **Kelly fractionné** (typiquement ¼ à ½ Kelly pour
  amortir la variance et l'erreur de modèle), plafonné à un pourcentage fixe de la
  bankroll par pari.
- Pour les combinés/tickets : tenir compte de la **corrélation** entre jambes (des
  événements liés ne se multiplient pas comme des indépendants) et de l'explosion du
  risque à chaque jambe ajoutée.
- Rappeler la règle d'or : ne jamais miser une somme dont la perte serait
  problématique ; l'edge ne dispense pas de la gestion de capital.
- **Suivre le CLV** (closing line value) : CLV = cote prise × proba juste de clôture
  (dévigée) − 1. C'est l'indicateur précoce le plus fiable d'un edge réel, bien
  avant le ROI. Ne jamais comparer à la cote de clôture brute (gonfle le CLV).
  Moyenne glissante sur 50 paris < +1 % → pause et audit.

### Étape 7 — Livrable structuré
Produire une sortie claire et actionnable (format ci-dessous).

## Routage par discipline

Lire le fichier correspondant AVANT de modéliser :

| Demande | Fichier à lire |
|---|---|
| Course hippique : Quinté+, plat handicap, trot attelé (échelons), autostart, Grande Piste Vincennes, obstacle/Auteuil | `references/hippisme.md` |
| Match de football : 1X2, BTTS, over/under, score exact, combinés, "sûr à 90 %" | `references/football.md` |
| Match de tennis : vainqueur, sets, surface (terre/gazon/dur), "sûr à 90 %" | `references/tennis.md` |

**Football — calculs exécutables** : si le skill `prevision-football` est
disponible, utiliser ses scripts (modèle Dixon-Coles ajusté sur historique,
dérivation des marchés, dévigage Shin/power, EV + Kelly plafonné, CLV, gel
SHA-256, rapport de calibration) plutôt que de calculer à la main.

Si la demande couvre plusieurs disciplines (ex. programme mixte), traiter chacune
avec son fichier puis regrouper les tickets en fin de livrable.

## Format de sortie (gabarit)

Utiliser cette structure, adaptée à la discipline :

```
# [Épreuve / Match] — Analyse Value

## 1. Cadre
Discipline, format, conditions, heure. Données manquantes signalées.

## 2. Variables retenues (et écartées)
- Retenues : liste + poids/justification
- Écartées : liste + raison (faible signal, VIF élevé, redondance)

## 3. Probabilités du modèle
Tableau : sélection | proba modèle | cote marché | proba marché dévigée (Shin) | EV | mise
Marge bookmaker observée.

## 4. Value bets
Sélections à edge positif robuste, triées par fiabilité.

## 5. Tickets & mises proposés
- Base / associés / value (hippisme) ou combinés (foot/tennis)
- Taille de mise (% bankroll, Kelly fractionné)
- Note sur la corrélation des jambes le cas échéant

## 6. Confiance & réserves
Niveau de calibration (Brier + IC, ECE et fiabilité des bins), incertitudes,
aléa résiduel. Empreinte de gel si le pronostic est figé. Rappel : proba ≠ certitude.
```

## Principes transversaux (à respecter à chaque analyse)

- **Honnêteté probabiliste** : toujours exprimer une confiance, jamais une
  certitude. Un « pari à 90 % » est une probabilité, pas une garantie.
- **Transparence** : exposer la chaîne de raisonnement, les variables retenues et
  éliminées, et la méthode de calibration.
- **Robustesse avant flair** : préférer une donnée solide à une intuition ; un edge
  n'a de valeur que s'il survit à la validation.
- **Discipline de capital** : la gestion de mise (Kelly fractionné, plafond par
  pari) protège plus sûrement que n'importe quel « coup sûr ».
- **Reproductibilité** : sorties déterministes et structurées, réutilisables d'une
  journée de courses à l'autre.

## Repère de réalisme

Un modèle de buts sérieux, validé hors échantillon sur 135 matchs internationaux
(projet open source sports-forecasting-platform), obtient un Brier 1X2 d'environ
0.21–0.22 — et manque ses propres objectifs de calibration. Plusieurs raffinements
séduisants (inflation des nuls, calibration bêta, pondération par enjeu, modèles
bayésiens hiérarchiques, valeur marchande des effectifs) n'y ont apporté **aucun
gain significatif**. Leçon : la simplicité bien calibrée bat la complexité, et un
raffinement ne s'adopte qu'après preuve en backtest.

## Jeu responsable

Cet outil vise l'analyse et l'edge à long terme, pas le gain garanti. Le pari
comporte un risque de perte réel. Ne miser que des sommes dont la perte reste sans
conséquence, ne jamais tenter de « se refaire » après une perte, et fixer des
limites à l'avance. La rigueur statistique ne supprime pas le risque — elle le rend
gérable.
