import numpy as np
import math
import scipy.stats
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("loi", type=int, help="loi")
parser.add_argument("param1",type=float,help="param1")
parser.add_argument("param2",type=float,help="param2")
parser.add_argument("taille",type=int,help="taille")
args = parser.parse_args()

def logvs_hyperexpo(x,M): # x est un vecteur de R2 représentant les paramètres et M est un échantillon (x1,...,xn)
    res=0
    c=(x[0]*x[1])/(x[0]+x[1])
    for i in range(0,np.size(M)):
        res=res+np.log(c*(np.exp(-x[0]*M[i])+np.exp(-x[1]*M[i])))
    return res

def grad_logvs_hyperexpo(x,M):
    return gradient(lambda y: logvs_hyperexpo(y,M),x)

def max_vs(M):
    valeur_initiale=np.array([np.random.rand(),np.random.rand()])
    print(valeur_initiale)
    R=scipy.optimize.root(lambda x: grad_logvs_hyperexpo(x,M),valeur_initiale)
    return R

def generate_hyperexpo(l1,l2,N):
    valeur_initiale=np.random.rand()
    res=[]
    for i in range(N-1):
        u=np.random.rand()
        res.append((scipy.optimize.fsolve(lambda x: fdr_hyperexpo2(x,u,l1,l2),valeur_initiale))[0])
    return res

def contrainteE(x,M):
    return ((x[1]/(x[0]*(x[0]+x[1])) + x[0]/(x[1]*(x[0]+x[1])))-np.mean(M))

def contrainteE2(x,M):
    return ((2*x[1]/(x[0]*x[0]*(x[0]+x[1])) + 2*x[0]/(x[1]*x[1]*(x[0]+x[1])))-mom_emp2(M))

def mom_emp2(M):
    n=np.size(M)
    res=0
    for i in M:
        res=res+i*i
    return res/n

def eq1(x,M):
    return [gradient((lambda y: logvs_hyperexpo(y,M)),x)[0],gradient((lambda y: logvs_hyperexpo(y,M)),x)[1],contrainteE(x,M),contrainteE2(x,M)]

def max_vs_m1(M):
    valeur_initiale=np.array([np.random.rand()*3,np.random.rand()*3,0,0])
    R=scipy.optimize.fsolve(lambda x: eq1(x,M),valeur_initiale)
    return R

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
