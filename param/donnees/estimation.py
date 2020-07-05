import numpy as np
import math
import scipy.stats
from scipy.special import gamma
import argparse
import random

# parser = argparse.ArgumentParser()
# parser.add_argument("loi", type=int, help="loi")
# parser.add_argument("param1",type=float,help="param1")
# parser.add_argument("param2",type=float,help="param2")
# parser.add_argument("taille",type=int,help="taille")
# args = parser.parse_args()



def generate_hyperexpo(l1,l2,N):
    def fdr_hyperexpo2(x,u,l1,l2):
        return ((1-math.exp(-l1*x))/l1 + (1-math.exp(-l2*x))/l2 - (u*(l1+l2))/(l1*l2))
    valeur_initiale=np.random.rand()
    res=[]
    for i in range(N-1):
        u=np.random.rand()
        res.append((scipy.optimize.fsolve(lambda x: fdr_hyperexpo2(x,u,l1,l2),valeur_initiale))[0])
    return res

def generate_hyperexpo2(a,b,N):
    c1=-b/(a*(a+b))
    c2=-a/(b*(a+b))
    res=[]
    for k in range(N):
        res.append(c1*np.log(1-np.random.rand())+c2*np.log(1-np.random.rand()))
    return res

### Gradient
def derivee_num(fonction,x0,i,h=1e-06):
    a=np.zeros(np.size(x0))
    a[i]=1
    return (fonction(x0+0.5*h*a)-fonction(x0-0.5*h*a))/h

#fonction test : test(x,y,z)=x+2yz+4z
def test(a): # attention : a est un np.array (autrement dit un vecteur)
    return a[0]+2*a[1]*a[2]+4*a[2]

def gradient(fonction,point):
    res=np.array([])
    for k in range(0,np.size(point)):
        a=derivee_num(fonction,point,k,1e-06)
        res=np.append(res,a)
    return res

## fonction de calcul de la norme du gradient
def norme(vect):
    return np.dot(vect,vect)

### scipy fsolve
#contraintes
def contrainte1(x,M,esp):
    return -esp(x)+np.mean(M)

def contrainte2(x,M,mom2):
    return -mom2(x)+mom_emp2(M)

#système d'équation à résoudre
def eq1_bis(x,M,logvs,esp,mom2):
    return [gradient((lambda y: logvs(y,M)),x)[0],gradient((lambda y: logvs(y,M)),x)[1],contrainte1(x,M,esp),contrainte2(x,M,mom2)]

def max_vs_m1_bis(M,logvs,esp,mom2):
    res=[]
    Rlist=[]
    for k in range(0,100):
        valeur_initiale=np.array([np.random.rand(),np.random.rand(),0,0])
        R=scipy.optimize.fsolve(lambda x: eq1_bis(x,M,logvs,esp,mom2),valeur_initiale,xtol=1e-3,maxfev=30)
        R=np.array([R[0],R[1]])
        res.append(norme(gradient((lambda y: logvs(y,M)),R)))
        Rlist.append(R)
        if norme(gradient((lambda y: logvs(y,M)),R))<1e-3:
            return R
    ind=res.index(min(res))
    return Rlist[ind]


def mom_emp2(M):
    n=np.size(M)
    res=0
    for i in range(n):
        res=res+M[i]*M[i]
    return res/n

### Log-vraisemblances
def logvs_hyperexpo(x,M): # x est un vecteur de R2 représentant les paramètres et M est un échantillon (x1,...,xn)
    res=0
    c=(x[0]*x[1])/(x[0]+x[1])
    for i in range(0,np.size(M)):
        res=res+np.log(c)+np.log(np.exp(-x[0]*M[i])+np.exp(-x[1]*M[i]))
    return res

def logvs_norm(x,M):
    n=np.size(M)
    c=(1/2*np.pi*x[1])**(n/2)
    m=np.mean(M)
    res=0
    for i in M:
        res=res+((i-m)**2)
    return -n*np.log(x[1])/2-n*np.log(2*np.pi)/2-(1/(2*x[1]))*res

def logvs_burr(x,M):
    n=np.size(M)
    y=n*np.log(x[0]*x[1])
    res=0
    for k in range(0,n):
        res=res+((x[0]-1)*np.log(M[k])-(x[1]+1)*np.log(1+M[k]**(x[0])))
    return -y-res

def logvs_lomax(x,M):
    n=np.size(M)
    c=n*np.log(x[0]*(x[1]**(x[0])))
    res=0
    for k in range(n):
        res=res+(x[0]+1)*np.log(x[1]+M[k])
    return -c+res

def logvs_weibull(x,M):
    n=np.size(M)
    c=n*np.log(x[1]/(x[0]**(x[1])))
    res=0
    for k in range(n):
        res=res+((x[1]-1)*np.log(M[k])-(M[k]**(x[1]))/(x[0]**(x[1])))
    return -c-res

### Espérances et moments d'ordre 2

def esp_burr(x):
    return gamma(x[1]-(1/x[0]))*gamma(1+(1/x[0]))*(1/gamma(x[1]))

def mom2_burr(x):
    return gamma(x[1]-(2/x[0]))*gamma(1+(2/x[0]))*(1/gamma(x[1]))

def esp_hyperexpo(x):
    return x[1]/(x[0]*(x[0]+x[1])) + x[0]/(x[1]*(x[0]+x[1]))

def mom2_hyperexpo(x):
    return (2*x[1]/(x[0]*x[0]*(x[0]+x[1])) + 2*x[0]/(x[1]*x[1]*(x[0]+x[1])))

def esp_lomax(x):
    return (x[1]/(x[0]-1))

def mom2_lomax(x):
    return (x[1]**x[1]*gamma(x[0]-2)*gamma(3))/(gamma(x[0]))

def esp_weibull(x):
    return x[0]*gamma(1+1/x[1])

def mom2_weibull(x):
    return x[0]*x[0]*gamma(1+2/x[1])

### Echantillons de test
m=generate_hyperexpo2(2,10,500)
ma=generate_hyperexpo2(2,10,500)
m2=np.random.normal(17,5,500)
m3=scipy.stats.burr12.rvs(15,3,size=500)

lomax=scipy.stats.lomax.rvs(c=2,scale=6,size=500)
weibull=scipy.stats.weibull_min.rvs(c=2,scale=5,size=500)


### Matrice hessienne
def derivee_seconde_differentes(fonction,x0,i,j,h=1e-06): # cas de dérivées partielles secondes sur deux variables différentes
    a=np.zeros(np.size(x0))
    a[i]=1
    b=np.zeros(np.size(x0))
    b[j]=1
    return (fonction(x0+h*a+h*b)-fonction(x0+h*a-h*b)-fonction(x0-h*a+h*b)+fonction(x0-h*a-h*b))/(4*h*h)

def derivee_seconde_identique(fonction,x0,i,h=1e-06): # cas de dérivée partielle seconde sur deux variables identiques
    a=np.zeros(np.size(x0))
    a[i]=1
    return (fonction(x0+h*a)-2*fonction(x0)+fonction(x0-h*a))/(h*h)

#fonction test2 : test2(x,y,z)=3x^2+4yz^2+5z^2
def test2(a): # attention : a est un np.array (autrement dit un vecteur)
    return 3*a[0]*a[0]+4*a[1]*a[2]*a[2]+5*a[2]*a[2]

def hessienne(fonction,x0,h=1e-06):
    res=np.zeros((np.size(x0),np.size(x0)))
    for i in range(0,np.size(x0)):
        for j in range(0,np.size(x0)):
            if (i==j):
                res[i][i]=derivee_seconde_identique(fonction,x0,i,h=1e-06)
            else:
                res[i][j]=derivee_seconde_differentes(fonction,x0,i,j,h=1e-06)
    return res
