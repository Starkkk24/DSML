lst = []

for i in range(1,11):
    lst.append(2*i)

print(lst)

lstt = [2*i for i in range(1,11)]
print(lstt)



func = lambda x,y,z: x**2 + y**2 + z**2 + 2*x*y + 2*y*z + 2*z*x + 3*x*y*z

funcc=func(1,2,3)
print(funcc)