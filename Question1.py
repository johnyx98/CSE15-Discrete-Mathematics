def AND(p,q):
   if p == True and q == True:
      return True
   return False

def OR(p,q):
   if p==False and q==False:
      return False
   return True

def IF(p,q):
   if p==True and q==False:
      return False
   return True

def NOT(p):
   if p==True:
      return False
   return True

def IFF(p,q):
   if (p == True and q ==True) or (p==False and q == False):
      return True
   return False

def Evaluate(x,p,q):
   
      if x == 'AND':
         return AND(p, q)
      elif x == 'OR':
         return OR(p, q)
      elif x == 'IF':
         return IF(p, q)
      elif x == 'IFF':
         return IFF(p,q)
      elif x == 'NOT':
         return NOT(p)
      

   
p = True
q = False

print ("Simple evaluation function test")
print ("p= ", p)
print ("q= ", q)

print ("(p or q): ",Evaluate("OR",p,q))
print ("(p and q): ", Evaluate("AND", p,q))
print ("(p -> q): ", Evaluate("IF", p,q))
print ("(p <-> q): ", Evaluate("IFF",p,q))
print ("-p:  ", Evaluate("NOT", p,q))




