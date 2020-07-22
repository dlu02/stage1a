import argparse
import numpy as np
import json
import math
from histogramme import histo_Continue, histo_discretes, discretes_continues
from annexes import convert, skewness, kurtosis


parser = argparse.ArgumentParser()
parser.add_argument("nom_fichier", type=str, help="nom du fichier")
parser.add_argument("size2", type=int, help="taille2")
args = parser.parse_args()

m = np.loadtxt(args.nom_fichier)


def do_operation(array, n):
    if (n == 0):
        return round(np.amin(array), 5)
    elif (n == 1):
        return round(np.amax(array), 5)
    elif (n == 2):
        return round(np.mean(array), 5)
    elif (n == 3):
        return round(np.var(array), 5)
    elif (n == 4):
        return round(np.std(array), 5)
    elif (n == 5):
        return round(skewness(array), 5)
    elif (n == 6):
        return round(kurtosis(array), 5)
    elif (n == 7):
        if (discretes_continues(array) == "discrete"):
            nb_rand = np.random.randint(1, 9999999)
            file = "../images/m" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
            histo_discretes(array, nom=file)
        if (discretes_continues(array) == "continue"):
            classe = int(5*math.log10(n))
            nb_rand = np.random.randint(1, 9999999)
            file = "../images/m" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
            histo_Continue(array, classe, nom=file)
            return nb_rand
    else:
        return "Saisie invalide."


L = {"min": do_operation(m, 0), "max": do_operation(m, 1), "moy": do_operation(m, 2), "var": do_operation(m, 3), "ec": do_operation(m, 4), "skew": do_operation(m, 5), "kurt": do_operation(m, 6), "hist": do_operation(m, 7)}  # dictionnaire des valeurs à calculer


######
# Script
######

if np.size(m) != args.size2:
    L = {"error": "error"}
else:
    L = {"min": do_operation(m, 0), "max": do_operation(m, 1), "moy": do_operation(m, 2), "var": do_operation(m, 3), "ec": do_operation(m, 4), "skew": do_operation(m, 5), "kurt": do_operation(m, 6), "hist": do_operation(m, 7)}  # dictionnaire des valeurs à calculer
res = json.dumps(L, default=convert)  # appliquer convert si le nombre est un entier numpy
print(res)
