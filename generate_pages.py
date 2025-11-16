#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de génération automatique des pages Markdown
pour le lexique météorologique multilingue.

Ce script crée automatiquement toutes les pages de termes
avec navigation, boutons audio et mise en page cohérente.

Auteur: SODEXAM - Côte d'Ivoire
Date: Novembre 2024
"""

import os
import re
from typing import Dict, List, Tuple
from generate_audio import TERMES_METEO, slugify  # Importer les données et fonctions communes

def create_audio_button(slug: str, lang: str, text: str) -> str:
    """
    Crée le HTML pour un bouton audio avec le texte de traduction.
    
    Args:
        slug (str): Slug du terme pour le nom de fichier audio
        lang (str): Code de la langue
        text (str): Texte de la traduction
        
    Returns:
        str: HTML du bouton audio et du texte
    """
    return f"""<div class="translation-item">
    <span class="translation-text">{text}</span>
    <button class="audio-btn" data-audio="../audio/{slug}_{lang}.mp3" title="Écouter la prononciation">🔊</button>
</div>"""

def create_terme_page(terme_data: Dict, index: int, total: int) -> str:
    """
    Génère le contenu Markdown complet d'une page de terme.
    
    Args:
        terme_data (Dict): Données du terme (français + traductions)
        index (int): Index du terme (0-based)
        total (int): Nombre total de termes
        
    Returns:
        str: Contenu Markdown de la page
    """
    terme_fr = terme_data["terme_fr"]
    definition_fr = terme_data["definition_fr"]
    traductions = terme_data["traductions"]
    slug = slugify(terme_fr)
    
    # Génération de la navigation précédent/suivant
    navigation_links = []
    
    # Lien retour à l'index
    navigation_links.append('[🏠 Retour à l\'accueil](../index.md)')
    
    # Lien précédent
    if index > 0:
        prev_terme = TERMES_METEO[index - 1]
        prev_slug = slugify(prev_terme["terme_fr"])
        navigation_links.append(f'[◄ {prev_terme["terme_fr"]}]({prev_slug}.md)')
    
    # Lien suivant
    if index < total - 1:
        next_terme = TERMES_METEO[index + 1]
        next_slug = slugify(next_terme["terme_fr"])
        navigation_links.append(f'[{next_terme["terme_fr"]} ►]({next_slug}.md)')
    
    # Configuration des langues pour l'affichage
    langues_display = {
        'baoule': 'Baoulé',
        'bete': 'Bété', 
        'lobi': 'Lobi',
        'malinke': 'Malinké',
        'senoufo': 'Sénoufo',
        'koulango': 'Koulango',
        'yacouba': 'Yacouba'
    }
    
    # Génération du contenu de la page
    content = f"""# {terme_fr}

<div class="terme-header">
    <h1 class="terme-title">{terme_fr}</h1>
    {create_audio_button(slug, 'fr', terme_fr)}
</div>

![{terme_fr}](../images/{slug}.jpg)
{{ .terme-image }}

## Définition (Français facile)

<div class="terme-definition">
{definition_fr}
</div>

## Traductions

<div class="traductions-section">
    <div class="traductions-grid">
"""

    # Ajouter chaque traduction avec son bouton audio
    for lang_code, lang_display in langues_display.items():
        if lang_code in traductions:
            traduction = traductions[lang_code]
            content += f"""        <div class="langue-group">
            <div class="language-label">{lang_display}</div>
            {create_audio_button(slug, lang_code, traduction)}
        </div>
"""
    
    content += """    </div>
</div>

---

<div class="terme-navigation">
"""
    content += " | ".join(navigation_links)
    content += """
</div>

!!! info "À propos de ce terme"
    Ce terme fait partie du lexique météorologique multilingue développé par la SODEXAM (Société d'Exploitation et de Développement Aéroportuaire, Aéronautique et Météorologique) de Côte d'Ivoire. Les traductions ont été élaborées en collaboration avec des locuteurs natifs des différentes langues locales.

<div class="language-badge">Français</div>
"""
    
    # Ajouter les badges de langues disponibles
    for lang_code in traductions.keys():
        lang_display = langues_display.get(lang_code, lang_code.title())
        content += f'<div class="language-badge">{lang_display}</div>\n'
    
    return content

def generate_all_pages() -> None:
    """
    Génère toutes les pages de termes dans le répertoire docs/termes/.
    """
    # Créer le répertoire de destination
    termes_dir = os.path.join("docs", "termes")
    os.makedirs(termes_dir, exist_ok=True)
    
    print("📄 Génération des pages Markdown pour le lexique météorologique")
    print(f"📁 Répertoire de destination: {termes_dir}")
    print(f"📊 {len(TERMES_METEO)} pages à générer")
    print("-" * 70)
    
    pages_generees = 0
    erreurs = 0
    
    for i, terme_data in enumerate(TERMES_METEO):
        terme_fr = terme_data["terme_fr"]
        slug = slugify(terme_fr)
        
        try:
            # Générer le contenu de la page
            content = create_terme_page(terme_data, i, len(TERMES_METEO))
            
            # Nom du fichier
            filename = f"{slug}.md"
            filepath = os.path.join(termes_dir, filename)
            
            # Écrire le fichier
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            pages_generees += 1
            print(f"[{i+1:2d}/{len(TERMES_METEO)}] ✓ {filename} - {terme_fr}")
            
        except Exception as e:
            erreurs += 1
            print(f"[{i+1:2d}/{len(TERMES_METEO)}] ✗ Erreur pour {terme_fr}: {str(e)}")
    
    print("-" * 70)
    print(f"📈 Résumé de la génération:")
    print(f"   ✓ Pages générées: {pages_generees}")
    if erreurs > 0:
        print(f"   ✗ Erreurs: {erreurs}")
    else:
        print(f"   🎉 Aucune erreur!")
    print(f"   📁 Pages disponibles dans: {termes_dir}")

def generate_navigation_config() -> str:
    """
    Génère la configuration de navigation pour mkdocs.yml.
    
    Returns:
        str: Configuration YAML de navigation
    """
    print("\n🧭 Génération de la configuration de navigation...")
    
    # Grouper les termes par première lettre
    groupes = {}
    for terme_data in TERMES_METEO:
        terme_fr = terme_data["terme_fr"]
        slug = slugify(terme_fr)
        premiere_lettre = terme_fr[0].upper()
        
        if premiere_lettre not in groupes:
            groupes[premiere_lettre] = []
        
        groupes[premiere_lettre].append((terme_fr, f"termes/{slug}.md"))
    
    # Générer la configuration YAML
    nav_config = """nav:
  - Accueil: index.md
  - Termes météorologiques:"""
    
    for lettre in sorted(groupes.keys()):
        nav_config += f"\n    - {lettre}:"
        for terme_fr, chemin in sorted(groupes[lettre]):
            nav_config += f"\n      - {terme_fr}: {chemin}"
    
    return nav_config

def update_mkdocs_config() -> None:
    """
    Met à jour le fichier mkdocs.yml avec la navigation automatique.
    """
    print("\n📝 Mise à jour de la configuration MkDocs...")
    
    nav_config = generate_navigation_config()
    
    # Lire le fichier mkdocs.yml existant
    mkdocs_file = "mkdocs.yml"
    try:
        with open(mkdocs_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remplacer la section nav (simple approximation)
        # Dans un vrai projet, utiliser PyYAML pour une manipulation propre
        lines = content.split('\n')
        new_lines = []
        in_nav_section = False
        
        for line in lines:
            if line.strip().startswith('nav:'):
                in_nav_section = True
                new_lines.extend(nav_config.split('\n'))
            elif in_nav_section and line.strip() and not line.startswith('  ') and not line.startswith('\t'):
                # Fin de la section nav
                in_nav_section = False
                new_lines.append(line)
            elif not in_nav_section:
                new_lines.append(line)
        
        # Écrire le fichier mis à jour
        with open(mkdocs_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        
        print(f"✓ Configuration MkDocs mise à jour: {mkdocs_file}")
        
    except Exception as e:
        print(f"⚠️  Impossible de mettre à jour mkdocs.yml automatiquement: {str(e)}")
        print("   Vous devrez ajouter la navigation manuellement.")

def create_images_placeholder() -> None:
    """
    Crée des fichiers placeholder pour les images manquantes.
    """
    print("\n🖼️  Création des placeholders d'images...")
    
    images_dir = os.path.join("docs", "images")
    os.makedirs(images_dir, exist_ok=True)
    
    # Créer un fichier README pour les images
    readme_content = """# Images du lexique météorologique

Ce répertoire contient les images illustratives pour chaque terme météorologique.

## Format requis
- Format: JPG ou PNG
- Taille recommandée: 800x600 pixels maximum
- Poids: moins de 500KB par image
- Noms: utiliser le slug du terme (ex: abri-meteo.jpg)

## Sources d'images recommandées
- Unsplash (https://unsplash.com) - Images libres de droits
- Wikimedia Commons (https://commons.wikimedia.org)
- Photos personnelles de la SODEXAM

## Liste des images nécessaires
"""
    
    for terme_data in TERMES_METEO:
        terme_fr = terme_data["terme_fr"]
        slug = slugify(terme_fr)
        readme_content += f"- `{slug}.jpg` - {terme_fr}\n"
    
    readme_path = os.path.join(images_dir, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✓ Guide des images créé: {readme_path}")

def main():
    """Fonction principale du script."""
    print("🌍 Lexique Météorologique Multilingue - Générateur de Pages")
    print("💡 Développé par SODEXAM - Côte d'Ivoire")
    print("=" * 70)
    
    try:
        # Générer toutes les pages
        generate_all_pages()
        
        # Mettre à jour la configuration MkDocs
        update_mkdocs_config()
        
        # Créer les placeholders d'images
        create_images_placeholder()
        
        print("\n🎉 Génération terminée avec succès!")
        print("\n📝 Étapes suivantes:")
        print("   1. Ajoutez les images dans docs/images/")
        print("   2. Exécutez generate_audio.py pour créer les fichiers audio")
        print("   3. Testez avec: mkdocs serve")
        print("   4. Personnalisez le contenu si nécessaire")
        
    except KeyboardInterrupt:
        print("\n⏹️  Génération interrompue par l'utilisateur.")
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {str(e)}")
        print("   Veuillez vérifier votre configuration et réessayer.")

if __name__ == "__main__":
    main()