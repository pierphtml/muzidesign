#!/usr/bin/env python3
"""
Script per pulire tutti gli script duplicati/vecchi del menu mobile e lasciare solo lo script universale dopo script.js.
"""
import os
import re

UNIVERSAL_MENU_SCRIPT = '''    <script>
        // Script universale per menu mobile moderno e super
        document.addEventListener('DOMContentLoaded', function() {
            // Modern
            var modernToggle = document.querySelector('.modern-mobile-toggle');
            var modernMenu = document.querySelector('.modern-mobile-menu');
            var modernClose = document.querySelector('.modern-mobile-menu .close-mobile-menu');
            if (modernToggle && modernMenu) {
                if (modernClose) {
                    modernClose.addEventListener('click', function() {
                        modernMenu.classList.remove('open');
                        document.body.classList.remove('menu-open');
                        var icon = modernToggle.querySelector('i');
                        if (icon) {
                            icon.classList.add('fa-bars');
                            icon.classList.remove('fa-times');
                        }
                    });
                }
                modernToggle.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    modernMenu.classList.toggle('open');
                    document.body.classList.toggle('menu-open');
                    var icon = this.querySelector('i');
                    if (icon) {
                        if (modernMenu.classList.contains('open')) {
                            icon.classList.remove('fa-bars');
                            icon.classList.add('fa-times');
                        } else {
                            icon.classList.remove('fa-times');
                            icon.classList.add('fa-bars');
                        }
                    }
                });
                document.querySelectorAll('.modern-mobile-menu a').forEach(function(link) {
                    link.addEventListener('click', function() {
                        modernMenu.classList.remove('open');
                        document.body.classList.remove('menu-open');
                        var icon = modernToggle.querySelector('i');
                        if (icon) {
                            icon.classList.add('fa-bars');
                            icon.classList.remove('fa-times');
                        }
                    });
                });
            }
            // Super
            var superToggle = document.querySelector('.super-mobile-toggle');
            var superMenu = document.querySelector('.super-mobile-menu');
            var superClose = document.querySelector('.super-mobile-menu .close-mobile-menu');
            if (superToggle && superMenu) {
                if (superClose) {
                    superClose.addEventListener('click', function() {
                        superMenu.classList.remove('open');
                        superToggle.classList.remove('open');
                        document.body.classList.remove('menu-open');
                        var bars = superToggle.querySelector('.fa-bars');
                        var times = superToggle.querySelector('.fa-times');
                        if (bars) bars.style.opacity = 1;
                        if (times) times.style.opacity = 0;
                    });
                }
                superToggle.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    superMenu.classList.toggle('open');
                    superToggle.classList.toggle('open');
                    if (superMenu.classList.contains('open')) {
                        document.body.classList.add('menu-open');
                    } else {
                        document.body.classList.remove('menu-open');
                    }
                    var bars = superToggle.querySelector('.fa-bars');
                    var times = superToggle.querySelector('.fa-times');
                    if (superToggle.classList.contains('open')) {
                        if (bars) bars.style.opacity = 0;
                        if (times) times.style.opacity = 1;
                    } else {
                        if (bars) bars.style.opacity = 1;
                        if (times) times.style.opacity = 0;
                    }
                });
                var closeBtn = document.querySelector('.super-mobile-menu-close');
                if (closeBtn) {
                    closeBtn.addEventListener('click', function(e) {
                        e.stopPropagation();
                        superMenu.classList.remove('open');
                        superToggle.classList.remove('open');
                        document.body.classList.remove('menu-open');
                        var bars = superToggle.querySelector('.fa-bars');
                        var times = superToggle.querySelector('.fa-times');
                        if (bars) bars.style.opacity = 1;
                        if (times) times.style.opacity = 0;
                    });
                }
                superMenu.addEventListener('click', function(e) {
                    if (e.target === superMenu) {
                        superMenu.classList.remove('open');
                        superToggle.classList.remove('open');
                        document.body.classList.remove('menu-open');
                        var bars = superToggle.querySelector('.fa-bars');
                        var times = superToggle.querySelector('.fa-times');
                        if (bars) bars.style.opacity = 1;
                        if (times) times.style.opacity = 0;
                    }
                });
            }
        });
    </script>'''

# Pattern per trovare tutti gli script vecchi/duplicati del menu mobile
SCRIPT_PATTERNS = [
    re.compile(r'<script>.*?Script inline per il menu mobile.*?</script>', re.DOTALL),
    re.compile(r'<script>.*?Mobile menu toggle.*?</script>', re.DOTALL),
    re.compile(r'<script>.*?super-mobile-toggle.*?</script>', re.DOTALL),
    re.compile(r'<script>.*?modern-mobile-toggle.*?</script>', re.DOTALL),
    re.compile(r'<script>.*?menu-open.*?</script>', re.DOTALL),
    re.compile(r'<script>.*?menu mobile.*?</script>', re.DOTALL),
    re.compile(r'<script>.*?menu hamburger.*?</script>', re.DOTALL),
    re.compile(r'<script>.*?Script universale per menu mobile moderno e super.*?</script>', re.DOTALL),
]

def clean_and_add_universal_script(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        # Rimuovi tutti gli script vecchi/duplicati
        for pat in SCRIPT_PATTERNS:
            content = pat.sub('', content)
        # Rimuovi spazi vuoti multipli
        content = re.sub(r'\n\s*\n', '\n', content)
        # Aggiungi lo script universale dopo script.js (se non già presente)
        if 'Script universale per menu mobile moderno e super' not in content:
            script_pattern = r'(<script src="[^"]*script\.js"></script>)'
            match = re.search(script_pattern, content)
            if match:
                replacement = match.group(1) + '\n' + UNIVERSAL_MENU_SCRIPT
                content = content.replace(match.group(1), replacement)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Errore nel processare {file_path}: {e}")
        return False

def main():
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    print(f"Trovati {len(html_files)} file HTML")
    updated_count = 0
    for file_path in html_files:
        if clean_and_add_universal_script(file_path):
            print(f"Pulito e aggiornato: {file_path}")
            updated_count += 1
    print(f"\nCompletato! Aggiornati {updated_count} file.")

if __name__ == "__main__":
    main() 