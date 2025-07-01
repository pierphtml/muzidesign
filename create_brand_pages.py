#!/usr/bin/env python3
import os
from pathlib import Path

# Dati dei brand e dei loro divani
BRANDS_DATA = {
    'egoitaliano': {
        'name': 'Egoitaliano',
        'logo': 'attached_assets/PRODOTTI/EGOITALIANO/idae6XM_kA_logos.png',
        'count': '30 divani',
        'description': 'Design italiano contemporaneo, comfort artigianale e qualità made in Italy. Collezione completa per ogni esigenza di arredamento.',
        'stats': {
            'modelli': '30',
            'stili': '4',
            'qualita': '100% Made in Italy'
        },
        'divani': [
            'Astoria', 'Babouche', 'Bebop', 'Beverly', 'Bliss', 'Candice', 'Caveoso', 'Dusk', 'Eros', 'Feng',
            'Funny', 'Gaia', 'Giada', 'Gloria', 'Ludo', 'Lego', 'Looming', 'Mavie', 'Martine', 'Masù',
            'Momo', 'Namy', 'Nefele', 'Nora', 'Oliver', 'Pacha', 'Piper', 'Plaza', 'Pongo', 'Sauvanne',
            'Selfy', 'Shai', 'Sofia', 'Tate', 'Vera', 'Viola', 'Zara', 'Zazou', 'Zoe', 'Zoomy'
        ]
    },
    'novamobili': {
        'name': 'Novamobili',
        'logo': 'attached_assets/PRODOTTI/NOVAMOBILI/idVzTltcdc_1750753949777.png',
        'count': '12 divani',
        'description': 'Innovazione e design moderno si incontrano in questa collezione di divani dalle linee pulite e funzionali.',
        'stats': {
            'modelli': '12',
            'serie': '3',
            'design': 'Mod'
        },
        'divani': [
            'Velvet', 'Reef', 'Kubì', 'Suite', 'Kubì Plus', 'Velvet Plus', 'Reef 2.0', 'Airy', 'Echo', 'Filo', 'Joy', 'Frame'
        ]
    },
    'cattelan': {
        'name': 'Cattelan',
        'logo': 'attached_assets/PRODOTTI/CATTELAN/b22515a0-bc14-47bd-9a27-8b7e8629b556.jpg',
        'count': '14 divani',
        'description': 'Design internazionale e qualità artigianale. Collezione di divani che unisce eleganza e comfort per ambienti raffinati.',
        'stats': {
            'modelli': '14',
            'stili': '3',
            'qualita': 'Elite'
        },
        'divani': [
            'Bristol', 'New York', 'Soho', 'Velvet', 'Monaco', 'Shangai', 'Glamour', 'Harlem', 'Domino', 'York', 'Oregon', 'Miami', 'London', 'Kensington'
        ]
    },
    'cubo-rosso': {
        'name': 'Cubo Rosso',
        'logo': 'attached_assets/images.jpeg',
        'count': '13 divani',
        'description': 'Novità 2025! Collezione innovativa con design all\'avanguardia e comfort rivoluzionario.',
        'stats': {
            'modelli': '13',
            'novita': '2025',
            'design': 'Innov'
        },
        'divani': [
            'Alcor', 'Bonny', 'Twix', 'Sax', 'Alita', 'Tempo', 'Diesis', 'Elba', 'Libeccio', 'Atria', 'Gordon', 'Alira', 'Ares'
        ]
    }
}

# Template per le pagine dei brand
BRAND_PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Divani {brand_name} - Muzi Design</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Playfair+Display:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .hero {{
            background: none;
            color: var(--primary);
            text-align: center;
            height: 400px;
            min-height: 400px;
            max-height: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
        }}
        .hero-decor {{
            position: absolute;
            width: 100%;
            height: 100%;
            left: 0;
            top: 0;
            pointer-events: none;
            z-index: 1;
        }}
        .hero-decor .circle {{
            position: absolute;
            border-radius: 50%;
            background: rgba(52, 152, 219, 0.28);
        }}
        .hero-decor .circle1 {{
            width: 240px; height: 240px;
            left: 4%; top: 10%;
        }}
        .hero-decor .circle2 {{
            width: 110px; height: 110px;
            right: 10%; top: 38%;
        }}
        .hero-decor .circle3 {{
            width: 80px; height: 80px;
            left: 22%; bottom: 12%;
        }}
        .hero-decor .line {{
            position: absolute;
            width: 140px; height: 6px;
            background: rgba(52, 152, 219, 0.32);
            border-radius: 3px;
        }}
        .hero-decor .line1 {{
            left: 32%; top: 14%; transform: rotate(-18deg);
        }}
        .hero-decor .line2 {{
            right: 16%; bottom: 18%; transform: rotate(12deg);
        }}
        .hero-box {{
            background: #1a3a4c;
            border-radius: 18px;
            box-shadow: 0 2px 16px rgba(0,0,0,0.08);
            padding: 38px 32px 28px 32px;
            max-width: 520px;
            margin: 0 auto;
            display: inline-block;
            position: relative;
            z-index: 2;
        }}
        .hero-box h1,
        .hero-box p {{
            color: #fff;
        }}
        .hero-box h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            margin-bottom: 18px;
        }}
        .hero-box p {{
            font-size: 1.2rem;
            margin: 0;
        }}
        @media (max-width: 768px) {{
            .hero {{
                height: 220px;
                min-height: 220px;
                max-height: 220px;
            }}
            .hero-box {{
                padding: 22px 10px 16px 10px;
            }}
            .hero-box h1 {{
                font-size: 2rem;
            }}
            .hero-box p {{
                font-size: 1rem;
            }}
        }}

        .products {{
            padding: 60px 0;
        }}

        .products-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }}

        .product-image img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            transition: var(--transition);
        }}

        .product-card {{
            background: white;
            border-radius: var(--radius);
            overflow: hidden;
            box-shadow: var(--shadow);
            transition: var(--transition);
        }}

        .product-card:hover {{
            transform: translateY(-5px);
            box-shadow: var(--shadow-hover);
        }}

        .product-info {{
            padding: 20px;
            text-align: center;
        }}

        .product-title {{
            font-family: 'Playfair Display', serif;
            color: var(--primary);
            margin-bottom: 10px;
            font-size: 1.5rem;
        }}

        .product-description {{
            color: var(--gray);
            margin-bottom: 20px;
            line-height: 1.6;
        }}

        .btn {{
            display: inline-block;
            padding: 12px 30px;
            background: var(--primary);
            color: white;
            text-decoration: none;
            border-radius: var(--radius);
            transition: var(--transition);
        }}

        .btn:hover {{
            background: var(--secondary);
            transform: translateY(-2px);
        }}

        .brand-header {{
            background: #f8f9fa;
            padding: 40px 0;
            text-align: center;
            margin-bottom: 40px;
        }}

        .brand-logo {{
            max-width: 200px;
            margin-bottom: 20px;
        }}

        .brand-description {{
            max-width: 800px;
            margin: 0 auto;
            color: var(--gray);
            line-height: 1.6;
        }}
    </style>
</head>
<body>
    <!-- Header & Navigation -->
    <header class="modern-header fade-in">
        <div class="container">
            <nav class="modern-navbar">
                <a href="index.html" class="modern-logo">
                    <img src="attached_assets/logo.png" alt="Muzi Design">
                </a>
                <ul class="modern-nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="chi-siamo.html">Chi Siamo</a></li>
                    <li><a href="prodotti.html">Prodotti</a></li>
                    <li><a href="promozioni.html">Promozioni</a></li>
                    <li><a href="gallery.html">Gallery</a></li>
                    <li><a href="contatti.html">Contatti</a></li>
                </ul>
                <a href="contatti.html" class="modern-cta-btn">Prenota una visita</a>
                <button class="modern-mobile-toggle" aria-label="Apri menu">
                    <i class="fas fa-bars"></i>
                </button>
            </nav>
            <div class="modern-mobile-menu">
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="chi-siamo.html">Chi Siamo</a></li>
                    <li><a href="prodotti.html">Prodotti</a></li>
                    <li><a href="promozioni.html">Promozioni</a></li>
                    <li><a href="gallery.html">Gallery</a></li>
                    <li><a href="contatti.html">Contatti</a></li>
                </ul>
                <a href="contatti.html" class="modern-cta-btn-mobile"><span><i class="fas fa-calendar-check"></i> PRENOTA UNA VISITA</span></a>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-decor">
            <div class="circle circle1"></div>
            <div class="circle circle2"></div>
            <div class="circle circle3"></div>
            <div class="line line1"></div>
            <div class="line line2"></div>
        </div>
        <div class="hero-box">
            <h1>{brand_name}</h1>
            <p>{brand_description_short}</p>
        </div>
    </section>

    <!-- Brand Header -->
    <section class="brand-header">
        <div class="container">
            <img src="{brand_logo}" alt="{brand_name}" class="brand-logo">
            <p class="brand-description">
                {brand_description}
            </p>
        </div>
    </section>

    <!-- Products Section -->
    <section class="products">
        <div class="container">
            <div class="products-grid">
                {divani_cards}
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
                        <li><a href="index.html"><i class="fas fa-chevron-right"></i> Home</a></li>
                        <li><a href="chi-siamo.html"><i class="fas fa-chevron-right"></i> Chi Siamo</a></li>
                        <li><a href="brand-divani.html"><i class="fas fa-chevron-right"></i> Brand Divani</a></li>
                        <li><a href="prodotti.html"><i class="fas fa-chevron-right"></i> Prodotti</a></li>
                        <li><a href="promozioni.html"><i class="fas fa-chevron-right"></i> Promozioni</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>Brand Divani</h3>
                    <ul class="footer-links">
                        <li><a href="egoitaliano-divani.html"><i class="fas fa-chevron-right"></i> Egoitaliano</a></li>
                        <li><a href="novamobili-divani.html"><i class="fas fa-chevron-right"></i> Novamobili</a></li>
                        <li><a href="cattelan-divani.html"><i class="fas fa-chevron-right"></i> Cattelan</a></li>
                        <li><a href="cubo-rosso-divani.html"><i class="fas fa-chevron-right"></i> Cubo Rosso</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>Contatti</h3>
                    <ul class="footer-links">
                        <li><a href="contatti.html"><i class="fas fa-map-marker-alt"></i> Via Artena 54, Valmontone (RM)</a></li>
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

    <script src="script.js"></script>
</body>
</html>'''

def create_divano_card(divano_name):
    """Crea una card per un divano"""
    # Descrizioni personalizzate per ogni divano
    descriptions = {
        'Astoria': 'Design elegante e comfort superiore per il tuo salotto.',
        'Babouche': 'Stile orientale incontra design italiano contemporaneo.',
        'Bebop': 'Ritmo e movimento nel design del comfort.',
        'Beverly': 'Eleganza hollywoodiana per ambienti raffinati.',
        'Bliss': 'Felicità e serenità nel comfort quotidiano.',
        'Candice': 'Dolcezza e grazia nel design contemporaneo.',
        'Caveoso': 'Forme organiche e comfort naturale.',
        'Dusk': 'Atmosfera crepuscolare e relax serale.',
        'Eros': 'Passione e seduzione nel design.',
        'Feng': 'Armonia e equilibrio secondo la filosofia orientale.',
        'Funny': 'Allegria e divertimento nel comfort.',
        'Gaia': 'Connessione con la natura e la terra.',
        'Giada': 'Purezza e preziosità come la pietra omonima.',
        'Gloria': 'Splendore e magnificenza nel design.',
        'Ludo': 'Gioco e divertimento per la famiglia.',
        'Lego': 'Modularità e versatilità nel design.',
        'Looming': 'Presenza imponente e design distintivo.',
        'Mavie': 'La mia vita, il mio comfort personalizzato.',
        'Martine': 'Eleganza francese e raffinatezza.',
        'Masù': 'Design giapponese e minimalismo zen.',
        'Momo': 'Semplicità e purezza nel design.',
        'Namy': 'Personalità e carattere distintivo.',
        'Nefele': 'Leggerezza e morbidezza delle nuvole.',
        'Nora': 'Luce e luminosità nel design.',
        'Oliver': 'Classicità britannica e raffinatezza.',
        'Pacha': 'Forme organiche e comfort naturale.',
        'Piper': 'Musicalità e ritmo nel design.',
        'Plaza': 'Spazio urbano e design contemporaneo.',
        'Pongo': 'Flessibilità e adattabilità nel design.',
        'Sauvanne': 'Eleganza francese e raffinatezza.',
        'Selfy': 'Design contemporaneo per l\'era digitale.',
        'Shai': 'Regalità e maestosità nel design.',
        'Sofia': 'Saggezza e intelligenza nel design.',
        'Tate': 'Arte e cultura nel design contemporaneo.',
        'Vera': 'Verità e autenticità nel design.',
        'Viola': 'Musicalità e armonia nel design.',
        'Zara': 'Stile moderno e design contemporaneo.',
        'Zazou': 'Allegria e vivacità nel design.',
        'Zoe': 'Vita e vitalità nel design contemporaneo.',
        'Zoomy': 'Velocità e dinamismo nel design.',
        'Velvet': 'Velluto e morbidezza nel comfort.',
        'Reef': 'Design marino e relax oceanico.',
        'Kubì': 'Forme geometriche e design moderno.',
        'Suite': 'Lusso e comfort per ambienti esclusivi.',
        'Kubì Plus': 'Versione ampliata di Kubì, comfort extra.',
        'Velvet Plus': 'Variante luxury, tessuti esclusivi.',
        'Reef 2.0': 'Evoluzione di Reef, ancora più comfort.',
        'Airy': 'Design leggero, struttura sottile.',
        'Echo': 'Linee essenziali, stile moderno.',
        'Filo': 'Struttura sottile, design minimalista.',
        'Joy': 'Divano giovane, colorato, perfetto.',
        'Frame': 'Struttura a vista, design industriale.',
        'Bristol': 'Design moderno, ampie sedute, comfort elegante, stile internazionale.',
        'New York': 'Look urbano, struttura sottile, dettagli sartoriali, grande versatilità.',
        'Soho': 'Geometrie pulite, moduli componibili, ideale per ambienti contemporanei.',
        'Velvet': 'Morbidezza assoluta, linee eleganti, estetica accogliente, materiali pregiati.',
        'Monaco': 'Lusso sobrio, proporzioni generose, braccioli bassi, finiture artigianali.',
        'Shangai': 'Stile orientale, design compatto, finiture sofisticate, comfort strutturato.',
        'Glamour': 'Sofisticato, elegante, schienale alto, ideale per living ricercati.',
        'Harlem': 'Componibile, seduta profonda, tessuti pregiati, perfetto per ambienti moderni.',
        'Domino': 'Modulabile, piede nascosto, linee pure, schienale basso e comodo.',
        'York': 'Compatto, schienale inclinato, bracciolo integrato, estetica sobria e chic.',
        'Oregon': 'Linee arrotondate, struttura avvolgente, ideale per relax domestico elegante.',
        'Miami': 'Design minimale, piedini sottili, volumi leggeri, spirito giovane e urbano.',
        'London': 'Sofisticato, proporzioni armoniose, ideale per spazi eleganti e classici.',
        'Kensington': 'Estetica inglese, materiali di pregio, perfetto per ambienti raffinati.'
    }
    
    description = descriptions.get(divano_name, f'Design moderno e confortevole per {divano_name}.')
    
    return f'''<!-- {divano_name} -->
                <div class="product-card">
                    <div class="product-image">
                        <img src="attached_assets/images.jpeg" alt="{divano_name}">
                    </div>
                    <div class="product-info">
                        <h3 class="product-title">{divano_name}</h3>
                        <p class="product-description">{description}</p>
                        <a href="divani/{divano_name.lower().replace(' ', '-').replace('ù', 'u').replace('ì', 'i').replace('2.0', '2')}.html" class="btn">Scopri di più</a>
                    </div>
                </div>'''

def create_brand_page(brand_key, brand_data):
    """Crea una pagina per un brand specifico"""
    filename = f"{brand_key}-divani.html"
    
    # Genera le card dei divani
    divani_cards = ""
    for divano in brand_data['divani']:
        divani_cards += create_divano_card(divano) + "\n"
    
    # Descrizione breve per l'hero
    brand_description_short = brand_data['description'].split('.')[0] + '.'
    
    # Genera il contenuto della pagina
    content = BRAND_PAGE_TEMPLATE.format(
        brand_name=brand_data['name'],
        brand_logo=brand_data['logo'],
        brand_description=brand_data['description'],
        brand_description_short=brand_description_short,
        divani_cards=divani_cards
    )
    
    # Scrivi il file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Creato: {filename}")

def main():
    """Funzione principale per creare tutte le pagine dei brand"""
    print("Creazione pagine per i brand di divani...")
    
    # Crea ogni pagina brand
    for brand_key, brand_data in BRANDS_DATA.items():
        try:
            create_brand_page(brand_key, brand_data)
        except Exception as e:
            print(f"Errore nella creazione di {brand_key}-divani.html: {e}")
    
    print("Creazione completata!")

if __name__ == "__main__":
    main() 