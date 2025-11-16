<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Prompt optimisé pour GitHub Copilot : Création d'un site MkDocs multilingue avec audio

Voici un prompt complet et structuré que vous pouvez utiliser avec GitHub Copilot pour reproduire correctement votre projet.[^1][^2][^3][^4][^5]

***

## 📋 PROMPT PRINCIPAL POUR COPILOT

```
## CONTEXTE DU PROJET

Je veux créer un site web de documentation statique avec MkDocs qui servira de dictionnaire 
multilingue de terminologie météorologique accessible en ligne. Le projet doit être développé 
dans VS Code avec un environnement virtuel Conda.

## DONNÉES SOURCE

J'ai un fichier PDF (DRAFT_LEXIQUE_METEO_VERSION-FINALE.pdf) contenant plus de 200 termes 
météorologiques avec :
- Terme en français
- Définition en français facile
- Traductions dans 7 langues locales de Côte d'Ivoire : Baoulé, Bété, Lobi, Malinké, 
  Sénoufo, Koulango, Yacouba

Exemple d'entrée du lexique :
- Terme : "Abri météo"
- Définition : "Petite cage blanche contenant des instruments météo"
- Baoulé : "blɛ amanniɛn sua"
- Bété : "ɔnun alaka"
- Lobi : "meteolinɛnιköbhänιde"
- Malinké : "bɔ́hín tʰɩ̰́ tʰɩ̀ɩ̀n pár"
- Sénoufo : "wagati ɟateminanso"
- Koulango : "Kpapilé nì be lǎli kama yabàra"
- Yacouba : "cɛ́ɛ lè tɛ́m ɡɷ̰ ́ɷ̰ ̀ mɩ̰́rɩ́ɡɔ̀ ɡbúkò"

## OBJECTIFS FONCTIONNELS

1. **Navigation intuitive** : 
   - Une page d'accueil avec présentation du projet
   - Une page dédiée pour chaque terme météorologique
   - Navigation entre les termes (précédent/suivant)
   - Barre de recherche fonctionnelle

2. **Audio interactif** : 
   - Chaque traduction doit avoir un bouton audio (icône 🔊)
   - Cliquer sur le bouton lit le mot dans la langue correspondante
   - Les fichiers audio doivent être générés automatiquement avec gTTS
   - Interface audio avec feedback visuel pendant la lecture

3. **Structure multilingue** :
   - Support de 8 langues (français + 7 langues locales)
   - Chaque page de terme affiche toutes les traductions
   - Format cohérent : titre, audio, image, définition, traductions

4. **Images** :
   - Chaque terme doit avoir une image illustrative
   - Images stockées dans docs/images/
   - Format : nom-du-terme.jpg (slug)

## EXIGENCES TECHNIQUES

### Stack technologique obligatoire :
- **Python** : 3.11
- **Gestionnaire d'environnement** : Conda (pas venv)
- **Générateur de site** : MkDocs
- **Thème** : Material for MkDocs
- **Génération audio** : gTTS (Google Text-to-Speech)
- **IDE** : VS Code
- **Contrôle de version** : Git + GitHub

### Structure du projet requise :
```

lexique-meteo-multilingue/
├── docs/
│   ├── index.md                 \# Page d'accueil
│   ├── termes/                  \# Pages des termes
│   │   ├── abri-meteo.md
│   │   ├── accalmie.md
│   │   └── ...
│   ├── audio/                   \# Fichiers audio générés
│   │   ├── abri-meteo_fr.mp3
│   │   ├── abri-meteo_baoule.mp3
│   │   └── ...
│   ├── images/                  \# Images des termes
│   │   ├── abri-meteo.jpg
│   │   └── ...
│   ├── javascripts/
│   │   └── audio-player.js      \# Logique des boutons audio
│   └── stylesheets/
│       └── extra.css            \# Styles personnalisés
├── mkdocs.yml                   \# Configuration MkDocs
├── environment.yml              \# Configuration Conda
├── generate_audio.py            \# Script génération audio
├── generate_pages.py            \# Script génération pages
├── .gitignore
└── README.md

```

## TÂCHES À ACCOMPLIR (ÉTAPE PAR ÉTAPE)

### ÉTAPE 1 : Configuration de l'environnement Conda
- Créer un environnement Conda nommé "lexique-meteo" avec Python 3.11
- Installer mkdocs, mkdocs-material via conda-forge
- Installer gtts, pydub via pip
- Créer le fichier environment.yml pour reproduire l'environnement
- Configurer VS Code pour utiliser l'interpréteur Python de cet environnement

### ÉTAPE 2 : Initialisation du dépôt Git/GitHub
- Initialiser un dépôt Git local
- Créer un fichier .gitignore adapté (ignorer audio/, site/, __pycache__, etc.)
- Créer un dépôt GitHub et connecter le dépôt local
- Faire le premier commit avec la structure de base

### ÉTAPE 3 : Configuration MkDocs
- Créer mkdocs.yml avec :
  - Thème Material for MkDocs
  - Configuration de navigation
  - Plugins de recherche
  - Extensions Markdown (attr_list, md_in_html, pymdownx.superfences)
  - Inclusion de fichiers CSS/JS personnalisés
  - Icône de logo météo
  - Palette de couleurs bleue

### ÉTAPE 4 : Script de génération audio (generate_audio.py)
- Créer une fonction slugify() pour convertir les termes en slugs (URL-safe)
- Lire les données du PDF ou d'une structure Python (liste de dictionnaires)
- Pour chaque terme et chaque langue :
  - Générer un fichier audio MP3 avec gTTS
  - Nommer le fichier : {slug}_{code_langue}.mp3
  - Sauvegarder dans docs/audio/
- Afficher une barre de progression ou des logs clairs
- Gestion des erreurs (connexion Internet requise pour gTTS)

### ÉTAPE 5 : Lecteur audio JavaScript (audio-player.js)
- Créer une fonction initAudioButtons() qui :
  - Sélectionne tous les boutons avec la classe "audio-btn"
  - Attache un écouteur d'événement click à chaque bouton
- Créer une fonction playAudio(src, button) qui :
  - Crée ou réutilise un élément <audio>
  - Charge le fichier audio spécifié
  - Lance la lecture
  - Change l'icône du bouton pendant la lecture (⏸️)
  - Restaure l'icône originale (🔊) après la lecture
  - Gère les erreurs de lecture
- Optimisation : arrêter tout audio en cours avant d'en jouer un nouveau

### ÉTAPE 6 : Styles CSS (extra.css)
- Créer des styles pour :
  - .audio-btn : bouton bleu arrondi avec transition hover
  - .translation-item : conteneur flex pour traduction + bouton
  - .translation-text : texte de la traduction
  - .language-label : étiquette de langue en gras et bleu
  - Animation de pulsation pendant la lecture audio
  - État désactivé pour les boutons pendant la lecture

### ÉTAPE 7 : Script de génération de pages (generate_pages.py)
- Créer une fonction create_audio_button(slug, lang, text) qui génère le HTML :
```

  <div class="translation-item">
      ```
      <span class="translation-text">{text}</span>
      ```
      ```
      <button class="audio-btn" data-audio="../audio/{slug}_{lang}.mp3">🔊</button>
      ```
  </div>
```
- Créer une fonction create_term_page(terme, index, total) qui :
- Génère le contenu Markdown complet d'une page
- Inclut : titre + audio, image, définition, toutes les traductions avec boutons audio
- Ajoute navigation précédent/suivant
- Sauvegarde le fichier dans docs/termes/{slug}.md
- Boucler sur tous les termes pour générer toutes les pages

### ÉTAPE 8 : Page d'accueil (docs/index.md)
- Créer une page d'accueil avec :
- Titre du projet
- Description du lexique (200+ termes, 8 langues)
- Instructions d'utilisation
- Liste des langues disponibles
- Crédits (SODEXAM - Côte d'Ivoire)

### ÉTAPE 9 : Test local
- Commande : `conda activate lexique-meteo && mkdocs serve`
- Vérifier que :
- Le site se charge à http://127.0.0.1:8000
- La navigation fonctionne
- Les boutons audio jouent correctement
- Les images s'affichent
- La recherche fonctionne
- Le design est responsive

### ÉTAPE 10 : Déploiement GitHub Pages
- Créer .github/workflows/ci.yml pour déploiement automatique avec :
- Configuration Conda
- Installation des dépendances depuis environment.yml
- Commande mkdocs gh-deploy --force
- Activer GitHub Pages dans les paramètres du dépôt (branche gh-pages)
- Vérifier le déploiement à https://[username].github.io/lexique-meteo-multilingue

## CONTRAINTES ET BONNES PRATIQUES

1. **Gestion des erreurs** :
 - Vérifier que les dossiers existent avant d'écrire des fichiers
 - Logger clairement les succès et échecs
 - Afficher des messages d'erreur explicites

2. **Performance** :
 - Générer tous les fichiers audio en une seule exécution
 - Optimiser la taille des images (max 500KB par image)
 - Utiliser des fichiers audio MP3 compressés

3. **Accessibilité** :
 - Attributs alt sur toutes les images
 - Attributs title sur les boutons audio
 - Contraste de couleurs suffisant (WCAG AA)

4. **Maintenance** :
 - Code commenté en français
 - Fonctions réutilisables et modulaires
 - Documentation dans le README.md

5. **Reproductibilité** :
 - environment.yml complet et fonctionnel
 - Instructions claires dans README.md
 - Commandes simples à exécuter

## FORMAT ATTENDU DES PAGES DE TERMES

Chaque page (exemple : docs/termes/abri-meteo.md) doit suivre ce format :

```


# Abri météo

<div class="translation-item">
    ```
    <span class="translation-text">Abri météo</span>
    ```
    ```
    <button class="audio-btn" data-audio="../audio/abri-meteo_fr.mp3" title="Écouter">🔊</button>
    ```
</div>

## Définition (Français facile)

Petite cage blanche contenant des instruments météo

## Traductions

### Baoulé

<div class="translation-item">
    ```
    <span class="translation-text">blɛ amanniɛn sua</span>
    ```
    ```
    <button class="audio-btn" data-audio="../audio/abri-meteo_baoule.mp3" title="Écouter">🔊</button>
    ```
</div>

### Bété

<div class="translation-item">
    ```
    <span class="translation-text">ɔnun alaka</span>
    ```
    ```
    <button class="audio-btn" data-audio="../audio/abri-meteo_bete.mp3" title="Écouter">🔊</button>
    ```
</div>
[... autres langues ...]

***

[◄ Retour à l'index](../index.md) | [Terme suivant: Accalmie ►](accalmie.md)

```

## COMMANDES ESSENTIELLES À DOCUMENTER

Dans le README.md, inclure ces commandes :

```


# Créer l'environnement

conda env create -f environment.yml

# Activer l'environnement

conda activate lexique-meteo

# Générer les fichiers audio (nécessite Internet)

python generate_audio.py

# Générer les pages MkDocs

python generate_pages.py

# Tester localement

mkdocs serve

# Construire le site statique

mkdocs build

# Déployer sur GitHub Pages

mkdocs gh-deploy

# Désactiver l'environnement

conda deactivate

```

## LIVRABLES ATTENDUS

1. ✅ Dépôt GitHub fonctionnel et organisé
2. ✅ Site MkDocs déployé et accessible en ligne
3. ✅ Plus de 1600 fichiers audio générés (200+ termes × 8 langues)
4. ✅ 200+ pages de termes avec navigation fluide
5. ✅ Boutons audio fonctionnels sur toutes les pages
6. ✅ Interface responsive et moderne
7. ✅ Documentation complète (README.md)
8. ✅ Code propre et commenté
9. ✅ Configuration Conda reproductible (environment.yml)
10. ✅ Workflow CI/CD pour déploiement automatique

## DÉFINITION DE "TERMINÉ"

Le projet est considéré comme terminé quand :
- [ ] L'environnement Conda se crée sans erreur avec environment.yml
- [ ] Le script generate_audio.py crée tous les fichiers MP3 dans docs/audio/
- [ ] Le script generate_pages.py crée toutes les pages Markdown dans docs/termes/
- [ ] `mkdocs serve` démarre le serveur local sans erreur
- [ ] Tous les boutons audio jouent correctement les prononciations
- [ ] Toutes les images s'affichent correctement
- [ ] La recherche MkDocs trouve les termes
- [ ] La navigation entre pages fonctionne (précédent/suivant)
- [ ] Le site est déployé et accessible via GitHub Pages
- [ ] Le README.md contient toutes les instructions nécessaires
- [ ] Le dépôt GitHub est public et bien organisé
- [ ] Les commits Git sont clairs et logiques

## PRIORITÉS

Ordre de priorité si vous devez faire des compromis :
1. **CRITIQUE** : Structure de base MkDocs fonctionnelle
2. **CRITIQUE** : Génération automatique des pages
3. **HAUTE** : Boutons audio avec lecture fonctionnelle
4. **HAUTE** : Navigation et recherche
5. **MOYENNE** : Génération automatique des fichiers audio
6. **MOYENNE** : Déploiement GitHub Pages
7. **BASSE** : Optimisations de performance
8. **BASSE** : Animations et transitions CSS avancées
```


***

## 📝 PROMPTS COMPLÉMENTAIRES POUR TÂCHES SPÉCIFIQUES

Si Copilot a besoin de plus de détails sur certaines parties, utilisez ces sous-prompts :[^3][^5][^6][^1]

### Pour la génération audio :

```
Crée un script Python (generate_audio.py) qui :
1. Importe gTTS pour générer les fichiers audio
2. Définit un dictionnaire de termes météorologiques avec leurs traductions
3. Pour chaque terme dans chaque langue :
   - Génère un fichier MP3 avec gTTS
   - Nomme le fichier selon le pattern : {slug}_{code_langue}.mp3
   - Sauvegarde dans docs/audio/
4. Affiche des logs de progression clairs
5. Gère les erreurs de connexion Internet
6. Retourne un compte total des fichiers générés

Exemple de structure de données :
termes = [
    {
        "terme_fr": "Abri météo",
        "traductions": {
            "baoule": "blɛ amanniɛn sua",
            "bete": "ɔnun alaka",
            ...
        }
    },
    ...
]
```


### Pour le lecteur audio JavaScript :

```
Crée un fichier JavaScript (docs/javascripts/audio-player.js) qui :
1. Attend que le DOM soit chargé
2. Sélectionne tous les boutons avec la classe "audio-btn"
3. Pour chaque bouton, attache un écouteur click qui :
   - Récupère l'attribut data-audio du bouton
   - Arrête tout audio en cours de lecture
   - Crée/réutilise un élément <audio>
   - Charge et joue le fichier audio
   - Change l'icône du bouton pendant la lecture (🔊 → ⏸️)
   - Restaure l'icône après la lecture
   - Gère les erreurs avec un message console
4. Utilise des fonctions modulaires et réutilisables
5. Ajoute des commentaires en français
```


### Pour les styles CSS :

```
Crée un fichier CSS (docs/stylesheets/extra.css) avec :
1. Styles pour .audio-btn :
   - Bouton inline-flex, bleu (#2196F3), arrondi (4px)
   - Padding 0.4rem 0.8rem, margin-left 0.5rem
   - Transitions smooth (0.3s ease)
   - Hover : couleur plus foncée (#1976D2) et scale(1.05)
   - Active : scale(0.95)
   - Disabled : gris (#BDBDBD), cursor not-allowed

2. Styles pour .translation-item :
   - Display flex, align-items center
   - Background #f5f5f5, border-radius 4px
   - Padding 0.5rem, margin 0.5rem 0

3. Animation de pulsation pour .audio-btn.playing :
   - Keyframes qui alternent opacity entre 1 et 0.5
   - Animation infinie de 1.5s

4. Styles responsive pour mobile
```


### Pour la configuration MkDocs :

```
Crée un fichier mkdocs.yml avec :
- site_name: "Lexique Météorologique Multilingue"
- theme: material avec :
  - language: fr
  - palette: primary blue, accent light blue
  - features: navigation.tabs, navigation.sections, navigation.top, search.suggest
  - icon.logo: material/weather-cloudy
- extra_javascript: javascripts/audio-player.js
- extra_css: stylesheets/extra.css
- markdown_extensions: attr_list, md_in_html, pymdownx.superfences
- plugins: search avec lang fr
- nav: structure avec page d'accueil et section termes
```


***

## 🎯 CONSEILS POUR UTILISER CE PROMPT AVEC COPILOT

### Stratégies d'interaction optimales :[^7][^5][^6][^1]

1. **Décomposition en tâches** :
    - Ne donnez pas tout le prompt d'un coup
    - Commencez par l'ÉTAPE 1 (environnement Conda)
    - Attendez que Copilot la complète avant de passer à l'ÉTAPE 2
    - Vérifiez chaque étape avant de continuer[^2][^6]
2. **Utilisation du contexte** :
    - Utilisez `@workspace` pour que Copilot analyse tout le projet[^4]
    - Utilisez `#file` pour référencer des fichiers spécifiques[^4]
    - Ouvrez les fichiers pertinents dans VS Code avant de poser des questions[^4]
3. **Itération et révision** :
    - Si le code généré n'est pas correct, dites "Révise le code pour..." au lieu de recommencer[^1][^3]
    - Utilisez "Améliore ce code en ajoutant..." pour ajouter des fonctionnalités[^3]
    - Demandez des revues de code : "Analyse ce code et suggère des améliorations"[^3]
4. **Exemples concrets** :
    - Copilot fonctionne mieux avec des exemples[^2][^1]
    - Le prompt inclut déjà des exemples de données et de format attendu
    - Référencez ces exemples : "Utilise le format montré dans l'exemple ci-dessus"[^1]
5. **Feedback et clarifications** :
    - Si Copilot ne comprend pas, reformulez plus simplement[^1]
    - Soyez explicite sur les technologies : "Utilise gTTS, pas pyttsx3"[^8]
    - Confirmez les étapes : "Est-ce que cette structure est correcte avant de continuer ?"[^6]

***

## 📊 CHECKLIST DE VALIDATION

Après chaque génération de code par Copilot, vérifiez :[^5][^1]

- [ ] Le code respecte les exigences techniques spécifiées
- [ ] Les noms de fichiers et dossiers correspondent à la structure définie
- [ ] Les commentaires sont en français
- [ ] Le code gère les erreurs potentielles
- [ ] Les imports sont corrects et disponibles dans environment.yml
- [ ] Le style de code est cohérent
- [ ] Les fonctions ont des noms descriptifs
- [ ] Le code est testable localement avec `mkdocs serve`

***

Ce prompt structuré suivant les meilleures pratiques d'ingénierie de prompt devrait permettre à GitHub Copilot de comprendre précisément ce qu'il faut faire et de générer un code de haute qualité qui répond exactement à vos besoins. La clé est de décomposer le projet en tâches séquentielles claires et de fournir des exemples concrets à chaque étape.[^9][^7][^5][^6][^2][^3][^4][^1]
<span style="display:none">[^10]</span>

<div align="center">⁂</div>

[^1]: https://docs.github.com/en/copilot/get-started/best-practices

[^2]: https://arxiv.org/html/2506.01604v1

[^3]: https://margabagus.com/prompt-engineering-code-generation-practices/

[^4]: https://docs.github.com/copilot/get-started/getting-started-with-prompts-for-copilot-chat

[^5]: https://prompt.16x.engineer/blog/effective-ai-coding-tips

[^6]: https://github.blog/ai-and-ml/github-copilot/5-tips-and-tricks-when-using-github-copilot-workspace/

[^7]: https://nx.dev/blog/practical-guide-effective-ai-coding

[^8]: https://zencoder.ai/blog/how-to-use-ai-in-coding

[^9]: https://www.linkedin.com/pulse/mastering-prompt-engineering-reliable-ai-code-generation-xtlbf

[^10]: https://dev.to/pwd9000/supercharge-vscode-github-copilot-using-instructions-and-prompt-files-2p5e

