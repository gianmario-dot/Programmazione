import os

cartella_origine = r"C:\University"
file_output = r"C:\Users\gianm\OneDrive\Documenti\output_unito.txt"

# Apri il file di destinazione in modalità scrittura
with open(file_output, 'w', encoding='utf-8') as outfile:
    for root, dirs, files in os.walk(cartella_origine):
        for file in files:
            # Filtra solo i file che contengono testo leggibile
            if file.endswith(('.txt', '.py', '.csv', '.md', '.json')):
                percorso_completo = os.path.join(root, file)
                
                # Aggiunge un'intestazione chiara per far distinguere i file all'IA
                outfile.write(f"\n\n{'='*50}\n")
                outfile.write(f"NOME FILE: {file}\n")
                outfile.write(f"PERCORSO ORIGINALE: {percorso_completo}\n")
                outfile.write(f"{'='*50}\n\n")
                
                # Legge il contenuto e lo aggiunge al file unico
                with open(percorso_completo, 'r', encoding='utf-8', errors='ignore') as infile:
                    outfile.write(infile.read())

print(f"File unito con successo in: {file_output}")