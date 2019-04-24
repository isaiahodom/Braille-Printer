import sys

brailleLetters = {
    "A": [1, 0, 0, 0, 0, 0], #A
    "B": [1, 0, 1, 0, 0, 0], #B
    "C": [1, 1, 0, 0, 0, 0], #C
    "D": [1, 1, 0, 1, 0, 0], #D
    "E": [1, 0, 0, 1, 0, 0], #E
    "F": [1, 1, 1, 0, 0, 0], #F
    "G": [1, 1, 1, 1, 0, 0], #G
    "H": [1, 0, 1, 1, 0, 0], #H
    "I": [0, 1, 1, 0, 0, 0], #I
    "J": [0, 1, 1, 1, 0, 0], #J
    "K": [1, 0, 0, 0, 1, 0], #K
    "L": [1, 0, 1, 0, 1, 0], #L
    "M": [1, 1, 0, 0, 1, 0], #M
    "N": [1, 1, 0, 1, 0, 1], #N
    "O": [1, 0, 0, 1, 1, 0], #O
    "P": [1, 1, 1, 0, 1, 0], #P
    "Q": [1, 1, 1, 1, 1, 0], #Q
    "R": [1, 0, 1, 1, 1, 0], #R
    "S": [0, 1, 1, 0, 1, 0], #S
    "T": [0, 1, 1, 1, 1, 0], #T
    "U": [1, 0, 0, 0, 1, 1], #U
    "V": [1, 0, 1, 0, 1, 1], #V
    "W": [0, 1, 1, 1, 0, 1], #W
    "X": [1, 1, 0, 0, 1, 1], #X
    "Y": [1, 1, 0, 1, 1, 1], #Y
    "Z": [1, 0, 0, 1, 1, 1], #Z
    " ": [0, 0, 0, 0, 0, 0]
}

class Letter:
    def __init__(self, letter):
        self.dots = brailleLetters[letter.upper()]

class Letters:
    def __init__(self, str):
        self.letters = []
        for letter in str:
            l = Letter(letter)
            self.letters.append(l)

def printBraille(brailleString):
    index = 0
    for i in range(3):
        for letter in brailleString.letters:
            sys.stdout.write("." if letter.dots[index] else " ")
            sys.stdout.write("." if letter.dots[index + 1] else " ")
            sys.stdout.write("  ")
        index += 2
        sys.stdout.write("\n")

def main():
    str = raw_input("Enter a string: ")
    brailleStr = Letters(str)
    printBraille(brailleStr)

if __name__ == "__main__":
    main()
