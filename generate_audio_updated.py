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
        'fr': "Abri météorologique",
        'baoule': "Nglo ji sunzunlɛ",
        'bete': "Ñ̀gbliposu tɛnyι",
        'koulango': "dúɡù tɛ́m zɩ́kpàa lɛ̰̀",
        'lobi': "tʰá̰gbá bɔ́",
        'malinke': "wagati ka ji",
        'senoufo': "lǎli su",
        'yacouba': "Tʌ̰̋ŋ̰̋-yààŋ-nàà",
    },
    {
        'fr': "Accalmie",
        'baoule': "Angban sansiɛ",
        'bete': "Nyͻmι klolai",
        'koulango': "ɟéwò pɩ̰̀r sɩ̰̀",
        'lobi': "ɟɛ̀ dɛ̀wɛ̀",
        'malinke': "fɔnyɔn saniya",
        'senoufo': "kafá laɡi",
        'yacouba': "tḛ̋ḛ̋-pɪ̰̋",
    },
    {
        'fr': "Adaptation",
        'baoule': "Akwan bonunlɛ",
        'bete': "Àwɛnsɛnͻ",
        'koulango': "sɔ́ɔ́r tákɷ́",
        'lobi': "gbɛ̀nì",
        'malinke': "ladɔnniya",
        'senoufo': "kanǎn",
        'yacouba': "kàà-sɤ̄-ɓà",
    },
    {
        'fr': "Altitude",
        'baoule': "Nglo sunzunlɛ",
        'bete': "Nǫ̈gbliɛ",
        'koulango': "hálààr kɷ̰̀",
        'lobi': "dò̰ɔ̀r kᵒò",
        'malinke': "kundama ka bɔ kɔgɔji hakεja la",
        'senoufo': "lɔgi tɔnɔnɡama",
        'yacouba': "nū-kàà-sɤ́",
    },
    {
        'fr': "Anticyclone",
        'baoule': "Blɛ kpa",
        'bete': "Gïnyklʋylιpözɛgbälιbhιyenιde",
        'koulango': "jɔ́kɔ̰̀ ɟóflúlémjò dakɔ̰̀",
        'lobi': "pá ʔwé dàwɛ̀",
        'malinke': "wagatibasiginin jɔrɔ",
        'senoufo': "larijánna",
        'yacouba': "tḛ̋ḛ̋-kʌ̄gbɪ̰̋-sɯ̏",
    },
    {
        'fr': "Anémomètre",
        'baoule': "Angban toe",
        'bete': "Nyͻmιpiopionͻyakana",
        'koulango': "ɟéwò bɩ́ɩ́kà zɷ́ŋɔ̰̀",
        'lobi': "ɟɛ̀ mɩ́ɛ́dàà",
        'malinke': "fɔnyɔn telija sumamina",
        'senoufo': "kafálaɡi tumɛ̀nɛ́ yaga",
        'yacouba': "tḛ̋ḛ̋-da-ká-pʌ́",
    },
    {
        'fr': "Arc-en-ciel",
        'baoule': "Nyangoduin",
        'bete': "Lagͻlöbhäbhili",
        'koulango': "ɡláɡlàɡlóɡlò",
        'lobi': "tʰá̰gbákʰàbìr",
        'malinke': "ala ja muru",
        'senoufo': "nyԑn bariwi",
        'yacouba': "ɗáŋ́-tȁ-pȍȍ",
    },
    {
        'fr': "Aride",
        'baoule': "Kee",
        'bete': "Sιɛka",
        'koulango': "hɩ́lɛ̰̀",
        'lobi': "kʰɩ̀ɩ̀",
        'malinke': "ɟalan",
        'senoufo': "nwáà",
        'yacouba': "gbla̰̋a̰̋gblàà",
    },
    {
        'fr': "Atmosphère",
        'baoule': "Angban kpa",
        'bete': "Zlιmönyͻmʋkwë",
        'koulango': "jééɡòmɩ́là ɲɩ́ŋmɔ̰̀",
        'lobi': "ɟɩ̀ɛ̀",
        'malinke': "dugukolo laminili gazi",
        'senoufo': "tԑgi kama",
        'yacouba': "nű-ɤ́kpá-kō-tā",
    },
    {
        'fr': "Aérosol",
        'baoule': "Nglo sunzun titiɛ",
        'bete': "Zlιgbäbä",
        'koulango': "kásà kprɩ́kprɩ̰̀",
        'lobi': "ɟɩ̀ɛ̀ pɔ̀rì",
        'malinke': "fɔnyɔn kɔnɔ finman",
        'senoufo': "kafá kama bɔlɔge",
        'yacouba': "tḛ̋ḛ̋-pɪ̰̋-ɓāā",
    },
    {
        'fr': "Baromètre",
        'baoule': "Sunzun sumanlɛ",
        'bete': "Sιɛkapιopιonͻyakana",
        'koulango': "bɔ́ɔ́ŋɔ̰̀ bɩ́ɩ́kà zɷ́ŋɔ̰̀",
        'lobi': "pá bɩ́ɛ́dàà",
        'malinke': "nakɔ sumamina",
        'senoufo': "tum barometiri",
        'yacouba': "pá-ká-pʌ́",
    },
    {
        'fr': "Brouillard",
        'baoule': "Nyibuolɛ",
        'bete': "Gblógblógblí",
        'koulango': "ɲɩ́ɩ́ŋmɔ̰̀ wūrū",
        'lobi': "ɟɔ̰̀lɔ̰̀pà ɓírə́",
        'malinke': "sumaya",
        'senoufo': "súmaya",
        'yacouba': "ɓū-tíí",
    },
    {
        'fr': "Climat",
        'baoule': "Blɛ kɛlɛ",
        'bete': "Tɛmö",
        'koulango': "dúɡù tɛ́m",
        'lobi': "bɔ́ kʰɛ̀rɛ̀",
        'malinke': "wagati",
        'senoufo': "lǎli",
        'yacouba': "Tʌ̰̋ŋ̰̋",
    },
    {
        'fr': "Cyclone",
        'baoule': "Angban tritrilɛ",
        'bete': "Nyͻmι kädɛgbä",
        'koulango': "ɟéwò kprɩ́kprɩ̰̀ ɡò",
        'lobi': "ɟɛ̀ gbɛ̀là",
        'malinke': "fɔnyɔn belebele",
        'senoufo': "kafá gbɔ́ɔ̀ŋɔ",
        'yacouba': "tḛ̋ḛ̋-kprɛ̰̋",
    },
    {
        'fr': "Humidité",
        'baoule': "Nzue nɛnɛlɛ",
        'bete': "Nyizιmöklólólό",
        'koulango': "mɩ́ɩ̰̀ wūrū sɩ̰̀",
        'lobi': "ɲɷ̀ɔ̀n pɔ̀rì",
        'malinke': "jinunuma",
        'senoufo': "zéʔe kóló",
        'yacouba': "ɗájḭ̋-kō",
    },
    {
        'fr': "Nuage",
        'baoule': "Nyanmien",
        'bete': "Ylimönyuzl",
        'koulango': "jɔ́kɔ̰̀",
        'lobi': "tʰá̰gbá",
        'malinke': "kabanɔgɔ",
        'senoufo': "fafaán",
        'yacouba': "ɗűű",
    },
    {
        'fr': "Pluie",
        'baoule': "Nzue",
        'bete': "Nyizi",
        'koulango': "mɩ́ɩ̰̀",
        'lobi': "ɲɷ̀ɔ̀n",
        'malinke': "ji",
        'senoufo': "zéʔe",
        'yacouba': "ɗájḭ̋",
    },
    {
        'fr': "Soleil",
        'baoule': "Awia",
        'bete': "Cie",
        'koulango': "ɡbrékò",
        'lobi': "wìr",
        'malinke': "tile",
        'senoufo': "tchang",
        'yacouba': "jʌ́",
    },
    {
        'fr': "Sécheresse",
        'baoule': "Ketelɛ",
        'bete': "Sιɛkagbä",
        'koulango': "hɩ́lɛ́ɡɛ̰̀",
        'lobi': "kʰéwé",
        'malinke': "jaalan",
        'senoufo': "wama tɛʔɛ",
        'yacouba': "ɗá-ja̰̋a̰̋-ba-ɗɛ̄ɛ̄-ɓà",
    },
    {
        'fr': "Température",
        'baoule': "Blɛ fanu",
        'bete': "Tɛmιka",
        'koulango': "bén bà̰ lɔ́m",
        'lobi': "pá ʔwii",
        'malinke': "kalaje",
        'senoufo': "lǎli kama",
        'yacouba': "tʌ̰̋ŋ̰̋-kʌ̄sɯ̄",
    },
    {
        'fr': "Vent",
        'baoule': "Angban",
        'bete': "Nyͻmι",
        'koulango': "ɟéwò",
        'lobi': "ɟɛ̀",
        'malinke': "fɔnyɔn",
        'senoufo': "kafá",
        'yacouba': "tḛ̋ḛ̋",
    },
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
        terme_fr = terme_data["fr"]
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
        for code_langue in ['baoule', 'bete', 'koulango', 'lobi', 'malinke', 'senoufo', 'yacouba']:
            if code_langue in terme_data:
                traduction = terme_data[code_langue]
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