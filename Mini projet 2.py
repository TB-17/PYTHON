#cette fonction sert à définir les variables
def entree():
    a= int (input("Entrez une valeur de a:")) 
    b= int (input("Entrez une valeur de b:")) 
    c=10000
    d=10000
    x=0;
    return a,b,c,d,x;
#cette fonction sert a calculer
def calcul(a,b,c,d,x):
    while a<b:
        x=6.67*10**-11*(c*d/a**2);
        affichage(a,x);
        a=a*2;
#cette fonction sert à afficher les résultats
def affichage(a,x):
    print("F(",a,")","=",x,"N");

a,b,c,d,x=entree();
a,x=calcul(a,b,c,d,x);
affichage(a,x);
