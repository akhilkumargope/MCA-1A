a=[1,2,3,4,5,6]
b=["akhil","tony","batman",]

#Sum of the elements
print(sum(a))

#Product of the elements
p=1
for i in range(len(a)):
    p= p*a[i]
print(p)

#Largest of all
max=a[i]
for i in range(len(a)-1):
    if(a[i] > max):
        max=a[i]
print(max)


#Minimum of all
min=a[i]
for i in range(len(a)-1):
    if(a[i] < min):
        min=a[i]
print(min)