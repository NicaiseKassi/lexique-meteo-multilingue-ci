#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de génération automatique des fichiers audio
pour le lexique météorologique multilingue avec gTTS.

Auteur: SODEXAM - Côte d'Ivoire
Date: Novembre 2024
"""

import os
import re
import time
from gtts import gTTS
from typing import Dict, List

# Configuration des langues avec codes ISO pour gTTS
LANGUES_CONFIG = {
    'fr': {
        'nom': 'français',
        'code_gtts': 'fr',
        'tld': 'fr'
    },
    'baoule': {
        'nom': 'baoulé', 
        'code_gtts': 'fr',  # Utilisation du français comme approximation
        'tld': 'fr'
    },
    'bete': {
        'nom': 'bété',
        'code_gtts': 'fr',
        'tld': 'fr'
    },
    'lobi': {
        'nom': 'lobi',
        'code_gtts': 'fr',
        'tld': 'fr'
    },
    'malinke': {
        'nom': 'malinké',
        'code_gtts': 'fr',
        'tld': 'fr'
    },
    'senoufo': {
        'nom': 'sénoufo',
        'code_gtts': 'fr',
        'tld': 'fr'
    },
    'koulango': {
        'nom': 'koulango',
        'code_gtts': 'fr',
        'tld': 'fr'
    },
    'yacouba': {
        'nom': 'yacouba',
        'code_gtts': 'fr',
        'tld': 'fr'
    }
}

# Données exemple du lexique météorologique
# TODO: Remplacer par l'extraction automatique du PDF
TERMES_METEO = [
    {
        "terme_fr": "Abri météo",
        "definition_fr": "Petite cage blanche contenant des instruments météo",
        "traductions": {
            "baoule": "blɛ amanniɛn sua",
            "bete": "ɔnun alaka",
            "lobi": "meteolinɛnιköbhänιde",
            "malinke": "bɔ́hín tʰɩ̰́ tʰɩ̀ɩ̀n pár",
            "senoufo": "wagati ɟateminanso",
            "koulango": "Kpapilé nì be lǎli kama yabàra",
            "yacouba": "cɛ́ɛ lè tɛ́m ɡɷ̰ ́ɷ̰ ̀ mɩ̰́rɩ́ɡɔ̀ ɡbúkò"
        }
    },
    {
        "terme_fr": "Accalmie",
        "definition_fr": "Période de calme entre deux tempêtes",
        "traductions": {
            "baoule": "sɛmɛntrɛ kɔlɔ",
            "bete": "gbɛ̀gbɛ́ sù",
            "lobi": "thεεrinεthiιle",
            "malinke": "sáɓátɩ́ kɔ̀ɔ̀",
            "senoufo": "kɛlɛɛ sɛnɛ",
            "koulango": "gbàgbà sálì",
            "yacouba": "wɛ̀ɛ́ ɓlà"
        }
    },
    {
        "terme_fr": "Adaptation",
        "definition_fr": "Ajustement aux changements climatiques",
        "traductions": {
            "baoule": "mi tɛ kpokpo",
            "bete": "yíyɛ̀ gbɛ́ɛ̀",
            "lobi": "daabiitine",
            "malinke": "làmɩ̀n tʰɩ́ɩ̀",
            "senoufo": "ɲɛlɛɛ kɛɛ",
            "koulango": "fálì bàrà",
            "yacouba": "dɩ́à ɓɛ́"
        }
    },
    {
        "terme_fr": "Aérosol",
        "definition_fr": "Petites particules dans l'air",
        "traductions": {
            "baoule": "nfiε kεsε",
            "bete": "fìfì pɛ̀lɛ̀",
            "lobi": "cεεlinεsible",
            "malinke": "fɩ̀n kàlà",
            "senoufo": "fɛɛrɛ sɛɛ",
            "koulango": "fífì yàrà",
            "yacouba": "fɛ̀ɛ́ kpà"
        }
    },
    {
        "terme_fr": "Altitude",
        "definition_fr": "Hauteur par rapport au niveau de la mer",
        "traductions": {
            "baoule": "kɔkɔ yɛlɛ",
            "bete": "kòlò yɛ̀lɛ̀",
            "lobi": "būgbulile",
            "malinke": "kɔ̀ɔ̀ yálɛ́",
            "senoufo": "kuluu yɛlɛ",
            "koulango": "kúlú yàlì",
            "yacouba": "kɔ̀ɔ́ yɛ̀"
        }
    }
]

def slugify(text: str) -> str:
    """
    Convertit un texte en slug pour les noms de fichiers.
    
    Args:
        text (str): Le texte à convertir
        
    Returns:
        str: Le slug généré (URL-safe, sans accents, minuscules)
    """
    # Remplacer les caractères accentués
    text = text.lower()
    text = re.sub(r'[àâäá]', 'a', text)
    text = re.sub(r'[éèêë]', 'e', text)
    text = re.sub(r'[îïí]', 'i', text)
    text = re.sub(r'[ôöó]', 'o', text)
    text = re.sub(r'[ùûüú]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    # Remplacer les espaces et caractères spéciaux par des tirets
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Supprimer les tirets en début et fin
    text = text.strip('-')
    
    return text

def generer_audio_terme(terme: str, langue: str, slug: str, audio_dir: str) -> bool:
    """
    Génère un fichier audio MP3 pour un terme dans une langue donnée.
    
    Args:
        terme (str): Le terme à prononcer
        langue (str): Code de la langue
        slug (str): Slug du terme pour le nom de fichier
        audio_dir (str): Répertoire de destination
        
    Returns:
        bool: True si succès, False sinon
    """
    try:
        # Configuration de la langue pour gTTS
        config_langue = LANGUES_CONFIG[langue]
        
        # Créer l'objet gTTS
        tts = gTTS(
            text=terme,
            lang=config_langue['code_gtts'],
            tld=config_langue['tld'],
            slow=False
        )
        
        # Nom du fichier audio
        nom_fichier = f"{slug}_{langue}.mp3"
        chemin_fichier = os.path.join(audio_dir, nom_fichier)
        
        # Sauvegarder le fichier audio
        tts.save(chemin_fichier)
        
        print(f"   ✓ Audio généré: {nom_fichier}")
        return True
        
    except Exception as e:
        print(f"   ✗ Erreur pour {terme} ({langue}): {str(e)}")
        return False

def generer_tous_audios() -> None:
    """
    Génère tous les fichiers audio pour tous les termes et toutes les langues.
    """
    # Créer le répertoire audio s'il n'existe pas
    audio_dir = os.path.join("docs", "audio")
    os.makedirs(audio_dir, exist_ok=True)
    
    print("🎵 Génération des fichiers audio pour le lexique météorologique")
    print(f"📁 Répertoire de destination: {audio_dir}")
    print(f"📊 {len(TERMES_METEO)} termes × {len(LANGUES_CONFIG)} langues = {len(TERMES_METEO) * len(LANGUES_CONFIG)} fichiers à générer")
    print("-" * 70)
    
    total_generes = 0
    total_erreurs = 0
    
    for i, terme_data in enumerate(TERMES_METEO, 1):
        terme_fr = terme_data["terme_fr"]
        slug = slugify(terme_fr)
        
        print(f"[{i:2d}/{len(TERMES_METEO)}] 🌤️  {terme_fr}")
        
        # Générer l'audio pour le français
        if generer_audio_terme(terme_fr, 'fr', slug, audio_dir):
            total_generes += 1
        else:
            total_erreurs += 1
        
        # Petite pause pour éviter la surcharge de l'API
        time.sleep(0.2)
        
        # Générer l'audio pour toutes les traductions
        for code_langue, traduction in terme_data["traductions"].items():
            if generer_audio_terme(traduction, code_langue, slug, audio_dir):
                total_generes += 1
            else:
                total_erreurs += 1
            
            # Petite pause pour éviter la surcharge de l'API
            time.sleep(0.2)
        
        print()  # Ligne vide entre les termes
    
    print("=" * 70)
    print(f"📈 Résumé de la génération:")
    print(f"   ✓ Fichiers générés avec succès: {total_generes}")
    if total_erreurs > 0:
        print(f"   ✗ Erreurs rencontrées: {total_erreurs}")
    else:
        print(f"   🎉 Aucune erreur!")
    print(f"   📁 Fichiers disponibles dans: {audio_dir}")

def verifier_internet() -> bool:
    """
    Vérifie si une connexion Internet est disponible.
    
    Returns:
        bool: True si connecté, False sinon
    """
    try:
        import requests
        response = requests.get("https://www.google.com", timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    """Fonction principale du script."""
    print("🌍 Lexique Météorologique Multilingue - Générateur Audio")
    print("💡 Développé par SODEXAM - Côte d'Ivoire")
    print("=" * 70)
    
    # Vérifier la connexion Internet
    print("🌐 Vérification de la connexion Internet...")
    if not verifier_internet():
        print("❌ ERREUR: Connexion Internet requise pour utiliser gTTS!")
        print("   Veuillez vérifier votre connexion et réessayer.")
        return
    else:
        print("✅ Connexion Internet OK")
    
    print()
    
    try:
        generer_tous_audios()
        print("\n🎉 Génération terminée avec succès!")
        print("\n📝 Étapes suivantes:")
        print("   1. Vérifiez les fichiers dans docs/audio/")
        print("   2. Exécutez generate_pages.py pour créer les pages")
        print("   3. Testez avec: mkdocs serve")
        
    except KeyboardInterrupt:
        print("\n⏹️  Génération interrompue par l'utilisateur.")
    except Exception as e:
        print(f"\n❌ Erreur inattendue: {str(e)}")
        print("   Veuillez vérifier votre configuration et réessayer.")

if __name__ == "__main__":
    main()