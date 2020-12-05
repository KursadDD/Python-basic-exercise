PROBLEM:
Let's say you left a message in the past that prints a password you need. To see the password you wrote, you need to enter your name and the program should recognize you.
Write a program that 

Takes the first name from the user and compares it to yours,
Then if the name the user entered is the same as yours, print out such as : "Hello, Joseph! The password is : W@12",
If the name the user entered is not the same as yours, print out such as : "Hello, Amina! See you later."

SOLUTİON:
name_user = "Joseph"

name = (input("Adınızı giriniz: ")).title().strip()

if name == name_user:

    print(f"Hello, {name_user} The password is : W@12")

else:

    print(f"Hello, {name} See you later.")