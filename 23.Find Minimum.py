PROBLEM:

Define a function named my_min to find the min of the inputted numbers.

SOLUTİON:
def my_min(x, *arg):
    try:
        return min(x, *arg)
    except:
        return x