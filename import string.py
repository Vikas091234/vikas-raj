# counts character frequency
import string

def Valid_char(a):
    correct_char=string.ascii_letters 
    return all(char in correct_char or char == ' ' for char in a)# allows only alphabets with spaces

def count(a):
    
    frequency={}
    a = a.replace(" ","") # removes spaces in the string

    for char in a:
        if char in frequency:
            frequency[char]+=1            
        else:
            frequency[char]=1
    return frequency

def main():
    while True: # ask for input until a valid input is given

        a = input("enter a string: ")
        
        if not Valid_char(a):
            print ("enter the valid input")
        else:
            break
    result= count(a)
    print(result)

if __name__=="__main__":
    main()
    
