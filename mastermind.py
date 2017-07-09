# master.py
# allows user to play a text-based version of Mastermind.
# Rachael Schwartz
#
import random

def main():
    def top():
        print("I have a 4 letter code, made from 6 colours.")
        print("The colours are R, G, B, Y, P, or O.")
    def generateCode():
        a = 0
        b = 1
        c = 2
        d = 3
        for i in range(1,5):
            colori = random.choice('RBGYOP')
            if (i == 1):
                a = colori
            elif (i == 2):
                b = colori
            elif (i == 3):
                c = colori
            else:
                d = colori
        codeList = [a, b, c, d]
        codeString = codeList[0] + codeList[1] + codeList[2] + codeList[3]
        codeReal = str(codeString)
	#codeReal="RYGY"
        return codeReal
    def clue(c, g):
        black = 0
        for j in range(0,4):
            if (g[j] == c[j]):
                black = black + 1
        both = str(c + g)
        b = both
        only = []
        for k in range(0,8):
            s = b[k]
            d = 0
            for i in range(0,k):
                if (b[k] == b[i]):
                    d = d+1
            if (d == 0):
                only.append(s)
        length = len(only)
        x = 0
        if (length == 0):
            x = 0
        else:
            for l in range(0,length):
                n = only[l]
                appearcode = c.count(n)
                appearguess = g.count(n)
                if (appearguess < appearcode):
                    x = x + appearguess
                else:
                    x = x + appearcode    
        w = (x - black)
        white = 0
        if (w > 0):
            white = w
        else:
            white = 0
        if (black == 4):
            print("Yay! You win!")
            return 10
        else:
            print("Not quite. You get", black, "black pegs,", white, "white pegs.")
            return 1
    top()
    a = generateCode()
    i = 1
    while (i < 11):
        code ="RYGY"     #if you'd like to hard-code in a code for testing purposes, replace variable a with for-character string using acceptable characters.
        guess = input("Your guess: ")
        c = clue(code, guess)
        i = (i + c)
    if (i == 11):
        print("Sorry, you lost.")


main()
