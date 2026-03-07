n=list(map(int,input()))
for i in n[::-1]:
    print(i,end="")
print()

k=int(input())
rev=0
while(k>0):
    rev=rev*10+k%10
    k=k//10
print(rev)
