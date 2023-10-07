def represent_list(list):
    representation = ""
    for element in list:
        if element == list[-2]:
            representation += f"{element} i "
            continue
        if element == list[-1]:
            representation += str(element)
            return representation
        representation += f"{element}, "
        print(representation)

print(represent_list(['jabłka', 'banany', ["a", "b", "c"]]))