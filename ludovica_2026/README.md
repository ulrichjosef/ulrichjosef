# Prix Ludovica 2026 — R1C4 Vincennes (02/10/2026)

Trot attelé, autostart, Grande Piste 2700 m, 14 partants, terrain bon.

- `modele.py` : score composite pondéré (7 dimensions), softmax τ=1,5,
  fusion log-linéaire 50/50 avec le marché dévigé, Monte-Carlo
  Plackett-Luce (200 000 tirages), Kelly ¼ sur rapport réaliste, tickets Quinté+.
- `resultats.txt` : sortie brute.

Les notes par dimension sont expertes (pas d'historique pour un apprentissage
SHAP) : à recalibrer via le journal `../sgc_plat_cpl/output/journal_pronostics.jsonl`.
