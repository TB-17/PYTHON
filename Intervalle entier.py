#cette fonction sert à définir les variables
def entree():
    a= int (input("Entrez une valeur de a:")) 
    b= int (input("Entrez une valeur de b:")) 
    c=0;
    return a,b,c ;
#cette fonction sert a calculer
def calcul(a,b,c):
    while(a<b):
        if (a%5==0):
            c=c+a
        a=a+1
    return c
#cette fonction sert à afficher les calculs
def affichage(c):
    print("somme =",c);        
              

a,b,c=entree()
c=calcul(a,b,c)
affichage(c)
