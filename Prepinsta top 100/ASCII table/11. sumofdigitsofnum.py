# 1
n=list(map(int,input()))
print(sum(n))
# 2
print(sum(int(i)for i in input()))
# 3
sum=0
while(n>0):
    sum+=n%10
    n=n//10
print(sum)
