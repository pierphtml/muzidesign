#!/usr/bin/env python3
import os
import re

def update_close_button_in_file(file_path):
    """Aggiorna il pulsante di chiusura in un singolo file HTML"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Conta le modifiche
        changes = 0
        
        # Sostituisci la X con l'icona "indietro" nello script
        # Cerca diversi pattern possibili
        patterns = [
            (r'closeBtn\.innerHTML = \'×\';', 'closeBtn.innerHTML = \'<i class="fas fa-arrow-left"></i>\';'),
            (r'closeBtn\.innerHTML = "×";', 'closeBtn.innerHTML = "<i class=\\"fas fa-arrow-left\\"></i>";'),
            (r'innerHTML = \'×\';', 'innerHTML = \'<i class="fas fa-arrow-left"></i>\';'),
            (r'innerHTML = "×";', 'innerHTML = "<i class=\\"fas fa-arrow-left\\"></i>";')
        ]
        
        for pattern, replacement in patterns:
            if pattern in content:
                content = content.replace(pattern, replacement)
                changes += 1
        
        # Se ci sono modifiche, scrivi il file
        if changes > 0:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"✅ Aggiornato {file_path} ({changes} modifiche)")
            return True
        else:
            print(f"⏭️  Nessuna modifica necessaria in {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ Errore nel file {file_path}: {e}")
        return False

def add_universal_script_to_file(file_path):
    """Aggiunge lo script universale per il menu mobile se non presente"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Controlla se il file ha già lo script universale
        if '// Script universale per menu mobile' in content:
            return False
        
        # Controlla se il file ha un menu mobile
        has_modern_menu = '.modern-mobile-toggle' in content or '.super-mobile-toggle' in content
        if not has_modern_menu:
            return False
        
        # Trova la posizione per inserire lo script (prima della chiusura del body)
        if '</body>' in content:
            script_to_add = '''
    <script>
    // Script universale per menu mobile
    document.addEventListener('DOMContentLoaded', function() {
        // Gestione menu moderno (.modern-mobile-toggle)
        const modernToggle = document.querySelector('.modern-mobile-toggle');
        const modernMenu = document.querySelector('.modern-mobile-menu');
        
        if (modernToggle && modernMenu) {
            // Aggiungi X se non presente
            if (!modernMenu.querySelector('.close-mobile-menu')) {
                const closeBtn = document.createElement('button');
                closeBtn.className = 'close-mobile-menu';
                closeBtn.innerHTML = '<i class="fas fa-arrow-left"></i>';
                closeBtn.setAttribute('aria-label', 'Chiudi menu');
                modernMenu.insertBefore(closeBtn, modernMenu.firstChild);
            }
            
            modernToggle.addEventListener('click', function() {
                modernMenu.classList.toggle('open');
                document.body.classList.toggle('menu-open');
            });
            
            // Chiudi con X
            const closeBtn = modernMenu.querySelector('.close-mobile-menu');
            if (closeBtn) {
                closeBtn.addEventListener('click', function(e) {
                    e.stopPropagation();
                    modernMenu.classList.remove('open');
                    document.body.classList.remove('menu-open');
                });
            }
            
            // Chiudi cliccando fuori
            document.addEventListener('click', function(e) {
                if (!modernMenu.contains(e.target) && !modernToggle.contains(e.target)) {
                    modernMenu.classList.remove('open');
                    document.body.classList.remove('menu-open');
                }
            });
        }
        
        // Gestione menu super (.super-mobile-toggle)
        const superToggle = document.querySelector('.super-mobile-toggle');
        const superMenu = document.querySelector('.super-mobile-menu');
        
        if (superToggle && superMenu) {
            // Aggiungi X se non presente
            if (!superMenu.querySelector('.close-mobile-menu')) {
                const closeBtn = document.createElement('button');
                closeBtn.className = 'close-mobile-menu';
                closeBtn.innerHTML = '<i class="fas fa-arrow-left"></i>';
                closeBtn.setAttribute('aria-label', 'Chiudi menu');
                superMenu.insertBefore(closeBtn, superMenu.firstChild);
            }
            
            superToggle.addEventListener('click', function() {
                superMenu.classList.toggle('open');
                document.body.classList.toggle('menu-open');
            });
            
            // Chiudi con X
            const closeBtn = superMenu.querySelector('.close-mobile-menu');
            if (closeBtn) {
                closeBtn.addEventListener('click', function(e) {
                    e.stopPropagation();
                    superMenu.classList.remove('open');
                    document.body.classList.remove('menu-open');
                });
            }
            
            // Chiudi cliccando fuori
            document.addEventListener('click', function(e) {
                if (!superMenu.contains(e.target) && !superToggle.contains(e.target)) {
                    superMenu.classList.remove('open');
                    document.body.classList.remove('menu-open');
                }
            });
        }
        
        // Gestione menu vecchio (.mobile-toggle)
        const oldToggle = document.querySelector('.mobile-toggle');
        const oldMenu = document.querySelector('.nav-links');
        
        if (oldToggle && oldMenu) {
            oldToggle.addEventListener('click', function() {
                oldMenu.classList.toggle('active');
                document.body.classList.toggle('menu-open');
            });
            
            // Chiudi cliccando fuori
            document.addEventListener('click', function(e) {
                if (!oldMenu.contains(e.target) && !oldToggle.contains(e.target)) {
                    oldMenu.classList.remove('active');
                    document.body.classList.remove('menu-open');
                }
            });
        }
    });
    </script>'''
            
            content = content.replace('</body>', script_to_add + '\n</body>')
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            print(f"✅ Aggiunto script universale a {file_path}")
            return True
        
        return False
            
    except Exception as e:
        print(f"❌ Errore nel file {file_path}: {e}")
        return False

def main():
    """Funzione principale per aggiornare tutti i file HTML"""
    print("🔄 Aggiornamento pulsanti di chiusura menu mobile...")
    print("=" * 60)
    
    # Conta i file processati
    total_files = 0
    updated_files = 0
    script_added_files = 0
    
    # Cerca tutti i file HTML nella directory corrente e sottodirectory
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                total_files += 1
                
                # Prima aggiungi lo script universale se necessario
                if add_universal_script_to_file(file_path):
                    script_added_files += 1
                
                # Poi aggiorna il pulsante di chiusura
                if update_close_button_in_file(file_path):
                    updated_files += 1
    
    print("=" * 60)
    print(f"📊 Riepilogo:")
    print(f"   • File totali processati: {total_files}")
    print(f"   • File con script aggiunto: {script_added_files}")
    print(f"   • File con pulsante aggiornato: {updated_files}")
    print(f"   • File senza modifiche: {total_files - script_added_files - updated_files}")
    
    if script_added_files > 0 or updated_files > 0:
        print(f"\n✅ Aggiornamento completato!")
        if script_added_files > 0:
            print(f"   • Script universale aggiunto a {script_added_files} file")
        if updated_files > 0:
            print(f"   • Pulsante di chiusura aggiornato in {updated_files} file")
    else:
        print(f"\nℹ️  Nessun file è stato aggiornato.")

if __name__ == "__main__":
    main() 