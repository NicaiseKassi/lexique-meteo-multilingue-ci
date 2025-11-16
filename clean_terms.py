#!/usr/bin/env python3
"""
Script pour nettoyer et créer une liste propre de termes météorologiques
à partir des données extraites et des termes existants
"""

import json
import logging
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_clean_meteorological_terms():
    """Retourne une liste propre de termes météorologiques essentiels"""
    
    # Termes existants (déjà validés)
    existing_terms = [
        {
            "fr": "Abri météorologique",
            "baoule": "Nglo ji sunzunlɛ",
            "bete": "Ñ̀gbliposu tɛnyι",
            "koulango": "dúɡù tɛ́m zɩ́kpàa lɛ̰̀",
            "lobi": "tʰá̰gbá bɔ́",
            "malinke": "wagati ka ji",
            "senoufo": "lǎli su",
            "yacouba": "Tʌ̰̋ŋ̰̋-yààŋ-nàà"
        },
        {
            "fr": "Accalmie",
            "baoule": "Angban sansiɛ",
            "bete": "Nyͻmι klolai",
            "koulango": "ɟéwò pɩ̰̀r sɩ̰̀",
            "lobi": "ɟɛ̀ dɛ̀wɛ̀",
            "malinke": "fɔnyɔn saniya",
            "senoufo": "kafá laɡi",
            "yacouba": "tḛ̋ḛ̋-pɪ̰̋"
        },
        {
            "fr": "Adaptation",
            "baoule": "Akwan bonunlɛ",
            "bete": "Àwɛnsɛnͻ",
            "koulango": "sɔ́ɔ́r tákɷ́",
            "lobi": "gbɛ̀nì",
            "malinke": "ladɔnniya",
            "senoufo": "kanǎn",
            "yacouba": "kàà-sɤ̄-ɓà"
        },
        {
            "fr": "Aérosol",
            "baoule": "Nglo sunzun titiɛ",
            "bete": "Zlιgbäbä",
            "koulango": "kásà kprɩ́kprɩ̰̀",
            "lobi": "ɟɩ̀ɛ̀ pɔ̀rì",
            "malinke": "fɔnyɔn kɔnɔ finman",
            "senoufo": "kafá kama bɔlɔge",
            "yacouba": "tḛ̋ḛ̋-pɪ̰̋-ɓāā"
        },
        {
            "fr": "Altitude",
            "baoule": "Nglo sunzunlɛ",
            "bete": "Nǫ̈gbliɛ",
            "koulango": "hálààr kɷ̰̀",
            "lobi": "dò̰ɔ̀r kᵒò",
            "malinke": "kundama ka bɔ kɔgɔji hakεja la",
            "senoufo": "lɔgi tɔnɔnɡama",
            "yacouba": "nū-kàà-sɤ́"
        },
        {
            "fr": "Baromètre",
            "baoule": "Sunzun sumanlɛ",
            "bete": "Sιɛkapιopιonͻyakana",
            "koulango": "bɔ́ɔ́ŋɔ̰̀ bɩ́ɩ́kà zɷ́ŋɔ̰̀",
            "lobi": "pá bɩ́ɛ́dàà",
            "malinke": "nakɔ sumamina",
            "senoufo": "tum barometiri",
            "yacouba": "pá-ká-pʌ́"
        },
        {
            "fr": "Brouillard",
            "baoule": "Nyibuolɛ",
            "bete": "Gblógblógblí",
            "koulango": "ɲɩ́ɩ́ŋmɔ̰̀ wūrū",
            "lobi": "ɟɔ̰̀lɔ̰̀pà ɓírə́",
            "malinke": "sumaya",
            "senoufo": "súmaya",
            "yacouba": "ɓū-tíí"
        },
        {
            "fr": "Climat",
            "baoule": "Blɛ kɛlɛ",
            "bete": "Tɛmö",
            "koulango": "dúɡù tɛ́m",
            "lobi": "bɔ́ kʰɛ̀rɛ̀",  
            "malinke": "wagati",
            "senoufo": "lǎli",
            "yacouba": "Tʌ̰̋ŋ̰̋"
        },
        {
            "fr": "Cyclone",
            "baoule": "Angban tritrilɛ",
            "bete": "Nyͻmι kädɛgbä",
            "koulango": "ɟéwò kprɩ́kprɩ̰̀ ɡò",
            "lobi": "ɟɛ̀ gbɛ̀là",
            "malinke": "fɔnyɔn belebele",
            "senoufo": "kafá gbɔ́ɔ̀ŋɔ",
            "yacouba": "tḛ̋ḛ̋-kprɛ̰̋"
        }
    ]
    
    # Nouveaux termes essentiels à ajouter (basés sur l'extraction)
    new_essential_terms = [
        {
            "fr": "Anticyclone",
            "baoule": "Blɛ kpa",
            "bete": "Gïnyklʋylιpözɛgbälιbhιyenιde", 
            "koulango": "jɔ́kɔ̰̀ ɟóflúlémjò dakɔ̰̀",
            "lobi": "pá ʔwé dàwɛ̀",
            "malinke": "wagatibasiginin jɔrɔ",
            "senoufo": "larijánna",
            "yacouba": "tḛ̋ḛ̋-kʌ̄gbɪ̰̋-sɯ̏"
        },
        {
            "fr": "Anémomètre", 
            "baoule": "Angban toe",
            "bete": "Nyͻmιpiopionͻyakana",
            "koulango": "ɟéwò bɩ́ɩ́kà zɷ́ŋɔ̰̀",
            "lobi": "ɟɛ̀ mɩ́ɛ́dàà",
            "malinke": "fɔnyɔn telija sumamina",
            "senoufo": "kafálaɡi tumɛ̀nɛ́ yaga",
            "yacouba": "tḛ̋ḛ̋-da-ká-pʌ́"
        },
        {
            "fr": "Atmosphère",
            "baoule": "Angban kpa",
            "bete": "Zlιmönyͻmʋkwë", 
            "koulango": "jééɡòmɩ́là ɲɩ́ŋmɔ̰̀",
            "lobi": "ɟɩ̀ɛ̀",
            "malinke": "dugukolo laminili gazi",
            "senoufo": "tԑgi kama",
            "yacouba": "nű-ɤ́kpá-kō-tā"
        },
        {
            "fr": "Aride",
            "baoule": "Kee",
            "bete": "Sιɛka",
            "koulango": "hɩ́lɛ̰̀",
            "lobi": "kʰɩ̀ɩ̀",
            "malinke": "ɟalan",
            "senoufo": "nwáà",
            "yacouba": "gbla̰̋a̰̋gblàà"
        },
        {
            "fr": "Arc-en-ciel",
            "baoule": "Nyangoduin",
            "bete": "Lagͻlöbhäbhili",
            "koulango": "ɡláɡlàɡlóɡlò",
            "lobi": "tʰá̰gbákʰàbìr",
            "malinke": "ala ja muru",
            "senoufo": "nyԑn bariwi",
            "yacouba": "ɗáŋ́-tȁ-pȍȍ"
        },
        {
            "fr": "Température",
            "baoule": "Blɛ fanu",
            "bete": "Tɛmιka",
            "koulango": "bén bà̰ lɔ́m",
            "lobi": "pá ʔwii",
            "malinke": "kalaje",
            "senoufo": "lǎli kama",
            "yacouba": "tʌ̰̋ŋ̰̋-kʌ̄sɯ̄"
        },
        {
            "fr": "Pluie",
            "baoule": "Nzue",
            "bete": "Nyizi",
            "koulango": "mɩ́ɩ̰̀",
            "lobi": "ɲɷ̀ɔ̀n",
            "malinke": "ji",
            "senoufo": "zéʔe",
            "yacouba": "ɗájḭ̋"
        },
        {
            "fr": "Vent",
            "baoule": "Angban",
            "bete": "Nyͻmι",
            "koulango": "ɟéwò",
            "lobi": "ɟɛ̀",
            "malinke": "fɔnyɔn",
            "senoufo": "kafá",
            "yacouba": "tḛ̋ḛ̋"
        },
        {
            "fr": "Nuage",
            "baoule": "Nyanmien",
            "bete": "Ylimönyuzl",
            "koulango": "jɔ́kɔ̰̀",
            "lobi": "tʰá̰gbá",
            "malinke": "kabanɔgɔ",
            "senoufo": "fafaán",
            "yacouba": "ɗűű"
        },
        {
            "fr": "Soleil",
            "baoule": "Awia",
            "bete": "Cie",
            "koulango": "ɡbrékò",
            "lobi": "wìr",
            "malinke": "tile",
            "senoufo": "tchang",
            "yacouba": "jʌ́"
        },
        {
            "fr": "Humidité",
            "baoule": "Nzue nɛnɛlɛ",
            "bete": "Nyizιmöklólólό",
            "koulango": "mɩ́ɩ̰̀ wūrū sɩ̰̀",
            "lobi": "ɲɷ̀ɔ̀n pɔ̀rì",
            "malinke": "jinunuma",
            "senoufo": "zéʔe kóló",
            "yacouba": "ɗájḭ̋-kō"
        },
        {
            "fr": "Sécheresse",
            "baoule": "Ketelɛ",
            "bete": "Sιɛkagbä",
            "koulango": "hɩ́lɛ́ɡɛ̰̀",
            "lobi": "kʰéwé",
            "malinke": "jaalan",
            "senoufo": "wama tɛʔɛ",
            "yacouba": "ɗá-ja̰̋a̰̋-ba-ɗɛ̄ɛ̄-ɓà"
        }
    ]
    
    # Combiner tous les termes
    all_terms = existing_terms + new_essential_terms
    
    # Ajouter des IDs uniques et trier par ordre alphabétique
    for term in all_terms:
        # Créer un ID basé sur le terme français
        term_id = term['fr'].lower()
        term_id = term_id.replace(' ', '-').replace('é', 'e').replace('è', 'e')
        term_id = term_id.replace('à', 'a').replace('ç', 'c').replace('ô', 'o')
        term_id = ''.join(c for c in term_id if c.isalnum() or c == '-')
        term['id'] = term_id
    
    # Trier par ordre alphabétique français
    all_terms.sort(key=lambda x: x['fr'].lower())
    
    return all_terms

def update_generate_audio_script(terms_list):
    """Met à jour le script generate_audio.py avec la nouvelle liste de termes"""
    
    # Créer le code Python pour la liste des termes
    terms_code = "TERMES_METEO = [\n"
    
    for term in terms_list:
        terms_code += "    {\n"
        for lang in ['fr', 'baoule', 'bete', 'koulango', 'lobi', 'malinke', 'senoufo', 'yacouba']:
            if lang in term:
                # Échapper les guillemets dans les traductions
                translation = term[lang].replace('"', '\\"').replace("'", "\\'")
                terms_code += f"        '{lang}': \"{translation}\",\n"
        terms_code += "    },\n"
    
    terms_code += "]\n"
    
    # Lire le fichier actuel
    with open('generate_audio.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remplacer la liste existante
    import re
    pattern = r'TERMES_METEO = \[.*?\]'
    new_content = re.sub(pattern, terms_code.rstrip(), content, flags=re.DOTALL)
    
    # Sauvegarder le fichier mis à jour
    with open('generate_audio_updated.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    logger.info(f"✅ Script generate_audio_updated.py créé avec {len(terms_list)} termes")

def update_generate_pages_script(terms_list):
    """Met à jour le script generate_pages.py avec la nouvelle liste"""
    
    # Créer le code Python pour la liste des termes (même format)
    terms_code = "TERMES_METEO = [\n"
    
    for term in terms_list:
        terms_code += "    {\n"
        for lang in ['fr', 'baoule', 'bete', 'koulango', 'lobi', 'malinke', 'senoufo', 'yacouba']:
            if lang in term:
                # Échapper les guillemets dans les traductions
                translation = term[lang].replace('"', '\\"').replace("'", "\\'")
                terms_code += f"        '{lang}': \"{translation}\",\n"
        terms_code += "    },\n"
    
    terms_code += "]\n"
    
    # Lire le fichier actuel
    with open('generate_pages.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remplacer la liste existante
    import re
    pattern = r'TERMES_METEO = \[.*?\]'
    new_content = re.sub(pattern, terms_code.rstrip(), content, flags=re.DOTALL)
    
    # Sauvegarder le fichier mis à jour
    with open('generate_pages_updated.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    logger.info(f"✅ Script generate_pages_updated.py créé avec {len(terms_list)} termes")

def create_terms_summary(terms_list):
    """Crée un résumé des termes pour validation"""
    
    summary = []
    summary.append("# LEXIQUE MÉTÉOROLOGIQUE MULTILINGUE - TERMES FINALISÉS")
    summary.append("=" * 70)
    summary.append(f"\n## STATISTIQUES")
    summary.append(f"- Nombre total de termes: {len(terms_list)}")
    summary.append(f"- Langues supportées: 8 (Français + 7 langues locales)")
    summary.append(f"- Fichiers audio à générer: {len(terms_list) * 8}")
    
    # Grouper par première lettre
    letters = {}
    for term in terms_list:
        first_letter = term['fr'][0].upper()
        if first_letter not in letters:
            letters[first_letter] = []
        letters[first_letter].append(term)
    
    summary.append(f"\n## RÉPARTITION PAR LETTRES")
    for letter in sorted(letters.keys()):
        summary.append(f"- {letter}: {len(letters[letter])} termes")
    
    summary.append(f"\n## LISTE COMPLÈTE DES TERMES")
    summary.append("-" * 50)
    
    for i, term in enumerate(terms_list, 1):
        summary.append(f"\n{i:2d}. **{term['fr']}** (ID: `{term['id']}`)")
        summary.append("    Traductions:")
        for lang in ['baoule', 'bete', 'koulango', 'lobi', 'malinke', 'senoufo', 'yacouba']:
            if lang in term:
                # Limiter la longueur pour la lisibilité
                translation = term[lang][:50] + "..." if len(term[lang]) > 50 else term[lang]
                summary.append(f"    - {lang.title()}: {translation}")
    
    summary.append(f"\n## PROCHAINES ÉTAPES")
    summary.append("1. Valider les traductions avec les linguistes")
    summary.append("2. Générer les fichiers audio avec gTTS")
    summary.append("3. Créer les pages MkDocs")
    summary.append("4. Tester le site web")
    summary.append("5. Déployer sur GitHub Pages")
    
    # Sauvegarder le résumé
    with open('terms_summary.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(summary))
    
    logger.info("📋 Résumé créé: terms_summary.md")

def main():
    """Fonction principale"""
    logger.info("🧹 NETTOYAGE ET ORGANISATION DES TERMES MÉTÉOROLOGIQUES")
    logger.info("=" * 70)
    
    # Obtenir la liste propre des termes
    logger.info("📝 Création de la liste des termes essentiels...")
    clean_terms = get_clean_meteorological_terms()
    
    logger.info(f"✅ {len(clean_terms)} termes organisés")
    
    # Sauvegarder la liste finale
    with open('clean_meteorological_terms.json', 'w', encoding='utf-8') as f:
        json.dump(clean_terms, f, ensure_ascii=False, indent=2)
    
    logger.info("💾 Liste sauvegardée: clean_meteorological_terms.json")
    
    # Mettre à jour les scripts
    logger.info("🔄 Mise à jour des scripts...")
    update_generate_audio_script(clean_terms)
    update_generate_pages_script(clean_terms)
    
    # Créer le résumé
    logger.info("📊 Création du résumé...")
    create_terms_summary(clean_terms)
    
    logger.info("\n" + "=" * 70)
    logger.info("🎉 NETTOYAGE TERMINÉ AVEC SUCCÈS!")
    logger.info("📁 Fichiers créés:")
    logger.info("   - clean_meteorological_terms.json")
    logger.info("   - generate_audio_updated.py")
    logger.info("   - generate_pages_updated.py")
    logger.info("   - terms_summary.md")
    logger.info("\n💡 Utilisez les scripts *_updated.py pour régénérer le site")
    
    return True

if __name__ == "__main__":
    main()