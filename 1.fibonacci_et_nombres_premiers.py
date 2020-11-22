# demande un nombre strictement positif
N = 0
while N <= 0 :
	N = int(input("Combien de nombres voulez-vous ? \n = "))
	if N <= 0 :
		print("arrete de jouer au con et met un nombre strictement positif !")


def fibonacci (nombre) :
    """
    trouve la ième valeure de la suite de fibonnacci 
    N.B. le nombre doit etre entier et strictement positif
    """

    u1 = 1
    u2 = 1
    i=0
    while i < (nombre-2):
	    u1 = u1+u2
	    i = i + 1
	    if i < (nombre-2):
		    u2 = u1+u2
		    i = i + 1
	    else :
		    break
    
    if u1 >= u2 :
        return u1
    else :
        return u2


def Prime (Nombre) :
    """
    verifie la condition si un nombre entier positif est premier 
    """
    
    
    if (Nombre == 1):
	    return(False)
    else :
        i = 2
        while (not(Nombre%i == 0)) :
            i += 1
        if (i == Nombre) :
            return (True)
        else : 
            return (False)

#l'impression
for x in range(1,N+1):
    print ("Number {tour}  : {fibo} ; {prime}".format(tour = x , fibo = fibonacci(x), 
        prime = "is prime." if Prime (fibonacci(x)) else "isn't prime." ))

