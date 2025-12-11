# 🔄 Guide de Mise à Jour de Version

## 📍 Version Actuelle : 1.0

### Où voir la version ?

1. **Sur le site** : http://127.0.0.1:8000
   - Scrollez tout en bas de la page
   - Vous verrez : **"Version 1.0"** dans le footer

2. **Dans le code** : `mkdocs.yml` ligne 7
   ```yaml
   extra:
     version: 1.0
   ```

---

## 🚀 Comment Mettre à Jour la Version

### Exemple : Passer de 1.0 à 1.1

#### Étape 1 : Modifier le footer (docs/overrides/main.html)

Ouvrir `docs/overrides/main.html` et chercher la ligne avec "Version 1.0" (vers la ligne 210) :

```html
# AVANT
<strong>Version 1.0</strong> | 

# APRÈS
<strong>Version 1.1</strong> | 
```

#### Étape 2 : Modifier mkdocs.yml (optionnel mais recommandé)

Ouvrir `mkdocs.yml` et changer la ligne 7 :

```yaml
# AVANT
extra:
  version: 1.0

# APRÈS
extra:
  version: 1.1
```

#### Étape 3 : Mettre à jour VERSION.md

Ajouter la nouvelle version en haut de `VERSION.md` :

```markdown
## Version 1.1 (Date)

### ✨ Nouveautés
- ✅ [Description de ce qui a été ajouté]

### 🔧 Améliorations
- ✅ [Description des améliorations]

### 🐛 Corrections
- ✅ [Description des bugs corrigés]

---

## Version 1.0 (11 décembre 2024)
[Contenu existant...]
```

#### Étape 3 : Vérifier sur le site

```bash
# Le serveur MkDocs recharge automatiquement
# Visitez http://127.0.0.1:8000
# Scrollez en bas → Vous devriez voir "Version 1.1"
```

#### Étape 4 : Commiter sur Git

```bash
# Ajouter les fichiers modifiés
git add mkdocs.yml VERSION.md docs/

# Commiter avec message clair
git commit -m "chore: Bump version to 1.1

Nouveautés:
- [Liste des changements]
"

# Pousser vers GitHub
git push origin master

# Créer un tag de version
git tag -a v1.1 -m "Version 1.1 - Description"
git push origin v1.1
```

---

## 📊 Convention de Numérotation

### Format : MAJEURE.MINEURE.PATCH

- **MAJEURE** (1.x.x) : Changements incompatibles, refonte complète
- **MINEURE** (x.1.x) : Nouvelles fonctionnalités, compatibles
- **PATCH** (x.x.1) : Corrections de bugs, petites améliorations

### Exemples

| Version | Type | Exemple |
|---------|------|---------|
| 1.0 → 1.1 | Mineure | Ajout de 100 nouveaux termes |
| 1.1 → 1.2 | Mineure | Ajout de recherche avancée |
| 1.2 → 1.2.1 | Patch | Correction bug audio |
| 1.2.1 → 2.0 | Majeure | Refonte complète de l'interface |

---

## ⚡ Raccourci Rapide

### Script de mise à jour (copier-coller)

```bash
# Remplacer 1.1 par votre nouvelle version
NEW_VERSION="1.1"

# 1. Mettre à jour mkdocs.yml
sed -i "s/version: .*/version: $NEW_VERSION/" mkdocs.yml

# 2. Vérifier
grep "version:" mkdocs.yml

# 3. Éditer VERSION.md manuellement (ajouter les changements)

# 4. Tester
echo "Visitez http://127.0.0.1:8000 pour vérifier"

# 5. Commiter
git add mkdocs.yml VERSION.md docs/
git commit -m "chore: Bump version to $NEW_VERSION"
git push origin master
git tag -a v$NEW_VERSION -m "Version $NEW_VERSION"
git push origin v$NEW_VERSION

echo "✅ Version $NEW_VERSION déployée !"
```

---

## 📋 Checklist de Mise à Jour

Avant de déployer une nouvelle version :

- [ ] Version modifiée dans `mkdocs.yml`
- [ ] `VERSION.md` mis à jour avec les changements
- [ ] Site testé localement (http://127.0.0.1:8000)
- [ ] Footer affiche la bonne version
- [ ] Toutes les nouvelles fonctionnalités testées
- [ ] Git commit créé avec message descriptif
- [ ] Tag Git créé (vX.X)
- [ ] Poussé vers GitHub

---

## 🔍 Vérification

### Vérifier la version actuelle

```bash
# Dans mkdocs.yml
grep "version:" mkdocs.yml

# Sur le site (doit afficher "Version X.X")
curl -s http://127.0.0.1:8000 | grep -o "Version [0-9.]*"

# Tags Git
git tag -l
```

---

## 📝 Exemples de Messages de Commit

```bash
# Nouvelle fonctionnalité
git commit -m "feat: Ajout de 50 nouveaux termes en Sénoufo"

# Amélioration
git commit -m "style: Amélioration du design du header"

# Correction
git commit -m "fix: Correction lecteur audio sur mobile"

# Version
git commit -m "chore: Bump version to 1.2"

# Plusieurs changements
git commit -m "chore: Version 1.2 - Ajout termes + corrections

- feat: 50 nouveaux termes
- fix: Audio mobile
- style: Header amélioré"
```

---

## 🎯 Résumé Ultra-Rapide

**Pour passer de 1.0 à 1.1 :**

1. `mkdocs.yml` → `version: 1.1`
2. Ajouter section dans `VERSION.md`
3. Tester : http://127.0.0.1:8000
4. Git : `commit + tag + push`

**Fichiers à modifier :**
- ✅ `mkdocs.yml` (ligne 7)
- ✅ `VERSION.md` (ajouter en haut)

**Le footer se met à jour automatiquement !**
