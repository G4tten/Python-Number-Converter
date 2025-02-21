def roman_to_int(number):
    total = 0
    correct = True
    for i in number:
        if "CM" in number:
            total += 900
            number = number.replace("CM", "") #Rimuove il numero romano per assicurarsi che non ci siano intoppi nel successivo for
                                              #Quando ricomincia il ciclo siamo sicuri che non essendoci più un numero a doppia cifra andremo
                                              #a prendere direttamente il numero succssivo
        if "CD" in number:
            total += 400
            number = number.replace("CD", "")
        if "XC" in number:
            total += 90
            number = number.replace("XC", "")
        if "XL" in number:
            total += 40
            number = number.replace("XL", "")
        if "IX" in number:
            total += 9
            number = number.replace("IX", "")
        if "IV" in number:
            total += 4
            number = number.replace("IV", "")
        if i == "M":
            total += 1000
        elif i == "D":
            total += 500
        elif i == "C":
            total += 100
        elif i == "L":
            total += 50
        elif i == "X":
            total += 10
        elif i == "V":
            total += 5
        elif i == "I":
            total += 1
        else:
            print("Incorrect Roman numeral entered. Try again :(")
            correct = False
            break
    if correct:
        print(f"The Roman numeral entered corresponds to the number {total}!")

def int_to_roman(number):
    if not (0 < number < 4000):
        return "Number out of range (must be 1..3999)" #perché i numeri romani non venivano utilizzati per numeri più alti di questi
    
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    total = ''
    i = 0
    while number > 0:
        for n in range(number // val[i]):
            total += syb[i]
            number -= val[i]
        i += 1
    print(f"The integer numeral entered corresponds to the Roman number {total}!")


run = True
while run:
    print("\n")
    print("-- MENU --")
    print("1 - Converting a Roman numeral to a whole number")
    print("2 - Converting an integer to a Roman numeral")
    print("0 - Exit")

    try:
        choice = int(input("What do you want to do? -> "))
    except ValueError: #se l'utente non inserisce un numero
        print("Ups... that was a mistake, right? Try again ;)", end="\n")
        continue

    if choice not in [0, 1, 2]:
        print("Ups... that was a mistake, right? Try again ;)", end="\n")
        continue

    match choice:
        case 0:
            print("Thank you and have a nice day! <3")
            run = False
        case 1:
            number = input("Enter the Roman numeral to be converted: ")
            roman_to_int(number)
        case 2:
            number = int(input("Enter the integer numeral to be converted: "))
            int_to_roman(number)