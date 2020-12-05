PROBLEM : 
Find out the most frequent number and its frequency.

Write a program that;

Finds out the most frequent number in the given list.
Calculates its frequency.
Prints out the result such as :

SOLUTİON:
numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]

en_sık = max(numbers, key = numbers.count)

miktar = numbers.count(en_sık)

print(f"the most frequent number is {en_sık} and it was {miktar} times repeated")