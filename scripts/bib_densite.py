import matplotlib.pyplot as plt
import numpy
import random


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


# tracé de la densité (2 param)
def Axes_simple1(axe):
    axe.spines['top'].set_visible(False)
    axe.spines['right'].set_visible(False)
    axe.xaxis.set_ticks_position('bottom')
    axe.yaxis.set_ticks_position('left')


def trace_densite(f, fdr_loi, a, b):
    nb_rand = numpy.random.randint(1, 9999999)
    file = "../images/d" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
    fig, ax = plt.subplots(figsize=(10, 7))
    Axes_simple1(ax)
    # détermination de la borne sup de l'intervalle
    m7 = fdr_inv_2param([a, b, 0.98], fdr_loi)
    plt.plot(densite_2param(a, b, f, m7)[0], densite_2param(a, b, f, m7)[1], color=[random.random(), random.random(), random.random()], lw=3)
    plt.xlabel('$x$', fontsize=15)
    plt.ylabel('$f(x)$', fontsize=17)
    plt.savefig(file, dpi=400)
    plt.close()
    return nb_rand
