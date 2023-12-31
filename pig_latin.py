print("Podaj tekst w j. angielskim do zamiany na świńską łacinę")
text = input()

VOWELS = ('a', 'e', 'i', 'o', 'u')

pig_latin = []

for word in text.split():
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
        if len(word) == 0:
            pig_latin.append(prefix_non_letters)
            continue

        suffix_non_letters = ''
        while not word[-1].isalpha():
            suffix_non_letters += word[-1]
            word = word[:-1]
        
        wasUpper = word.isupper()
        wasTitle = word.istitle()

        word = word.lower()

        prefix_constants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefix_constants += word[0]
            word = word[1:]

        if prefix_constants != '':
            word += prefix_constants + 'ay'

        else:
            word += 'yay'

        if wasUpper:
            word = word.upper()

        if wasTitle:
            word = word.title()

        pig_latin.append(prefix_non_letters + word + suffix_non_letters)

print(" ".join(pig_latin))
        