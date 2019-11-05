# Exercise (medium)
# Ask the user for a sentence, and then tell him how many words are in it.

print("Word count in a sentence")
user_name = input("Please enter a sentence")
res = len(user_name.split())
print("Word count: ", res)
