/**
 * Lecteur audio interactif pour le lexique météorologique multilingue
 * 
 * Fonctionnalités:
 * - Boutons audio avec feedback visuel
 * - Lecture automatique des prononciations
 * - Gestion des erreurs audio
 * - Arrêt automatique des autres lectures
 * 
 * Auteur: SODEXAM - Côte d'Ivoire
 * Date: Novembre 2024
 */

// Configuration globale
const AUDIO_CONFIG = {
    volume: 0.8,
    playbackRate: 1.0,
    preloadStrategy: 'metadata'
};

// Variables globales
let currentAudio = null;
let currentButton = null;

/**
 * Initialise le système de lecture audio au chargement de la page
 */
function initAudioSystem() {
    console.log('🎵 Initialisation du système audio du lexique météorologique');
    
    // Attendre que le DOM soit complètement chargé
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setupAudioButtons);
    } else {
        setupAudioButtons();
    }
}

/**
 * Configure tous les boutons audio de la page
 */
function setupAudioButtons() {
    const audioButtons = document.querySelectorAll('.audio-btn');
    
    console.log(`🔊 ${audioButtons.length} boutons audio détectés`);
    
    if (audioButtons.length === 0) {
        console.warn('⚠️ Aucun bouton audio trouvé sur cette page');
        return;
    }
    
    audioButtons.forEach((button, index) => {
        setupSingleAudioButton(button, index);
    });
    
    // Ajouter un gestionnaire global pour arrêter l'audio avec Escape
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && currentAudio) {
            stopCurrentAudio();
        }
    });
    
    console.log('✅ Système audio initialisé avec succès');
}

/**
 * Configure un bouton audio individuel
 * @param {HTMLElement} button - Le bouton audio
 * @param {number} index - Index du bouton (pour debug)
 */
function setupSingleAudioButton(button, index) {
    const audioSrc = button.getAttribute('data-audio');
    
    if (!audioSrc) {
        console.warn(`⚠️ Bouton ${index}: Pas de source audio (data-audio manquant)`);
        button.disabled = true;
        button.title = "Audio non disponible";
        return;
    }
    
    // Ajouter les attributs d'accessibilité
    button.setAttribute('role', 'button');
    button.setAttribute('aria-label', `Écouter la prononciation`);
    
    // Gestionnaire de clic
    button.addEventListener('click', (event) => {
        event.preventDefault();
        playAudio(audioSrc, button);
    });
    
    // Gestionnaire de survol pour précharger (optionnel)
    button.addEventListener('mouseenter', () => {
        preloadAudio(audioSrc);
    });
    
    // Support clavier (Entrée et Espace)
    button.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            playAudio(audioSrc, button);
        }
    });
    
    console.log(`✓ Bouton ${index} configuré: ${audioSrc}`);
}

/**
 * Précharge un fichier audio (améliore la réactivité)
 * @param {string} src - Source du fichier audio
 */
function preloadAudio(src) {
    // Créer un audio temporaire pour le préchargement
    const tempAudio = new Audio();
    tempAudio.preload = 'metadata';
    tempAudio.src = src;
    
    // Libérer la mémoire après le préchargement
    tempAudio.addEventListener('loadedmetadata', () => {
        tempAudio.remove();
    });
}

/**
 * Joue un fichier audio avec feedback visuel
 * @param {string} src - Source du fichier audio
 * @param {HTMLElement} button - Bouton déclencheur
 */
async function playAudio(src, button) {
    try {
        // Arrêter toute lecture en cours
        stopCurrentAudio();
        
        // Vérifier que la source existe
        if (!src) {
            throw new Error('Source audio manquante');
        }
        
        // Désactiver le bouton pendant le chargement
        setButtonState(button, 'loading');
        
        // Créer l'élément audio
        const audio = new Audio();
        audio.src = src;
        audio.volume = AUDIO_CONFIG.volume;
        audio.playbackRate = AUDIO_CONFIG.playbackRate;
        audio.preload = AUDIO_CONFIG.preloadStrategy;
        
        // Stocker les références globales
        currentAudio = audio;
        currentButton = button;
        
        // Gestionnaires d'événements audio
        audio.addEventListener('canplay', () => {
            setButtonState(button, 'ready');
        });
        
        audio.addEventListener('play', () => {
            setButtonState(button, 'playing');
            console.log(`▶️ Lecture: ${src}`);
        });
        
        audio.addEventListener('ended', () => {
            setButtonState(button, 'default');
            cleanupAudio();
            console.log(`⏹️ Fin: ${src}`);
        });
        
        audio.addEventListener('error', (event) => {
            console.error(`❌ Erreur audio: ${src}`, event);
            setButtonState(button, 'error');
            showErrorMessage(`Impossible de lire le fichier audio: ${src}`);
            cleanupAudio();
        });
        
        // Lancer la lecture
        await audio.play();
        
    } catch (error) {
        console.error('❌ Erreur lors de la lecture audio:', error);
        setButtonState(button, 'error');
        
        if (error.name === 'NotAllowedError') {
            showErrorMessage('Lecture audio bloquée. Cliquez pour permettre l\'audio.');
        } else if (error.name === 'NotSupportedError') {
            showErrorMessage('Format audio non supporté par votre navigateur.');
        } else {
            showErrorMessage('Erreur de lecture audio. Vérifiez votre connexion.');
        }
        
        cleanupAudio();
    }
}

/**
 * Arrête la lecture audio en cours
 */
function stopCurrentAudio() {
    if (currentAudio) {
        currentAudio.pause();
        currentAudio.currentTime = 0;
        
        if (currentButton) {
            setButtonState(currentButton, 'default');
        }
        
        cleanupAudio();
    }
}

/**
 * Nettoie les références audio globales
 */
function cleanupAudio() {
    if (currentAudio) {
        currentAudio.remove();
        currentAudio = null;
    }
    currentButton = null;
}

/**
 * Définit l'état visuel d'un bouton audio
 * @param {HTMLElement} button - Le bouton à modifier
 * @param {string} state - L'état ('default', 'loading', 'ready', 'playing', 'error')
 */
function setButtonState(button, state) {
    // Supprimer toutes les classes d'état existantes
    button.classList.remove('loading', 'ready', 'playing', 'error');
    
    // Restaurer le contenu par défaut
    if (!button.dataset.originalContent) {
        button.dataset.originalContent = button.innerHTML;
    }
    
    switch (state) {
        case 'loading':
            button.classList.add('loading');
            button.innerHTML = '⏳';
            button.disabled = true;
            button.title = 'Chargement de l\'audio...';
            break;
            
        case 'ready':
            button.classList.add('ready');
            button.innerHTML = '🔊';
            button.disabled = false;
            button.title = 'Cliquez pour écouter';
            break;
            
        case 'playing':
            button.classList.add('playing');
            button.innerHTML = '⏸️';
            button.disabled = false;
            button.title = 'Lecture en cours... (Cliquez pour arrêter)';
            
            // Permettre d'arrêter la lecture en cliquant à nouveau
            const stopHandler = (event) => {
                event.preventDefault();
                stopCurrentAudio();
                button.removeEventListener('click', stopHandler);
            };
            button.addEventListener('click', stopHandler);
            break;
            
        case 'error':
            button.classList.add('error');
            button.innerHTML = '❌';
            button.disabled = false;
            button.title = 'Erreur audio - Cliquez pour réessayer';
            
            // Permettre de réessayer après une erreur
            setTimeout(() => {
                if (button.classList.contains('error')) {
                    setButtonState(button, 'default');
                }
            }, 3000);
            break;
            
        default: // 'default'
            button.innerHTML = button.dataset.originalContent || '🔊';
            button.disabled = false;
            button.title = 'Cliquez pour écouter la prononciation';
            break;
    }
}

/**
 * Affiche un message d'erreur temporaire
 * @param {string} message - Message à afficher
 */
function showErrorMessage(message) {
    // Créer ou réutiliser l'élément de message
    let errorDiv = document.getElementById('audio-error-message');
    
    if (!errorDiv) {
        errorDiv = document.createElement('div');
        errorDiv.id = 'audio-error-message';
        errorDiv.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #f44336;
            color: white;
            padding: 12px 16px;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
            z-index: 10000;
            max-width: 300px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-size: 14px;
            line-height: 1.4;
        `;
        document.body.appendChild(errorDiv);
    }
    
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    
    // Masquer automatiquement après 5 secondes
    setTimeout(() => {
        errorDiv.style.display = 'none';
    }, 5000);
    
    console.warn(`⚠️ Message utilisateur: ${message}`);
}

/**
 * Détecte les capacités audio du navigateur
 */
function detectAudioCapabilities() {
    const audio = new Audio();
    const capabilities = {
        canPlayMP3: audio.canPlayType('audio/mpeg') !== '',
        canPlayOGG: audio.canPlayType('audio/ogg') !== '',
        canPlayWAV: audio.canPlayType('audio/wav') !== '',
        hasAudioAPI: typeof Audio !== 'undefined'
    };
    
    console.log('🔍 Capacités audio détectées:', capabilities);
    
    if (!capabilities.hasAudioAPI) {
        console.error('❌ API Audio non supportée par ce navigateur');
        showErrorMessage('Votre navigateur ne supporte pas la lecture audio.');
    }
    
    return capabilities;
}

/**
 * Fonction d'initialisation appelée au chargement
 */
(function() {
    console.log('🌤️ Lexique Météorologique - Module Audio chargé');
    
    // Détecter les capacités
    detectAudioCapabilities();
    
    // Initialiser le système
    initAudioSystem();
    
    // Exposer des fonctions utiles globalement (pour debug)
    if (typeof window !== 'undefined') {
        window.lexiqueAudio = {
            playAudio,
            stopCurrentAudio,
            setupAudioButtons
        };
    }
})();