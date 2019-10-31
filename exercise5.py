# Ask a user for his birthdate (specify the format, for example: `DD/MM/YYYY`) and then tell him how old he is today.
from datetime import datetime, timedelta, date


bday = input("Please enter your birthdate in this formate DD/MM/YYYY : ")

dateformat = datetime.strptime(bday, '%d/%m/%Y')

a=dateformat
b=datetime.now()

months = b.month - a.month
years = b.year - a.year
days =  b.day - a.day


# If the months is > 0 then it's their bday and it shows a message

if months<0 :
    print( "Hey!! next month is your Birthday")

# prints out the age split into years, months, days
print("You are a current/today: ")
print("Years: ",years)
if months>0 :
    print("Months: ",months)
print("Days: ",days)
print( "young/old, up till Until 120+")

