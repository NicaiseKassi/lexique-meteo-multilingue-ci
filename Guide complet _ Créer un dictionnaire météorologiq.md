<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Guide complet : Créer un dictionnaire météorologique multilingue avec MkDocs

Ce guide vous accompagne pas à pas pour créer un site web de documentation MkDocs accessible en ligne, structuré comme un dictionnaire de terminologie météorologique dans plusieurs langues, à partir du lexique joint. Chaque terme disposera de sa propre page avec une image et des traductions dans toutes les langues disponibles.

## Vue d'ensemble du projet

D'après le document PDF analysé, votre lexique météorologique contient des termes en :[^1_1]

- **Français facile** (langue source et définitions)
- **Baoulé**
- **Bété**
- **Lobi**
- **Malinké**
- **Sénoufo**
- **Koulango**
- **Yacouba**

Le document comprend plus de 200 termes météorologiques avec leurs définitions et traductions.[^1_1]

## Étape 1 : Préparer l'environnement de développement dans VS Code

### 1.1 Créer le dossier du projet

Ouvrez VS Code et créez un nouveau dossier pour votre projet :

- Allez dans **File → Open Folder**
- Créez un nouveau dossier nommé `lexique-meteo-multilingue`
- Sélectionnez ce dossier[^1_2]


### 1.2 Créer un environnement virtuel Python

Ouvrez le terminal intégré dans VS Code (**Terminal → New Terminal** ou `Ctrl + \``) et exécutez:[^1_3][^1_2]

```bash
python -m venv venv
```

Cette commande crée un environnement virtuel isolé dans le dossier `venv` de votre projet.[^1_3]

### 1.3 Activer l'environnement virtuel

**Sous Windows** :

```bash
venv\Scripts\activate
```

**Sous macOS/Linux** :

```bash
source venv/bin/activate
```

Vous verrez `(venv)` apparaître dans votre terminal, indiquant que l'environnement virtuel est activé.[^1_2][^1_3]

### 1.4 Installer MkDocs et le thème Material

Une fois l'environnement virtuel activé, installez MkDocs et le thème Material:[^1_4][^1_5][^1_6]

```bash
pip install mkdocs
pip install mkdocs-material
```

Vérifiez l'installation :

```bash
mkdocs --version
```


## Étape 2 : Créer le dépôt GitHub depuis VS Code

### 2.1 Initialiser Git localement

Dans VS Code, cliquez sur l'icône **Source Control** (Git) dans la barre latérale gauche, puis sur **Initialize Repository**.[^1_7][^1_8]

Alternativement, utilisez le terminal :

```bash
git init
```


### 2.2 Publier sur GitHub

Appuyez sur `Ctrl+Shift+P` pour ouvrir la palette de commandes, puis tapez **"Publish to GitHub"**.[^1_9][^1_8][^1_7]

VS Code vous demandera :

- Le nom du dépôt (par défaut : le nom du dossier)
- Si vous souhaitez un dépôt **privé** ou **public**
- Les fichiers à inclure dans le premier commit[^1_7][^1_9]

VS Code créera automatiquement le dépôt GitHub, configurera l'origine distante et effectuera le premier push.[^1_7]

## Étape 3 : Structurer le projet MkDocs multilingue

### 3.1 Créer la structure de base

Créez la structure de dossiers suivante:[^1_10][^1_11]

```
lexique-meteo-multilingue/
├── docs/
│   ├── fr/              # Français
│   │   ├── index.md
│   │   └── termes/
│   ├── baoulé/
│   │   ├── index.md
│   │   └── termes/
│   ├── bété/
│   │   ├── index.md
│   │   └── termes/
│   ├── lobi/
│   │   ├── index.md
│   │   └── termes/
│   ├── malinké/
│   │   ├── index.md
│   │   └── termes/
│   ├── sénoufo/
│   │   ├── index.md
│   │   └── termes/
│   ├── koulango/
│   │   ├── index.md
│   │   └── termes/
│   ├── yacouba/
│   │   ├── index.md
│   │   └── termes/
│   └── images/          # Images pour tous les termes
├── mkdocs.yml           # Configuration principale (français)
├── mkdocs.baoulé.yml
├── mkdocs.bété.yml
├── mkdocs.lobi.yml
├── mkdocs.malinké.yml
├── mkdocs.sénoufo.yml
├── mkdocs.koulango.yml
├── mkdocs.yacouba.yml
└── venv/
```


### 3.2 Créer le fichier de configuration principal (mkdocs.yml)

Créez le fichier `mkdocs.yml` à la racine du projet:[^1_12][^1_10]

```yaml
site_name: Lexique Météorologique Multilingue
site_description: Dictionnaire de terminologie météorologique en 8 langues
site_author: Votre Nom

theme:
  name: material
  language: fr
  palette:
    primary: blue
    accent: light blue
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - search.suggest
    - search.highlight
  icon:
    logo: material/weather-cloudy

docs_dir: docs/fr

extra:
  alternate:
    - name: Français
      link: /
      lang: fr
    - name: Baoulé
      link: /baoulé/
      lang: baoulé
    - name: Bété
      link: /bété/
      lang: bété
    - name: Lobi
      link: /lobi/
      lang: lobi
    - name: Malinké
      link: /malinké/
      lang: malinké
    - name: Sénoufo
      link: /sénoufo/
      lang: sénoufo
    - name: Koulango
      link: /koulango/
      lang: koulango
    - name: Yacouba
      link: /yacouba/
      lang: yacouba

exclude_docs: |
  baoulé/
  bété/
  lobi/
  malinké/
  sénoufo/
  koulango/
  yacouba/

nav:
  - Accueil: index.md
  - Termes météorologiques:
    - Abri météo: termes/abri-meteo.md
    - Accalmie: termes/accalmie.md
    # Ajoutez tous les autres termes ici

plugins:
  - search:
      lang: fr

markdown_extensions:
  - attr_list
  - md_in_html
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```


### 3.3 Créer les configurations pour les autres langues

Pour chaque langue, créez un fichier de configuration similaire. Par exemple, `mkdocs.baoulé.yml`:[^1_11][^1_10]

```yaml
site_name: Lexique Météorologique - Baoulé
site_description: Dictionnaire de terminologie météorologique en Baoulé
site_author: Votre Nom

theme:
  name: material
  language: fr  # Gardez 'fr' pour l'interface Material
  palette:
    primary: blue
    accent: light blue
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - search.suggest
    - search.highlight
  icon:
    logo: material/weather-cloudy

docs_dir: docs/baoulé

extra:
  alternate:
    - name: Français
      link: /
      lang: fr
    - name: Baoulé
      link: /baoulé/
      lang: baoulé
    # Répétez pour toutes les langues

nav:
  - Accueil: index.md
  - Termes météorologiques:
    - Abri météo: termes/abri-meteo.md
    # Ajoutez tous les termes

plugins:
  - search

markdown_extensions:
  - attr_list
  - md_in_html
  - admonition
  - pymdownx.details
  - pymdownx.superfences
```

Répétez ce processus pour toutes les autres langues.[^1_10][^1_11]

## Étape 4 : Créer les pages de contenu

### 4.1 Page d'accueil (index.md)

Créez `docs/fr/index.md` :

```markdown
# Lexique Météorologique Multilingue

Bienvenue dans le lexique météorologique multilingue de la Côte d'Ivoire.

## À propos

Ce lexique contient plus de 200 termes météorologiques traduits en 8 langues :

- Français facile
- Baoulé
- Bété
- Lobi
- Malinké
- Sénoufo
- Koulango
- Yacouba

## Comment utiliser ce lexique

Naviguez dans les différentes sections pour trouver les termes météorologiques et leurs traductions. Chaque terme dispose :

- D'une définition en français facile
- De traductions dans les 7 langues locales
- D'une image illustrative

## Navigation

Utilisez le menu de navigation pour explorer les termes par ordre alphabétique, ou utilisez la barre de recherche pour trouver un terme spécifique.

---

*Développé par la Société d'Exploitation et de Développement Aéroportuaire, Aéronautique et Météorologique (SODEXAM) - Côte d'Ivoire*
```


### 4.2 Créer une page de terme exemple

Créez `docs/fr/termes/abri-meteo.md` :[^1_1]

```markdown
# Abri météo

![Abri météo](../../images/abri-meteo.jpg)

## Définition (Français facile)

Petite cage blanche contenant des instruments météo.

## Traductions

### Baoulé
**blɛ amanniɛn sua** / **blɛ amanniɛn tangannin** / **sitivɛnis**

### Bété
**ɔnun alaka** / **akpa**

### Lobi
**meteolinɛnιköbhänιde**

### Malinké
**bɔ́hín tʰɩ̰́ tʰɩ̀ɩ̀n pár**

### Sénoufo
**wagati ɟateminanso**

### Koulango
**Kpapilé nì be lǎli kama yabàra**

### Yacouba
**cɛ́ɛ lè tɛ́m ɡɷ̰ ́ɷ̰ ̀ mɩ̰́rɩ́ɡɔ̀ ɡbúkò**

---

[◄ Retour à l'index](../index.md) | [Terme suivant: Accalmie ►](accalmie.md)
```


### 4.3 Script Python pour générer automatiquement les pages

Créez un script `generate_pages.py` pour automatiser la création de toutes les pages à partir du PDF :

```python
import os
import re

# Données extraites du PDF (exemple simplifié)
termes = [
    {
        "terme_fr": "Abri météo",
        "definition_fr": "Petite cage blanche contenant des instruments météo",
        "baoule": "blɛ amanniɛn sua / blɛ amanniɛn tangannin / sitivɛnis",
        "bete": "ɔnun alaka / akpa",
        "lobi": "meteolinɛnιköbhänιde",
        "malinke": "bɔ́hín tʰɩ̰́ tʰɩ̀ɩ̀n pár",
        "senoufo": "wagati ɟateminanso",
        "koulango": "Kpapilé nì be lǎli kama yabàra",
        "yacouba": "cɛ́ɛ lè tɛ́m ɡɷ̰ ́ɷ̰ ̀ mɩ̰́rɩ́ɡɔ̀ ɡbúkò"
    },
    # Ajoutez tous les autres termes ici...
]

def slugify(text):
    """Convertit un texte en slug pour les URLs"""
    text = text.lower()
    text = re.sub(r'[àâä]', 'a', text)
    text = re.sub(r'[éèêë]', 'e', text)
    text = re.sub(r'[îï]', 'i', text)
    text = re.sub(r'[ôö]', 'o', text)
    text = re.sub(r'[ùûü]', 'u', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def create_term_page(terme, index, total):
    """Crée une page Markdown pour un terme"""
    slug = slugify(terme["terme_fr"])
    
    # Déterminer les liens précédent/suivant
    prev_link = ""
    next_link = ""
    if index > 0:
        prev_slug = slugify(termes[index-1]["terme_fr"])
        prev_link = f"[◄ {termes[index-1]['terme_fr']}]({prev_slug}.md)"
    if index < total - 1:
        next_slug = slugify(termes[index+1]["terme_fr"])
        next_link = f"[{termes[index+1]['terme_fr']} ►]({next_slug}.md)"
    
    # Contenu de la page
    content = f"""# {terme["terme_fr"]}

![{terme["terme_fr"]}](../../images/{slug}.jpg)

## Définition (Français facile)

{terme["definition_fr"]}

## Traductions

### Baoulé
**{terme["baoule"]}**

### Bété
**{terme["bete"]}**

### Lobi
**{terme["lobi"]}**

### Malinké
**{terme["malinke"]}**

### Sénoufo
**{terme["senoufo"]}**

### Koulango
**{terme["koulango"]}**

### Yacouba
**{terme["yacouba"]}**

---

[◄ Retour à l'index](../index.md) | {prev_link} | {next_link}
"""
    
    # Créer le fichier pour chaque langue
    languages = ["fr", "baoulé", "bété", "lobi", "malinké", "sénoufo", "koulango", "yacouba"]
    
    for lang in languages:
        dir_path = f"docs/{lang}/termes"
        os.makedirs(dir_path, exist_ok=True)
        
        file_path = f"{dir_path}/{slug}.md"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"✓ Page créée pour : {terme['terme_fr']}")

# Générer toutes les pages
for i, terme in enumerate(termes):
    create_term_page(terme, i, len(termes))

print(f"\n✓ {len(termes)} pages créées avec succès!")
```

Exécutez le script :

```bash
python generate_pages.py
```


## Étape 5 : Ajouter des images

### 5.1 Créer le dossier images

Créez le dossier `docs/images/` et ajoutez les images pour chaque terme météorologique.

### 5.2 Nommer les images

Les images doivent être nommées selon le même slug que les pages, par exemple :

- `abri-meteo.jpg`
- `accalmie.jpg`
- `adaptation.jpg`

Vous pouvez trouver des images météorologiques sur des sites comme :

- Unsplash (images libres de droits)
- Wikimedia Commons
- Créer vos propres illustrations


## Étape 6 : Tester localement

### 6.1 Construire et servir le site

Pour la version française:[^1_5]

```bash
mkdocs serve
```

Pour une autre langue:[^1_10]

```bash
mkdocs serve -f mkdocs.baoulé.yml
```

Ouvrez votre navigateur à l'adresse `http://127.0.0.1:8000` pour voir le site.[^1_5]

### 6.2 Construire le site statique

Pour générer les fichiers HTML statiques:[^1_4][^1_5]

```bash
mkdocs build
mkdocs build -f mkdocs.baoulé.yml -d site/baoulé
mkdocs build -f mkdocs.bété.yml -d site/bété
mkdocs build -f mkdocs.lobi.yml -d site/lobi
mkdocs build -f mkdocs.malinké.yml -d site/malinké
mkdocs build -f mkdocs.sénoufo.yml -d site/sénoufo
mkdocs build -f mkdocs.koulango.yml -d site/koulango
mkdocs build -f mkdocs.yacouba.yml -d site/yacouba
```


## Étape 7 : Déployer en ligne

### 7.1 Option 1 : GitHub Pages (gratuit)

Ajoutez un fichier `.github/workflows/ci.yml` pour le déploiement automatique :

```yaml
name: Déploiement MkDocs
on:
  push:
    branches:
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Configuration Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.x
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV
      - uses: actions/cache@v3
        with:
          key: mkdocs-material-${{ env.cache_id }}
          path: .cache
          restore-keys: |
            mkdocs-material-
      - run: pip install mkdocs-material
      - run: mkdocs gh-deploy --force
```

Activez GitHub Pages dans les paramètres du dépôt : **Settings → Pages → Source : gh-pages**.[^1_4]

### 7.2 Option 2 : Read the Docs (gratuit)

1. Créez un compte sur [readthedocs.org](https://readthedocs.org)[^1_10]
2. Importez votre dépôt GitHub[^1_10]
3. Créez un fichier `.readthedocs.yaml` à la racine :
```yaml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.11"

mkdocs:
  configuration: mkdocs.yml

python:
  install:
    - requirements: requirements.txt
```

4. Créez `requirements.txt` :
```
mkdocs-material>=9.0.0
```


### 7.3 Option 3 : Netlify (gratuit)

1. Créez un compte sur [netlify.com](https://netlify.com)
2. Connectez votre dépôt GitHub
3. Configuration de build :
    - **Build command** : `mkdocs build`
    - **Publish directory** : `site`

## Étape 8 : Mettre à jour et maintenir

### 8.1 Workflow Git dans VS Code

Pour ajouter des modifications:[^1_8][^1_9]

1. Modifiez vos fichiers
2. Cliquez sur l'icône **Source Control**
3. Cochez les fichiers à commiter
4. Ajoutez un message de commit
5. Cliquez sur **Commit**
6. Cliquez sur **Sync Changes** pour pousser vers GitHub

Ou via le terminal :

```bash
git add .
git commit -m "Ajout de nouveaux termes"
git push
```


### 8.2 Ajouter de nouveaux termes

1. Ajoutez le terme dans le script `generate_pages.py`
2. Exécutez le script : `python generate_pages.py`
3. Ajoutez l'image correspondante dans `docs/images/`
4. Testez localement : `mkdocs serve`
5. Commitez et poussez les changements

## Fonctionnalités avancées

### Navigation par catégories

Vous pouvez organiser les termes par catégories dans `mkdocs.yml` :

```yaml
nav:
  - Accueil: index.md
  - Instruments:
    - Abri météo: termes/abri-meteo.md
    - Anémomètre: termes/anemometre.md
    - Baromètre: termes/barometre.md
  - Phénomènes:
    - Accalmie: termes/accalmie.md
    - Cyclone: termes/cyclone.md
    - Tempête: termes/tempete.md
  - Climat:
    - Adaptation: termes/adaptation.md
    - Changement climatique: termes/changement-climatique.md
```


### Recherche multilingue

Pour améliorer la recherche, installez le plugin de recherche multilingue:[^1_12]

```bash
pip install mkdocs-material[search]
```


### Glossaire interactif

Vous pouvez ajouter des liens croisés entre les termes pour créer un glossaire interactif.

## Résumé des commandes essentielles

**Créer l'environnement virtuel** :

```bash
python -m venv venv
```

**Activer l'environnement (Windows)** :

```bash
venv\Scripts\activate
```

**Activer l'environnement (Mac/Linux)** :

```bash
source venv/bin/activate
```

**Installer MkDocs et Material** :

```bash
pip install mkdocs mkdocs-material
```

**Créer un nouveau projet MkDocs** :

```bash
mkdocs new .
```

**Servir localement** :

```bash
mkdocs serve
```

**Construire le site** :

```bash
mkdocs build
```

**Déployer sur GitHub Pages** :

```bash
mkdocs gh-deploy
```

**Commandes Git** :

```bash
git add .
git commit -m "Message"
git push
```


## Ressources complémentaires

- Documentation MkDocs officielle : [mkdocs.org](https://www.mkdocs.org)[^1_6][^1_5]
- Documentation Material for MkDocs : [squidfunk.github.io/mkdocs-material](https://squidfunk.github.io/mkdocs-material)[^1_12]
- Guide Git dans VS Code : [code.visualstudio.com/docs/sourcecontrol/overview](https://code.visualstudio.com/docs/sourcecontrol/overview)[^1_8]

Votre dictionnaire météorologique multilingue sera maintenant accessible en ligne avec une interface moderne et professionnelle, permettant une navigation facile entre les différentes langues et termes.[^1_5][^1_1][^1_4][^1_12][^1_10]
<span style="display:none">[^1_13][^1_14][^1_15][^1_16][^1_17][^1_18][^1_19]</span>

<div align="center">⁂</div>

[^1_1]: DRAFT_LEXIQUE_METEO_VERSION-FINALE.pdf

[^1_2]: https://www.youtube.com/watch?v=PQtlLzDiQF8

[^1_3]: https://realpython.com/python-virtual-environments-a-primer/

[^1_4]: https://www.letscloud.io/community/how-to-install-mkdocs-on-linux-server-and-docker

[^1_5]: https://dev.to/lynn_mikami_e94e5b9ad7daf/how-to-install-and-use-mkdocs-a-beginners-guide-4d53

[^1_6]: https://www.mkdocs.org/user-guide/installation/

[^1_7]: https://dev.to/n3wt0n/create-a-new-github-repo-in-1-click-vscode-29ae

[^1_8]: https://code.visualstudio.com/docs/sourcecontrol/overview

[^1_9]: https://stackoverflow.com/questions/46877667/how-to-add-a-new-project-to-github-using-vs-code

[^1_10]: https://kioku-space.com/en/readthedocs-mkdocs-multi-lang/

[^1_11]: https://github.com/squidfunk/mkdocs-material/discussions/2346

[^1_12]: https://squidfunk.github.io/mkdocs-material/setup/changing-the-language/

[^1_13]: https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code

[^1_14]: https://learn.openwaterfoundation.org/owf-learn-mkdocs/install/

[^1_15]: https://www.pythonsnacks.com/p/python-packages-for-meteorologists

[^1_16]: https://dev.to/edvichuki/comprehensive-weather-data-analysis-using-python-temperature-rainfall-trends-and-visualizations-1off

[^1_17]: https://pypi.org/project/mkdocs-material-langly/

[^1_18]: https://pvlib-python.readthedocs.io/en/v0.10.3/user_guide/weather_data.html

[^1_19]: https://code.visualstudio.com/docs/sourcecontrol/intro-to-git


---
