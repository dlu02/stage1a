import argparse
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import json
import math

parser = argparse.ArgumentParser()
parser.add_argument("loi", type=int, help="loi")
parser.add_argument("param1", type=float, help="param1")
parser.add_argument("param2", type=float, help="param2")
parser.add_argument("taille", type=int, help="taille")
args = parser.parse_args()

if args.loi == 1:
    m = np.random.normal(args.param1, args.param2, args.taille)
elif args.loi == 2:
    m = stats.expon.rvs(scale=args.param1, size=args.taille)
elif args.loi == 3:
    m = stats.poisson.rvs(mu=args.param1, size=args.taille)
else:
    m = np.random.binomial(args.param1, args.param2, args.taille)


###############################################################
# Histogramme
###############################################################

def Mode_D(data):  # mode (discrètes)
    data = list(data)
    Dic = {}
    for x in sorted(data):
        Dic[x] = data.count(x)
    Valeurs = [t for t in Dic.keys()]
    Effectifs = [t for t in Dic.values()]
    n_max = max(Effectifs)
    return [x for x in Valeurs if Dic[x] == n_max]


def discretes_continues(data):  # Tester si les données sont discrètes ou continues
    data = [x for x in data]
    dic_donnees = {}
    for x in sorted(data):
        dic_donnees[x] = data.count(x)
    effectifs = [v for v in dic_donnees.values()]
    # test
    if max(effectifs) > 1:
        return "discrete"
    else:
        return "continue"


def comptage_occurrences(data):  # nombre d'occurrences pour les données discrètes
    data = sorted(data)
    Dic_compt = {}
    for valeur in data:
        Dic_compt[valeur] = data.count(valeur)
    return Dic_compt


def histo_discretes(data, nom=None):  # Histogramme des données discrètes
    # nom : le nom (sans extension)  pour la figure

    plt.rcParams['hatch.color'] = [0.9, 0.9, 0.9]
    D = comptage_occurrences(data)
    valeurs = [k for k in D.keys()]
    effectifs = [v for v in D.values()]
    i_mode = np.argmax(effectifs)  # indice max
    # multi_mode
    indice_mode = [i for i in range(len(effectifs)) if effectifs[i] == effectifs[i_mode]]

    fig1 = plt.figure(figsize=(10, 7))
    ax1 = fig1.add_subplot(111)
    # cacher le cadre (haut,bas , à gauche)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(False)

    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')

    ax1.set_yticks([])

    ax1.set_xticks(valeurs)  # positions des extrémités des valeurs
    ax1.set_xticklabels(valeurs, fontsize=10, rotation=25)
    ax1.set_xlabel("Valeurs", fontsize=13)
    ax1.set_ylabel("Effectifs", fontsize=13)

    for k in range(len(valeurs)):
        if k not in indice_mode:
            plt.bar(valeurs[k], height=effectifs[k], edgecolor="white")
        else:
            plt.bar(valeurs[k], height=effectifs[k], edgecolor="white", color=[0.15, 0.15, 0.85], hatch="X", lw=1., zorder=0)
        for i in range(len(valeurs)):
            ax1.text(valeurs[i], effectifs[i], "%d" % (effectifs[i]), fontsize=9, horizontalalignment='center', verticalalignment='bottom', style='italic')

    if nom is None:
        plt.show()
    else:
        plt.savefig("hist.png")
        plt.close()


def histo_Continue(data, k, nom=None):
    # k=nombre de classes
    # nom : le nom (sans extension)  pour la figure
    # hachure
    plt.rcParams['hatch.color'] = [0.9, 0.9, 0.9]
    data = np.array([x for x in data])
    Ext = [min(data)+(max(data)-min(data))*i/(1.0*k) for i in range(k+1)]
    # Centres des classes
    C = [0.5*(Ext[i] + Ext[i+1]) for i in range(k)]
    # Effectifs des classes
    NN = []
    for i in range(k):
        NN.append(((Ext[i] <= data) & (data <= Ext[i+1])).sum())
    # pour la classe modale
    indice_max = [i for i in range(k) if NN[i] == np.max(NN)]
    TT = [str("{:.4f}".format(t)) for t in Ext]  # pour afficher les extrémités des classes
    # CC = [str("{:.4f}".format(t)) for t in C]   # pour afficher les centres des classes
    fig = plt.figure(figsize=(10, 7))
    ax1 = fig.add_subplot(111)
    # cacher le cadre
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.xaxis.set_ticks_position('bottom')

    ax1.set_yticks([])
    largeur = Ext[1] - Ext[0]  # largeur des classes

    for i in range(k):
        if i in indice_max:
            ax1.bar(C[i], NN[i], largeur, color=[0.15, 0.15, 0.80], edgecolor="white", hatch="/", lw=1., zorder=0, alpha=0.9)
        else:
            ax1.bar(C[i], NN[i], largeur, align='center', edgecolor="white")
        ax1.text(C[i], NN[i], "%d" % (NN[i]), fontsize=8, style='italic', horizontalalignment='center', verticalalignment='bottom')
    ax1.set_xticks(Ext)  # positions des extrémités des classes
    ax1.set_xticklabels(TT, fontsize=8, rotation=45)
    # ax1.set_xticklabels(CC ,fontsize=8, rotation=45)
    ax1.set_xlim(np.min(data)-0.75*largeur, np.max(data)+0.75*largeur)
    ax1.set_ylim(0.0, np.max(NN) + 3.0)
    ax1.set_xlabel("Valeurs", fontsize=12)
    ax1.set_ylabel("Effectifs", fontsize=14)

    if nom is None:
        plt.show()
    else:
        plt.savefig("hist.png", dpi=400)
        plt.close()


def do_operation(array, n):
    if (n == 0):
        return round(np.amin(array), 5)
    else:
        if (n == 1):
            return round(np.amax(array), 5)
        else:
            if (n == 2):
                return round(np.mean(array), 5)
            else:
                if (n == 3):
                    return round(np.var(array), 5)
                else:
                    if (n == 4):
                        return round(np.std(array), 5)
                    else:
                        if (n == 5):
                            return round(skewness(array), 5)
                        else:
                            if (n == 6):
                                return round(kurtosis(array), 5)
                            else:
                                if (n == 7):
                                    if (discretes_continues(array) == "discrete"):
                                        histo_discretes(array, nom="hist")
                                    if (discretes_continues(array) == "continue"):
                                        classe = int(5*math.log10(args.taille))
                                        histo_Continue(array, classe, nom="hist")
                                else:
                                    return "Saisie invalide."


def Moment_r(data, r):
    fonc_r = (lambda x: x**r)
    S = np.sum(fonc_r(data))
    return S/(1.0*np.size(data))


def Moment_cr(data, r):
    m = Moment_r(data, 1)
    fonc_r = (lambda x: (x-m)**r)
    S = np.sum(fonc_r(data))
    return S/(1.0*np.size(data))


def skewness(array):
    return (Moment_cr(array, 3)/(Moment_cr(array, 2)**(3/2)))


def kurtosis(array):
    return (Moment_cr(array, 4)/(Moment_cr(array, 2)**2)-3)


L = {"min": do_operation(m, 0), "max": do_operation(m, 1), "moy": do_operation(m, 2), "var": do_operation(m, 3), "ec": do_operation(m, 4), "skew": do_operation(m, 5), "kurt": do_operation(m, 6), "hist": do_operation(m, 7)}  # dictionnaire des valeurs à calculer


def convert(n):  # pour convertir les entiers numpy en flottants usuels pour que le parse JSON fonctionne et envoie bien le tableau à PHP
    if isinstance(n, np.int64):
        return float(n)


res = json.dumps(L, default=convert)  # appliquer convert si le nombre est un entier numpy
print(res)
