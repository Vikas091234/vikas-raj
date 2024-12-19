# this code sorts the given list of integers in decending order 
def Sort(a):
    return sorted(a, reverse=True)  # Returns a new list sorted in descending order


def main():
    n=int(input("enter the length of the list : "))# length of the list
    a=[]
    for i in range (n):
        
        a.append(int(input("enter an integer to the list a : "))) # list a 

    a = Sort(a)
    print(a) # prints the list after arranging from largest to smallest

if __name__=="__main__":
    main()


    