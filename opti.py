import numpy as np


######
# Gradient
######

def derivee_num(fonction, x0, i, h=1e-06):
    a = np.zeros(np.size(x0))
    a[i] = 1
    return (fonction(x0+0.5*h*a)-fonction(x0-0.5*h*a))/h


# fonction test : test(x,y,z)=x+2yz+4z
def test(a):  # attention : a est un np.array (autrement dit un vecteur)
    return a[0]+2*a[1]*a[2]+4*a[2]


def gradient(fonction, point):
    res = np.array([])
    for k in range(0, np.size(point)):
        a = derivee_num(fonction, point, k, 1e-06)
        res = np.append(res, a)
    return res


######
# Matrice hessienne
#####
def derivee_seconde_differentes(fonction, x0, i, j, h=1e-06):  # cas de dérivées partielles secondes sur deux variables différentes
    a = np.zeros(np.size(x0))
    a[i] = 1
    b = np.zeros(np.size(x0))
    b[j] = 1
    return (fonction(x0+h*a+h*b)-fonction(x0+h*a-h*b)-fonction(x0-h*a+h*b)+fonction(x0-h*a-h*b))/(4*h*h)


def derivee_seconde_identique(fonction, x0, i, h=1e-06):  # cas de dérivée partielle seconde sur deux variables identiques
    a = np.zeros(np.size(x0))
    a[i] = 1
    return (fonction(x0+h*a)-2*fonction(x0)+fonction(x0-h*a))/(h*h)


# fonction test2 : test2(x,y,z)=3x^2+4yz^2+5z^2
def test2(a):  # attention : a est un np.array (autrement dit un vecteur)
    return 3*a[0]*a[0]+4*a[1]*a[2]*a[2]+5*a[2]*a[2]


def hessienne(fonction, x0, h=1e-06):
    res = np.zeros((np.size(x0), np.size(x0)))
    for i in range(0, np.size(x0)):
        for j in range(0, np.size(x0)):
            if (i == j):
                res[i][i] = derivee_seconde_identique(fonction, x0, i, h=1e-06)
            else:
                res[i][j] = derivee_seconde_differentes(fonction, x0, i, j, h=1e-06)
    return res
