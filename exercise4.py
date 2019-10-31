from datetime import datetime

birthdate = input("enter your birthdate in this format DD/MM/YYYY")
birthdate_year = int(birthdate[6:10])


now = datetime.now() # current date and time
year = int(now.strftime("%Y"))
print("The Current year is: ", year)
print("Your Year of Birth is: ", birthdate_year)
print("In this year, your age is: ", year-birthdate_year)

