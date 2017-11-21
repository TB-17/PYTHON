#cette fonction sert à définir les variables
def entree():
    a= int (input("Entrez une valeur de a:")) 
    b= int (input("Entrez une valeur de b:")) 
    c=0;
    calcul(a,b,c);
#cette fonction sert a calculer la fonction affine
def calcul(a,b,c):
    for x in range(0,10):
        c=a*x+b
        affichage(c,x)
        x=x+1;
#cette fonction sert à afficher les calculs
def affichage(c,x):
    print(x,"est égale à",c);        
              
if __name__ == '__main__':
entree();
