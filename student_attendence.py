coding_club = set()
ml_club = set()

# Input Coding Club attendees
n1 = int(input("Enter number of students in Coding Club: "))
for _ in range(n1):
    student = input("Enter student name: ")
    coding_club.add(student)

# Input ML Club attendees
n2 = int(input("Enter number of students in ML Club: "))
for _ in range(n2):
    student = input("Enter student name: ")
    ml_club.add(student)

# Results
print("\nAll Unique Students:", coding_club | ml_club)
print("Students in Both Clubs:", coding_club & ml_club)
print("Only in Coding Club:", coding_club - ml_club)
print("Only in ML Club:", ml_club - coding_club)
print("In Exactly One Club:", coding_club ^ ml_club)
