# primes.py
# prints out some number of primes and the number of twin primes amongst them.
# Rachael Schwartz
# prints out the first $n$ primes and the number of twin primes within the first $n$ primes

def main():
    n = eval(input( "Please enter an integer: "))
    def top():
        print("The first", n, "primes are:")
    def two():
        print("2 ", end='')
    def isPrime():
        two()
        t = 0
        i = 1
        previousx = 2
        x = 3
        while (x > 1):
            f = 2
            while (f < x):
                if (x%f == 0):
                    break
                else:
                    f = f+1
            if (f == x):
                i = i+1
                if (i < n):
                    print(x, " ", sep='', end='')
                    if ((x - previousx) == 2):
                        t = t+1
                    previousx = x
                if (i == n):
                    print(x)
                if (i == n+1):
                    break
            x = x+1
        print("Amongst these are", t, "twin primes.")
        
    top()
    isPrime()

main()
