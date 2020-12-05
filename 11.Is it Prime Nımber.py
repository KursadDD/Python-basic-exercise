PROBLEM:
Write a program that takes a number from the user and prints the result to check if it is a prime number.

The examples of the desired output are as follows :

input →  19 ⇉ output : 19 is a prime number
input →  10 ⇉ output : 10 is not a prime number
Note that ⚠: This question is famous on the web, so to get more benefit from this assignment, try to complete this task on your own. 

SOLUTİON:
x = int(input("Kontrol edilmesini istediğiniz sayıyı giriniz: "))

y = ""

if x == 2 or x == 3:

    print(f"{x} sayısı asaldır")

else:

    for i in range(2,int(x/2)+1):

        if x % i == 0:

            y = "asal sayı değil"

            break

    if y == "asal sayı değil":

        print(f"{x} asal sayı değil")

    else:

        print(f"{x} asal sayıdır")