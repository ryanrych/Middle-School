import math
while True:
   a=float(raw_input('Enter side A'))
   b=float(raw_input('Enter side B'))
   C=float(raw_input('Enter angle c'))
   print 'C=',math.sqrt(a**2+b**2-2*a*b*math.cos(C))