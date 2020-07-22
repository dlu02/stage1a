import numpy as np
import argparse
import json
from bib_densite import trace_densite
from annexes import convert
from lois_theo import expo_poly, fdr_expopoly, expo_poly2, fdr_expopoly2

parser = argparse.ArgumentParser()
parser.add_argument("nom_fichier", type=str, help="nom du fichier")
parser.add_argument("b", type=float, help="b")
args = parser.parse_args()

m = np.loadtxt(args.nom_fichier)


######
# Script
######
if (np.size(m) == 1):
    L = {"hist": trace_densite(expo_poly2, fdr_expopoly2, m, args.b)}
else:
    L = {"hist": trace_densite(expo_poly, fdr_expopoly, m, args.b)}
res = json.dumps(L, default=convert)  # appliquer convert si le nombre est un entier numpy
print(res)
