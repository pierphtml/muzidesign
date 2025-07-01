#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Template base per tutti i file dei divani
TEMPLATE = '''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Muzi Design</title>
    <link rel="stylesheet" href="../style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .product-detail {{
            padding: 120px 0 60px;
        }}

        .product-gallery {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
            margin-bottom: 50px;
        }}

        .gallery-main {{
            grid-column: span 2;
            height: 600px;
            border-radius: var(--radius);
            overflow: hidden;
        }}

        .gallery-main img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}

        .gallery-thumb {{
            height: 300px;
            border-radius: var(--radius);
            overflow: hidden;
            cursor: pointer;
        }}

        .gallery-thumb img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: var(--transition);
        }}

        .gallery-thumb:hover img {{
            transform: scale(1.05);
        }}

        .product-info-table {{
            background: white;
            border-radius: var(--radius);
            padding: 40px;
            box-shadow: var(--shadow);
            margin-bottom: 50px;
        }}

        .info-table {{
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
        }}

        .info-table tr {{
            transition: var(--transition);
        }}

        .info-table tr:hover {{
            background-color: rgba(193, 154, 107, 0.05);
        }}

        .info-table th,
        .info-table td {{
            padding: 20px;
            text-align: left;
            border-bottom: 1px solid rgba(0, 0, 0, 0.1);
        }}

        .info-table th {{
            font-family: 'Playfair Display', serif;
            color: var(--primary);
            font-size: 1.2rem;
            width: 30%;
        }}

        .info-table td {{
            color: var(--gray);
            line-height: 1.6;
        }}

        .info-table tr:last-child td {{
            border-bottom: none;
        }}

        .product-features {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin-top: 50px;
        }}

        .feature-card {{
            background: white;
            padding: 30px;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            text-align: center;
            transition: var(--transition);
        }}

        .feature-card:hover {{
            transform: translateY(-5px);
            box-shadow: var(--shadow-hover);
        }}

        .feature-icon {{
            font-size: 2.5rem;
            color: var(--secondary);
            margin-bottom: 20px;
        }}

        .feature-title {{
            font-family: 'Playfair Display', serif;
            color: var(--primary);
            margin-bottom: 15px;
            font-size: 1.2rem;
        }}

        .feature-text {{
            color: var(--gray);
            line-height: 1.6;
        }}

        @media (max-width: 992px) {{
            .product-features {{
                grid-template-columns: repeat(2, 1fr);
            }}
        }}

        @media (max-width: 768px) {{
            .product-gallery {{
                grid-template-columns: 1fr;
            }}

            .gallery-main {{
                grid-column: span 1;
                height: 400px;
            }}

            .gallery-thumb {{
                height: 200px;
            }}

            .product-features {{
                grid-template-columns: 1fr;
            }}

            .info-table th,
            .info-table td {{
                padding: 15px;
            }}
        }}

        .hero-slider-cucina {{
            width: 100vw;
            max-width: 100%;
            background: #f7f7f7;
            padding: 0;
            margin-bottom: 40px;
        }}
        .slider-cucina {{
            position: relative;
            width: 100%;
            max-width: 900px;
            margin: 0 auto 36px auto;
            height: 480px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            background: #fff;
            border-radius: 18px;
            box-shadow: 0 6px 32px rgba(0,0,0,0.10);
        }}
        .slider-cucina .slider-img {{
            display: none;
            width: 100%;
            height: 100%;
            object-fit: cover;
            position: absolute;
            left: 0;
            top: 0;
            border-radius: 18px;
            transition: opacity 0.4s;
        }}
        .slider-cucina .slider-img.active {{
            display: block;
            position: relative;
            z-index: 2;
            opacity: 1;
        }}
        .slider-cucina .slider-btn {{
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            font-size: 2.2rem;
            color: var(--primary);
            padding: 0 10px;
            border-radius: 0;
            cursor: pointer;
            z-index: 3;
            transition: color 0.2s;
            box-shadow: none;
        }}
        .slider-cucina .slider-btn[disabled] {{
            display: none;
        }}
        .slider-cucina .slider-btn:hover {{
            color: var(--secondary);
            background: none;
        }}
        .slider-cucina .slider-btn.prev {{
            left: 8px;
        }}
        .slider-cucina .slider-btn.next {{
            right: 8px;
        }}
        .slider-thumbs {{
            position: absolute;
            bottom: 18px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 10px;
            z-index: 4;
        }}
        .slider-thumb {{
            width: 60px;
            height: 40px;
            object-fit: cover;
            border-radius: 6px;
            border: 2px solid transparent;
            cursor: pointer;
            opacity: 0.7;
            transition: border 0.2s, opacity 0.2s;
        }}
        .slider-thumb.active {{
            border: 2px solid var(--primary);
            opacity: 1;
        }}
        @media (max-width: 768px) {{
            .slider-cucina {{
                height: 320px;
                max-width: 98vw;
            }}
            .slider-thumb {{
                width: 40px;
                height: 28px;
            }}
        }}
    </style>
</head>
<body>
    <!-- Header & Navigation -->
    <header class="modern-header fade-in">
        <div class="container">
            <nav class="modern-navbar">
                <a href="../index.html" class="modern-logo">
                    <img src="../attached_assets/logo.png" alt="Muzi Design">
                </a>
                <ul class="modern-nav-links">
                    <li><a href="../index.html">Home</a></li>
                    <li><a href="../chi-siamo.html">Chi Siamo</a></li>
                    <li><a href="../prodotti.html">Prodotti</a></li>
                    <li><a href="../promozioni.html">Promozioni</a></li>
                    <li><a href="../gallery.html">Gallery</a></li>
                    <li><a href="../contatti.html">Contatti</a></li>
                </ul>
                <a href="../contatti.html" class="modern-cta-btn">Prenota una visita</a>
                <button class="modern-mobile-toggle" aria-label="Apri menu">
                    <i class="fas fa-bars"></i>
                </button>
            </nav>
            <div class="modern-mobile-menu">
                <ul>
                    <li><a href="../index.html">Home</a></li>
                    <li><a href="../chi-siamo.html">Chi Siamo</a></li>
                    <li><a href="../prodotti.html">Prodotti</a></li>
                    <li><a href="../promozioni.html">Promozioni</a></li>
                    <li><a href="../gallery.html">Gallery</a></li>
                    <li><a href="../contatti.html">Contatti</a></li>
                </ul>
                <a href="../contatti.html" class="modern-cta-btn-mobile"><span><i class="fas fa-calendar-check"></i> PRENOTA UNA VISITA</span></a>
            </div>
        </div>
    </header>

    <!-- Product Detail -->
    <section class="product-detail">
        <div class="container">
            <div class="slider-cucina" data-slider="{slider_name}">
                <button class="slider-btn prev" onclick="slidePrev(event, '{slider_name}')"><i class="fas fa-chevron-left"></i></button>
                <img src="../attached_assets/images.jpeg" alt="{title}" class="slider-img active">
                <button class="slider-btn next" onclick="slideNext(event, '{slider_name}')"><i class="fas fa-chevron-right"></i></button>
                <div class="slider-thumbs">
                    <img src="../attached_assets/images.jpeg" alt="{title}" class="slider-thumb active" onclick="goToSlide('{slider_name}',0)">
                </div>
            </div>
            <div class="product-info-table">
                <h2 class="section-title">{title}</h2>
                <p class="section-subtitle">{subtitle}</p>
                <table class="info-table">
                    <tr><th>Stile</th><td>{style}</td></tr>
                    <tr><th>Design</th><td>{design}</td></tr>
                    <tr><th>Colori</th><td>{colors}</td></tr>
                    <tr><th>Materiali</th><td>{materials}</td></tr>
                    <tr><th>Caratteristiche</th><td>{features}</td></tr>
                </table>
                <div class="product-features">
                    <div class="feature-card">
                        <div class="feature-icon"><i class="fas fa-{icon1}"></i></div>
                        <h3 class="feature-title">{feature1_title}</h3>
                        <p class="feature-text">{feature1_text}</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon"><i class="fas fa-{icon2}"></i></div>
                        <h3 class="feature-title">{feature2_title}</h3>
                        <p class="feature-text">{feature2_text}</p>
                    </div>
                    <div class="feature-card">
                        <div class="feature-icon"><i class="fas fa-{icon3}"></i></div>
                        <h3 class="feature-title">{feature3_title}</h3>
                        <p class="feature-text">{feature3_text}</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <h3>Muzi Design</h3>
                    <p>Arredamento di qualità dal 1957. Uniamo tradizione artigianale e design contemporaneo per creare spazi unici e personali.</p>
                    <div class="social-links">
                        <a href="#" class="social-link"><i class="fab fa-facebook-f"></i></a>
                        <a href="#" class="social-link"><i class="fab fa-instagram"></i></a>
                        <a href="#" class="social-link"><i class="fab fa-pinterest-p"></i></a>
                        <a href="#" class="social-link"><i class="fab fa-youtube"></i></a>
                    </div>
                </div>
                <div class="footer-col">
                    <h3>Link Utili</h3>
                    <ul class="footer-links">
                        <li><a href="../index.html"><i class="fas fa-chevron-right"></i> Home</a></li>
                        <li><a href="../chi-siamo.html"><i class="fas fa-chevron-right"></i> Chi Siamo</a></li>
                        <li><a href="../categorie.html"><i class="fas fa-chevron-right"></i> Categorie</a></li>
                        <li><a href="../prodotti.html"><i class="fas fa-chevron-right"></i> Prodotti</a></li>
                        <li><a href="../promozioni.html"><i class="fas fa-chevron-right"></i> Promozioni</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>Categorie</h3>
                    <ul class="footer-links">
                        <li><a href="../cucine-moderne.html"><i class="fas fa-chevron-right"></i> Cucine Moderne</a></li>
                        <li><a href="../cucine-contemporanee.html"><i class="fas fa-chevron-right"></i> Cucine Contemporanee</a></li>
                        <li><a href="../cucine-classiche.html"><i class="fas fa-chevron-right"></i> Cucine Classiche</a></li>
                        <li><a href="../categorie.html"><i class="fas fa-chevron-right"></i> Zona Giorno</a></li>
                        <li><a href="../categorie.html"><i class="fas fa-chevron-right"></i> Zona Notte</a></li>
                        <li><a href="../categorie.html"><i class="fas fa-chevron-right"></i> Camerette</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>Contatti</h3>
                    <ul class="footer-links">
                        <li><a href="../contatti.html"><i class="fas fa-map-marker-alt"></i> Via Artena 54, Valmontone (RM)</a></li>
                        <li><a href="tel:800202530"><i class="fas fa-phone-alt"></i> 800 202 530</a></li>
                        <li><a href="mailto:info@muzidesign.it"><i class="fas fa-envelope"></i> info@muzidesign.it</a></li>
                    </ul>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2025 Muzi Design. Tutti i diritti riservati. P.IVA IT15934181007</p>
            </div>
        </div>
    </footer>

    <!-- Back to Top Button -->
    <a href="#" class="back-to-top">
        <i class="fas fa-arrow-up"></i>
    </a>

    <!-- Floating AI Chatbot Button -->
    <button class="floating-chatbot">
        <i class="fas fa-robot"></i>
    </button>

    <script src="../script.js"></script>
    <script>
    function updateSliderButtons(sliderName) {{
        const slider = document.querySelector('.slider-cucina[data-slider="' + sliderName + '"]');
        const images = slider.querySelectorAll('.slider-img');
        const prevBtn = slider.querySelector('.slider-btn.prev');
        const nextBtn = slider.querySelector('.slider-btn.next');
        let current = Array.from(images).findIndex(img => img.classList.contains('active'));
        prevBtn.disabled = (current === 0);
        nextBtn.disabled = (current === images.length - 1);
    }}
    function slidePrev(event, sliderName) {{
        event.preventDefault();
        const slider = document.querySelector('.slider-cucina[data-slider="' + sliderName + '"]');
        const images = slider.querySelectorAll('.slider-img');
        const thumbs = slider.querySelectorAll('.slider-thumb');
        let current = Array.from(images).findIndex(img => img.classList.contains('active'));
        if (current === 0) return;
        images[current].classList.remove('active');
        thumbs[current].classList.remove('active');
        current = (current - 1 + images.length) % images.length;
        images[current].classList.add('active');
        thumbs[current].classList.add('active');
        updateSliderButtons(sliderName);
    }}
    function slideNext(event, sliderName) {{
        event.preventDefault();
        const slider = document.querySelector('.slider-cucina[data-slider="' + sliderName + '"]');
        const images = slider.querySelectorAll('.slider-img');
        const thumbs = slider.querySelectorAll('.slider-thumb');
        let current = Array.from(images).findIndex(img => img.classList.contains('active'));
        if (current === images.length - 1) return;
        images[current].classList.remove('active');
        thumbs[current].classList.remove('active');
        current = (current + 1) % images.length;
        images[current].classList.add('active');
        thumbs[current].classList.add('active');
        updateSliderButtons(sliderName);
    }}
    function goToSlide(sliderName, index) {{
        const slider = document.querySelector('.slider-cucina[data-slider="' + sliderName + '"]');
        const images = slider.querySelectorAll('.slider-img');
        const thumbs = slider.querySelectorAll('.slider-thumb');
        images.forEach(img => img.classList.remove('active'));
        thumbs.forEach(thumb => thumb.classList.remove('active'));
        images[index].classList.add('active');
        thumbs[index].classList.add('active');
        updateSliderButtons(sliderName);
    }}
    </script>
</body>
</html>'''

# Dati specifici per ogni divano
DIVANI_DATA = {
    'airy': {
        'title': 'Airy',
        'subtitle': 'Estetica leggera, basamento metallico, cuscini fluttuanti.',
        'style': 'Leggero, contemporaneo',
        'design': 'Basamento metallico, cuscini fluttuanti',
        'colors': 'Disponibile in vari tessuti e colori',
        'materials': 'Tessuti moderni, struttura in metallo',
        'features': 'Estetica leggera, comfort e design innovativo',
        'icon1': 'feather-alt',
        'feature1_title': 'Estetica leggera',
        'feature1_text': 'Linee sottili e volumi sospesi per un look arioso.',
        'icon2': 'couch',
        'feature2_title': 'Cuscini fluttuanti',
        'feature2_text': 'Seduta e schienale sembrano sospesi per il massimo comfort.',
        'icon3': 'grip-lines-vertical',
        'feature3_title': 'Basamento metallico',
        'feature3_text': 'Struttura solida e moderna che dona leggerezza visiva.'
    },
    'astoria': {
        'title': 'Astoria',
        'subtitle': 'Design elegante e raffinato per ambienti di classe.',
        'style': 'Elegante, raffinato',
        'design': 'Linee classiche, imbottitura premium',
        'colors': 'Tessuti pregiati in colori neutri',
        'materials': 'Tessuti di lusso, struttura in legno massello',
        'features': 'Comfort superiore, eleganza senza tempo',
        'icon1': 'crown',
        'feature1_title': 'Design elegante',
        'feature1_text': 'Linee classiche che si adattano a qualsiasi ambiente.',
        'icon2': 'star',
        'feature2_title': 'Qualità premium',
        'feature2_text': 'Materiali di prima scelta per una seduta eccezionale.',
        'icon3': 'heart',
        'feature3_title': 'Comfort superiore',
        'feature3_text': 'Imbottitura studiata per il massimo relax.'
    },
    'babouche': {
        'title': 'Babouche',
        'subtitle': 'Comfort orientale, design contemporaneo.',
        'style': 'Orientale, contemporaneo',
        'design': 'Seduta bassa, cuscini modulari',
        'colors': 'Tessuti naturali, colori terra',
        'materials': 'Cotone naturale, struttura in legno',
        'features': 'Seduta confortevole, atmosfera zen',
        'icon1': 'leaf',
        'feature1_title': 'Stile orientale',
        'feature1_text': 'Design ispirato alle tradizioni orientali.',
        'icon2': 'couch',
        'feature2_title': 'Seduta bassa',
        'feature2_text': 'Altezza ridotta per un comfort naturale.',
        'icon3': 'spa',
        'feature3_title': 'Atmosfera zen',
        'feature3_text': 'Perfetto per creare un ambiente rilassante.'
    }
}

def get_divano_data(filename):
    """Ottiene i dati specifici per un divano dal nome del file"""
    name = filename.replace('.html', '').lower()
    
    # Se abbiamo dati specifici, li usiamo
    if name in DIVANI_DATA:
        return DIVANI_DATA[name]
    
    # Altrimenti creiamo dati generici
    title = filename.replace('.html', '').title()
    return {
        'title': title,
        'subtitle': f'Design moderno e confortevole per il tuo soggiorno.',
        'style': 'Moderno, confortevole',
        'design': 'Linee pulite, imbottitura ergonomica',
        'colors': 'Disponibile in vari tessuti e colori',
        'materials': 'Tessuti di qualità, struttura robusta',
        'features': 'Comfort ottimale, design contemporaneo',
        'icon1': 'couch',
        'feature1_title': 'Design moderno',
        'feature1_text': 'Linee pulite e contemporanee per ambienti moderni.',
        'icon2': 'star',
        'feature2_title': 'Comfort superiore',
        'feature2_text': 'Imbottitura studiata per il massimo relax.',
        'icon3': 'palette',
        'feature3_title': 'Personalizzabile',
        'feature3_text': 'Vari tessuti e colori per ogni stile.'
    }

def update_divano_file(filepath):
    """Aggiorna un singolo file divano con il template standardizzato"""
    filename = os.path.basename(filepath)
    data = get_divano_data(filename)
    data['slider_name'] = filename.replace('.html', '')
    
    # Genera il contenuto con il template
    content = TEMPLATE.format(**data)
    
    # Scrivi il file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Aggiornato: {filename}")

def main():
    """Funzione principale per aggiornare tutti i file dei divani"""
    divani_dir = Path("divani")
    
    if not divani_dir.exists():
        print("Directory 'divani' non trovata!")
        return
    
    # Trova tutti i file HTML nella directory divani
    html_files = list(divani_dir.glob("*.html"))
    
    print(f"Trovati {len(html_files)} file da aggiornare...")
    
    # Aggiorna ogni file
    for filepath in html_files:
        try:
            update_divano_file(filepath)
        except Exception as e:
            print(f"Errore nell'aggiornamento di {filepath}: {e}")
    
    print("Aggiornamento completato!")

if __name__ == "__main__":
    main() 