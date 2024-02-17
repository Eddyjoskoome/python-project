my_dictionary = {
    'name': 'Eddy',
    'Gender': 'Male',
    'School': 'School of software development'

}
my_dictionary = dict(
    Name='Eddy',
    Gender='Male',
)
print(my_dictionary)
print(my_dictionary['Name'])
print(my_dictionary['Gender'])
my_dictionary['Gender'] = 'female'
print(my_dictionary)
my_dictionary['birthday'] = 18
print(my_dictionary)
my_dictionary2=my_dictionary.copy()
print(my_dictionary2)
print(len(my_dictionary2))
my_dictionary2.pop('Gender')
print(my_dictionary2)
del my_dictionary
print(my_dictionary2)
# for key, value in my_dictionary2.items() :
#     print(my_dictionary2[value])#print dictionary values found on the right

for key in my_dictionary2:
    print(key,)#prints the dict key

for key, value in my_dictionary2.items():
    print(key, value)#prints dict key&value