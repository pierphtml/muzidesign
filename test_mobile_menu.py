#!/usr/bin/env python3
import os
import re

def check_html_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    problems = []
    # Cerca toggle e menu
    has_modern_toggle = 'modern-mobile-toggle' in html
    has_modern_menu = 'modern-mobile-menu' in html
    has_super_toggle = 'super-mobile-toggle' in html
    has_super_menu = 'super-mobile-menu' in html
    # Script universale
    script_count = len(re.findall(r'// Script universale per menu mobile', html))
    # Segnala problemi
    if (has_modern_toggle or has_super_toggle):
        if not (has_modern_menu or has_super_menu):
            problems.append('Toggle presente ma menu mancante')
    if (has_modern_menu or has_super_menu):
        if not (has_modern_toggle or has_super_toggle):
            problems.append('Menu presente ma toggle mancante')
    if (has_modern_toggle or has_super_toggle or has_modern_menu or has_super_menu):
        if script_count == 0:
            problems.append('Script universale mancante')
        if script_count > 1:
            problems.append('Script universale duplicato')
    return problems

def main():
    totali = 0
    problematici = {}
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                totali += 1
                problems = check_html_file(path)
                if problems:
                    problematici[path] = problems
    print(f"\n=== REPORT MENU MOBILE ===\n")
    if not problematici:
        print("Tutti i file sono OK!")
    else:
        for path, problems in problematici.items():
            print(f"{path}:")
            for p in problems:
                print(f"  - {p}")
        print(f"\nTotale file problematici: {len(problematici)} su {totali}")

if __name__ == '__main__':
    main() 