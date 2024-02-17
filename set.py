my_set = {122,343,344,4243,344,6}
print(my_set)
char = 122
if char in my_set:
    output = char
    print(output)

my_set.add(343)
my_set.update([122,667,8688,6877])
my_set2=my_set.copy()
print(my_set2)
print(my_set)
print(len(my_set))
my_set.discard(122)
del my_set
print(my_set2)
max(my_set2)
min(my_set2)
sum(my_set2)
if 667 in my_set2:
    print('present')

else:
    print('not')
