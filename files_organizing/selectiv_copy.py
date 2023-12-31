import shutil, os
from pathlib import Path

folder = Path(input("Podaj ścieżkę do folderu z którego chcesz wykonać kopię: "))

if not folder.exists():
    print("Podana ścieżka nie istnieje")
    exit()

extension = input("podaj rozszeżenia które chcesz skopiować (np. pdf, txt): ")

number = 1
new_folder_name = folder / f"{folder.absolute().name}(.{extension})"
if not new_folder_name.exists():
    new_folder_name.mkdir()


for folder_name, subfolders, files in os.walk(folder):
    current_folder = folder
    if folder_name != folder.absolute().name:
        current_folder = folder / folder_name

    if current_folder == new_folder_name:
        continue

    for file in current_folder.glob("*." + extension):
        shutil.copy(file, new_folder_name / file.name)
