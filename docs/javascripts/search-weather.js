// Script pour ajouter une bande météo au-dessus de la recherche
document.addEventListener('DOMContentLoaded', function() {
    // Attendre que MkDocs Material soit chargé
    setTimeout(function() {
        // Trouver la barre de recherche
        const searchBar = document.querySelector('.md-search');
        const header = document.querySelector('.md-header');
        
        if (header && !document.querySelector('.search-weather-strip')) {
            // Créer la bande météo au-dessus de la recherche
            const weatherStrip = document.createElement('div');
            weatherStrip.className = 'search-weather-strip';
            weatherStrip.innerHTML = `
                <div class="search-weather-bg">
                    <div class="weather-icon sun-icon">☀️</div>
                    <div class="weather-icon cloud-icon">☁️</div>
                    <div class="weather-icon rain-icon">🌧️</div>
                    <div class="weather-icon storm-icon">⛈️</div>
                </div>
            `;
            
            // Insérer après le header
            header.parentNode.insertBefore(weatherStrip, header.nextSibling);
            
            // Animation des icônes météo
            const icons = weatherStrip.querySelectorAll('.weather-icon');
            let currentIcon = 0;
            
            function animateWeather() {
                icons.forEach((icon, index) => {
                    if (index === currentIcon) {
                        icon.classList.add('active');
                    } else {
                        icon.classList.remove('active');
                    }
                });
                currentIcon = (currentIcon + 1) % icons.length;
            }
            
            // Démarrer l'animation
            animateWeather();
            setInterval(animateWeather, 3000);
        }
    }, 200);
});