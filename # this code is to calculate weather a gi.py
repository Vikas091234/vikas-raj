# this code checks weather the given string is palindrome
import string
def Valid_string(a):
    "allows string only containing 'a-z','A-Z'"
    valid_char= string.ascii_letters
    return all(char in valid_char for char in a )
    


def Palindrome(a):
     return a == a[::-1]
    
def main():
    
    
    while True:
        a = input("enter a string with only ascii letters :").strip()
    
        if not Valid_string(a):
            print(" the string you entered is not valid please enter a valid string")
        else:
            break 

    if Palindrome(a):
        print("the give string is a palindrome")
    else:
        print("the entered string is not a palindrome")


if __name__=="__main__":
    main()
