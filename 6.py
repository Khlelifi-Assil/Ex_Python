from math import * 
n = int(input("Tapez la valeur de n :  "))
somme_paire = 0 
somme_impaire = 0
for number in range(1, n):
    if(number % 2 != 0):
        somme_impaire = somme_impaire + number
    else : 
	    somme_paire = somme_paire + number
print("La somme des entiers imapire est : ", somme_impaire) 
print("La somme des entiers paire est : ", somme_paire) 