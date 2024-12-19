# finds all the prime numbers less than the integer n

def prime_numbers(n):
    prime=[]

    for num in range(2, n):
        # Check if 'num' is a prime number
        for i in range(2, int(num ** 0.5) + 1):  # Loop till the square root of num
            if num % i == 0:
                break  # If divisible, 'num' is not prime, so break out of the loop
        else:
            prime.append(num)  # If the loop completes without a break, 'num' is prime
    return prime

def main():
    n= int(input(" enter an integer : "))
    result = prime_numbers(n)
    print(" the primenumbers less than n are : ", result) # print the prime numbers

if __name__=="__main__":
    main()