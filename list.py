my_list = [345,553,21,54,56,67,65,67]
print(my_list)
print(my_list[2])
print(my_list[7])
print(my_list[0:6])
my_list[3] = 520
print(my_list)
my_list[5] = 5555
print(my_list)
my_list.append(73)
print(my_list)
my_list.insert(3, 57)
print(my_list)
my_list.extend([43,646,678])
print(my_list)
my_list.remove(345)
print(my_list)
del my_list[2]
print(my_list)
my_list.clear()
print(my_list)
my_list.extend([45,56,47,474,849,949,77])
print(my_list)
my_list.append(67776)
print(my_list)
del my_list
#
my_list2 = [313,543,767,7888,9875,6453]
print(my_list2)
my_list2.append(655)
print(my_list2)
if 655 in my_list2:
    print('The value is in the list')
else:
    print('The value is not found')

my_list3 = [356,334,3443,3443,433,356,668,659,4678,433]
print(my_list3.count(433))
print(max(my_list3))
print(min(my_list3))
print(sum(my_list3))
print(len(my_list3))
print(my_list3.index(3443))

my_list4 = ['Tom', 'Jacob', 'simon', 'peter', 'ezekiel']
print(my_list4)
my_list4.append('ruth')
print(my_list4)
if 'ruth' in my_list4:
    print('Available')
else:
    print('Not detected')
print(my_list4)
my_list4.extend([5533,533,535,3534,])
print(my_list4)