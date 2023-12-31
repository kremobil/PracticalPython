from contact_data import FindElementsInText

text1 = FindElementsInText("aby się z nami skontaktować zadzwoń pod numer +48 505 005 917 lub 505 166 523 do Batwowowoman. Ale ten żart był śmieszny hahahaha")
print(f"znaleziono numer telefonu: {text1.find_phone_number()}")
print(f"Batmanie teksicie wystąpił: {text1.find_batmans_accesories()} ")
print(f"Batmanie teksicie wystąpił: {text1.find_laugh(True)} w którym zajdowało sie również {text1.find_laugh(False)}")
text2 = FindElementsInText("Wczoraj w nocy Batman wyjechał w batmobilu do mężczyzny o numerze telefonu 012 304 893")
print(f"znaleziono numer telefonu: {text1.find_phone_number()}")
print(f"Batmanie teksicie wystąpił: {text1.find_batmans_accesories()} ")

print(f"Wszystkie numery w tekscie 1 to: {', '.join(text1.find_all_phone_numbers())}")

shopping_list = FindElementsInText("""Zakupy na poniedziałek:
- 3 jajka
- 8 bananów
- zupka chińska
- 4 dynie
""")

print(f"na liście zakupów znaleziono {', '.join(shopping_list.find_all_listitems())}")
print(f"na liście zakupów znaleziono {', '.join(shopping_list.find_all_letters(find_vowels=True))}")
print(f"na liście zakupów znaleziono {', '.join(shopping_list.find_all_letters(find_vowels=False))}")
print(f"na liście zakupów znaleziono {shopping_list.find_ending_or_beginning('Zakupy')}")