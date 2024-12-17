# this code calculates age as of  the day dec 17, 2024
def age(birth_day, birth_month, birth_year, current_day, current_month, currnet_year):
     age_year = currnet_year - birth_year
     age_month = current_month - birth_month 
     age_day = current_day - birth_day 
     
     # if the age day is negative 
     if age_day < 0:
         age_day+=day_in_month(birth_year, current_month - 1)
         age_month-=1
     if age_month< 0:
          age_month+=12
          age_year-=1
     return age_day, age_month, age_year
def day_in_month(year,month):
     if month == 0 :
          month+=12
          year-=1
     if month in [1,3,5,7,8,10,12]:
          return 31
     elif month in [4,6,9,11]:
          return 30
     elif month == 2:
         if year == leap_year(year):
              return 29
         else:
              return 28
         return 0
     
def leap_year(year):
        return(year % 4 ==0 and (year%100!=0 or year%400==0))
def main():
     current_month=12
     current_year=2024
     current_day=17

     birth_day=int(input("enter the day of birth:"))
     birth_month=int(input("enter the month of birth:"))
     birth_year=int(input("enter the year of birth:"))

     age_day, age_month, age_year=age(birth_day, birth_month, birth_year, current_day, current_month, current_year)

     print(f"the age of the given induvidual is {age_day} days {age_month} months {age_year} years")

if __name__ == "__main__":
     main()

     



        