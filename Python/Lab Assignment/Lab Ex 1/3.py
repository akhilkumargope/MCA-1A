
#     a
#    a b
#   a b c
#  a b c d
# a b c d e


import string
test_list = list(string.ascii_lowercase)
# print(test_list)

n=int(input("Enter the range"))
for i in range(1,n+1):
    for space in range(n-1,i-1,-1):
        print(" ",end="")
    for a in range(i):
        print(test_list[a],end=" ")
    print()
    


# *
# **
# ***
# ****
# *****

n=int(input("Enter the range"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")

    print()
