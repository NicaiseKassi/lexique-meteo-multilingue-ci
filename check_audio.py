#!/usr/bin/env python3
"""
Script pour vérifier et optimiser les fichiers audio pour la compatibilité web
"""

import os
import subprocess
import logging
from pathlib import Path

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_ffmpeg():
    """Vérifie si ffmpeg est disponible"""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        logger.warning("FFmpeg n'est pas installé. Installation recommandée pour optimiser les fichiers audio.")
        return False

def get_audio_info(file_path):
    """Obtient les informations sur un fichier audio"""
    try:
        result = subprocess.run([
            'ffprobe', '-v', 'quiet', '-print_format', 'json', 
            '-show_format', '-show_streams', str(file_path)
        ], capture_output=True, text=True, check=True)
        
        import json
        info = json.loads(result.stdout)
        
        if 'streams' in info and len(info['streams']) > 0:
            stream = info['streams'][0]
            return {
                'codec': stream.get('codec_name', 'unknown'),
                'bitrate': stream.get('bit_rate', 'unknown'),
                'sample_rate': stream.get('sample_rate', 'unknown'),
                'duration': float(stream.get('duration', 0))
            }
    except Exception as e:
        logger.error(f"Erreur lors de l'analyse de {file_path}: {e}")
    
    return None

def optimize_audio_file(input_path, output_path):
    """Optimise un fichier audio pour le web"""
    try:
        # Paramètres optimisés pour le web
        cmd = [
            'ffmpeg', '-i', str(input_path),
            '-codec:a', 'libmp3lame',  # Codec MP3
            '-b:a', '128k',            # Bitrate 128 kbps
            '-ar', '44100',            # Sample rate 44.1 kHz
            '-ac', '2',                # Stéréo
            '-f', 'mp3',               # Format MP3
            '-y',                      # Overwrite
            str(output_path)
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        logger.info(f"✅ Fichier optimisé: {output_path}")
        return True
        
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Erreur lors de l'optimisation de {input_path}: {e.stderr}")
        return False

def check_and_fix_audio_files():
    """Vérifie et corrige les fichiers audio"""
    audio_dir = Path('docs/audio')
    
    if not audio_dir.exists():
        logger.error(f"Dossier audio introuvable: {audio_dir}")
        return False
    
    has_ffmpeg = check_ffmpeg()
    audio_files = list(audio_dir.glob('*.mp3'))
    
    logger.info(f"🔍 Vérification de {len(audio_files)} fichiers audio...")
    
    problematic_files = []
    
    for audio_file in audio_files:
        logger.info(f"📁 Vérification: {audio_file.name}")
        
        # Vérifier la taille du fichier
        file_size = audio_file.stat().st_size
        if file_size < 1000:  # Moins de 1KB
            logger.warning(f"⚠️  Fichier très petit: {audio_file.name} ({file_size} bytes)")
            problematic_files.append(audio_file)
            continue
        
        # Si ffmpeg est disponible, vérifier le format
        if has_ffmpeg:
            info = get_audio_info(audio_file)
            if info:
                logger.info(f"📊 {audio_file.name}: {info['codec']}, {info['bitrate']} bps, {info['duration']:.1f}s")
                
                # Si ce n'est pas du MP3 standard, l'optimiser
                if info['codec'] != 'mp3' or info['bitrate'] == 'unknown':
                    logger.info(f"🔧 Optimisation nécessaire pour: {audio_file.name}")
                    backup_path = audio_file.with_suffix('.mp3.backup')
                    audio_file.rename(backup_path)
                    
                    if optimize_audio_file(backup_path, audio_file):
                        backup_path.unlink()  # Supprimer le backup
                    else:
                        backup_path.rename(audio_file)  # Restaurer le backup
                        problematic_files.append(audio_file)
            else:
                logger.warning(f"⚠️  Impossible d'analyser: {audio_file.name}")
                problematic_files.append(audio_file)
    
    # Résumé
    logger.info(f"\n📊 RÉSUMÉ:")
    logger.info(f"✅ Fichiers audio trouvés: {len(audio_files)}")
    logger.info(f"⚠️  Fichiers problématiques: {len(problematic_files)}")
    
    if problematic_files:
        logger.warning("🚨 Fichiers à vérifier manuellement:")
        for file in problematic_files:
            logger.warning(f"   - {file.name}")
    
    return len(problematic_files) == 0

def create_audio_test_page():
    """Crée une page de test pour les fichiers audio"""
    test_html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Audio - Lexique Météorologique</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .audio-test { margin: 10px 0; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
        .success { background-color: #d4edda; border-color: #c3e6cb; }
        .error { background-color: #f8d7da; border-color: #f5c6cb; }
        audio { width: 100%; margin-top: 5px; }
        button { padding: 5px 10px; margin: 2px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>🎵 Test des Fichiers Audio</h1>
    <p>Cette page permet de tester la lecture de tous les fichiers audio.</p>
    
    <div id="audio-tests"></div>
    
    <script>
        const audioFiles = ["""
    
    # Lister tous les fichiers audio
    audio_dir = Path('docs/audio')
    if audio_dir.exists():
        for audio_file in sorted(audio_dir.glob('*.mp3')):
            test_html += f'\n            "audio/{audio_file.name}",'
    
    test_html += """
        ];
        
        const container = document.getElementById('audio-tests');
        
        audioFiles.forEach((audioFile, index) => {
            if (!audioFile) return;
            
            const div = document.createElement('div');
            div.className = 'audio-test';
            
            const title = document.createElement('h3');
            title.textContent = `Test ${index + 1}: ${audioFile}`;
            div.appendChild(title);
            
            const audio = document.createElement('audio');
            audio.controls = true;
            audio.preload = 'metadata';
            audio.src = audioFile;
            
            const status = document.createElement('p');
            status.textContent = 'Chargement...';
            
            audio.addEventListener('loadeddata', () => {
                status.textContent = '✅ Fichier chargé avec succès';
                status.style.color = 'green';
                div.className += ' success';
            });
            
            audio.addEventListener('error', (e) => {
                const errorCode = e.target.error ? e.target.error.code : 'inconnu';
                status.textContent = `❌ Erreur de chargement (code: ${errorCode})`;
                status.style.color = 'red';
                div.className += ' error';
            });
            
            div.appendChild(audio);
            div.appendChild(status);
            container.appendChild(div);
        });
    </script>
</body>
</html>"""
    
    test_file = Path('docs/test-audio.html')
    test_file.write_text(test_html, encoding='utf-8')
    logger.info(f"📄 Page de test créée: {test_file}")
    return test_file

if __name__ == "__main__":
    logger.info("🎵 VÉRIFICATION DES FICHIERS AUDIO")
    logger.info("=" * 50)
    
    # Vérifier les fichiers audio
    success = check_and_fix_audio_files()
    
    # Créer une page de test
    test_file = create_audio_test_page()
    
    logger.info("\n" + "=" * 50)
    logger.info("🏁 RÉSULTATS:")
    
    if success:
        logger.info("✅ Tous les fichiers audio semblent corrects")
    else:
        logger.warning("⚠️  Certains fichiers audio nécessitent une attention")
    
    logger.info(f"🌐 Page de test disponible: http://127.0.0.1:8000/test-audio.html")
    logger.info("💡 Lancez 'mkdocs serve' et visitez la page de test pour vérifier la lecture audio")