def print_table(table: list) -> None:
    """Prints the table to the console"""
    formated = [[] for _ in range(len(table[0]))]
    for row_idx, row in enumerate(table):
        width = max(map(len, row))
        for element_idx, element in enumerate(row):
            formated[element_idx].append(element.rjust(width))

    for row in formated:
        print(" | ".join(row))
        print("-|-".join(map(lambda x: "-" * len(x), row)))

    


print_table([
    ["jabłka", "pomarańcze", "wiśnie", "banany"], 
    ["Alicja", "Bartek", "Celina", "Dawid"],
    ["psy", "koty", "łosie", "gęsi"]
    ])