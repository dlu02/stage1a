import argparse
import json
from lois_theo import hyperexpo, lomax, weibull, burr, expo_convo, fdr_hyperexpo, fdr_lomax, fdr_weibull, fdr_burr, fdr_expoconvo
from annexes import convert
from bib_densite import trace_densite

parser = argparse.ArgumentParser()
parser.add_argument("a", type=float, help="a")
parser.add_argument("b", type=float, help="b")
parser.add_argument("loi", type=int, help="loi")
args = parser.parse_args()


# fonction de sélection de l'opération à effectuer
def do_operation():
    if (args.loi == 0):
        return trace_densite(hyperexpo, fdr_hyperexpo, args.a, args.b)
    elif (args.loi == 1):
        return trace_densite(lomax, fdr_lomax, args.a, args.b)
    elif (args.loi == 2):
        return trace_densite(weibull, fdr_weibull, args.a, args.b)
    elif (args.loi == 3):
        return trace_densite(burr, fdr_burr, args.a, args.b)
    elif (args.loi == 4):
        return trace_densite(expo_convo, fdr_expoconvo, args.a, args.b)


# exécution du script
L = {"hist": do_operation()}
res = json.dumps(L, default=convert)  # appliquer convert si le nombre est un entier numpy
print(res)
