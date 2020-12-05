PROBLEM:
Print the prime numbers which are between 1 to entered limit number (n).

You can use a nested for loop.
Collect all these numbers into a list
The desired output for n=100 :

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
61, 67, 71, 73, 79, 83, 89, 97]
Note that : This question is famous on the web, so to get more benefit from this assignment, try to complete this task on your own.

SOLUTİON:
x = int(input("Kaça kadar kontrol edelim: "))

prime = []

kontrol =True

for i in list(range(2,x+1)):

    for j in list(range(2,i)):

        if i % j == 0:

            kontrol = False

    if kontrol == False:

        kontrol = True

    else:

        prime.append(i)

        

print(prime)