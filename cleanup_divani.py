#!/usr/bin/env python3
import os
from pathlib import Path

# Lista dei divani autorizzati per brand
AUTHORIZED_DIVANI = {
    'egoitaliano': [
        'Astoria', 'Babouche', 'Bebop', 'Beverly', 'Bliss', 'Candice', 'Caveoso', 'Dusk', 'Eros', 'Feng',
        'Funny', 'Gaia', 'Giada', 'Gloria', 'Ludo', 'Lego', 'Looming', 'Mavie', 'Martine', 'Masù',
        'Momo', 'Namy', 'Nefele', 'Nora', 'Oliver', 'Pacha', 'Piper', 'Plaza', 'Pongo', 'Sauvanne',
        'Selfy', 'Shai', 'Sofia', 'Tate', 'Vera', 'Viola', 'Zara', 'Zazou', 'Zoe', 'Zoomy'
    ],
    'novamobili': [
        'Velvet', 'Reef', 'Kubì', 'Suite', 'Kubì Plus', 'Velvet Plus', 'Reef 2.0', 'Airy', 'Echo', 'Filo', 'Joy', 'Frame'
    ],
    'cinquanta3': [
        'Cross', 'Dallas', 'Daniel', 'Darwin', 'Dorian', 'Dylan', 'Hoops'
    ],
    'cubo-rosso': [
        'Alcor', 'Bonny', 'Twix', 'Sax', 'Alita', 'Tempo', 'Diesis', 'Elba', 'Libeccio', 'Atria', 'Gordon', 'Alira', 'Ares'
    ]
}

def normalize_name(name):
    """Normalizza il nome del divano per il confronto"""
    # Rimuovi estensioni e normalizza caratteri speciali
    name = name.replace('.html', '').replace('-', ' ').replace('_', ' ')
    
    # Mappatura per caratteri speciali
    replacements = {
        'ù': 'u',
        'ì': 'i',
        '2.0': '2',
        'plus': 'plus'
    }
    
    for old, new in replacements.items():
        name = name.replace(old, new)
    
    return name.lower().strip()

def get_all_authorized_divani():
    """Ottiene tutti i divani autorizzati da tutti i brand"""
    all_divani = []
    for brand_divani in AUTHORIZED_DIVANI.values():
        all_divani.extend(brand_divani)
    return all_divani

def cleanup_divani_folder():
    """Elimina i file dei divani non autorizzati"""
    divani_folder = Path('divani')
    
    if not divani_folder.exists():
        print("Cartella 'divani' non trovata!")
        return
    
    # Ottieni tutti i divani autorizzati
    authorized_divani = get_all_authorized_divani()
    authorized_normalized = [normalize_name(divano) for divano in authorized_divani]
    
    print(f"Divani autorizzati: {len(authorized_divani)}")
    print("Lista divani autorizzati:")
    for divano in authorized_divani:
        print(f"  - {divano}")
    
    # Conta i file nella cartella
    html_files = list(divani_folder.glob('*.html'))
    print(f"\nFile trovati nella cartella divani: {len(html_files)}")
    
    # Trova i file da eliminare
    files_to_delete = []
    files_to_keep = []
    
    for file_path in html_files:
        file_name = file_path.stem  # Nome senza estensione
        normalized_name = normalize_name(file_name)
        
        # Controlla se il file corrisponde a un divano autorizzato
        is_authorized = False
        for authorized in authorized_normalized:
            if normalized_name == authorized:
                is_authorized = True
                break
        
        if is_authorized:
            files_to_keep.append(file_path)
        else:
            files_to_delete.append(file_path)
    
    print(f"\nFile da mantenere: {len(files_to_keep)}")
    print(f"File da eliminare: {len(files_to_delete)}")
    
    if files_to_delete:
        print("\nFile che verranno eliminati:")
        for file_path in files_to_delete:
            print(f"  - {file_path.name}")
        
        # Chiedi conferma
        response = input("\nProcedere con l'eliminazione? (y/N): ")
        if response.lower() == 'y':
            deleted_count = 0
            for file_path in files_to_delete:
                try:
                    file_path.unlink()
                    print(f"Eliminato: {file_path.name}")
                    deleted_count += 1
                except Exception as e:
                    print(f"Errore nell'eliminazione di {file_path.name}: {e}")
            
            print(f"\nEliminazione completata! {deleted_count} file eliminati.")
        else:
            print("Eliminazione annullata.")
    else:
        print("\nNessun file da eliminare. Tutti i divani sono autorizzati.")

def main():
    """Funzione principale"""
    print("Pulizia cartella divani - Eliminazione divani non autorizzati")
    print("=" * 60)
    
    cleanup_divani_folder()

if __name__ == "__main__":
    main() 