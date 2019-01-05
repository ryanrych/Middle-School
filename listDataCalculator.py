from math import *
while True:
   cmd=input('Enter your list in the form [x1,x2,x3,etc.,]:')
   assert (cmd[0]==']','Invalid List')
   i=1
   try:
     del t
   except:
     pass
   data=[]
   while cmd[i]!=']':
     while cmd[i]!=',':
       try:
         t='%s%s' % (t,cmd[i])
       except:
         t=cmd[i]
       i+=1
     try:
       data.append(float(t))
     except:
       pass
     del t
     i+=1
   s=0
   for x in data:
     s=s+x
   mean=s/float(len(data))
   sd=[]
   for x in data:
     sd.append((x-mean)**2)
   s=0
   for x in sd:
     s=s+x
   standardDeviation=s/float(len(sd))
   standardDeviation=sqrt(standardDeviation)
   print 'Length of list: %s' % (len(data))
   print 'Average of list: %s' % (mean)
   print 'Sum of list: %s' % (str(s))
   print 'Standard Deviation: %s' % (standardDeviation)
   print
   print
   print