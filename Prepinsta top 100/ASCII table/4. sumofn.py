x=int(input())
#type1
s=0
for i in range(1,x+1):
    s=s+i
print(s)
#type2
sum= int((x*(x+1))/2)
print(sum)
#type3
def sumn(x):
    if x==0:
        return 0
    return x+ sumn(x-1)
print(sumn(5))
