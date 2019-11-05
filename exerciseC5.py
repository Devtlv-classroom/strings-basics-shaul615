# Exercise 4 (easy)
# Given a list, use a while loop to print out every elements from the end to the beginning.

demo_list = ["big", "small", "medium", "high", "low", "cheese", "meat"]
list_flag = True
print_count = 0

print("The Length of the list is : {}\n ".format(len(demo_list)))
while list_flag == True:
    if print_count < len(demo_list):
         print(print_count, "- ",demo_list[print_count],"\n")
         print_count += 1
    else:
         list_flag = False
         break
print("end of the list")


