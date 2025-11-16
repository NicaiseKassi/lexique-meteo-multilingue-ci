#!/usr/bin/env python3
"""
Script pour extraire les termes météorologiques depuis le PDF
et les intégrer dans le lexique multilingue
"""

import PyPDF2
import pandas as pd
import re
import logging
from pathlib import Path
import json

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def install_required_packages():
    """Installe les packages nécessaires pour l'extraction PDF"""
    try:
        import PyPDF2
        import pandas as pd
        logger.info("✅ Tous les packages sont déjà installés")
        return True
    except ImportError as e:
        logger.info(f"📦 Installation des packages manquants: {e.name}")
        import subprocess
        import sys
        
        packages_to_install = []
        try:
            import PyPDF2
        except ImportError:
            packages_to_install.append('PyPDF2')
        
        try:
            import pandas
        except ImportError:
            packages_to_install.append('pandas')
        
        if packages_to_install:
            for package in packages_to_install:
                try:
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                    logger.info(f"✅ {package} installé avec succès")
                except subprocess.CalledProcessError:
                    logger.error(f"❌ Échec de l'installation de {package}")
                    return False
        return True

def extract_text_from_pdf(pdf_path):
    """Extrait le texte d'un fichier PDF"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            text_content = []
            for page_num, page in enumerate(pdf_reader.pages, 1):
                try:
                    text = page.extract_text()
                    if text.strip():
                        text_content.append({
                            'page': page_num,
                            'text': text
                        })
                        logger.info(f"📄 Page {page_num}: {len(text)} caractères extraits")
                except Exception as e:
                    logger.warning(f"⚠️  Erreur page {page_num}: {e}")
            
            return text_content
    
    except Exception as e:
        logger.error(f"❌ Erreur lors de la lecture du PDF: {e}")
        return None

def parse_meteorological_terms(text_content):
    """Parse le contenu pour extraire les termes météorologiques"""
    all_terms = []
    
    for page_data in text_content:
        text = page_data['text']
        page_num = page_data['page']
        
        # Patterns pour identifier les termes météorologiques
        patterns = [
            # Format: TERME EN FRANÇAIS : traduction_langue
            r'([A-ZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÑÒÓÔÕÖØÙÚÛÜÝ][a-zàáâãäåæçèéêëìíîïñòóôõöøùúûüý\s\-]+)\s*:\s*([^\n]+)',
            # Format: Terme français - Traduction
            r'([A-ZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÑÒÓÔÕÖØÙÚÛÜÝ][a-zàáâãäåæçèéêëìíîïñòóôõöøùúûüý\s\-]+)\s*\-\s*([^\n]+)',
            # Format en tableau
            r'(\b[A-ZÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÑÒÓÔÕÖØÙÚÛÜÝ][a-zàáâãäåæçèéêëìíîïñòóôõöøùúûüý]+(?:\s+[a-zàáâãäåæçèéêëìíîïñòóôõöøùúûüý]+)*)\s+([^\s]+(?:\s+[^\s]+)*)',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text, re.MULTILINE)
            for match in matches:
                if len(match) == 2:
                    french_term = match[0].strip()
                    translation = match[1].strip()
                    
                    # Filtrer les faux positifs
                    if (len(french_term) > 3 and 
                        len(translation) > 2 and 
                        not french_term.isdigit() and
                        not translation.isdigit()):
                        
                        all_terms.append({
                            'french': french_term,
                            'translation': translation,
                            'page': page_num,
                            'pattern': pattern
                        })
    
    logger.info(f"🔍 {len(all_terms)} termes potentiels extraits")
    return all_terms

def identify_language_from_filename(filename):
    """Identifie la langue à partir du nom de fichier"""
    language_map = {
        'baoule': 'baoule',
        'baoulé': 'baoule',
        'bete': 'bete',
        'bété': 'bete',
        'koulango': 'koulango',
        'lobi': 'lobi',
        'malinke': 'malinke',
        'malinké': 'malinke',
        'senoufo': 'senoufo',
        'sénoufo': 'senoufo',
        'yacouba': 'yacouba'
    }
    
    filename_lower = filename.lower()
    for lang_key, lang_code in language_map.items():
        if lang_key in filename_lower:
            return lang_code
    
    return 'unknown'

def process_all_pdfs():
    """Traite tous les PDFs de glossaires pour extraire les termes"""
    docs_dir = Path('DOCS')
    
    # Chercher tous les PDFs de glossaires
    pdf_files = []
    for pattern in ['*glossaire*.pdf', '*Glossaire*.pdf', 'DRAFT_LEXIQUE*.pdf']:
        pdf_files.extend(docs_dir.glob(pattern))
    
    logger.info(f"📚 {len(pdf_files)} fichiers PDF trouvés:")
    for pdf_file in pdf_files:
        logger.info(f"   - {pdf_file.name}")
    
    all_terms_data = {}
    
    for pdf_file in pdf_files:
        logger.info(f"\n🔄 Traitement de: {pdf_file.name}")
        
        # Extraire le texte
        text_content = extract_text_from_pdf(pdf_file)
        if not text_content:
            continue
        
        # Parser les termes
        terms = parse_meteorological_terms(text_content)
        
        if terms:
            # Identifier la langue
            language = identify_language_from_filename(pdf_file.name)
            logger.info(f"🌍 Langue détectée: {language}")
            
            all_terms_data[language] = {
                'file': pdf_file.name,
                'terms': terms,
                'count': len(terms)
            }
            
            # Afficher quelques exemples
            logger.info(f"📝 Exemples de termes extraits:")
            for term in terms[:5]:
                logger.info(f"   {term['french']} → {term['translation']}")
            if len(terms) > 5:
                logger.info(f"   ... et {len(terms) - 5} autres")
    
    return all_terms_data

def organize_terms_by_french_word(all_terms_data):
    """Organise les termes par mot français avec toutes les traductions"""
    organized_terms = {}
    
    # D'abord, collecter tous les termes français uniques
    all_french_terms = set()
    for language, data in all_terms_data.items():
        for term in data['terms']:
            # Nettoyer et normaliser le terme français
            french_clean = term['french'].strip().lower()
            french_clean = re.sub(r'[^\w\s\-]', '', french_clean)  # Supprimer la ponctuation
            all_french_terms.add(french_clean)
    
    logger.info(f"📖 {len(all_french_terms)} termes français uniques identifiés")
    
    # Organiser par terme français
    for french_term in sorted(all_french_terms):
        organized_terms[french_term] = {
            'french': french_term,
            'translations': {},
            'sources': []
        }
        
        # Chercher les traductions dans toutes les langues
        for language, data in all_terms_data.items():
            if language == 'unknown':
                continue
                
            for term in data['terms']:
                french_clean = term['french'].strip().lower()
                french_clean = re.sub(r'[^\w\s\-]', '', french_clean)
                
                if french_clean == french_term:
                    organized_terms[french_term]['translations'][language] = term['translation']
                    organized_terms[french_term]['sources'].append({
                        'file': data['file'],
                        'page': term['page'],
                        'language': language
                    })
    
    # Filtrer les termes qui n'ont que peu de traductions
    filtered_terms = {
        term: data for term, data in organized_terms.items()
        if len(data['translations']) >= 2  # Au moins 2 traductions
    }
    
    logger.info(f"✅ {len(filtered_terms)} termes avec traductions multiples")
    return filtered_terms

def generate_updated_terms_list(organized_terms):
    """Génère une liste de termes mise à jour pour le site"""
    
    # Langues supportées
    languages = ['fr', 'baoule', 'bete', 'koulango', 'lobi', 'malinke', 'senoufo', 'yacouba']
    
    updated_terms = []
    
    for french_term, data in organized_terms.items():
        term_entry = {}
        
        # Terme français (obligatoire)
        term_entry['fr'] = data['french'].title()  # Capitaliser
        
        # Ajouter les traductions disponibles
        for lang in languages[1:]:  # Skip 'fr'
            if lang in data['translations']:
                term_entry[lang] = data['translations'][lang].strip()
            else:
                term_entry[lang] = f"[À traduire en {lang}]"
        
        # Créer un identifiant unique
        term_id = re.sub(r'[^\w\-]', '-', french_term.lower()).strip('-')
        term_entry['id'] = term_id
        
        updated_terms.append(term_entry)
    
    # Trier par ordre alphabétique français
    updated_terms.sort(key=lambda x: x['fr'].lower())
    
    logger.info(f"📊 {len(updated_terms)} termes organisés pour le site")
    return updated_terms

def save_extracted_data(all_terms_data, organized_terms, updated_terms):
    """Sauvegarde toutes les données extraites"""
    
    # 1. Données brutes par fichier
    with open('extracted_terms_raw.json', 'w', encoding='utf-8') as f:
        json.dump(all_terms_data, f, ensure_ascii=False, indent=2)
    
    # 2. Termes organisés par français
    with open('extracted_terms_organized.json', 'w', encoding='utf-8') as f:
        json.dump(organized_terms, f, ensure_ascii=False, indent=2)
    
    # 3. Liste finale pour le site
    with open('extracted_terms_for_site.json', 'w', encoding='utf-8') as f:
        json.dump(updated_terms, f, ensure_ascii=False, indent=2)
    
    # 4. CSV pour analyse
    if updated_terms:
        df = pd.DataFrame(updated_terms)
        df.to_csv('extracted_terms.csv', index=False, encoding='utf-8')
        logger.info("📄 Fichier CSV créé: extracted_terms.csv")
    
    logger.info("💾 Toutes les données sauvegardées")
    
    # 5. Rapport de synthèse
    report = []
    report.append("# RAPPORT D'EXTRACTION DES TERMES MÉTÉOROLOGIQUES")
    report.append("=" * 60)
    report.append(f"\n## RÉSUMÉ")
    report.append(f"- Fichiers PDF traités: {len(all_terms_data)}")
    report.append(f"- Termes extraits au total: {sum(data['count'] for data in all_terms_data.values())}")
    report.append(f"- Termes français uniques: {len(organized_terms)}")
    report.append(f"- Termes avec traductions multiples: {len(updated_terms)}")
    
    report.append(f"\n## LANGUES TRAITÉES")
    for language, data in all_terms_data.items():
        if language != 'unknown':
            report.append(f"- {language.title()}: {data['count']} termes ({data['file']})")
    
    report.append(f"\n## EXEMPLES DE TERMES EXTRAITS")
    for i, term in enumerate(updated_terms[:10], 1):
        report.append(f"{i}. {term['fr']}")
        for lang in ['baoule', 'bete', 'koulango']:
            if lang in term and not '[À traduire' in term[lang]:
                report.append(f"   - {lang}: {term[lang]}")
    
    if len(updated_terms) > 10:
        report.append(f"   ... et {len(updated_terms) - 10} autres termes")
    
    with open('extraction_report.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    logger.info("📋 Rapport d'extraction créé: extraction_report.txt")

def main():
    """Fonction principale"""
    logger.info("🚀 EXTRACTION DES TERMES MÉTÉOROLOGIQUES")
    logger.info("=" * 60)
    
    # Vérifier et installer les packages
    if not install_required_packages():
        logger.error("❌ Impossible d'installer les packages requis")
        return False
    
    # Traiter tous les PDFs
    logger.info("\n📚 TRAITEMENT DES FICHIERS PDF...")
    all_terms_data = process_all_pdfs()
    
    if not all_terms_data:
        logger.error("❌ Aucun terme extrait des PDFs")
        return False
    
    # Organiser les termes
    logger.info("\n🔄 ORGANISATION DES TERMES...")
    organized_terms = organize_terms_by_french_word(all_terms_data)
    
    # Générer la liste finale
    logger.info("\n📝 GÉNÉRATION DE LA LISTE FINALE...")
    updated_terms = generate_updated_terms_list(organized_terms)
    
    # Sauvegarder tout
    logger.info("\n💾 SAUVEGARDE DES DONNÉES...")
    save_extracted_data(all_terms_data, organized_terms, updated_terms)
    
    logger.info("\n" + "=" * 60)
    logger.info("🎉 EXTRACTION TERMINÉE AVEC SUCCÈS!")
    logger.info(f"📊 {len(updated_terms)} termes prêts pour intégration")
    logger.info("📁 Fichiers générés:")
    logger.info("   - extracted_terms_raw.json")
    logger.info("   - extracted_terms_organized.json") 
    logger.info("   - extracted_terms_for_site.json")
    logger.info("   - extracted_terms.csv")
    logger.info("   - extraction_report.txt")
    
    return True

if __name__ == "__main__":
    main()