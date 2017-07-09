def main():
    n = eval(input( "Please give me a number: "))
    product = 1
    for i in range (1,n+1):
        product = product * i
    print("The product of the first", n, "positive integers is", product)

main()
