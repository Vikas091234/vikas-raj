# this code prints the first n numbers of fibonacci sequence

def fibonacci_sequence(n):
    a,b=0,1
    for i in range(n) :
        if i != (n-1):
            print(a,end=", ")
        else:
            print(a)

        a,b = b, a+b
def main():
    n= int(input("enter how many fibonacii sequence you want to find: "))
    fibonacci_sequence(n)

if __name__=="__main__":
    main()

        

    


   