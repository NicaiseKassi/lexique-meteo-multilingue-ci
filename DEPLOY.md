# 🚀 Instructions de déploiement GitHub

## Étape 1: Créer le dépôt GitHub

1. Allez sur [github.com](https://github.com) et connectez-vous
2. Cliquez sur "New repository" (bouton vert)
3. Nommez le dépôt: `lexique-meteo-multilingue`
4. Description: `Dictionnaire météorologique multilingue - SODEXAM Côte d'Ivoire`
5. Cochez "Public" pour permettre GitHub Pages gratuit
6. **NE PAS** cocher "Initialize with README" (nous avons déjà les fichiers)
7. Cliquez "Create repository"

## Étape 2: Connecter le dépôt local

Copier-coller ces commandes dans le terminal (remplacer VOTRE-USERNAME):

```bash
# Ajouter l'origine GitHub (remplacer VOTRE-USERNAME)
git remote add origin https://github.com/VOTRE-USERNAME/lexique-meteo-multilingue.git

# Renommer la branche principale en 'main' si nécessaire
git branch -M main

# Pousser vers GitHub
git push -u origin main
```

## Étape 3: Activer GitHub Pages

1. Allez dans les **Settings** de votre dépôt
2. Descendez à la section **"Pages"** (dans le menu latéral)
3. Dans **"Source"**, sélectionnez **"GitHub Actions"**
4. Le workflow se lancera automatiquement après le push

## Étape 4: Vérifier le déploiement

1. Allez dans l'onglet **"Actions"** de votre dépôt
2. Vous devriez voir le workflow "🚀 Déploiement Lexique Météorologique" en cours
3. Une fois terminé (✅), votre site sera disponible à:
   `https://VOTRE-USERNAME.github.io/lexique-meteo-multilingue`

## 🔧 Dépannage

### Si le workflow échoue:

1. Vérifiez les logs dans l'onglet "Actions"
2. Assurez-vous que GitHub Pages est activé dans Settings > Pages
3. Si problème avec gTTS, les fichiers audio ne seront pas générés mais le site fonctionnera

### Pour tester localement:

```bash
# Activer l'environnement Conda
conda activate lexique-meteo

# Lancer le serveur local
mkdocs serve

# Site disponible sur http://127.0.0.1:8000
```

## 📝 Mise à jour future

Pour ajouter des termes ou faire des modifications:

```bash
# 1. Modifier generate_audio.py pour ajouter des termes
# 2. Régénérer les pages
python generate_pages.py

# 3. Commiter et pousser
git add .
git commit -m "Ajout de nouveaux termes météorologiques"
git push

# Le déploiement se fait automatiquement via GitHub Actions
```

## 🎯 Résultat attendu

Une fois déployé, vous aurez:
- ✅ Un site web moderne et responsive
- ✅ Navigation intuitive avec recherche
- ✅ Boutons audio fonctionnels (si connexion Internet)
- ✅ Compatible mobile/tablette/desktop
- ✅ Mise à jour automatique à chaque push
- ✅ URL publique accessible mondialement