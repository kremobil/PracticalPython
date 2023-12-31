def ask_question(min, max):
    question = input("Enter a number between {} and {}: ".format(min, max))

    try:
        answer = int(answer)
    except ValueError:
