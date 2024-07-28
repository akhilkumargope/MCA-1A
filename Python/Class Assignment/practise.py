# import calculator

# print(calculator.add_two(2,3))

a=[1,2,4,9,4]
for i in a:
    print(i," \t",end=" ")

a.append(16)
print("\n",a)

a.insert(3,'Akhil')
print(a)

a.remove(2)
print(a)

print("\n",a.index(9))

print(a.count(4))


a.remove('Akhil')


a.sort()
print(a)

a.sort(reverse=True)
print(a)
