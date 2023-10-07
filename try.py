while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("You must enter a number!\n")

while True:
    Sentence = input("Enter a sentence: ")
    try:
        int(Sentence)
        print("You must enter a sentence!\n")
    except ValueError:
        break;

print()
print((Sentence + " ") * number)
