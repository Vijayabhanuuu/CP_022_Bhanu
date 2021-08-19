def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def checkisAdditivePrime(n):
    l=sum(list(map(int,str(n))))
    print(l)
    return isPrime(l)   
def isAdditivePrime(n):
    if(isPrime(n)==True):
      if(checkisAdditivePrime(n)==True):
          return True
    return False

n=int(input())
print(isAdditivePrime(n))