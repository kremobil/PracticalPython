import os
from pathlib import Path

folder_to_search = Path(input("Podaj ścieżkę folderu który chcesz przeszukać: "))

print(folder_to_search)
if not folder_to_search.exists() and not folder_to_search.is_dir():
    print("Podana ścieżka nie istnieje bądź nie jest folderem")
while True:
    try:
        mb = float(input("Podaj dolną granicę plików w mb: "))
        break
    except ValueError:
        print("Podana wartość nie jest liczbą")

for root, dirs, files in os.walk(folder_to_search):
    root_path = Path(root)
    for file in files:
        file_path = root_path / file
        if os.path.getsize(file_path) >= (1024 * 1024 * mb):
            print(f"Plik {file_path}\n>> {round(os.path.getsize(file_path) / (1024 * 1024) * 100)/100}MB <<\n\n")