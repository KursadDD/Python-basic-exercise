PROBLEM:
Define a function named my_fact to calculate factorial of the given number. Given a non-negative integer return the factorial of the integer.

SOLUTİON:
def my_fact(n):
    if n == 0:
        return 1
    return n * my_fact(n-1)