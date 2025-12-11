# 🚀 Guide de Déploiement Git & GitHub

## 📋 Configuration Initiale (Déjà faite)

✅ Version 1.0 configurée dans `mkdocs.yml`  
✅ `.gitignore` configuré (tous les fichiers Python ignorés)  
✅ Remote GitHub configuré  
✅ Footer avec version créé  
✅ README.md mis à jour  

## 🔄 Workflow Git Quotidien

### 1️⃣ Vérifier l'état actuel

```bash
git status
```

### 2️⃣ Ajouter les fichiers MkDocs modifiés

**Ajouter tout le contenu MkDocs :**
```bash
git add docs/ mkdocs.yml README.md VERSION.md
```

**Ou ajouter des fichiers spécifiques :**
```bash
git add docs/index.md
git add docs/stylesheets/extra.css
git add mkdocs.yml
```

### 3️⃣ Vérifier ce qui sera commité

```bash
git status
```

### 4️⃣ Commiter avec un message clair

**Convention de messages :**

```bash
# Nouvelle fonctionnalité
git commit -m "feat: Ajout transition glissante pour header"

# Correction de bug
git commit -m "fix: Correction positionnement recherche"

# Amélioration design
git commit -m "style: Amélioration couleurs header dynamique"

# Documentation
git commit -m "docs: Mise à jour guide utilisateur"

# Nouveau terme
git commit -m "content: Ajout de 50 nouveaux termes météo"

# Version
git commit -m "chore: Version 1.0 - Release initiale"
```

### 5️⃣ Pousser vers GitHub

**Première fois (créer la branche main) :**
```bash
git branch -M main
git push -u origin main
```

**Ensuite (pushes normaux) :**
```bash
git push origin main
```

## 🏷️ Gestion des Versions

### Créer une nouvelle version

1. **Modifier la version dans `mkdocs.yml` :**
```yaml
extra:
  version: 1.1  # Nouvelle version
```

2. **Mettre à jour `VERSION.md` :**
```markdown
## Version 1.1 (Date)

### Nouveautés
- ✅ Ajout de X nouveaux termes
- ✅ Amélioration de Y fonctionnalité
...
```

3. **Commiter les changements :**
```bash
git add mkdocs.yml VERSION.md
git commit -m "chore: Bump version to 1.1"
```

4. **Créer un tag Git :**
```bash
git tag -a v1.1 -m "Version 1.1 - Description"
```

5. **Pousser avec les tags :**
```bash
git push origin main
git push origin v1.1
```

## 📦 Premier Déploiement Complet

```bash
# 1. Aller dans le dossier du projet
cd /home/kassi/Documents/PROJET_LEXIQUE_METEO_MULTILINGUE

# 2. Vérifier que Git est bien configuré
git remote -v
# Doit afficher: origin https://github.com/NicaiseKassi/lexique-meteo-multilingue-ci.git

# 3. Vérifier les fichiers à commiter (exclut les .py automatiquement)
git status

# 4. Ajouter tous les fichiers MkDocs
git add docs/ mkdocs.yml README.md VERSION.md .gitignore

# 5. Commiter la version initiale
git commit -m "chore: Version 1.0 - Release initiale

- 651 termes météorologiques en 8 langues
- Header dynamique avec images glissantes
- Interface responsive complète
- Recherche fonctionnelle
- Audio multilingue"

# 6. Créer la branche main et pousser
git branch -M main
git push -u origin main

# 7. Créer le tag de version 1.0
git tag -a v1.0 -m "Version 1.0 - Version initiale stable"
git push origin v1.0

# ✅ TERMINÉ ! Votre code est sur GitHub
```

## 🌿 Travailler avec des Branches

### Créer une branche pour une nouvelle fonctionnalité

```bash
# Créer et basculer sur une nouvelle branche
git checkout -b feature/nouvelle-fonction

# Faire vos modifications...

# Commiter
git add .
git commit -m "feat: Description de la nouvelle fonction"

# Pousser la branche
git push origin feature/nouvelle-fonction
```

### Fusionner une branche dans main

```bash
# Retourner sur main
git checkout main

# Fusionner la branche
git merge feature/nouvelle-fonction

# Pousser
git push origin main

# Supprimer la branche (optionnel)
git branch -d feature/nouvelle-fonction
git push origin --delete feature/nouvelle-fonction
```

## 🔍 Commandes Utiles

### Voir l'historique
```bash
git log --oneline --graph --all
```

### Voir les différences
```bash
# Différences non commitées
git diff

# Différences d'un fichier spécifique
git diff docs/index.md
```

### Annuler des modifications
```bash
# Annuler modifications d'un fichier (avant add)
git checkout -- docs/index.md

# Retirer un fichier du staging (après add)
git reset HEAD docs/index.md

# Annuler le dernier commit (garder les modifications)
git reset --soft HEAD~1
```

### Synchroniser avec GitHub
```bash
# Récupérer les changements
git pull origin main

# Voir les branches distantes
git branch -r
```

## 📊 Fichiers Suivis vs Ignorés

### ✅ Fichiers SUIVIS (commitables)

- `docs/` - Tout le contenu MkDocs
  - `docs/*.md` - Pages markdown
  - `docs/stylesheets/` - CSS
  - `docs/javascripts/` - JavaScript
  - `docs/images/` - Images
  - `docs/audio/` - Fichiers audio
  - `docs/overrides/` - Templates personnalisés
- `mkdocs.yml` - Configuration
- `README.md` - Documentation
- `VERSION.md` - Historique versions
- `.gitignore` - Configuration Git

### ❌ Fichiers IGNORÉS (non commitables)

- `*.py` - TOUS les scripts Python
- `__pycache__/` - Cache Python
- `site/` - Site généré
- `.venv/`, `venv/` - Environnements virtuels
- `*.log` - Logs
- `.DS_Store` - Fichiers macOS
- `*.tmp`, `*.bak` - Temporaires

## 🆘 Dépannage

### Problème : "Remote already exists"
```bash
git remote remove origin
git remote add origin https://github.com/NicaiseKassi/lexique-meteo-multilingue-ci.git
```

### Problème : Fichiers Python commitables
```bash
# Vérifier le .gitignore
cat .gitignore

# Forcer l'ignorage
git rm --cached *.py
git commit -m "chore: Retrait scripts Python du suivi Git"
```

### Problème : Conflit lors du pull
```bash
# Voir les conflits
git status

# Éditer les fichiers en conflit, puis:
git add <fichiers-resolus>
git commit -m "merge: Résolution conflits"
```

## 📞 Ressources

- **GitHub Desktop** : Interface graphique (recommandée pour débutants)
  - Télécharger : https://desktop.github.com/
  
- **Documentation Git** : https://git-scm.com/doc

- **Convention de Commits** : https://www.conventionalcommits.org/

---

**🎯 Checklist Déploiement V1.0**

- [ ] Repository GitHub créé : `lexique-meteo-multilingue-ci`
- [ ] Remote configuré
- [ ] `.gitignore` vérifié
- [ ] Version 1.0 dans `mkdocs.yml`
- [ ] `VERSION.md` complété
- [ ] README.md mis à jour
- [ ] Premier commit fait
- [ ] Push vers GitHub
- [ ] Tag v1.0 créé
- [ ] Tag v1.0 poussé

**Une fois tout coché, votre projet est officiellement sur GitHub ! 🎉**
