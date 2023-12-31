import sys, json, pyperclip

# Importing our messages
messages = {}
f = open("clip_messages.json", "r")
messages = json.load(f)

if len(sys.argv) < 2:
    print("Wpisz: python mclip.py <kot wiadomości>; Aby skopiować wiadomość.")
    sys.exit()

if "--help" in sys.argv:
    print(
        """
1. Dodaj wiadomość: python mclip.py --add -key <kod wiadomości> -message "<wiadomość>"
2. Usuń wiadomość: python mclip.py --delete -key <kod wiadomości>
3. Kopiuj wiadomość: python mclip.py --copy -key <kod wiadomości>
4. Wyświetl wiadomość: python mclip.py --show -key <kod wiadomości>
5. Wyświetl wszyskie wiadomości: python mclip.py --showall
        """
        )

if "--add" in sys.argv:
    if not "-key" in sys.argv:
        print("brakuje klucza wiadomości.")
        sys.exit()
    if not "-message" in sys.argv:
        print("brakuje wiadomość.")
        sys.exit()
    
    key = sys.argv.index("-key") + 1
    message = sys.argv.index("-message") + 1

    key = sys.argv[key]
    message = sys.argv[message]

    if len(key) == 0 or len(message) == 0:
        print("klucz bądź wiadomość są puste.")
    
    if key in messages:
        print(f"wiadomość o kodzie {key} została zaktualizowana z {messages[key]} na {message}.")
    else:
        print("dodano wiadomość: " + message)
    messages.setdefault(key, message)
    messages[key] = message
    with open("clip_messages.json", "w") as f:
        json.dump(messages, f, indent=4)
    f.close()
    sys.exit()

if "--delete" in sys.argv:
    if not "-key" in sys.argv:
        print("brakuje klucza wiadomości.")
        sys.exit()
    
    key = sys.argv.index("-key") + 1
    key = sys.argv[key]

    if key in messages:
        messages.pop(key)
    
    with open("clip_messages.json", "w") as f:
        json.dump(messages, f, indent=4)
    f.close()
    sys.exit()

if "--showall" in sys.argv:
    print(f"\nObecnie dostępnych jest {len(messages)} wiadomości: \n")
    for idx, (key, value) in enumerate(messages.items()):
        print(f"{idx + 1}. klucz: \"{key}\", wiadomość: \"{value}\"\n")
    sys.exit()
    
if "--show" in sys.argv:
    if not "-key" in sys.argv:
        print("brakuje klucza wiadomości.")
        sys.exit()
    
    key = sys.argv.index("-key") + 1
    key = sys.argv[key]

    print(f"wiadomość o kodzie {key}: {messages[key]}")
    f.close()
    sys.exit()

if "--copy" in sys.argv:
    if not "-key" in sys.argv:
        print("brakuje klucza wiadomości.")
        sys.exit()
    
    key = sys.argv.index("-key") + 1
    key = sys.argv[key]

    if key in messages:
        pyperclip.copy(messages[key])
    else:
        print("wiadomość o takim kodzie nie istnieje")

    f.close()
    sys.exit()

    