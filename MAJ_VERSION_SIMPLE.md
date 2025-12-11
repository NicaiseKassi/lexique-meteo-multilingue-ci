# 🔄 Guide Simple : Mettre à Jour la Version

## 📍 Version Actuelle : 1.0

---

## ✅ ÉTAPES POUR PASSER À LA VERSION 1.1

### 1️⃣ Modifier le Footer (OBLIGATOIRE)

**Fichier** : `docs/overrides/main.html`  
**Ligne** : ~210

```html
# Chercher cette ligne :
<strong>Version 1.0</strong> | 

# Remplacer par :
<strong>Version 1.1</strong> | 
```

### 2️⃣ Modifier mkdocs.yml (Recommandé)

**Fichier** : `mkdocs.yml`  
**Ligne** : 7

```yaml
# Chercher :
extra:
  version: 1.0

# Remplacer par :
extra:
  version: 1.1
```

### 3️⃣ Mettre à jour VERSION.md

**Fichier** : `VERSION.md`

Ajouter en haut du fichier :

```markdown
## Version 1.1 (Date du jour)

### ✨ Nouveautés
- Description des nouveaux termes ajoutés
- Nouvelles fonctionnalités

### 🔧 Améliorations  
- Ce qui a été amélioré

### 🐛 Corrections
- Bugs corrigés

---

## Version 1.0 (11 décembre 2024)
[Contenu existant...]
```

### 4️⃣ Vérifier

```bash
# Visitez le site
http://127.0.0.1:8000

# Scrollez tout en bas
# Vous devez voir : "Version 1.1"
```

### 5️⃣ Commiter sur Git

```bash
git add docs/overrides/main.html mkdocs.yml VERSION.md
git commit -m "chore: Version 1.1 - Description des changements"
git push origin master

# Créer le tag
git tag -a v1.1 -m "Version 1.1"
git push origin v1.1
```

---

## 📝 Résumé Ultra-Court

**3 fichiers à modifier :**

1. **`docs/overrides/main.html`** (ligne 210) → `Version 1.1`
2. **`mkdocs.yml`** (ligne 7) → `version: 1.1`  
3. **`VERSION.md`** → Ajouter section 1.1 en haut

**Puis :**
- Tester le site
- Git commit + tag + push

---

## 🎯 Où Trouver les Fichiers

```
PROJET_LEXIQUE_METEO_MULTILINGUE/
├── docs/
│   └── overrides/
│       └── main.html          ← Ligne 210 : Version X.X
├── mkdocs.yml                 ← Ligne 7 : version: X.X
└── VERSION.md                 ← Ajouter historique
```

---

## ⚠️ IMPORTANT

**Le numéro de version s'affiche uniquement dans :**
- Footer du site (en bas de chaque page)

**Pour le voir :**
1. Ouvrir http://127.0.0.1:8000
2. Scroller jusqu'en bas
3. Lire : "Version 1.0" (ou 1.1, etc.)

---

## 🔢 Convention de Version

- **1.0 → 1.1** : Ajout de fonctionnalités, nouveaux termes
- **1.1 → 1.2** : Autres améliorations
- **1.2 → 2.0** : Refonte majeure
- **1.1 → 1.1.1** : Petites corrections uniquement

---

## 📋 Checklist Rapide

Avant de déployer :

- [ ] `main.html` modifié (Version X.X)
- [ ] `mkdocs.yml` modifié (version: X.X)
- [ ] `VERSION.md` mis à jour
- [ ] Site testé (footer affiche bonne version)
- [ ] Git commit créé
- [ ] Tag Git créé (vX.X)
- [ ] Poussé vers GitHub

✅ TERMINÉ !
