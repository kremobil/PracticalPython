import re, io
from pathlib import Path

path = input("Podaj ścieżkę do katalogu: ")
path = Path(path)

if path.exists():
    regex = input("Podaj wyrażenie regularne do wyszukania w plikach")
    find_regex = re.compile(regex)
    for file in path.glob("*.txt"):
        with io.open(file, "r", encoding="UTF-8") as file:
            print(find_regex.findall(file.read()))

else:
    print("Katalog nie istnieje!")