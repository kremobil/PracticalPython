import random

guess = ''
while guess not in ('orzeł', 'reszka'):
    print('Odgadnij wynik rzutu monetą! Wpisz orzeł lub reszka: ')
    guess = input()

toss = ('orzeł', 'reszka')[random.randint(0, 1)]
if toss == guess:
    print('Odgadłeś!')
else:
    while guess not in ('orzeł', 'reszka'):
        print('Nie udało ci się spróbuj ponownie! ')
        guess = input()
    if toss == guess:
        print('Odgadłeś!')
    else:
        print('Nie udało ci się! Naprawdę kiepsko ci dziś idzie!')