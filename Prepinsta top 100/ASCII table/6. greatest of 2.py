x=int(input())
y=int(input())
#1
if (x>y): print(x, "is greater")
else: print(y, "is greater")
#2
print(x if x>y else y)
#3
print(max(x,y))
