# sequenceMatch.py
# for each pattern sequence, finds best match in proten sequence and reports location of and number of errors in match.
# Rachael Schwartz
#

def main():
    
    try:
        userInput = input("Please enter a file name: ")
        inputFile = open(userInput,"r")
        P = inputFile.readline()        #reads first line of text file
        if (P != "\n"):                 #if the first line is nonempty (i.e., file contains protein sequence):
            allS = inputFile.readlines()                #create string list of all lines in file
            for i in range(len(allS)):                  #iterate through each line
                S = allS[i][:(len(allS[i]) - 1)]        #define string S from start of line to end of line, excluding newline character
                if (S != ""):                           #if the line is nonempty
                    mis = len(S)
                    ind = 0
                    for j in range(0,(len(P) - len(S))):
                        sub = P[j:(j + len(S))]
                        m = 0
                        for k in range(0,len(S)):
                            if (sub[k] != S[k]):
                                m = m+1
                        if (m < mis):
                            mis = m
                            ind = j
                    print("Sequence ", (i+1), " has ", mis, " errors at position ", ind, ".", sep='')
                else:
                    print("Sequence", (i+1), "is empty.")
        else:
            print("Sorry! This file has no protein sequence.")
            
    except:
        print("Sorry! Something went wrong.")
