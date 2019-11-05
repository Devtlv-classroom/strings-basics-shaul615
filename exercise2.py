# Ask two users for their names, and then tell them who got the longest name.
#
user1 = input("User 1 please enter your name: ")
user2 = input("User 2 please enter your name: ")

if len(user1)> len(user2):
    print(user1," your name is longer than ", user2)
elif len(user1) == len(user2):
    print("{} and {} your names have equal lengths", format(user1,user2))
else:
    print(user2, " your name is longer than ", user1)
