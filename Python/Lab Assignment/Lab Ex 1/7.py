import math

print("For triangle 1")
a1=int(input("Enter the first side"))
b1=int(input("Enter the 2nd side"))
c1=int(input("Enter the 3rd side"))

print("For triangle 2")
a2=int(input("Enter the first side"))
b2=int(input("Enter the 2nd side"))
c2=int(input("Enter the 3rd side"))

def area(a,b,c):
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def percent(area1,area2):
    print("Percentage of area of triangle 1 = " ,(area1/(area1+area2))*100)
    print("Percentage of area of triangle 2 = " ,(area2/(area1+area2))*100)

area1=area(a1,b1,c1)
print("Area of 1st triangle = ",area1)
area2=area(a2,b2,c2)
print("Area of 2nd triangle = ",area2)

percent(area1,area2)
