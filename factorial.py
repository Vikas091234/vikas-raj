# this code calculates teh factorinal of an interger n 
# create the function to calculate factorial 
def factorial(n):
    product=1
    for i in range (1,n+1):
        product*=i # calculating the factorial 
    return product # return the result of the factorial 
def main():
    n= int(input("enter a integer: "))
    result=factorial(n) # stores the result of the factorial in 'result'
    print(" factorial of interger n is : ", result )
if __name__=="__main__":
    main()