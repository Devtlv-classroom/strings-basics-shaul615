# Exercise (hard)
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
#
# Then make an empty list called finished_sandwiches. Loop through the list of
# sandwich orders and print a message for each order, such as I made your tuna sandwich.
#
# As each sandwich is made, move it to the list of finished sandwiches.
#
# After all the sandwiches have been made, print a message listing each
# sandwich that was made.

sandwich_orders = ["Tuna", "Cheese", "Mushroom", "Greek", "Egg", "Carrot", "Meat", "Chicken"]
finished_sandwiches = []

list_counter = 0

while list_counter < len(sandwich_orders):
    print("I made your {} sandwich".format(sandwich_orders[list_counter]))
    finished_sandwiches.append(sandwich_orders[list_counter])
    list_counter += 1

list_counter = 0
print("\n\b The following sandwitches have been made:\n ")

while list_counter < len(finished_sandwiches):
    print("- {}".format(finished_sandwiches[list_counter]))
    list_counter += 1




