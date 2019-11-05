# Exercise (medium)
# Challenge the user to print the longest sentence without any "A", if he achieves it, tell him how many letters he wrote, else, print a fail message.

user_sentence = input("Challenge, quickly type the longest sentence you can without using the letter A: ")

letter_count = len(user_sentence) - user_sentence.count(' ')

if "A" not in str.upper(user_sentence) :
    print("well done")
    print("your length of your sentence is: ", len(user_sentence)," characters")
    print("your sentence has", letter_count," letters")
else:
    print("sorry you failed")
    user_sentence.cou