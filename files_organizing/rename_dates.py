import shutil, os, re
from pathlib import Path

date_pattern = re.compile(
    r"""
    ^(.*?)
    ((0|1)?\d)
    (-|\s|.)
    ((0|1|2|3)?\d)
    (-|\s|.)
    ((19|20)?\d\d)
    (.*?)$
    """,
    re.VERBOSE
)

catalog =  Path(input("Podaj ścieżkę do katalogu: "))

accept_all = False

for american_file_name in os.listdir():
    file = date_pattern.search(american_file_name)

    if file == None:
        continue

    day = file.group(2)
    month = file.group(5)

    europe_file_name = american_file_name.replace(month, day).replace(day, month, 1)

    print(f"Zmiana nazwy pliku: {american_file_name} na: {europe_file_name}")

    if accept_all:
        shutil.move(catalog / american_file_name, catalog / europe_file_name)

        print("pomyślnie zmieniono nazwę pliku")
        continue

    print("Czy na pewno chcesz zmienić nazwy plików? tak/(nie)/wszystkie ")
    accept = input()
    if accept.lower() == "tak" or accept.lower() == "t":
        shutil.move(catalog / american_file_name, catalog / europe_file_name)

        print("pomyślnie zmieniono nazwę pliku")
    elif accept.lower() == "wszyskie" or accept.lower() == "w":
        accept_all = True
        shutil.move(catalog / american_file_name, catalog / europe_file_name)

        print("pomyślnie zmieniono nazwę pliku")

