# Exercise (easy)
# Ask the user for his name, and tell him if the last letter is a vowel or a consonant

print("Test your name to see if the first letter is a vowel or a consonant")
user_name = input("Please enter your Name: ")

vowel_list = "AEIOU"

if str.upper(user_name[0]) in vowel_list:
    print("The first letter of your name", user_name," is -",user_name[0]," is a vowel")
else:
    print("The first letter of your name", user_name, " is - ", user_name[0], " is a consonant")
