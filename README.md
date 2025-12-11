# 🌍 Lexique Météorologique Multilingue - Côte d'Ivoire

<div align="center">
  <h2>Dictionnaire de terminologie météorologique en 8 langues</h2>
  <p><strong>Développé par la SODEXAM - Côte d'Ivoire 🇨🇮</strong></p>
  
  ![Version](https://img.shields.io/badge/version-1.0-blue.svg)
  ![MkDocs](https://img.shields.io/badge/MkDocs-1.5.3+-green.svg)
  ![Material](https://img.shields.io/badge/Material-9.0+-orange.svg)
  ![License](https://img.shields.io/badge/license-MIT-blue.svg)
  ![Status](https://img.shields.io/badge/status-active-success.svg)
</div>

---

## 📖 À propos

Ce projet est un **lexique météorologique multilingue interactif** développé par la **SODEXAM** (Société d'Exploitation et de Développement Aéroportuaire, Aéronautique et Météorologique) de Côte d'Ivoire en partenariat avec le **PNUE** et l'**Union Européenne**.

Le lexique contient **651 termes météorologiques** traduits dans **8 langues** (français + 7 langues locales ivoiriennes) avec des **prononciations audio interactives** et des **définitions complètes**.

🔗 **Site web** : [À définir lors du déploiement]
📦 **Repository** : [https://github.com/NicaiseKassi/lexique-meteo-multilingue-ci](https://github.com/NicaiseKassi/lexique-meteo-multilingue-ci)

### 🌍 Langues supportées

- **🇫🇷 Français** - Langue officielle et définitions
- **🌍 Baoulé** - Langue Akan du centre
- **🌍 Bété** - Langue Kru de l'ouest
- **🌍 Lobi** - Langue Gur du nord-est
- **🌍 Malinké** - Langue Mandé du nord-ouest
- **🌍 Sénoufo** - Langue Gur du nord
- **🌍 Koulango** - Langue Gur de l'est
- **🌍 Yacouba** - Langue Mandé de l'ouest

## ✨ Fonctionnalités

- 🔊 **Audio interactif** - Prononciation de chaque terme dans toutes les langues
- 📱 **Design responsive** - Optimisé pour mobile, tablette et desktop
- 🔍 **Recherche avancée** - Recherche rapide dans tous les termes et langues
- 🧭 **Navigation intuitive** - Organisation alphabétique et liens de navigation
- 🎨 **Interface moderne** - Basée sur Material Design
- ♿ **Accessible** - Conforme aux standards d'accessibilité web
- 📚 **Documentation complète** - Définitions claires en français facile

## 🚀 Installation et utilisation

### Prérequis

- **Python 3.11+**
- **Conda** (recommandé) ou pip
- **Connexion Internet** (pour la génération audio avec gTTS)

### Installation rapide

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-username/lexique-meteo-multilingue.git
cd lexique-meteo-multilingue

# 2. Créer l'environnement Conda
conda env create -f environment.yml

# 3. Activer l'environnement
conda activate lexique-meteo

# 4. Générer les fichiers audio (nécessite Internet)
python generate_audio.py

# 5. Générer les pages (déjà fait, optionnel)
python generate_pages.py

# 6. Lancer le serveur local
mkdocs serve
```

Le site sera accessible à l'adresse : **http://127.0.0.1:8000**

### Installation alternative (avec pip)

```bash
# 1. Cloner et entrer dans le dépôt
git clone https://github.com/votre-username/lexique-meteo-multilingue.git
cd lexique-meteo-multilingue

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# 3. Installer les dépendances
pip install mkdocs mkdocs-material gtts pydub

# 4. Suite identique...
```

## 📁 Structure du projet

```
lexique-meteo-multilingue/
├── 📄 README.md                    # Ce fichier
├── 📄 mkdocs.yml                   # Configuration MkDocs
├── 📄 environment.yml              # Environnement Conda
├── 🐍 generate_audio.py            # Script génération audio
├── 🐍 generate_pages.py            # Script génération pages
├── 📁 docs/                        # Documentation source
│   ├── 📄 index.md                 # Page d'accueil
│   ├── 📁 termes/                  # Pages des termes
│   │   ├── abri-meteo.md
│   │   ├── accalmie.md
│   │   └── ...
│   ├── 📁 audio/                   # Fichiers audio MP3
│   │   ├── abri-meteo_fr.mp3
│   │   ├── abri-meteo_baoule.mp3
│   │   └── ...
│   ├── 📁 images/                  # Images des termes
│   │   ├── abri-meteo.jpg
│   │   └── ...
│   ├── 📁 javascripts/
│   │   └── audio-player.js         # Lecteur audio interactif
│   └── 📁 stylesheets/
│       └── extra.css               # Styles personnalisés
└── 📁 site/                        # Site généré (après build)
```

## 🛠️ Commandes utiles

### Développement

```bash
# Servir le site en mode développement (rechargement automatique)
mkdocs serve

# Construire le site statique
mkdocs build

# Nettoyer et reconstruire
mkdocs build --clean
```

### Génération de contenu

```bash
# Régénérer tous les fichiers audio
python generate_audio.py

# Régénérer toutes les pages
python generate_pages.py

# Vérifier la syntaxe Python
python -m py_compile generate_audio.py generate_pages.py
```

### Tests et validation

```bash
# Vérifier les liens internes
mkdocs build --strict

# Tester la configuration
python -c "import yaml; yaml.safe_load(open('mkdocs.yml'))"

# Lister les environnements Conda
conda env list
```

## 📈 Personnalisation

### Ajouter de nouveaux termes

1. **Modifier `generate_audio.py`** - Ajouter le terme dans `TERMES_METEO`
2. **Régénérer** - Lancer `python generate_pages.py`
3. **Ajouter l'image** - Placer `nouveau-terme.jpg` dans `docs/images/`
4. **Tester** - Vérifier avec `mkdocs serve`

### Modifier les styles

- **CSS personnalisé** : Éditer `docs/stylesheets/extra.css`
- **Couleurs** : Modifier les variables CSS dans `:root`
- **Responsive** : Adapter les `@media queries`

### Configuration avancée

- **MkDocs** : Éditer `mkdocs.yml`
- **Navigation** : Auto-générée par `generate_pages.py`
- **Plugins** : Ajouter dans la section `plugins:` de `mkdocs.yml`

## 🌐 Déploiement

### GitHub Pages (Gratuit)

```bash
# Déploiement automatique
mkdocs gh-deploy

# Ou utiliser le workflow GitHub Actions (voir .github/workflows/ci.yml)
```

### Autres plateformes

- **Netlify** : Connecter le dépôt GitHub
- **Vercel** : Déploiement automatique
- **Read the Docs** : Pour documentation publique

## 🤝 Contribution

Nous accueillons les contributions ! Voici comment participer :

### Types de contributions

- 🐛 **Signaler des bugs** - Issues GitHub
- ✨ **Proposer des améliorations** - Feature requests
- 🌍 **Ajouter des langues** - Nouvelles traductions
- 📝 **Améliorer la documentation** - Corrections et ajouts
- 🔊 **Améliorer l'audio** - Qualité des prononciations

### Processus de contribution

1. **Fork** le dépôt
2. **Créer une branche** : `git checkout -b ma-fonctionnalite`
3. **Développer** et tester les modifications
4. **Commiter** : `git commit -m "Description claire"`
5. **Pousser** : `git push origin ma-fonctionnalite`
6. **Pull Request** avec description détaillée

### Guidelines

- **Code** : Respecter PEP 8 pour Python
- **Commits** : Messages clairs en français ou anglais
- **Tests** : Tester avec `mkdocs serve` avant PR
- **Documentation** : Mettre à jour le README si nécessaire

## 📞 Support et contact

### 🆘 Obtenir de l'aide

- **Issues GitHub** : Pour bugs et questions techniques
- **Discussions** : Pour questions générales et suggestions
- **Email SODEXAM** : contact@sodexam.ci

### 📧 Contacts professionnels

- **SODEXAM** : Société d'Exploitation et de Développement Aéroportuaire, Aéronautique et Météorologique
- **Adresse** : Abidjan, Côte d'Ivoire
- **Website** : [www.sodexam.ci](http://www.sodexam.ci)

## 📊 Statistiques du projet

| Métrique | Valeur |
|----------|--------|
| **Termes traduits** | 200+ |
| **Langues** | 8 |
| **Fichiers audio** | 1600+ |
| **Locuteurs touchés** | 15M+ |
| **Pages générées** | 200+ |
| **Technologies** | Python, MkDocs, gTTS |

## 🏆 Reconnaissance

### 🙏 Remerciements

- **Équipe SODEXAM** - Experts agro-météorologues et climatologues
- **Linguistes ivoiriens** - Validation des traductions
- **Communautés locales** - Contribution linguistique
- **PNUE** - Soutien institutionnel
- **Union Européenne** - Financement

## 📄 Licence et propriété intellectuelle

<div align="center">

**© SODEXAM - Tous droits réservés**

</div>

Ce projet est la **propriété exclusive de la SODEXAM** (Société d'Exploitation et de Développement Aéroportuaire, Aéronautique et Météorologique).

**Restrictions d'utilisation** :
- 🚫 **Pas de duplication** - Reproduction interdite sans autorisation
- 🚫 **Usage non commercial uniquement** - Toute utilisation commerciale est strictement interdite
- 📝 **Attribution obligatoire** - Toute utilisation autorisée doit créditer la SODEXAM
- ⚖️ **Tous droits réservés** - Toute utilisation nécessite l'autorisation écrite de la SODEXAM

**Pour toute demande d'utilisation** : contact@sodexam.ci

---

<div align="center">
  <h3>🌍 Fait avec ❤️ en Côte d'Ivoire</h3>
  <p>
    <strong>SODEXAM</strong> | <strong>PNUE</strong> | <strong>Union Européenne</strong>
  </p>
  <p>
    <em>Pour un accès équitable aux informations météorologiques</em>
  </p>
</div>