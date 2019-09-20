list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []
list3 = len(list)

for i in range(list3):
    if list[i] % 2 == 0:
        list2.append(list[i] / 4)
    else:
        list2.append(list[i] * 2)

print(list2)
