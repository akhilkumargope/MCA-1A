a=[1,2,3,4,5,6]
b=["akhil","tony","batman",]

#Sum of the elements
def add(a):
    print(sum(a))

#Product of the elements
def product(a):
    p=1
    for i in range(len(a)):
        p= p*a[i]
    print(p)

#Largest of all
def largest(a):
    max=a[0]
    for i in range(len(a)):
        if(a[i] > max):
            max=a[i]
    print(max)


#Minimum of all
def minimun(a):
    min=a[0]
    for i in range(len(a)):
        if(a[i] < min):
            min=a[i]
    print(min)


add(a)
product(a)
largest(a)
minimun(a)
