PROBLEM : 
Find out if the given word is "comfortable words" in relation to the ten-finger keyboard use.

A comfortable word is a word which you can type always alternating the hand you type with (assuming you type using a Q-keyboard and use of the ten-fingers standard).
The word will always be a string consisting of only letters from a to z.
Write a program to returns True if it's a comfortable word or False otherwise.

SOLUTİON:
word = input("Test etmek için bir kelime giriniz: ")

word = set(word)

left = set("qazwsxedcrfvtgb")

right = set("yhnujmıköolçpşğiü")

if word.intersection(left) == word:

    print("Tek sol el ile:", False)

elif word.intersection(right) == word:

    print("Tek sağ el ile:", False)

else:

    print("El değişerek:", True)