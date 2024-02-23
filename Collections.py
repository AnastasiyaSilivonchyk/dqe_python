# import library for random numbers and letters generation
import random
import string

# create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100)


rnd_num = random.randint(2, 10)
# declare empty list variable for further population with dictionaries
rnd_dict_list = []

# for loop to create required number of dictionaries
for i in range(rnd_num):
    rnd_dict = {}
    while len(rnd_dict) != rnd_num:  # repeat steps under while loop a certain number of times so to populate dictionary
        key = random.choice(string.ascii_letters)  # variable for dict key - as random letter
        value = random.randint(0, 100)  # variable for dict value - as random number
        rnd_dict[key] = value  # build key-value pairs
    rnd_dict_list.append(rnd_dict)  # append the list after the dict is formed

# print(rnd_dict_list)


# variables for common dictionary from the list, cnt - to define the number of dict with max value,
# cnt_rep - as the count of the equal keys across the list of dicts
common_dic = {}
cnt = 0
cnt_rep = 1

# for loop to go through each dict in the list and compare values for keys between taken dict from the list and
# existed one in the common_dict
for dct in rnd_dict_list:
    for key, value in dct.items():
        if key in common_dic:   # check if key already exist in common_dict
            if value > common_dic[key][0]:  # if the key exist - compare values
                common_dic[key] = [value, cnt, cnt_rep + 1]
# if value bigger than exist in common_dict - assign the list with: value, index of dict, how many times this key repeated
            else:
                common_dic[key][2] = cnt_rep + 1  # if the value is not bigger than in common_dic, just update cnt_rep
        else:
            cnt_rep = 1
            common_dic[key] = [value, cnt, cnt_rep]  # add key-value pair if such key doesn't exist in the common_dic
    cnt += 1

# print(common_dic)

dict_final = {}

# with for loop go through items in common_dic and if cnt_rep equal 1 than add standard key-value pare to thr dict_final
# else create key as key_<index of dict with max value>
for key, (value, cnt, cnt_rep) in common_dic.items():
    if cnt_rep == 1:
        dict_final[key] = value
    else:
        dict_final[f'{key}_{cnt}'] = value

print(dict_final)





