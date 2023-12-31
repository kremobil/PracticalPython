import re

class FindElementsInText:
    def __init__(self, text:str):
        self.text: str = text

    def find_phone_number(self):
        phone_number_regex = re.compile(r"(\+\d\d)? (\d{3} \d{3} \d{3})")
        mo = phone_number_regex.search(self.text)
        if mo:
            return mo.group()

    def find_all_phone_numbers(self):
        phone_number_regex = re.compile(r"(\+\d\d)? (\d{3} \d{3} \d{3})")
        mo:list = phone_number_regex.findall(self.text)
        if mo:
            mo = tuple(map(lambda x: " ".join(x), mo))
            return mo

    def find_batmans_accesories(self):
        batman_regex = re.compile(r"Bat((wo)*man|mobil|kopter)")
        bat = batman_regex.search(self.text)
        if bat:
            return bat.group()

    def find_all_batmans_accesories(self):
        batman_regex = re.compile(r"Bat((wo)*man|mobil|kopter)")
        bat = batman_regex.findall(self.text)
        if bat:
            return bat

    def find_laugh(self, greedy: bool = True):
        if greedy:
            laugh_regex = re.compile(r"(ha){3,5}")
        else:
            laugh_regex = re.compile(r"(ha){3,5}?")
        laugh = laugh_regex.search(self.text)
        if laugh:
            return laugh.group()

    def find_all_laughs(self, greedy: bool = True):
        if greedy:
            laugh_regex = re.compile(r"(ha){3,5}")
        else:
            laugh_regex = re.compile(r"(ha){3,5}?")
        laugh = laugh_regex.findall(self.text)
        if laugh:
            return laugh

    def find_all_listitems(self):
        items_regex = re.compile(r"\d+\s\w+")
        items = items_regex.findall(self.text)
        if items:
            return items

    def find_all_letters(self, find_vowels: bool = False):
        if find_vowels:
            vowel_regex = re.compile(r"[aeiouAIEOU]")
        else:
            vowel_regex = re.compile(r"[^aeiouAIEOU]")
        letters = vowel_regex.findall(self.text)
        if letters:
            return letters

    def find_ending_or_beginning(self, sentence_to_find: str, end_or_begin: str = "begin", ):
        if end_or_begin not in ["end", "begin"]:
            raise "bad argument error, end_or_begin could only be \"end\" or \"begin\""
        if end_or_begin == "begin":
            position_regex = re.compile(f"^{sentence_to_find}")
        elif end_or_begin == "end":
            position_regex = re.compile(f"{sentence_to_find}$")
        postion = position_regex.search(self.text)
        if postion:
            return postion.group()

    


