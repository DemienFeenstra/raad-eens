import random
Rounds = 0
Guesses = 0
correctAnswer = False
score = 0
print("raad het getal tussen de 1 en de 1000!")
while Rounds <= 20:
    number = random.randint(1, 1000)
    correctAnswer = False
    Guesses = 0
    r = range(int(number - 20), int(number + 20))
    print("raad het getal!")
    while Guesses != 10:
        print("Aantal keer gegokt: ",Guesses)
        goknummer = int(input("Nummer: "))
        Guesses = Guesses + 1
        if goknummer > number:
            print("Het getal is lager.")
        if goknummer < number:
            print("Het getal is hoger.")

        Close = goknummer in r
        if Close == True:
            print("Je bent heel dicht in de buurt.")

        if goknummer == number:
            print("Goed gedaan! Je hebt het juiste antwoord!")
            score = score + 1
            print("je hebt nu",score, "punt(en)")
            correctAnswer = True
            break
        else:
            print("")
    if correctAnswer == False:
        print("Het goede antwoord was:", number)
    Rounds = Rounds + 1
    if Rounds != 20:
        print("Wilt u verder spelen?")
        Continue = input("typ 'stop' om te stoppen, vul niks in om door te gaan: ").lower()
    else:
        print("Bedankt voor het spelen.")
    if Continue == "stop":
        break

print("Uw eindscore is:", score, "punt(en)")