import pyinputplus as pyip

prices = {
    "Pszenny": 2.99,
    "Biały": 1.99,
    "Na zakwasie": 4.49,
    "Kurczak": 4.29,
    "Indyk": 3.69,
    "Szynka": 2.99,
    "Tofu": 5.99,
    "cheddar": 3.49,
    "szwajcarski": 6.25,
    "mozzarella": 4.19,
    "musztarda": 1,
    "majonez": 1,
    "sałata": 1.50,
    "pomidor": 1.50
}

ingredients = []

ingredients += [pyip.inputMenu([
    "Pszenny",
    "Biały",
    "Na zakwasie"
], prompt="Wybierz rodzaj chleba:\n", numbered=True)]

ingredients += [pyip.inputMenu([
    "Kurczak",
    "Indyk",
    "Szynka",
    "Tofu"
], prompt="Wybierz rodzaj białka:\n", numbered=True)]

if(pyip.inputYesNo("Czy chcesz dodać ser? (tak/nie)\n", yesVal="Tak", noVal="Nie") == "Tak"):
    ingredients += [pyip.inputMenu(["cheddar", "szwajcarski", "mozzarella"], prompt="Jaki rodzaj sera chcesz dodać:\n", numbered=True)]

ingredients += [ingredient for ingredient in ["musztarda", "majonez", "sałata", "pomidor"] if pyip.inputYesNo(f"Czy chcesz dodać {ingredient}? (tak/nie)", yesVal="tak", noVal="nie") == "tak"]

prices = [prices[ingredient] for ingredient in ingredients]

sandwich_number = pyip.inputInt("Ile kanapek chcesz zamówić: ")

print(f"Do zapłaty: {round(sandwich_number * sum(prices), 2)}zł")

