import argparse
import numpy as np
from scipy import stats
import math
import json
from histogramme import histo_Continue, histo_discretes, discretes_continues
from annexes import convert, skewness, kurtosis

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
            file = "../images/u" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
            histo_discretes(array, nom=file)
        if (discretes_continues(array) == "continue"):
            classe = int(5*math.log10(n))
            nb_rand = np.random.randint(1, 9999999)
            file = "../images/u" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
            histo_Continue(array, classe, nom=file)
            return nb_rand
    else:
        return "Saisie invalide."


L = {"min": do_operation(m, 0), "max": do_operation(m, 1), "moy": do_operation(m, 2), "var": do_operation(m, 3), "ec": do_operation(m, 4), "skew": do_operation(m, 5), "kurt": do_operation(m, 6), "hist": do_operation(m, 7)}  # dictionnaire des valeurs à calculer


res = json.dumps(L, default=convert)  # appliquer convert si le nombre est un entier numpy
print(res)
