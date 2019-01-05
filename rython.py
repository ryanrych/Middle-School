def TaskLoop(S,s,e):
   i=s
   try:
     del t
   except:
     pass
   if e == 'end':
     while i!=len(S):
       try:
         t='%s%s' % (t,S[i],)
       except:
         t=S[i]
       i+=1
   else:
     while S[i]!=e:
       try:
         t='%s%s' % (t,S[i],)
       except:
         t=S[i]
       i+=1
   return t
def Delete(S,b,a):
   try:
     del r
   except:
     pass
   r=None
   if b=='b':
     for x in range(a,len(S)):
       if r!=None:
         r='%s%s' % (r,S[x])
       else:
         r=S[x]
   else:
     for x in range(0,len(S)-a):
       if r!=None:
         r='%s%s' % (r,S[x])
       else:
         r=S[x]
   return r
def Find(S,c,o):
   Source=[]
   Found=[]
   for i in range(0,len(S)-1):
     Source.append(S[i])
   for x in Source:
     if x==c:
       Found.append(Source.index(x))
   return Found[o]
def CheckLoop(t,e,a):
   assert type(a) is list,'Available input options must be in a list'
   assert type(t) is str,'Text must be a string value'
   assert type(e) is str,'Invalid message must be a string value'
   check=False
   while not check:
     cmd=input(t)
     if cmd in a:
       return cmd
     else:
       print e