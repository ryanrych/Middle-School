from math import sqrt
while True:
   x1=''
   y1=''
   x2=''
   y2=''
   i=0
   coord=raw_input('Enter your coordinates in this form. (x1,y1)(x2,y2)')
   while not coord[i]=='(':
     i+=1
   start=i
   i=0
   while not coord[i]==',':
     i+=1
   end=i
   i=start+1
   count=0
   while not count == (end-start)-1:
     if x1=='':
       x1=coord[i]
     else:
       x1='%s%s' % (x1,coord[i],)
     i+=1
     count+=1
   start=end
   i=0
   while not coord[i] == ')':
     i+=1
   end=i
   i=start+1
   count=0
   if y1 == '':
     y1=coord[i]
   else:
     y1='%s%s' % (y1,coord[i],)
   i+=1
   count+=1
   i=0
   while not coord[i] == '(':
     i+=1
   i+=1
   while not coord[i] == '(':
     i+=1
   i+=1
   while not coord[i] == ',':
     if x2=='':
       x2=coord[i]
     else:
       x2='%s%s' % (x2,coord[i],)
     i+=1
   i+=1
   while not coord[i]==')':
     if y2=='':
       y2=coord[i]
     else:
       y2='%s%s' % (y2,coord[i],)
     i+=1
   x1=float(x1)
   y1=float(y1)
   x2=float(x2)
   y2=float(y2)
   slope=(y2-y1)/(x2-x1)
   Yintercept=(slope*x1)-y1
   try:
     Xintercept=(0-Yintercept)/slope
   except:
     pass
   distance=sqrt((x2-x1)**2+(y2-y1)**2)
   midpoint='%s%s%s%s%s' % ('(',(x1+x2)/2,',',(y1+y2)/2,')',)
   sif='%s%s%s%s' % ('y=',slope,'x+',Yintercept,)
   psf='%s%s%s%s%s%s%s' % ('y-',y1,'=',slope,'(x-',x1,')')
   print '%s%s' % ('Slope: ',slope,)
   print '%s%s' % ('Y Intercept: ',Yintercept,)
   print '%s%s' % ('X Intercept: ',Xintercept,)
   print '%s%s' % ('Distance: ',distance,)
   print '%s%s' % ('Midpoint: ',midpoint,)
   print '%s%s' % ('Slope Intercept Form: ',sif,)
   print '%s%s' % ('Point Slope Form: ',psf,)