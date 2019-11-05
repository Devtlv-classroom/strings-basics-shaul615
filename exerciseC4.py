# Exercise 2 (easy)
# # A movie theater charges different ticket prices depending on a person’s age .
# # If a person is under the age of 3, the ticket is free; if they are between 3 and 12,
# # the ticket is $10; and if they are over age 12, the ticket is $15 .
# #
# # Write a loop in which you ask users their age, and then tell them the cost of
# # their movie ticket .

age = 0
price = 0
total_price = 0

while age != "" :
    age = (input("Please enter the age: (to quit press Enter)\n - "))
    if age == "":
        break
    age = int(age)
    if age < 3:
        price = 0
    if age >= 3 and age <= 12 :
        price = 10
    if age > 12:
        price = 15
    total_price +=  price
print(total_price)
