l1 = [1,1,2,3,4,5,5,6]

count_dict = {}

for item in l1:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)