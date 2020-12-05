PROBLEM :

Task : Estimating the risk of death from coronavirus. Write a program that;

Takes "Yes" or "No" from the user as an answer to the following questions :

Are you a cigarette addict older than 75 years old? Variable → age

Do you have a severe chronic disease? Variable → chronic

Is your immune system too weak? Variable → immune

Set a logical algorithm using boolean logic operators (and/or) and use if-statements with the given variables in order to print out us a message : "You are in risky group"(if True ) or "You are not in risky group" (if False).
age =  # can be assigned only True/False
chronic =  # can be assigned only True/False
immune =  # can be assigned only True/False
risk = ?

SOLUTİON:

age = input("Are you a cigarette addict older than 75 years old? (Yes or No):  ").title()

while age != "No" and age !="Yes":

    print("Yanlış cevap girdiniz, lütfen tekrar giriniz")

    age = input("Are you a cigarette addict older than 75 years old? (Yes or No):  ").title()

    if age == "No" or age == "Yes":

        break

    

chronic = input("Do you have a severe chronic disease? (Yes or No): ").title()

while chronic != "No" and chronic !="Yes":

    print("Yanlış cevap girdiniz, lütfen tekrar giriniz")

    chronic = input("Do you have a severe chronic disease? (Yes or No): ").title()

    if chronic == "No" or chronic == "Yes":

        break



immune = input("Is your immune system too weak? (Yes or No): ").title()

while immune != "No" and immune !="Yes":

    print("Yanlış cevap girdiniz, lütfen tekrar giriniz")

    immune = input("Is your immune system too weak? (Yes or No): ").title()

    if immune == "No" or immune == "Yes":

        break



listem = [age, chronic, immune]

i = 0

for i in range(len(listem)):

    if listem[i] == "Yes":

        listem[i] = True

        i += 1

    elif listem[i] == "No":

        listem[i] = False

        i += 1

    else:

        print(f"{i+1}.soru için hatalı cevap")

        i += 1

 

risk = listem[0] or listem[1] or listem[2]

print(f"Risk durumunuz: {risk}")
