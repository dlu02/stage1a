import matplotlib.pyplot as plt
import numpy
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nom_fichier", type=str, help="nom du fichier")
parser.add_argument("b", type=float, help="b")
args = parser.parse_args()

m = numpy.loadtxt(args.nom_fichier)


def densite_2param(a, b, f, x_max):
    nb_point = 200
    # x_max de l'axe des x
    intervalle = [max(0, x_max)*i/(nb_point-1) for i in range(nb_point)]
    y = [f(t, a, b) for t in intervalle]  # densité
    return intervalle, y


def fdr_inv_2param(param, fdr_Loi):  # déterminer la fonction de répartition réciproque numériquement (2 paramètres)
    import warnings
    warnings.filterwarnings("ignore")  # ignorer les warnings
    import scipy.optimize
    a = param[0]
    b = param[1]
    alpha = param[2]
    valeur_initiale = numpy.random.rand()
    R = scipy.optimize.fsolve((lambda x: fdr_Loi(x, a, b)-alpha), valeur_initiale)
    return R[0]


def Axes_simple1(axe):
    axe.spines['top'].set_visible(False)
    axe.spines['right'].set_visible(False)
    axe.xaxis.set_ticks_position('bottom')
    axe.yaxis.set_ticks_position('left')


def trace_densite(f, fdr_loi, a, b):
    fig, ax = plt.subplots(figsize=(10, 7))
    Axes_simple1(ax)
    # détermination de la borne sup de l'intervalle
    m7 = fdr_inv_2param([a, b, 0.98], fdr_loi)

    plt.plot(densite_2param(a, b, f, m7)[0], densite_2param(a, b, f, m7)[1], color=[random.random(), random.random(), random.random()], lw=3)
    plt.xlabel('$x$', fontsize=15)
    plt.ylabel('$f(x)$', fontsize=17)
    plt.savefig("densite.png", dpi=400)
    plt.close()


######
# loi exponentielle polynomiale
######

def fact(n):
    if n < 2:
        return 1
    else:
        return n*fact(n-1)


def cab(a, b):  # coefficient C(a,b)
    res = 0
    for k in range(1, numpy.size(a)+1):
        res = res+((a[k-1]*fact(k))/(b**(k+1)))
    return 1/res


def expo_poly(x, a, b):
    res = 0
    for k in range(0, numpy.size(a)):
        res = res+a[k]*(x**k)
    return cab(a, b)*res*numpy.exp(-b*x)


def fdr_expopoly(x, a, b):
    res = 0
    for k in range(0, numpy.size(a)):
        res = res+a[k]*fact(k)/(b**(k+1))
    return cab(a, b)*res*(1-numpy.exp(-b*x))


# cas où a est un unique réel
def cab2(a, b):
    return (b*b)/a


def expo_poly2(x, a, b):
    return cab2(a, b)*a*x*numpy.exp(-b*x)


def fdr_expopoly2(x, a, b):
    return cab2(a, b)*a*(1-numpy.exp(-b*x))/(b*b)


######
# Script
######
if (numpy.size(m) == 1):
    trace_densite(expo_poly2, fdr_expopoly2, m, args.b)
else:
    trace_densite(expo_poly, fdr_expopoly, m, args.b)
