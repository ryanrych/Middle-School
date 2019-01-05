def prime(x):
   z=False
   for y in range(2,x):
     if x%y==0:
       return False
       z=True
   if not z:
     return True
def addends(x):
   addends=[]
   for y in range(0,x+1):
     for z in range(0,x+1):
       if y+z==x:
         addends.append((y,z))
   return addends
   
   
while True:
   x=int(input('Enter any integer greater than 2'))
   primes=[]
   addendsx=[]
   print
   addendsx=addends(x)
   primes=[]
   for y in addendsx:
     if prime(y[0]) and prime(y[1]):
       primes.append(y)
   for z in primes:
     print z
   print