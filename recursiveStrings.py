# recstr.py
# performs recursive functions on two strings entered by user
# Rachael Schwartz

def main():
    
    def rev(s):
        if (s == ""):
            return s
        else:
            f = (len(s) - 1)
            return s[f] + rev(s[0:f])
        
    def pal(s):
        if (len(s) < 2):
            return True
        else:
            f = (len(s) - 1)
            if (s[0] == s[f]):
                return pal(s[1:f])
            else:
                return False
            
    def subseq(s,t):
        if (len(t) == 0):
            return True
        elif (len(t) > len(s)):
            return False
        else:
            if (t[0] == s[0]):
                return subseq(s[1:],t[1:])
            else:
                return subseq(s[1:],t)
            
    def printAns(s,t,R,P,S):
        print('The string "', s, '" backwards is "', R, '".', sep='')
        if (P == True):
            print('The string "', s, '" is a palindrome.', sep='')
        else:
            print('The string "', s, '" is not a palindrome.', sep='')
        if (S == True):
            print('The string "', t, '" is a subsequence of "', s, '".', sep='')
        else:
            print('The string "', t, '" is not a subsequence of "', s, '".', sep='')
    
    s = input("Please enter a string: ")
    t = input("Please enter another string: ")
    R = rev(s)
    P = pal(s)
    S = subseq(s,t)
    printAns(s,t,R,P,S)
    
    
    
main()
