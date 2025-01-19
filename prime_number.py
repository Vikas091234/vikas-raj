# prime_number
# this code checks weather the given number is a prime number or not 

def Prime_Number(n):
    for i in range(2,n//2 +1):
        if n% i == 0:
            return False
           
    return True

def main():
    n=int(input(" enter a integer :"))
    if Prime_Number(n):
        print(f" the entered integer {n} is a prime number")
    else:
         print(f"the entered integer {n} is not a prime number ")

   

if __name__=="__main__":
    main()
            