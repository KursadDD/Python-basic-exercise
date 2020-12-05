PROBLEM:
Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements.

The desired output is like :

fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

SOLUTİON:
x = int(input("Kaç terim yazdırılsın: "))

fibb = [1,1]



for i in list(range(2,x)):

    fibb.append(fibb[i-2]+fibb[i-1])

print(fibb)