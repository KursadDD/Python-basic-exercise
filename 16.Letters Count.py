PROBLEM:
Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
Write a Python program that;
takes a sentence from the user,
counts the number of each letter of the sentence,
collects the letters/chars as a key and the counted numbers as a value in a dictionary.

SOLUTİON:
 cml = input("cümle gir: ")

hrf = list(cml)

rakam = lambda x : hrf.count(x)

z = list(map(rakam, hrf))



print(dict(zip(hrf, z)))