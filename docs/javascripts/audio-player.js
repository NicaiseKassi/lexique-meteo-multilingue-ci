document.addEventListener('DOMContentLoaded', function() {
    console.log('🎵 Lecteur audio initialisé pour structure simple');
    
    // Fonction de lecture audio simple et robuste
    window.playAudio = function(audioPath, button) {
        console.log('🔊 Lecture audio:', audioPath);
        
        // Indicateur visuel
        const originalText = button.textContent;
        const originalBg = button.style.backgroundColor;
        
        button.textContent = '⏳ Chargement...';
        button.style.backgroundColor = '#FFA726';
        button.disabled = true;
        
        // Créer l'élément audio
        const audio = new Audio();
        audio.preload = 'auto';
        audio.volume = 0.8;
        
        // Gestion des événements
        audio.addEventListener('canplay', function() {
            console.log('✅ Audio prêt');
            button.textContent = '▶️ Lecture...';
            button.style.backgroundColor = '#4CAF50';
        });
        
        audio.addEventListener('ended', function() {
            console.log('⏹️ Lecture terminée');
            button.textContent = originalText;
            button.style.backgroundColor = originalBg;
            button.disabled = false;
        });
        
        audio.addEventListener('error', function(e) {
            console.error('❌ Erreur audio:', e);
            button.textContent = '❌ Erreur';
            button.style.backgroundColor = '#F44336';
            
            setTimeout(() => {
                button.textContent = originalText;
                button.style.backgroundColor = originalBg;
                button.disabled = false;
            }, 3000);
        });
        
        // URL audio (structure simple, pas de termes/)
        console.log('🔗 URL audio:', audioPath);
        audio.src = audioPath;
        
        // Lancer la lecture
        audio.play().then(() => {
            console.log('🎵 Lecture démarrée');
        }).catch(error => {
            console.error('⚠️ Erreur de lecture:', error);
            button.textContent = '🔊 Cliquez pour écouter';
            button.style.backgroundColor = '#2196F3';
            button.disabled = false;
        });
    };
});