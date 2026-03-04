x=int(input())
y=int(input())
z=int(input())
#1
if (x>y and x>z):
    print(x)
elif (y>x and y>z):
    print(y)
else:
    print(z)
#2
a=x if x>y else y
b=a if a>z else z
print(b)
    