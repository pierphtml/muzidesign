
// Header scroll effect
window.addEventListener('scroll', function() {
    const header = document.querySelector('header');
    const backToTop = document.querySelector('.back-to-top');
    
    if (window.scrollY > 50) {
        header.classList.add('header-scrolled');
    } else {
        header.classList.remove('header-scrolled');
    }
    
    if (window.scrollY > 500) {
        backToTop.classList.add('visible');
    } else {
        backToTop.classList.remove('visible');
    }
});

// Back to top functionality
const backToTopBtn = document.querySelector('.back-to-top');
if (backToTopBtn) {
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Mobile menu toggle
const mobileToggle = document.querySelector('.mobile-toggle');
const navLinks = document.querySelector('.nav-links');

if (mobileToggle && navLinks) {
    mobileToggle.addEventListener('click', function() {
        navLinks.classList.toggle('active');
        this.querySelector('i').classList.toggle('fa-bars');
        this.querySelector('i').classList.toggle('fa-times');
    });

    // Close mobile menu when clicking a link
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', function() {
            navLinks.classList.remove('active');
            mobileToggle.querySelector('i').classList.add('fa-bars');
            mobileToggle.querySelector('i').classList.remove('fa-times');
        });
    });
}

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        
        if (navLinks) {
            navLinks.classList.remove('active');
        }
        if (mobileToggle) {
            mobileToggle.querySelector('i').classList.add('fa-bars');
            mobileToggle.querySelector('i').classList.remove('fa-times');
        }
        
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            window.scrollTo({
                top: target.offsetTop - 80,
                behavior: 'smooth'
            });
        }
    });
});

// Hero slider (only on pages with slider)
const slides = document.querySelectorAll('.slide');
if (slides.length > 0) {
    let currentSlide = 0;
    
    function showSlide(n) {
        slides.forEach(slide => slide.classList.remove('active'));
        slides[n].classList.add('active');
    }
    
    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    }
    
    // Change slide every 5 seconds
    setInterval(nextSlide, 5000);
}

// Countdown timer for promotions (only on promotions page)
function updateCountdown() {
    const daysEl = document.getElementById('days');
    const hoursEl = document.getElementById('hours');
    const minutesEl = document.getElementById('minutes');
    const secondsEl = document.getElementById('seconds');
    
    if (daysEl && hoursEl && minutesEl && secondsEl) {
        const endDate = new Date('June 30, 2025 23:59:59').getTime();
        const now = new Date().getTime();
        const timeLeft = endDate - now;
        
        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);
        
        daysEl.textContent = days.toString().padStart(2, '0');
        hoursEl.textContent = hours.toString().padStart(2, '0');
        minutesEl.textContent = minutes.toString().padStart(2, '0');
        secondsEl.textContent = seconds.toString().padStart(2, '0');
    }
}

// Update countdown every second if elements exist
if (document.getElementById('days')) {
    setInterval(updateCountdown, 1000);
    updateCountdown();
}

// Fade-in animation for elements
const fadeElements = document.querySelectorAll('.fade-in');

function checkFade() {
    fadeElements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        
        if (elementTop < windowHeight - 50) {
            element.classList.add('appear');
        }
    });
}

window.addEventListener('scroll', checkFade);
window.addEventListener('load', checkFade);

// Form submission
const form = document.getElementById('consultationForm');
if (form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Grazie per la tua richiesta! Un nostro consulente ti contatterà al più presto per confermare l\'appuntamento.');
        form.reset();
    });
}

// Product detail modal
const modal = document.getElementById('productModal');
const modalClose = document.querySelector('.modal-close');

const productData = {
    oyster: {
        title: 'Veneta Cucine Oyster',
        image: 'https://www.venetacucine.com/cache/media/2021/05/oyster-bianca-veneta-cucine-be-personal-1000x560_6900.jpg/f5651754e98d5c2752f8f7cd3ec57080.jpg',
        description: 'Cucina minimalista con apertura senza maniglie (ShellSystem), superfici lisce e ampio ventaglio di finiture moderne. Design pulito ed elegante per chi ama la semplicità raffinata.',
        specs: {
            'Materiali': 'Laminato opaco, Legno',
            'Apertura': 'ShellSystem senza maniglie',
            'Colori disponibili': 'Bianco, Grigio, Noce',
            'Personalizzazione': 'Completamente personalizzabile',
            'Garanzia': '5 anni'
        }
    },
    iconica: {
        title: 'Veneta Cucine Iconica',
        image: 'https://www.venetacucine.com/cache/media/2023/04/iconica_anteprima_01_13089.jpg/11553f147e7fa6806ef86f78ec163877.jpg',
        description: 'Design innovativo e asimmetrico, mix di materiali pregiati (vetro, legno, metallo), massimo livello di personalizzazione. Una cucina che non passa inosservata.',
        specs: {
            'Materiali': 'Vetro, Legno, Metallo',
            'Design': 'Asimmetrico innovativo',
            'Finiture': 'Premium e ricercate',
            'Personalizzazione': 'Massimo livello',
            'Garanzia': '5 anni'
        }
    },
    lounge: {
        title: 'Veneta Cucine Lounge',
        image: 'https://www.venetacucine.com/cache/media/2023/06/veneta_cucine_-_lounge_shellsystem__13653.jpg/77437985ce50331b883db44ce03ec079.jpg',
        description: 'Cucina funzionale e compatta con zoccolo ribassato (8 cm), offre più spazio contenitivo e combinazioni materiche ricercate. Perfetta per spazi moderni.',
        specs: {
            'Zoccolo': 'Ribassato 8 cm',
            'Spazio': 'Maggiore contenimento',
            'Materiali': 'Combinazioni ricercate',
            'Stile': 'Moderno e funzionale',
            'Garanzia': '5 anni'
        }
    },
    plaza: {
        title: 'EgoItaliano Plaza',
        image: 'https://immagini.designbest.com/pictures/product-107022-80482.jpg',
        description: 'Divano modulare e profondo, con braccioli larghi, rivestimenti antimacchia o in pelle, e configurazione personalizzabile. Comfort e design in perfetto equilibrio.',
        specs: {
            'Tipo': 'Modulare personalizzabile',
            'Rivestimenti': 'Antimacchia o pelle',
            'Braccioli': 'Larghi e comodi',
            'Configurazione': 'Completamente personalizzabile',
            'Garanzia': '2 anni'
        }
    }
};

// Event listeners for product detail buttons
if (modal && modalClose) {
    document.querySelectorAll('.product-detail-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.getAttribute('data-product');
            const product = productData[productId];
            
            if (product) {
                document.getElementById('modalTitle').textContent = 'Dettagli Prodotto';
                document.getElementById('modalProductTitle').textContent = product.title;
                document.getElementById('modalImage').src = product.image;
                document.getElementById('modalImage').alt = product.title;
                document.getElementById('modalProductDescription').textContent = product.description;
                
                const specsContainer = document.getElementById('modalSpecs');
                specsContainer.innerHTML = '';
                
                Object.entries(product.specs).forEach(([key, value]) => {
                    const specItem = document.createElement('div');
                    specItem.className = 'spec-item';
                    specItem.innerHTML = `<strong>${key}:</strong><span>${value}</span>`;
                    specsContainer.appendChild(specItem);
                });
                
                modal.style.display = 'block';
            }
        });
    });

    // Close modal
    modalClose.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
}
