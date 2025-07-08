"""This code collects data of students and anylizes there performance
 and returns the highest and lowest marks and average of the marks"""
def collect_data():
  students={}
  while True:
    name=input("Enter the name of the student \n enter 'done' to end the entry:")# takes the name of the student 
    if name.lower()=='done': # breaks the loop when entered done
      break
    if name in students :
      print("name already exists")
      continue
    else:
      try:
        marks=int(input(f"enter marks for {name}"))
        students[name]=marks # assign the student and the marks to the dictionary 
      
      except ValueError : # checks wheather the entry is a integer if not displays the error message
        print("please input a valid real number marks")
  return students
def analyze_data(students): 
  if not students: # checks whether their are no entries 
    print("No entries data to analyze")
    return
  average=sum(students.values())/len(students) # calculates the average of the marks
  max_score = max(students.values())# returns the highest marks 
  min_score = min(students.values())# returns the lowest marks
    
  top_students = [marks for name, marks in students.items() if marks == max_score] # returns the students with highest marks 
  bottom_students = [marks for name, marks in students.items() if marks == min_score]# returns hte students with lowest marks
  high_scorers = {name: marks for name, marks in students.items() if marks > 75}# returns the data of students with score >75
  low_scorers = {name: marks for name, marks in students.items() if marks < 40} # returns the data of students with score < 40

  print("\n  Students Data "  )  
  print("Average Score:",average)
  print(f"Student with top score is {top_students} with a score {students[top_students]}")
  print(f"Student with lowest score is {bottom_students} with a score {students[bottom_students]}")
  print("High scorers (>75):", high_scorers)
  print("Low scorers (<40):", low_scorers)

# run the project 
students=collect_data()
analyze_data(students)
     

