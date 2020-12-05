TASK-1:

Write a short Python program that asks the user to enter Celsius temperature (it can be a decimal number), converts the entered temperature into Fahrenheit degree and prints the result.

TASK-2:
Write a short Python program that asks the user to enter a distance (it can be a decimal number) in kilometers, converts the entered distance into miles and prints the result.

SOLUTİON-1:
cels = float(input("Bir celsius değeri giriniz:"))

fahr = float(cels*1.8+32)

print("Girdiğiniz Celsius değeri", fahr,  "Fahrenheit'dır." )



SOLUTİON-2:

km = float(input("Bir KİLOMETRE değeri giriniz:"))

mil = float(km*0.6213)


print("Girdiğiniz Kilometre değeri", mil, "dir." )