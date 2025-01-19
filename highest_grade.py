def highest_grade(students):
    # Sort by grade (item[1]) in descending order, and get the highest grade
    sorted_students = sorted(students.items(), key=lambda item: item[1], reverse=True)
    highest_grade_student = sorted_students[0]
    print(f"The student with the highest grade is {highest_grade_student[0]} with grade {highest_grade_student[1]}")

def entry(students):
    # Take name and grade and add it to the dictionary
    name = input("Enter the student's name: ").strip()
    grade = int(input(f"Enter {name}'s grade: "))
    students[name] = grade

def main():
    students = {}
    while True:
        print("\nEnter an entry:")
        print("1. Add a student and their grade")
        print("2. Get the student with the highest grade")
        print("3. Exit the program")
        
        option = int(input("Choose an option (1-3): "))
        
        if option == 1:
            entry(students)
        elif option == 2:
            highest_grade(students)
        elif option == 3:
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
