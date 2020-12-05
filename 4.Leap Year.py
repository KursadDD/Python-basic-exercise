PROBLEM:

Find out if a given year is a "leap" year.

In the Gregorian calendar, three criteria must be taken into account to identify leap years:
The year must be evenly divisible by 4;
If the year can also be evenly divided by 100, it is not a leap year; unless...
The year is also evenly divisible by 400. Then it is a leap year.
According to these rules, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300, and 2500 are not the leap years.
Write a Python program that;
Takes a 4-digit year from the user,
Prints True if the given year by the user is a leap year, prints False otherwise.

SOLUTİON:
year = int(input("Lütfen bir yıl giriniz: "))

mod1 = year%4

mod2 = year%100

mod3 = year%400

print("{} yılı {} çıktı".format(year,(not mod1 and not mod3 and not mod2)))