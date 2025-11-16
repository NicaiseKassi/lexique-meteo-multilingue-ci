#!/usr/bin/env python3
"""
Script pour créer des images SVG simples pour les termes météorologiques
"""

import os
from pathlib import Path

def create_svg_image(terme_id, terme_fr, emoji, color="#4A90E2"):
    """Crée une image SVG simple avec emoji et texte"""
    
    svg_content = f'''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
  <!-- Fond avec dégradé -->
  <defs>
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color};stop-opacity:0.1" />
      <stop offset="100%" style="stop-color:{color};stop-opacity:0.3" />
    </linearGradient>
  </defs>
  
  <!-- Fond -->
  <rect width="400" height="300" fill="url(#bgGradient)" rx="15" ry="15"/>
  
  <!-- Bordure -->
  <rect width="390" height="290" x="5" y="5" fill="none" stroke="{color}" stroke-width="2" rx="10" ry="10"/>
  
  <!-- Emoji principal -->
  <text x="200" y="130" text-anchor="middle" font-size="80" font-family="Arial, sans-serif">
    {emoji}
  </text>
  
  <!-- Texte du terme -->
  <text x="200" y="220" text-anchor="middle" font-size="24" font-family="Arial, sans-serif" 
        fill="{color}" font-weight="bold">
    {terme_fr}
  </text>
  
  <!-- Sous-titre -->
  <text x="200" y="250" text-anchor="middle" font-size="14" font-family="Arial, sans-serif" 
        fill="#666666">
    Lexique Météorologique SODEXAM
  </text>
</svg>'''
    
    return svg_content

def generate_basic_images():
    """Génère des images SVG de base pour les termes principaux"""
    
    # Créer le répertoire images
    images_dir = Path("docs/images")
    images_dir.mkdir(exist_ok=True)
    
    # Définition des termes avec leurs emojis et couleurs
    termes_images = [
        ("abri-meteorologique", "Abri météorologique", "🏠", "#4A90E2"),
        ("accalmie", "Accalmie", "😌", "#87CEEB"),
        ("adaptation", "Adaptation", "🔄", "#32CD32"),
        ("aerosol", "Aérosol", "💨", "#B0C4DE"),
        ("altitude", "Altitude", "🏔️", "#8B4513"),
        ("anemometre", "Anémomètre", "📏", "#FF6347"),
        ("anticyclone", "Anticyclone", "🌀", "#4169E1"),
        ("arc-en-ciel", "Arc-en-ciel", "🌈", "#FF69B4"),
        ("aride", "Aride", "🏜️", "#DEB887"),
        ("atmosphere", "Atmosphère", "🌍", "#00CED1"),
        ("barometre", "Baromètre", "⚖️", "#FF4500"),
        ("brouillard", "Brouillard", "🌫️", "#D3D3D3"),
        ("climat", "Climat", "🌡️", "#FF6347"),
        ("cyclone", "Cyclone", "🌪️", "#8B0000"),
        ("humidite", "Humidité", "💧", "#1E90FF"),
        ("nuage", "Nuage", "☁️", "#C0C0C0"),
        ("pluie", "Pluie", "🌧️", "#4682B4"),
        ("secheresse", "Sécheresse", "🔥", "#DC143C"),
        ("soleil", "Soleil", "☀️", "#FFD700"),
        ("temperature", "Température", "🌡️", "#FF4500"),
        ("vent", "Vent", "🌬️", "#87CEEB"),
    ]
    
    print("🖼️  Génération des images SVG...")
    print("=" * 50)
    
    images_generees = 0
    
    for terme_id, terme_fr, emoji, color in termes_images:
        try:
            # Créer le contenu SVG
            svg_content = create_svg_image(terme_id, terme_fr, emoji, color)
            
            # Nom du fichier
            filename = f"{terme_id}.svg"
            filepath = images_dir / filename
            
            # Écrire le fichier
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(svg_content)
            
            images_generees += 1
            print(f"✓ {filename} - {terme_fr} {emoji}")
            
        except Exception as e:
            print(f"✗ Erreur pour {terme_fr}: {str(e)}")
    
    print("=" * 50)
    print(f"📊 Résumé: {images_generees} images SVG générées")
    print(f"📁 Images disponibles dans: {images_dir}")
    
    return images_generees

def create_weather_icons():
    """Crée des icônes météorologiques plus sophistiquées pour certains termes"""
    
    images_dir = Path("docs/images")
    
    # Icône spéciale pour le soleil
    sun_svg = '''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="sunGradient" cx="50%" cy="50%" r="40%">
      <stop offset="0%" style="stop-color:#FFD700;stop-opacity:1" />
      <stop offset="70%" style="stop-color:#FF8C00;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#FF4500;stop-opacity:0.8" />
    </radialGradient>
  </defs>
  
  <!-- Fond -->
  <rect width="400" height="300" fill="#87CEEB" rx="15" ry="15"/>
  
  <!-- Rayons du soleil -->
  <g stroke="#FFD700" stroke-width="4" stroke-linecap="round">
    <line x1="200" y1="50" x2="200" y2="30"/>
    <line x1="280" y1="70" x2="290" y2="60"/>
    <line x1="330" y1="150" x2="350" y2="150"/>
    <line x1="280" y1="230" x2="290" y2="240"/>
    <line x1="200" y1="250" x2="200" y2="270"/>
    <line x1="120" y1="230" x2="110" y2="240"/>
    <line x1="70" y1="150" x2="50" y2="150"/>
    <line x1="120" y1="70" x2="110" y2="60"/>
  </g>
  
  <!-- Cercle du soleil -->
  <circle cx="200" cy="150" r="60" fill="url(#sunGradient)"/>
  
  <!-- Texte -->
  <text x="200" y="250" text-anchor="middle" font-size="20" font-family="Arial, sans-serif" 
        fill="#FF4500" font-weight="bold">Soleil</text>
</svg>'''
    
    # Icône pour la pluie
    rain_svg = '''<svg width="400" height="300" xmlns="http://www.w3.org/2000/svg">
  <!-- Fond -->
  <rect width="400" height="300" fill="#E6F3FF" rx="15" ry="15"/>
  
  <!-- Nuage -->
  <g fill="#B0C4DE">
    <circle cx="150" cy="80" r="25"/>
    <circle cx="180" cy="70" r="35"/>
    <circle cx="220" cy="70" r="35"/>
    <circle cx="250" cy="80" r="25"/>
    <rect x="125" y="70" width="150" height="35"/>
  </g>
  
  <!-- Gouttes de pluie -->
  <g fill="#4682B4" opacity="0.7">
    <ellipse cx="160" cy="140" rx="3" ry="12"/>
    <ellipse cx="180" cy="160" rx="3" ry="12"/>
    <ellipse cx="200" cy="130" rx="3" ry="12"/>
    <ellipse cx="220" cy="150" rx="3" ry="12"/>
    <ellipse cx="240" cy="170" rx="3" ry="12"/>
    
    <ellipse cx="170" cy="190" rx="3" ry="12"/>
    <ellipse cx="190" cy="210" rx="3" ry="12"/>
    <ellipse cx="210" cy="180" rx="3" ry="12"/>
    <ellipse cx="230" cy="200" rx="3" ry="12"/>
  </g>
  
  <!-- Texte -->
  <text x="200" y="250" text-anchor="middle" font-size="20" font-family="Arial, sans-serif" 
        fill="#4682B4" font-weight="bold">Pluie</text>
</svg>'''
    
    # Sauvegarder les icônes spéciales
    special_icons = [
        ("soleil", sun_svg),
        ("pluie", rain_svg)
    ]
    
    print("\n🎨 Création d'icônes météorologiques spéciales...")
    
    for nom, svg_content in special_icons:
        filepath = images_dir / f"{nom}.svg"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✓ Icône spéciale créée: {nom}.svg")

def main():
    """Fonction principale"""
    print("🖼️  GÉNÉRATEUR D'IMAGES SVG POUR LE LEXIQUE MÉTÉOROLOGIQUE")
    print("=" * 60)
    
    # Générer les images de base
    images_count = generate_basic_images()
    
    # Créer quelques icônes spéciales
    create_weather_icons()
    
    print("\n" + "=" * 60)
    print("🎉 GÉNÉRATION TERMINÉE!")
    print(f"📊 {images_count + 2} images créées au total")
    print("📁 Toutes les images sont dans: docs/images/")
    print("💡 Les images sont de simples SVG avec emojis")
    print("🔄 Vous pouvez les remplacer par de vraies photos si nécessaire")

if __name__ == "__main__":
    main()