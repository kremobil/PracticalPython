def collatz(number: int) -> int:
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

while True: 
    try:
        user_number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a number")

result = user_number

while result != 1:
    result = collatz(result)
    print(result)