# Exercise (medium)
# Write a Python program to find those numbers which are
# divisible by 7 and multiple of 5, between 1500 and 2700.

num_counter = 1500
correct_num_list = []
stop_process = True

while stop_process == True:
    if num_counter > 2700:
        break
    else:
        if (num_counter % 7 == 0) and (num_counter % 5 == 0):
            correct_num_list.append(num_counter)
        num_counter += 1

print(correct_num_list, "\n")
