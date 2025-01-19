# even_or_odd
# the code checks weather the entered number is ever or odd

def Even_Or_Odd(n):
    if n%2==0:
        return True
    else:
        return False
def main():
    t=1
    while(t==1):
        n= int(input(" enter a valid integer :"))
        if Even_Or_Odd(n):
            print(f" the entered integer {n} is an even number")
        else:
            print(f"the entered integer {n} is an odd number")
 
if __name__=="__main__":
    main()


