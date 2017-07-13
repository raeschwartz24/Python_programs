# syracuse.py
# takes in an integer x and returns an integer indicating the number of elements in the syracuse sequence starting with x
# Rachael Schwartz

def main():
    
    def rec(x):
        if (x == 1):
            return 1
        elif ((x%2) == 0):
            f = x/2
        else:
            f = (3*x)+1
        return rec(f) + 1
    
    n = (eval(input("Please enter a length: ")))
    x = 0
    eNum = 0
    while (eNum < n):
        x = x+1
        eNum = rec(x)
    print(x)
    
main()
