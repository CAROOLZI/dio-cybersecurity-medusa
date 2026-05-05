# Script para gerar wordlist focada em variações de nomes conhecidos
usuarios = ['admin', 'carolina', 'root']
anos = ['2024', '2025', '2026']

with open('wordlist_custom.txt', 'w') as f:
    for user in usuarios:
        for ano in anos:
            f.write(f"{user}{ano}\n")
            f.write(f"{user}@{ano}\n")
print("Wordlist gerada com sucesso!")
