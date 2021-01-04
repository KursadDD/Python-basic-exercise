PROBLEM:
Given a string, return a new string where the first and last chars have been exchanged.

SOLUTİON:
def front_back(word):
    word = list(word)
    start = word[0]
    stop = word[-1]
    word.remove(stop)
    word.append(start)
    word.remove(start)
    word.insert(0, stop)
    word = "".join(word)
    return word