#!/usr/bin/env python3
import os
from pathlib import Path

# Dati dei nuovi divani
NEW_DIVANI = {
    'alcor': {
        'title': 'Alcor',
        'subtitle': 'Modulare, poggiatesta regolabile, comfort artigianale made in Puglia.',
        'style': 'Modulare, artigianale',
        'design': 'Poggiatesta regolabile, comfort superiore',
        'colors': 'Disponibile in vari tessuti e colori',
        'materials': 'Tessuti di qualità, struttura robusta',
        'features': 'Made in Puglia, comfort artigianale',
        'icon1': 'puzzle-piece',
        'feature1_title': 'Modulare',
        'feature1_text': 'Composizione flessibile per adattarsi a ogni spazio.',
        'icon2': 'arrows-alt-v',
        'feature2_title': 'Poggiatesta regolabile',
        'feature2_text': 'Comfort personalizzabile per il massimo relax.',
        'icon3': 'hands-helping',
        'feature3_title': 'Made in Puglia',
        'feature3_text': 'Artigianalità e qualità italiana garantita.'
    },
    'bonny': {
        'title': 'Bonny',
        'subtitle': 'Lineare o angolare, rivestimento sfoderabile moderno.',
        'style': 'Lineare, angolare',
        'design': 'Rivestimento sfoderabile, versatilità',
        'colors': 'Disponibile in vari tessuti e colori',
        'materials': 'Tessuti sfoderabili, struttura moderna',
        'features': 'Versatile, pratico, moderno',
        'icon1': 'expand-arrows-alt',
        'feature1_title': 'Lineare o angolare',
        'feature1_text': 'Due configurazioni per adattarsi a ogni spazio.',
        'icon2': 'tshirt',
        'feature2_title': 'Sfoderabile',
        'feature2_text': 'Rivestimento facilmente rimovibile per la pulizia.',
        'icon3': 'magic',
        'feature3_title': 'Moderno',
        'feature3_text': 'Design contemporaneo per ambienti attuali.'
    },
    'twix': {
        'title': 'Twix',
        'subtitle': 'Angolare reclinabile, tessuto, novità modulare 2025.',
        'style': 'Angolare, reclinabile',
        'design': 'Modulare, tessuto, novità 2025',
        'colors': 'Disponibile in vari tessuti e colori',
        'materials': 'Tessuti di qualità, meccanismo reclinabile',
        'features': 'Novità 2025, comfort superiore',
        'icon1': 'angle-double-right',
        'feature1_title': 'Angolare',
        'feature1_text': 'Perfetto per sfruttare gli angoli degli ambienti.',
        'icon2': 'bed',
        'feature2_title': 'Reclinabile',
        'feature2_text': 'Meccanismo per il massimo comfort e relax.',
        'icon3': 'star',
        'feature3_title': 'Novità 2025',
        'feature3_text': 'Design all\'avanguardia per il nuovo anno.'
    },
    'sax': {
        'title': 'Sax',
        'subtitle': 'Capitonné elegante 3 posti, compatto e chic.',
        'style': 'Elegante, capitonné',
        'design': '3 posti, compatto, chic',
        'colors': 'Disponibile in vari tessuti e colori',
        'materials': 'Tessuti eleganti, capitonné',
        'features': 'Elegante, compatto, chic',
        'icon1': 'thumbtack',
        'feature1_title': 'Capitonné',
        'feature1_text': 'Dettaglio elegante che dona carattere al divano.',
        'icon2': 'users',
        'feature2_title': '3 posti',
        'feature2_text': 'Perfetto per famiglie e ospiti.',
        'icon3': 'gem',
        'feature3_title': 'Chic',
        'feature3_text': 'Stile raffinato per ambienti eleganti.'
    },
    'alita': {
        'title': 'Alita',
        'subtitle': 'Recliner 2‑3 posti, pelle raffinata premium.',
        'style': 'Recliner, premium',
        'design': '2-3 posti, pelle raffinata',
        'colors': 'Pelle premium in vari colori',
        'materials': 'Pelle raffinata, meccanismo reclinabile',
        'features': 'Premium, comfort superiore',
        'icon1': 'bed',
        'feature1_title': 'Recliner',
        'feature1_text': 'Meccanismo per il massimo comfort e relax.',
        'icon2': 'users',
        'feature2_title': '2-3 posti',
        'feature2_text': 'Versatile per diverse esigenze.',
        'icon3': 'crown',
        'feature3_title': 'Premium',
        'feature3_text': 'Pelle raffinata per un look di lusso.'
    },
    'tempo': {
        'title': 'Tempo',
        'subtitle': 'Sfoderabile con penisola, pratico e versatile.',
        'style': 'Sfoderabile, pratico',
        'design': 'Con penisola, versatile',
        'colors': 'Disponibile in vari tessuti e colori',
        'materials': 'Tessuti sfoderabili, struttura pratica',
        'features': 'Pratico, versatile, funzionale',
        'icon1': 'tshirt',
        'feature1_title': 'Sfoderabile',
        'feature1_text': 'Rivestimento facilmente rimovibile per la pulizia.',
        'icon2': 'plus-square',
        'feature2_title': 'Con penisola',
        'feature2_text': 'Elemento aggiuntivo per maggiore funzionalità.',
        'icon3': 'cogs',
        'feature3_title': 'Versatile',
        'feature3_text': 'Adattabile a diverse esigenze e spazi.'
    },
    'diesis': {
        'title': 'Diesis',
        'subtitle': 'Con poggiatesta e penisola, tessuto/pelle, funzioni relax.',
        'style': 'Relax, funzionale',
        'design': 'Poggiatesta, penisola, tessuto/pelle',
        'colors': 'Tessuto o pelle in vari colori',
        'materials': 'Tessuto o pelle, funzioni relax',
        'features': 'Funzioni relax, comfort superiore',
        'icon1': 'head-side-couch',
        'feature1_title': 'Poggiatesta',
        'feature1_text': 'Supporto per il collo per il massimo comfort.',
        'icon2': 'plus-square',
        'feature2_title': 'Penisola',
        'feature2_text': 'Elemento aggiuntivo per maggiore funzionalità.',
        'icon3': 'heart',
        'feature3_title': 'Funzioni relax',
        'feature3_text': 'Meccanismi per il massimo comfort e relax.'
    },
    'elba': {
        'title': 'Elba',
        'subtitle': 'Pelle o tessuto, disponibile anche angolare.',
        'style': 'Versatile, elegante',
        'design': 'Pelle o tessuto, angolare disponibile',
        'colors': 'Pelle o tessuto in vari colori',
        'materials': 'Pelle o tessuto, struttura robusta',
        'features': 'Versatile, elegante, funzionale',
        'icon1': 'expand-arrows-alt',
        'feature1_title': 'Angolare disponibile',
        'feature1_text': 'Configurazione per sfruttare gli angoli.',
        'icon2': 'palette',
        'feature2_title': 'Pelle o tessuto',
        'feature2_text': 'Scelta tra due materiali per ogni stile.',
        'icon3': 'star',
        'feature3_title': 'Elegante',
        'feature3_text': 'Design raffinato per ambienti di classe.'
    },
    'libeccio': {
        'title': 'Libeccio',
        'subtitle': 'Pelle con chaise longue, stile caldo e contemporaneo.',
        'style': 'Caldo, contemporaneo',
        'design': 'Pelle, chaise longue',
        'colors': 'Pelle in vari colori',
        'materials': 'Pelle di qualità, chaise longue',
        'features': 'Caldo, contemporaneo, comfort',
        'icon1': 'couch',
        'feature1_title': 'Chaise longue',
        'feature1_text': 'Estensione per il massimo comfort e relax.',
        'icon2': 'fire',
        'feature2_title': 'Stile caldo',
        'feature2_text': 'Atmosfera accogliente e invitante.',
        'icon3': 'clock',
        'feature3_title': 'Contemporaneo',
        'feature3_text': 'Design moderno per ambienti attuali.'
    },
    'atria': {
        'title': 'Atria',
        'subtitle': 'Componibile, spalliere generose e poggiatesta regolabile.',
        'style': 'Componibile, generoso',
        'design': 'Spalliere generose, poggiatesta regolabile',
        'colors': 'Disponibile in vari tessuti e colori',
        'materials': 'Tessuti di qualità, struttura componibile',
        'features': 'Componibile, generoso, regolabile',
        'icon1': 'puzzle-piece',
        'feature1_title': 'Componibile',
        'feature1_text': 'Moduli flessibili per ogni spazio.',
        'icon2': 'expand',
        'feature2_title': 'Spalliere generose',
        'feature2_text': 'Supporto ampio per il massimo comfort.',
        'icon3': 'arrows-alt-v',
        'feature3_title': 'Poggiatesta regolabile',
        'feature3_text': 'Comfort personalizzabile per ogni esigenza.'
    },
    'gordon': {
        'title': 'Gordon',
        'subtitle': 'Capitonné, raffinato, look classico da salotto.',
        'style': 'Classico, raffinato',
        'design': 'Capitonné, salotto',
        'colors': 'Disponibile in vari tessuti e colori',
        'materials': 'Tessuti raffinati, capitonné',
        'features': 'Classico, raffinato, salotto',
        'icon1': 'thumbtack',
        'feature1_title': 'Capitonné',
        'feature1_text': 'Dettaglio elegante che dona carattere al divano.',
        'icon2': 'crown',
        'feature2_title': 'Raffinato',
        'feature2_text': 'Stile elegante per ambienti di classe.',
        'icon3': 'home',
        'feature3_title': 'Look classico',
        'feature3_text': 'Design senza tempo per salotti tradizionali.'
    },
    'alira': {
        'title': 'Alira',
        'subtitle': 'Modulare elegante, braccioli squadrati, schienali ampi.',
        'style': 'Modulare, elegante',
        'design': 'Braccioli squadrati, schienali ampi',
        'colors': 'Disponibile in vari tessuti e colori',
        'materials': 'Tessuti eleganti, struttura modulare',
        'features': 'Modulare, elegante, ampio',
        'icon1': 'puzzle-piece',
        'feature1_title': 'Modulare',
        'feature1_text': 'Composizione flessibile per ogni spazio.',
        'icon2': 'square',
        'feature2_title': 'Braccioli squadrati',
        'feature2_text': 'Design geometrico moderno e pulito.',
        'icon3': 'expand',
        'feature3_title': 'Schienali ampi',
        'feature3_text': 'Supporto generoso per il massimo comfort.'
    },
    'ares': {
        'title': 'Ares',
        'subtitle': 'Sezionale elegante, tagli netti e comfort moderno.',
        'style': 'Sezionale, elegante',
        'design': 'Tagli netti, comfort moderno',
        'colors': 'Disponibile in vari tessuti e colori',
        'materials': 'Tessuti moderni, struttura sezionale',
        'features': 'Sezionale, elegante, moderno',
        'icon1': 'cut',
        'feature1_title': 'Tagli netti',
        'feature1_text': 'Linee precise e geometriche moderne.',
        'icon2': 'star',
        'feature2_title': 'Elegante',
        'feature2_text': 'Design raffinato per ambienti di classe.',
        'icon3': 'clock',
        'feature3_title': 'Comfort moderno',
        'feature3_text': 'Seduta contemporanea per il massimo relax.'
    }
}

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

def create_divano_file(divano_name, data):
    """Crea un file HTML per un divano specifico"""
    filepath = Path(f"divani/{divano_name}.html")
    data['slider_name'] = divano_name
    
    # Genera il contenuto con il template
    content = TEMPLATE.format(**data)
    
    # Scrivi il file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Creato: {divano_name}.html")

def main():
    """Funzione principale per creare tutti i nuovi divani"""
    print("Creazione schede per i nuovi divani...")
    
    # Crea ogni file divano
    for divano_name, data in NEW_DIVANI.items():
        try:
            create_divano_file(divano_name, data)
        except Exception as e:
            print(f"Errore nella creazione di {divano_name}.html: {e}")
    
    print("Creazione completata!")

if __name__ == "__main__":
    main() 