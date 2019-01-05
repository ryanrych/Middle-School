from random import *
characters=' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~`!@#$%^&*()-_=+[{]}\|;:\'\",<.>/?'
randoms=' qwFGHNM564J}|:\"?SDXerKLZTY~%p,.UIOPA291{C0`/_QWERasd^$&ghjklzxc#*@(!)-ty\';vbnm=uiof[\]+VB738><'
randomsC=' qwFGHNM564J}|:\"?SDXerKLZTY~%p,.UIOPA291{C0`/_QWERasd^$&ghjklzxc#*@(!)-ty\';vbnm=uiof[\]+VB738><'
randomsList=[]
for x in randoms:
   randomsList.append(x)
shuffle(randomsList)
del randoms
for x in randomsList:
   try:
     randoms='%s%s' % (randoms,x)
   except:
     randoms=x
def encode(x):
   i=0
   j=0
   try:
     del task
   except:
     pass
   base26=x
   while not j == len(base26):
     while not characters[i]==base26[j]:
       i+=1
     if i < 10:
       i='%s%s' % (0,i,)
     try:
       base10='%s%s' % (base10,i,)
     except:
       base10=i
     i=0
     j+=1
   return base10
def decode(x):
   i=0
   j=1
   base10=x
   count=0
   try:
     del task
   except:
     pass
   while not count >= len(base10)/2:
     task=int('%s%s' % (base10[i],base10[j],))
     try:
       base26='%s%s' % (base26,characters[task],)
     except:
       base26=characters[task]
     i+=2
     j+=2
     count+=1
   return base26
def infinityEncrypt(x):
   i=0
   j=0
   try:
     del encrypted
   except:
     pass
   decrypted=x
   while not j == len(decrypted):
     while not characters[i]==decrypted[j]:
       i+=1
     try:
       encrypted='%s%s' % (encrypted,randoms[i],)
     except:
       encrypted=randoms[i]
     i=0
     j+=1
   return encrypted
def infinityDecrypt(x):
   i=0
   encrypted=x
   count=0
   try:
     del task
   except:
     pass
   while not count >= len(encrypted):
     for x in randoms:
       if x==encrypted[i]:
         task=randoms.index(x)
         break
     try:
       decrypted='%s%s' % (decrypted,characters[task],)
     except:
       decrypted=characters[task]
     i+=1
     count+=1
   return decrypted
def encrypt(x):
   i=0
   j=0
   try:
     del encrypted
   except:
     pass
   decrypted=x
   while not j == len(decrypted):
     while not characters[i]==decrypted[j]:
       i+=1
     try:
       encrypted='%s%s' % (encrypted,randomsC[i],)
     except:
       encrypted=randomsC[i]
     i=0
     j+=1
   return encrypted
def decrypt(x):
   i=0
   encrypted=x
   count=0
   try:
     del task
   except:
     pass
   while not count >= len(encrypted):
     for x in randomsC:
       if x==encrypted[i]:
         task=randomsC.index(x)
         break
     try:
       decrypted='%s%s' % (decrypted,characters[task],)
     except:
       decrypted=characters[task]
     i+=1
     count+=1
   return decrypted