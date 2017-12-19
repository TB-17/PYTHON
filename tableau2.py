def entrée ():
    p=input("Entrez une phrase :")
    str=""
    t=p.split(' ')
    return p,str,t;

def métier():
    a=t[0]
    n=len(t[0])
    b=t[x]
    m=len(t[x])
    return a,n,b,m;

def sortie ():
    print(a, " : ", n)


p,str,t=entrée()
for x in range (0,len(t)):
    a,n,b,m=métier()
    if (n<m):
        n=m
        a=b
sortie()
