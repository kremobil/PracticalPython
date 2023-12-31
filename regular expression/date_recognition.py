import re

date_regex = re.compile(r'''
(0[1-9]|[1-2][0-9]|3[0-1])    #day
(\s|-|\.|/)?                 #separator
(0[1-9]|1[0-2])               #month
(\s|-|\.|/)?                 #separator
([1-2][0-9]{3})               #year
''', re.VERBOSE)

text = input("Enter a sentence to find a date in it:\n")

matches = date_regex.findall(text)

dates = list(map(
    lambda x: {"day": int(x[0]), "month": int(x[2]), "year": int(x[4])},
    matches
))

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for date in dates:
    if date["month"] in (4, 6, 9, 11) and date["day"] == 31:
        date["day"] = 30
    if date["month"] == 2 and date["day"] > 28:
        if date["year"] % 4 == 0 and (not date["year"] % 100 == 0 or date["year"] % 400 == 0):
            date["day"] = 29
        else:
            date["day"] = 28

    print(f"- {date['day']} {months[date['month'] - 1]} {date['year']}")
