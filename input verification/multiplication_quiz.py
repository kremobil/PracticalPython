import pyinputplus as pyip
import random, time

number_of_questions = pyip.inputInt("Ile pytań chcesz otrzymać: ")
correct_answers = 0
operation = pyip.inputChoice(["dodawanie", "odejmowanie", "mnozenie", "dzielenie"], "Jakie działanie chcesz przetestować: ")
for question_number in range(number_of_questions):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)


    result = {"dodawanie": num1 + num2, "odejmowanie": num1 - num2, "mnozenie": num1 * num2, "dzielenie": num1 / num2}
    symbols = {"dodawanie": "+", "odejmowanie": "-", "mnozenie": "*", "dzielenie": "/"}

    prompt = f"#{question_number + 1}: {num1} {symbols[operation]} {num2} = "

    try:
        pyip.inputStr(prompt, allowRegexes=[f"^{result[operation]}$"], blockRegexes=[(".*", "Źle")], timeout=10, limit=3)
    except pyip.TimeoutException:
        print("Czas minął")
    except pyip.RetryLimitException:
        print("Zbyt wiele prób")
    else:
        print("Dobrze!")
        correct_answers += 1

        time.sleep(1)

print(f"Twój wynik to: {correct_answers} / {number_of_questions}")