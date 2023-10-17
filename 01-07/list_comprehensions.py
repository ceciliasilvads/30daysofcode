list = [20, 50, 30, 60]
new_list = []

#Normal method
for i in list:
    new_list.append(i * 2)

#List Comprehension
new_list2 = [j * 2 for j in list]

print(new_list)
print(new_list2)