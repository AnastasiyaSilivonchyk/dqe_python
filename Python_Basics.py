# import library for random numbers generation
import random

# create list of 100 random numbers from 0 to 1000

rnd_list = []

# for loop for population rnd_list with random numbers, range function for definition of the list size
for i in range(0, 99):
    n = random.randint(0, 1000)
    rnd_list.append(n)

# sort list from min to max(without using sort())

# for loop to compare each element in the list one by one, i.e. at the beginning 0 element (i)
# is compared with each other element (j) in the created list and each time the item j is less than i they are replaced,
# if condition is used for comparison
for i in range(len(rnd_list)):
    for j in range(i+1, len(rnd_list)):
        if rnd_list[i] > rnd_list[j]:
            rnd_list[i], rnd_list[j] = rnd_list[j], rnd_list[i]


# calculate average for even and odd numbers

# declare four variables to store sum of even and odd numbers and their count
even_numb, cnt_even = 0, 0
odd_num, cnt_odd = 0, 0

# loop through the list items to check if the item is divided by 2 completely
for i in rnd_list:
    if i % 2 == 0:
        even_numb = even_numb + i       # if the item is divided by two completely sum this number with even_num ver.
        cnt_even += 1                   # increase cnt_even variable by 1
    else:
        odd_num = odd_num + i           # if the item doesn't divide by two sum this item with odd_num
        cnt_odd += 1                    # and increase cnt_odd by 1


# try - except constructions is used to handle ZeroDivsion errors (when there are no even or odd numbers in the list)
# the block of code store calculation of even and odd numbers averages and print results in console
# in case of ZeroDivsion error message in except block is printed in console
try:
    avg_even = even_numb/cnt_even
except ZeroDivisionError:
    print("The number of even numbers in the list equal 0")
else:
    print("Average for even: ", avg_even)

try:
    avg_odd = odd_num/cnt_odd
except ZeroDivisionError:
    print("The number of odd numbers in the list equal 0")
else:
    print("Average for odd: ", avg_odd)