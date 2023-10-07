import random

def count_6_streaks(throws):
    streak = 0
    values = [0, 0]
    for index in range(len(throws)-1):
        if throws[index] == throws[index + 1]:
            streak += 1
        else:
            streak = 0
        if streak >= 6 and throws[index] == "O":
            values[0] += 1
        elif streak >= 6 and throws[index] == "R":
            values[1] += 1
    return values

global_score = [0, 0]
for experimet_number in range(10000):
    throws = ["R" if random.randint(0, 1) == 1 else "O" for a in range(100)]
    score = count_6_streaks(throws)
    global_score[0] += score[0]
    global_score[1] += score[1]

print(global_score)
print(f"Procent Orłów: {global_score[0] / 1000000}%, Procent Reszek: {global_score[1] / 1000000}%")