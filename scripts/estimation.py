import argparse
import numpy as np
import json
import warnings
import math
from histogramme import histo_Continue, histo_discretes, discretes_continues
from annexes import convert, skewness, kurtosis
from bib_estimation import max_vs_m1, max_vs_m2, max_vs_m1_epp, max_vs_m2_epp

parser = argparse.ArgumentParser()
parser.add_argument("nom_fichier", type=str, help="nom du fichier")
parser.add_argument("loi", type=str, help="loi")
parser.add_argument("modele", type=int, help="modele")
parser.add_argument("taille", type=int, help="taille")
args = parser.parse_args()


########
# Script
########

def do_operation(array, n, loi):
	if loi == "expo_poly":
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
				file = "../images/e" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
				histo_discretes(array, nom=file)
				return nb_rand
			if (discretes_continues(array) == "continue"):
				classe = int(5*math.log10(n))
				nb_rand = np.random.randint(1, 9999999)
				file = "../images/e" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
				histo_Continue(array, classe, nom=file)
				return nb_rand
			else:
				return "Saisie invalide"
		elif (n == 8):
			global temp
			temp = max_vs_m1_epp(array, args.taille)
			res = []
			for i in range(1, np.size(temp)):
				res.append(round(temp[i], 5))
			return res
		elif (n == 9):
			return round(temp[0], 5)
		elif (n == 10):
			temp = max_vs_m2_epp(array, args.taille)
			res = []
			for i in range(1, np.size(temp)):
				res.append(round(temp[i], 5))
			return res
		elif (n == 11):
			return round(temp[0], 5)
		else:
			return "Saisie invalide."
	else:
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
				file = "../images/e" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
				histo_discretes(array, nom=file)
			if (discretes_continues(array) == "continue"):
				classe = int(5*math.log10(n))
				nb_rand = np.random.randint(1, 9999999)
				file = "../images/e" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
				histo_Continue(array, classe, nom=file)
				return nb_rand
			else:
				return "Saisie invalide"
		elif (n == 8):
			temp = max_vs_m1(array, loi)
			return round(temp[0], 5)
		elif (n == 9):
			return round(temp[1], 5)
		elif (n == 10):
			temp = max_vs_m2(array, loi)
			return round(temp[0], 5)
		elif (n == 11):
			return round(temp[1], 5)
		else:
			return "Saisie invalide."


warnings.filterwarnings("ignore")  # ignorer les warnings


####
# script
####
m = np.loadtxt(args.nom_fichier)

if discretes_continues(m) == "discrete":
	L = {"error": "error"}
else:
	if (args.modele == 1):
		L = {"min": do_operation(m, 0, args.loi), "max": do_operation(m, 1, args.loi), "moy": do_operation(m, 2, args.loi), "var": do_operation(m, 3, args.loi), "ec": do_operation(m, 4, args.loi), "skew": do_operation(m, 5, args.loi), "kurt": do_operation(m, 6, args.loi), "hist": do_operation(m, 7, args.loi), "param_a": do_operation(m, 8, args.loi), "param_b": do_operation(m, 9, args.loi)}
	elif (args.modele == 2):
		L = {"min": do_operation(m, 0, args.loi), "max": do_operation(m, 1, args.loi), "moy": do_operation(m, 2, args.loi), "var": do_operation(m, 3, args.loi), "ec": do_operation(m, 4, args.loi), "skew": do_operation(m, 5, args.loi), "kurt": do_operation(m, 6, args.loi), "hist": do_operation(m, 7, args.loi), "param_a": do_operation(m, 10, args.loi), "param_b": do_operation(m, 11, args.loi)}

res = json.dumps(L, default=convert)  # appliquer convert si le nombre est un entier numpy
print(res)
