---
name: pronostics-apprentissage
description: >-
  Boucle d'amélioration continue (backtest + calibration) pour les analyses de
  pronostics sportifs et hippiques. À utiliser quand l'utilisateur veut que ses
  skills d'analyse (courses hippiques PMU/Quinté+, football, tennis) s'améliorent
  avec le temps : journaliser les pronostics et leurs résultats, mesurer la
  calibration / score de Brier / log-loss / ROI, diagnostiquer les biais
  systématiques, faire un post-mortem après une course ou un match, ou proposer
  des corrections validées à un skill d'analyse. Déclenche aussi quand
  l'utilisateur dit « améliore le modèle », « apprends de mes résultats »,
  « pourquoi le pronostic a raté », « backtest », « suivi de performance », ou
  demande de rendre un skill de pronostic progressivement plus fiable. Ne pas
  utiliser pour produire une analyse initiale (c'est le rôle des skills
  d'analyse) — celui-ci sert à mesurer, diagnostiquer et corriger après coup.
---

# Pronostics — Apprentissage & Amélioration Continue

Cette compétence transforme chaque analyse en donnée, suit les pronostics face aux
résultats réels, et affine les skills d'analyse là où ils montrent une erreur
**systématique** — sans jamais surapprendre le bruit d'un résultat isolé. Elle
travaille en français et complète les skills d'analyse (ex. `pronostics-value`),
qu'elle cherche à rendre progressivement mieux calibrés.

## Vérité fondamentale : ce que la boucle peut et ne peut pas faire

À garder en tête à chaque itération, et à rappeler à l'utilisateur :

- Elle réduit l'erreur **réductible** (biais systématiques) vers le **plancher
  d'aléa incompressible** propre au sport. Elle ne l'amène pas à zéro : une chute,
  un cadre de filet, un carton, une disqualification restent hors de portée de
  toute donnée.
- **Le piège n°1 est le surapprentissage.** Un pronostic à 65 % qui perd n'est PAS
  une preuve de défaut : il est censé perdre 35 % du temps. Corriger le skill après
  chaque perte le fait courir après le bruit et le dégrade. On ne corrige QUE des
  biais systématiques établis sur un échantillon suffisant.
- Le marché s'adapte : l'edge se dégrade avec le temps. C'est une **vigilance
  continue**, pas une ligne d'arrivée. Il n'existe pas d'état final « résolu ».
- « Très puissant », honnêtement, veut dire : **bien calibré + edge réellement
  réalisé sur un grand nombre de paris, avec surveillance de la dégradation** — pas
  une erreur nulle.

## La boucle en 7 phases

### Phase 1 — Journaliser chaque pronostic
Au moment de l'analyse, écrire une ligne par sélection dans le journal JSONL
(schéma ci-dessous), en incluant `skill_utilise` et `skill_version` pour savoir
quel skill a produit le pronostic.

### Phase 2 — Enregistrer le résultat
Une fois la course/le match connu, compléter la même entrée : `resultat`
(gagne/perdu) et `gain_net` (résultat net de la mise, négatif si perdu).

### Phase 3 — Revue périodique (JAMAIS après chaque événement)
Déclencher une revue seulement après un **échantillon suffisant** de pronostics
résolus (repère : ≥ ~50 par discipline/marché) ou à cadence fixe (hebdomadaire).
Lancer `scripts/calibration_report.py` sur le journal.

Indicateur précoce : le **CLV** se stabilise bien plus vite que le ROI. Un CLV
moyen positif sur 50+ paris est un meilleur signe d'edge qu'un ROI positif sur
le même volume (le ROI est dominé par la variance).

### Phase 4 — Diagnostiquer (signal vs bruit)
Lire le rapport et distinguer un **biais systématique** d'une simple variance :
taille d'échantillon, cohérence de la direction de l'erreur, ampleur. Détails et
grille de lecture dans `references/diagnostic-et-corrections.md`.

### Phase 5 — Proposer une correction ciblée
Seulement si un biais systématique est établi avec des preuves. Viser une
modification **précise** du fichier de référence concerné du skill d'analyse
(poids d'une variable, facteur de correction, méthode de devigging,
recalibration globale de température, variable ajoutée/retirée). Une seule
modification à la fois.

### Phase 6 — Valider sur données mises de côté (hold-out)
Avant d'appliquer : la correction améliore-t-elle Brier / log-loss / ROI sur des
pronostics **non utilisés** pour la diagnostiquer ? Exiger que l'amélioration du
Brier sorte de l'intervalle de confiance bootstrap de l'ancienne version ; sinon,
la consigner comme **résultat négatif** (sans l'appliquer) — c'est une information
utile, pas un échec. Si elle n'améliore pas
hors-échantillon, la rejeter. On ne garde qu'une amélioration nette et robuste.

### Phase 7 — Appliquer avec changelog, version et possibilité de rollback
Appliquer la modification, incrémenter la version du skill d'analyse, et écrire une
entrée de changelog (date, biais diagnostiqué, changement, effet attendu, résultat
de validation). Conserver l'historique pour tracer — et pouvoir annuler — toute
régression.

## Schéma du journal (JSONL — un objet par sélection)

Une ligne = une sélection. Champs (ceux marqués * requis pour la calibration) :

```json
{
  "id": "2026-07-06-stcloud-r1c3-c7",
  "date_analyse": "2026-07-06",
  "date_evenement": "2026-07-06",
  "discipline": "hippisme",              // hippisme | football | tennis
  "format": "plat_handicap",             // ex: trot_attele, autostart, 1X2, vainqueur...
  "epreuve": "Quinté+ Saint-Cloud R1C3",
  "selection": "Cheval 7",
  "marche": "victoire",                  // victoire | place | 1X2 | BTTS | over_2.5 | handicap_jeux ...
  "p_modele": 0.62,                       // * probabilité estimée par le skill (0-1)
  "cote": 2.10,
  "p_marche_devig": 0.55,
  "edge": 0.07,
  "mise": 5.0,                            // mise engagée
  "skill_utilise": "pronostics-value",   // quel skill a produit ce pronostic
  "skill_version": "1.0.0",
  "resultat": "gagne",                   // * gagne | perdu | null (en attente)
  "gain_net": 5.50,                       // résultat net (négatif si perdu ; null si en attente)
  "cote_cloture": 1.95,                   // cote à la clôture (pour le CLV)
  "clv_pct": 3.3,                         // optionnel : CLV déjà calculé (dévigé)
  "lock_sha256": "9a70…",                 // optionnel : empreinte du pronostic gelé
  "notes": "terrain lourd, compo confirmée"
}
```

`p_modele` et `resultat` suffisent pour la calibration et Brier/log-loss.
`mise` et `gain_net` permettent le ROI. Le reste sert aux ventilations et au
diagnostic.

## Garde-fous anti-surapprentissage (le cœur de l'outil)

Ces règles font la différence entre une boucle qui améliore et une boucle qui
dégrade :

- **Jamais de correction sur un résultat isolé.** Une perte à 65 % est un événement
  normal, pas un bug.
- **Échantillon minimum** avant tout changement de poids ; sans volume, on ne
  distingue pas biais et malchance.
- **Juger par bin de calibration**, pas par ticket : c'est l'écart *systématique*
  entre proba prédite et fréquence observée sur un intervalle qui révèle un biais.
- **Valider hors-échantillon** chaque correction ; ne conserver que le gain net.
- **Versionner** chaque skill d'analyse et pouvoir revenir en arrière.
- **Revérifier périodiquement** la dégradation d'edge (adaptation du marché) : une
  correction utile hier peut ne plus l'être.

## Utiliser le script de calibration

```bash
python scripts/calibration_report.py --journal chemin/vers/journal.jsonl
# filtrer une discipline :
python scripts/calibration_report.py --journal chemin/vers/journal.jsonl --discipline hippisme
# sortie machine :
python scripts/calibration_report.py --journal chemin/vers/journal.jsonl --json
```

Le script (Python standard, sans dépendance) renvoie : comptages
(total/résolus/en attente), **score de Brier avec IC 95 % bootstrap**,
**log-loss**, **ECE** avec contrôle de fiabilité (≥ 80 % des bins remplis),
**courbe de calibration** (proba prédite vs fréquence observée par intervalle),
**ROI réalisé**, **CLV glissant sur 50 paris** (alerte si < +1 %), et
ventilations par discipline et par marché. Interpréter via
`references/diagnostic-et-corrections.md`.

## Modifier un skill d'analyse en toute sécurité

- Cibler le **fichier de référence précis** du skill utilisé (champ
  `skill_utilise`) — ex. `references/hippisme.md`, `references/football.md`,
  `references/tennis.md`.
- **Une modification à la fois**, documentée. Tenir un `CHANGELOG.md` dans le skill
  d'analyse : date, biais diagnostiqué (avec la métrique à l'appui), changement
  effectué, effet attendu, résultat de la validation hold-out, nouvelle version.
- En cas de régression détectée à la revue suivante, **annuler** via le changelog.

## Jeu responsable

Ne jamais augmenter les mises sur une bonne série : la variance coupe dans les deux
sens, et une série heureuse n'est pas une preuve d'edge. La boucle améliore la
calibration, pas la certitude ; la discipline de capital reste indispensable.

Pour la grille de diagnostic détaillée, les biais systématiques fréquents par
discipline et leurs corrections, et les techniques de recalibration (température /
Platt / isotonique), lire `references/diagnostic-et-corrections.md`.
