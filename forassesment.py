l = [1,2,3,4,5,6,7,8,9,10]
print(l)
total=0
for num in l:
    total=total+num
print(total)
del l


a = float(input("Your math mark scores? "))
b = float(input("Your english mark score? "))
if a <=30 or b <=0:
    print("Failed")
if a >=30 <=100 and b >=30 <=100:
    print("Pass")
