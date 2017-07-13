# recursiveCalculations.py
# perform computations on numberes entered by user (exponentiation, sum of squares, k-combination)
# Rachael Schwartz


def main():
    
    def power(n,k):
        if (k == 0):
            return 1
        else:
            return n * power(n,(k-1))
        
    def sps(n):
        if (n == 1):
            return 1
        else:
            return (n*n) + sps(n-1)
        
    def choose(n,k):
        if (k > n):
            return 0
        if (k == n) or (k == 0):
            return 1
        else:
            return choose((n-1),k) + choose((n-1),(k-1))
        
    def printAns(n,k,P,S,C):
        print(n, " raised to the power of ", k, " is ", P, ".", sep='')
        print("The sum of the first ", n, " squares is ", S, ".", sep='')
        print(n, " choose ", k, " is ", C, ".", sep='')
        
    n = eval(input("Please enter a non-negative integer: "))
    k = eval(input("Please enter another non-negative integer: "))
    P = power(n,k)
    S = sps(n)
    C = choose(n,k)
    printAns(n,k,P,S,C)
    
main()
