# Changelog

## 1.1.0 — 2026-11-25
Apports issus de sports-forecasting-platform (MIT) :
- Calibration : Brier avec IC bootstrap 95 %, Platt si n ≤ 500 / isotonique au-delà,
  ECE par classe, contrôle de fiabilité des bins (≥ 80 % remplis).
- Gel des pronostics avant l'épreuve (horodatage + SHA-256).
- Dévigage Shin par défaut, marge affichée ; seuil de value EV ≥ 5 %.
- Suivi CLV dévigé, alerte si moyenne glissante 50 paris < +1 %.
- Football : pondération temporelle, matchs antérieurs uniquement, proba conjointe
  des combinés dans la matrice de scores, mélange modèle/marché si données minces ;
  renvoi vers les scripts du skill `prevision-football`.
- Repère de réalisme (Brier ~0.21–0.22) et résultats négatifs documentés.

## 1.0.0
Version d'origine.
