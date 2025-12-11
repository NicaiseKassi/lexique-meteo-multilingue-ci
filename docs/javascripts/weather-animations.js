/**
 * Script pour les animations météorologiques dynamiques
 * Contrôle les effets visuels de l'en-tête du lexique météorologique
 * 
 * Auteur: SODEXAM - Côte d'Ivoire
 * Date: Novembre 2024
 */

class WeatherAnimations {
    constructor() {
        this.currentWeather = 'sunny';
        this.animationContainer = null;
        this.weatherStates = {
            sunny: { name: '☀️ Ensoleillé', class: 'sunny' },
            rainy: { name: '🌧️ Pluvieux', class: 'rainy' },
            cloudy: { name: '☁️ Nuageux', class: 'cloudy' },
            stormy: { name: '⛈️ Orageux', class: 'stormy' }
        };
        
        this.init();
        this.startAutoRotation();
    }

    init() {
        this.createTopWeatherHeader();
        this.createTopControls();
        this.bindEvents();
        this.setWeather('sunny');
    }

    createTopWeatherHeader() {
        // Créer l'en-tête météo en haut de page
        let topHeader = document.querySelector('.weather-header-top');
        if (!topHeader) {
            topHeader = document.createElement('div');
            topHeader.className = 'weather-header-top';
            document.body.insertBefore(topHeader, document.body.firstChild);
        }

        // Ajouter le titre si pas déjà présent
        if (!topHeader.querySelector('.weather-header-title')) {
            const title = document.createElement('div');
            title.className = 'weather-header-title';
            title.textContent = '🌤️ Lexique Météorologique - SODEXAM Côte d\'Ivoire';
            topHeader.appendChild(title);
        }

        // Ajouter le conteneur d'animation
        if (!topHeader.querySelector('.top-weather-animation')) {
            this.animationContainer = document.createElement('div');
            this.animationContainer.className = 'top-weather-animation';
            topHeader.appendChild(this.animationContainer);
        } else {
            this.animationContainer = topHeader.querySelector('.top-weather-animation');
        }
    }

    createTopControls() {
        const topHeader = document.querySelector('.weather-header-top');
        if (!topHeader) return;

        let controlsContainer = document.querySelector('.top-weather-controls');
        if (!controlsContainer) {
            controlsContainer = document.createElement('div');
            controlsContainer.className = 'top-weather-controls';
            topHeader.appendChild(controlsContainer);
        }

        // Créer les boutons de contrôle
        controlsContainer.innerHTML = '';
        Object.keys(this.weatherStates).forEach(weather => {
            const btn = document.createElement('button');
            btn.className = 'top-weather-btn';
            btn.dataset.weather = weather;
            btn.textContent = this.weatherStates[weather].name;
            
            btn.addEventListener('click', () => {
                this.setWeather(weather);
                this.stopAutoRotation();
                
                // Redémarrer l'auto-rotation après 10 secondes
                setTimeout(() => this.startAutoRotation(), 10000);
            });
            
            controlsContainer.appendChild(btn);
        });
    }

    setWeather(weatherType) {
        if (!this.weatherStates[weatherType]) return;

        this.currentWeather = weatherType;
        const topHeader = document.querySelector('.weather-header-top');
        
        // Nettoyer les classes météorologiques existantes
        Object.values(this.weatherStates).forEach(state => {
            topHeader.classList.remove(state.class);
        });
        
        // Ajouter la nouvelle classe
        topHeader.classList.add(this.weatherStates[weatherType].class);
        
        // Mettre à jour les boutons
        document.querySelectorAll('.top-weather-btn').forEach(btn => {
            btn.classList.remove('active');
            if (btn.dataset.weather === weatherType) {
                btn.classList.add('active');
            }
        });
        
        // Créer les animations spécifiques
        this.createTopWeatherElements(weatherType);
    }

    createTopWeatherElements(weatherType) {
        if (!this.animationContainer) return;
        
        // Nettoyer les éléments existants
        this.animationContainer.innerHTML = '';
        
        switch (weatherType) {
            case 'sunny':
                this.createTopSun();
                this.createTopClouds(2, true);
                break;
                
            case 'rainy':
                this.createTopClouds(3, false);
                this.createTopRain();
                break;
                
            case 'cloudy':
                this.createTopClouds(4, false);
                break;
                
            case 'stormy':
                this.createTopClouds(2, false);
                this.createTopRain();
                this.createTopLightning();
                break;
        }
    }

    createTopSun() {
        const sun = document.createElement('div');
        sun.className = 'top-sun';
        this.animationContainer.appendChild(sun);
    }

    createTopClouds(count, light = false) {
        for (let i = 0; i < count; i++) {
            const cloud = document.createElement('div');
            cloud.className = 'top-cloud';
            
            // Variations de taille et position pour l'en-tête du haut
            const size = 40 + Math.random() * 25;
            const top = 20 + Math.random() * 40;
            const delay = Math.random() * 15;
            
            cloud.style.width = `${size}px`;
            cloud.style.height = `${size * 0.6}px`;
            cloud.style.top = `${top}px`;
            cloud.style.animationDelay = `-${delay}s`;
            cloud.style.animationDuration = `${10 + Math.random() * 8}s`;
            
            if (light) {
                cloud.style.opacity = '0.5';
            }
            
            // Ajouter les pseudo-éléments pour la forme du nuage
            cloud.innerHTML = '<div style="position:absolute;width:30px;height:30px;background:inherit;border-radius:50%;top:-15px;left:8px;"></div><div style="position:absolute;width:35px;height:35px;background:inherit;border-radius:50%;top:-18px;right:12px;"></div>';
            
            this.animationContainer.appendChild(cloud);
        }
    }

    createTopRain() {
        // Créer plusieurs gouttes de pluie pour l'en-tête du haut
        for (let i = 0; i < 30; i++) {
            const raindrop = document.createElement('div');
            raindrop.className = 'top-raindrop';
            
            const left = Math.random() * 100;
            const delay = Math.random() * 1.5;
            const duration = 0.4 + Math.random() * 0.8;
            
            raindrop.style.left = `${left}%`;
            raindrop.style.animationDelay = `${delay}s`;
            raindrop.style.animationDuration = `${duration}s`;
            
            this.animationContainer.appendChild(raindrop);
        }
    }

    createTopLightning() {
        const lightning = document.createElement('div');
        lightning.className = 'lightning';
        lightning.style.height = '80px';
        lightning.style.top = '20px';
        lightning.style.width = '4px';
        
        // Position aléatoire
        lightning.style.left = `${30 + Math.random() * 40}%`;
        
        this.animationContainer.appendChild(lightning);
    }

    startAutoRotation() {
        this.stopAutoRotation(); // S'assurer qu'il n'y a qu'une rotation active
        
        const weatherTypes = Object.keys(this.weatherStates);
        let currentIndex = weatherTypes.indexOf(this.currentWeather);
        
        this.autoRotationInterval = setInterval(() => {
            currentIndex = (currentIndex + 1) % weatherTypes.length;
            this.setWeather(weatherTypes[currentIndex]);
        }, 8000); // Changer toutes les 8 secondes
    }

    stopAutoRotation() {
        if (this.autoRotationInterval) {
            clearInterval(this.autoRotationInterval);
            this.autoRotationInterval = null;
        }
    }

    bindEvents() {
        // Pause/reprise sur hover
        document.addEventListener('DOMContentLoaded', () => {
            const topHeader = document.querySelector('.weather-header-top');
            if (topHeader) {
                topHeader.addEventListener('mouseenter', () => this.stopAutoRotation());
                topHeader.addEventListener('mouseleave', () => this.startAutoRotation());
            }
        });

        // Contrôle par clavier
        document.addEventListener('keydown', (e) => {
            const weatherTypes = Object.keys(this.weatherStates);
            const currentIndex = weatherTypes.indexOf(this.currentWeather);
            
            switch (e.key) {
                case 'ArrowLeft':
                    e.preventDefault();
                    const prevIndex = (currentIndex - 1 + weatherTypes.length) % weatherTypes.length;
                    this.setWeather(weatherTypes[prevIndex]);
                    break;
                    
                case 'ArrowRight':
                    e.preventDefault();
                    const nextIndex = (currentIndex + 1) % weatherTypes.length;
                    this.setWeather(weatherTypes[nextIndex]);
                    break;
                    
                case ' ':
                    e.preventDefault();
                    if (this.autoRotationInterval) {
                        this.stopAutoRotation();
                    } else {
                        this.startAutoRotation();
                    }
                    break;
            }
        });
    }
}

// Initialiser les animations quand le DOM est prêt
document.addEventListener('DOMContentLoaded', () => {
    // Attendre un peu pour que MkDocs finisse de charger
    setTimeout(() => {
        new WeatherAnimations();
    }, 500);
});

// Réinitialiser sur les changements de page (pour MkDocs)
if (typeof navigation !== 'undefined') {
    navigation.addEventListener('location', () => {
        setTimeout(() => {
            new WeatherAnimations();
        }, 500);
    });
}