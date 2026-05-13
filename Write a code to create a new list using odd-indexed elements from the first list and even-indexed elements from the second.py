list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()


odd_element = list1[1::2]
print(odd_element)

even_elements = list2[0::2]
print(even_elements)

res.extend(odd_element)
res.extend(even_elements)
print(res)