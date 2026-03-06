n=int(input())
from math import sqrt
if n==2 or n==3:
    print("prime")
else:
    for i in range(2,int(sqrt(n)+1)):
        print("Not prime" if n%i==0 else "prime")
        break
   
