import webbrowser, sys, pyperclip

adress = "https://www.google.pl/maps/place/"

if len(sys.argv) > 1:
    adress += " ".join(sys.argv[1:])
else:
    adress += pyperclip.paste()

webbrowser.open(adress)