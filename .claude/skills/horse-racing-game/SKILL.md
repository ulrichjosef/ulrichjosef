---
name: horse-racing-game
description: Lancer, modifier ou publier le jeu de course de chevaux JavaScript du dossier horse-racing-game/ (HTML/CSS/JS sans dépendances). Utiliser quand l'utilisateur veut jouer au jeu, le tester, changer ses règles (paris, vitesse, nombre de tours, chevaux), ses graphismes, ou le publier en page web.
---

# Jeu de course de chevaux

Jeu web statique de Fotios Kitsantas, sous licence GPL-3.0. Quiconque le modifie ou le redistribue doit garder `LICENSE` et la mention de l'auteur.
Version en ligne (Artifact privé) : https://claude.ai/artifact/7cUi3amt6QobCNjPRjecHZ

## Fichiers (dans `horse-racing-game/`)
- `index.html` : 4 chevaux (`#horse1`…`#horse4`), la piste, le formulaire de pari (`#amount`, `#bethorse`, `#num_lap`), le bouton `#start` et le tableau `#results`.
- `game.js` : l'objet `Horse(id, x, y)`. La vitesse est tirée au hasard entre 10 et 20 et retirée à chaque virage. Le cheval suit la boucle `moveRight` → `moveDown` → `moveLeft` → `moveUp` (positions en vw/vh), puis `arrive()` enregistre le classement et règle le pari. Le joueur part avec `funds = 100` £.
- `game.css` : les sprites (en-têtes `background-position`), les animations `runLeft`/`runRight`/`runUp`/`runDown` et la mise en page de la piste.
- `images/` : sprites des chevaux, des têtes et corps des jockeys, et textures de la piste.

## Lancer le jeu
Il n'y a pas de build. Ouvrir `horse-racing-game/index.html` dans un navigateur, ou servir le dossier en local :
```bash
cd horse-racing-game && python3 -m http.server 8000
```
Pour vérifier le jeu sans navigateur visible : avec Playwright, remplir `#amount`, cliquer `#start`, attendre environ 10 s, puis lire `#funds` et `#results`.

## Modifications courantes
- Mise de départ : `funds = 100` dans `game.js` et `<span id="funds">100</span>` dans `index.html`.
- Plage de vitesse : `Math.random()*10 + 10`, à changer partout où elle apparaît dans `game.js`.
- Gain : dans `arrive()`, `funds += amount`. Pour une cote, multiplier `amount`.
- Ajouter un cheval : il faut à la fois un `div` dans `index.html`, une règle CSS `#horseN` (top et sprite), `new Horse('horseN', 20, y)` dans `game.js`, une ligne de résultat et une option de pari. Les couloirs dépendent de `horse.number*2.5`.

## Publier en Artifact
La page publiée est générée à partir de ces fichiers. CSS et JS sont mis en ligne dans la page, et `images/` est envoyé via `files`. Les `alert()` y sont remplacés par un message `#msg` dans la page, parce que le viewer n'affiche pas `alert()`. Garder la mention de l'auteur et de la licence en pied de page.
