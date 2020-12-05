PROBLEM:
Find out if a given number is an "Armstrong Number".

An n-digit number that is the sum of the nth powers of its digits is called an n-Armstrong number. Examples :
371 = 3^3 + 7^3 + 1^3;
9474 = 9^4 + 4^4 + 7^4 + 4^4;
93084 = 9^5 + 3^5 + 0^5 + 8^5 + 4^5.

Write a Python program that;
takes a positive integer number from the user,
checks the entered number if it is Armstrong,
consider the negative, float and any entries other than numeric values then display a warning message to the user.

SOLUTİON:
sayi = input("Bir tam sayı giriniz: ")



while sayi.isnumeric() == False:

    print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")

    sayi = input("Bir tam sayı giriniz: ")



    

listem = list(sayi)

toplam = 0

for i in sayi:

    i = int(i)

    i = i**len(sayi)

    toplam += i

if int(sayi) == toplam:

    print(f"{sayi} is an Armstrong number")

else:

    print(f"{sayi} is not an Armstrong number")