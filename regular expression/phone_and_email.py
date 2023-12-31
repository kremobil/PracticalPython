import re, pyperclip

phone_regex = re.compile(r'''
(\+?\d{2})? #optional country code eg. +48
(\s|-|\.)?  #country separator
(\d{3})     #first 3 digits
(\s|-|\.)   #separator
(\d{3})     #second 3 digits
(\s|-|\.)   #separator
(\d{3})     #third 3 digits
''', re.VERBOSE)

email_regex = re.compile(r'''
([a-zA-Z0-9._-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,3}))
''', re.VERBOSE)

text = str(pyperclip.paste())

matches = list(map(lambda x: x[0], email_regex.findall(text))) +\
          list(map(lambda x: "".join(x).replace("-", " ").replace(".", " "), phone_regex.findall(text)))

if matches:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print(pyperclip.paste())
else:
    print("No matches found")
