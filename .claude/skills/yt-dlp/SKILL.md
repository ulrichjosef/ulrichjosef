---
name: yt-dlp
description: Télécharger des vidéos, de l'audio, des sous-titres ou des métadonnées depuis YouTube et des milliers d'autres sites avec l'outil en ligne de commande yt-dlp. À utiliser quand l'utilisateur veut télécharger une vidéo ou une playlist, extraire l'audio en MP3/M4A, récupérer des sous-titres ou une transcription, lister les formats disponibles, couper un extrait, ou obtenir les infos d'une vidéo (titre, durée, chaîne) à partir d'une URL.
---

# yt-dlp

Outil CLI de téléchargement de médias (fork maintenu de youtube-dl). Fonctionne avec YouTube, Vimeo, TikTok, X/Twitter, Instagram, SoundCloud, Twitch, Dailymotion, etc. (`yt-dlp --list-extractors` pour la liste complète).

## 1. Vérifier l'installation

```bash
yt-dlp --version && ffmpeg -version | head -1
```

- Absent → `pip install -U "yt-dlp[default]"` (ou `pipx install yt-dlp`, `brew install yt-dlp`, `winget install yt-dlp`).
- **ffmpeg est requis** pour fusionner vidéo+audio, extraire l'audio, intégrer sous-titres/miniatures. Sans lui, signaler la limite à l'utilisateur.
- YouTube : un runtime JavaScript (deno recommandé, ou node avec `--js-runtimes node`) évite les formats manquants / erreurs de signature.
- En cas d'erreur sur un site, **mettre à jour d'abord** : `yt-dlp -U` (binaire) ou `pip install -U yt-dlp`. Les sites changent souvent.

## 2. Toujours inspecter avant de télécharger

```bash
yt-dlp --print "%(title)s | %(uploader)s | %(duration_string)s | %(upload_date)s" "URL"   # infos rapides
yt-dlp -F "URL"           # formats disponibles
yt-dlp --list-subs "URL"  # sous-titres disponibles
yt-dlp -J "URL" > info.json   # toutes les métadonnées en JSON, sans télécharger
```

Pour une playlist ou une chaîne, compter d'abord : `yt-dlp --flat-playlist --print "%(title)s" "URL" | wc -l`, et prévenir l'utilisateur si c'est volumineux.

## 3. Recettes courantes

Toujours mettre l'URL **entre guillemets** (les `&` cassent le shell).

| Besoin | Commande |
|---|---|
| Vidéo meilleure qualité | `yt-dlp "URL"` |
| MP4 compatible partout (H.264/AAC) | `yt-dlp -S "res,ext:mp4:m4a" --merge-output-format mp4 "URL"` |
| Limiter à 1080p | `yt-dlp -S "res:1080" "URL"` |
| Audio MP3 | `yt-dlp -x --audio-format mp3 --audio-quality 0 "URL"` |
| Audio sans réencodage (meilleur) | `yt-dlp -f "ba" -x "URL"` |
| Audio avec pochette + tags | `yt-dlp -x --audio-format mp3 --embed-thumbnail --embed-metadata "URL"` |
| Sous-titres FR seuls | `yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "fr.*" --convert-subs srt "URL"` |
| Vidéo + sous-titres intégrés | `yt-dlp --embed-subs --sub-langs "fr,en" "URL"` |
| Extrait (1:00 → 2:30) | `yt-dlp --download-sections "*1:00-2:30" --force-keyframes-at-cuts "URL"` |
| Découper par chapitres | `yt-dlp --split-chapters "URL"` |
| Playlist entière, numérotée | `yt-dlp -o "%(playlist)s/%(playlist_index)03d - %(title)s.%(ext)s" "URL_PLAYLIST"` |
| Éléments 1 à 5 d'une playlist | `yt-dlp -I 1:5 "URL_PLAYLIST"` |
| Seulement la vidéo, pas la playlist | `yt-dlp --no-playlist "URL"` |
| Ne pas retélécharger (archive) | `yt-dlp --download-archive archive.txt "URL_CHAINE"` |
| Liste d'URL dans un fichier | `yt-dlp -a urls.txt` |
| Miniature seule | `yt-dlp --skip-download --write-thumbnail --convert-thumbnails jpg "URL"` |
| Retirer sponsors (YouTube) | `yt-dlp --sponsorblock-remove sponsor "URL"` |
| Limiter le débit | `yt-dlp -r 2M "URL"` |

## 4. Nom et dossier de sortie

`-o` accepte un modèle : `yt-dlp -o "~/Videos/%(uploader)s/%(title)s [%(id)s].%(ext)s" "URL"`.
Champs utiles : `title`, `id`, `uploader`, `channel`, `upload_date`, `playlist`, `playlist_index`, `ext`, `resolution`. Ajouter `--restrict-filenames` pour des noms sans espaces ni accents. `-P DOSSIER` fixe le dossier de destination.

Après le téléchargement, indiquer à l'utilisateur le **chemin exact** du fichier produit (utiliser `--print after_move:filepath` pour l'obtenir de façon fiable).

## 5. Contenu protégé par connexion / âge / région

- Contenu privé, réservé aux membres ou limité par l'âge : `--cookies-from-browser firefox` (ou `chrome`, `edge`, `safari`), ou `--cookies cookies.txt` (format Netscape).
- Ne jamais demander à l'utilisateur son mot de passe dans le chat ; préférer les cookies du navigateur sur sa propre machine.
- Erreur 403 / "Sign in to confirm you're not a bot" : mettre à jour yt-dlp, essayer les cookies, puis `--impersonate chrome` (nécessite `curl_cffi`).

## 6. Dépannage rapide

| Symptôme | Action |
|---|---|
| `Unsupported URL` / extracteur cassé | `yt-dlp -U`, puis réessayer ; sinon `--use-extractors generic` |
| Vidéo et audio en fichiers séparés | ffmpeg manquant → l'installer |
| `Requested format is not available` | lancer `-F`, choisir un format existant ou utiliser `-S` au lieu de `-f` |
| Formats YouTube manquants / erreur nsig | installer deno ou `--js-runtimes node` ; mettre à jour |
| HTTP 429 (trop de requêtes) | `--sleep-requests 1 --sleep-interval 5 --max-sleep-interval 15` |
| Diagnostic détaillé | ajouter `-v` et lire la sortie |

## 7. Règles d'usage

- Télécharger uniquement du contenu que l'utilisateur a le droit de récupérer (le sien, libre de droits, usage personnel autorisé). Ne pas aider à contourner des DRM : yt-dlp ne le fait pas et il ne faut pas chercher d'autre outil pour ça.
- Pour un gros lot (chaîne entière, centaines de vidéos), confirmer avec l'utilisateur avant de lancer, et proposer `--download-archive`.
- Dans un environnement cloud au réseau restreint, le site cible peut être bloqué par le proxy : le dire clairement plutôt que de contourner.
- Documentation complète : `yt-dlp --help` ou le README du projet (sections OUTPUT TEMPLATE et FORMAT SELECTION).
