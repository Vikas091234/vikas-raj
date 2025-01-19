# this code calculates the frequency of the words  in the string entered

def count_words(string):
    string = string.lower().strip()
    words = string.split()  # Split the string into words
    word_count = {}  # Dictionary to store word frequencies

    for word in words:  # Iterate through each word
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1  # Initialize with 1 if new word found

    return word_count  # Return the dictionary

def main():
    string = input("Enter a string: ")
    word_frequencies = count_words(string)
    
    print("\nWord Frequencies:")
    for word, count in word_frequencies.items():
        print(f"{word}: {count}")  # Print each word and its count

if __name__ == "__main__":
    main()
