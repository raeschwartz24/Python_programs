def main():
    n = eval(input( "How many darts do you want to throw? "))
    hits = 0
    for i in range(1,n+1):
        randX = random.uniform(-1.0, 1.0)
        x = randX
        randY = random.uniform(-1.0, 1.0)
        y = randY
        def simpleDistance(x, y) :
            return math.sqrt( x*x + y*y )
        if simpleDistance( x, y) <= 1:
            hits = hits + 1    
    Pi = 4*(hits/n)
    print("The value of Pi after", n, "iterations is", Pi)
    
main()
