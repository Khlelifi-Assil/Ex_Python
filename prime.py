def isprime( n ):
   i = 2
   while i < n and n % i != 0 :
        i = i + 1
   if i == n :
        return (n, "est un nomre prmier")
   else :
        return (n, "n est un nomre prmier")

def primes( n ):
    List=[]
    for i in range(1, n) :
         j=2
         while j < i and i % j != 0 :
            j = j + 1
         if j == i :
             List.append(i)
    return ("les nombre primaire entre 1 est ", n ," : ", List)

def nextprime( n ):
   premier = False  
   n=n+1
   while  (premier == False) :
     i=2
     while i < n and n % i != 0 :
        i = i + 1
     if i == n :
           premier = True
           return ("le nombre premier suivant est : " , n)
           break
     else :
            n=n+1