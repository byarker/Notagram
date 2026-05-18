from random import randint

def scramble(word: str) -> str:
    length = len(word)
    listword = list(word)
    anagram = ""
    for i in range(1, length + 1):
        anagram += listword.pop(randint(0, length - i))
        print(anagram)
    return anagram