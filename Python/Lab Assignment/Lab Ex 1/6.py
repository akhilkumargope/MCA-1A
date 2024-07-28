#Sum of digits and reverse

n=int(input("Enter the Number"))
temp=n
sum=0
reverse=0

# for i in range(n,0,/10):

while(temp!=0):
    sum+= (temp%10)
    reverse= reverse*10 + temp%10
    temp//=10

print("Sum of digits = ",sum ,"\n Reverse of number = ",reverse)