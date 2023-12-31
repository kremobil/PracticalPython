import pyperclip

text = pyperclip.paste()

bulletPointList = []

for point in text.split("\n"):
    bulletPointList.append(f"* {point.strip()}")

pyperclip.copy("\n".join(bulletPointList))