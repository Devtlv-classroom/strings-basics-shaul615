# Exercise 1 (easy)
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value .
# As they enter each topping, print a message saying you’ll add that topping to their pizza .

pitza_toppings = []
topping = ""


while topping != "quit":
    topping = input("Please enter a toping: (to finish type 'quit') \n -")

    if topping != "quit":
        pitza_toppings.append(topping)
        print("Your pitza will have {} added to it.".format(topping))
        print("Your pitza has {} toppings".format(len(pitza_toppings)))
print("Your Grand big pitza has {} toppings, they are:\n {}".format(len(pitza_toppings),pitza_toppings))