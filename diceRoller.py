from random import *
dice, roll, values, duplicates = int(input('How many sides does the die have?')), int(input('How many times would you like to roll this die')), [], []
for i in range(0,roll):
   values.append(randint(1,dice))
for x in range(1,dice+1):
   if values.count(x)>0:
     duplicates.append((x,values.count(x)))
print 'You Rolled:'
for x in duplicates:
   if x[1]>1:
     print '%s;%s\'s' % (x[1],x[0])
   else:
     print '%s;%s' % (x[1],x[0])