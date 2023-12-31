import io, re

with io.open("mad_libs_template.txt", "r", encoding="UTF-8") as template_file:
    template = template_file.read()

    keywords_regex = re.compile(r"(PRZYMIOTNIK|CZASOWNIK|RZECZOWNIK)")
    keywords = keywords_regex.findall(template)
    for keyword in keywords:
        template = template.replace(keyword, input(f"Podaj {keyword.lower()}: "), 1)

    print(template)

    template_file.close()



