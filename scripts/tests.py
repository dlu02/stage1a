import argparse
import numpy as np
import json
import math
import scipy.stats
import warnings
from histogramme import histo_Continue, histo_discretes, discretes_continues
from annexes import convert, skewness, kurtosis
from lois_theo import fdr_expopoly, fdr
from bib_estimation import max_vs_m1, max_vs_m2, max_vs_m1_epp, max_vs_m2_epp


parser = argparse.ArgumentParser()
parser.add_argument("nom_fichier", type=str, help="nom_fichier")
parser.add_argument("loi", type=str, help="loi")
parser.add_argument("modele", type=int, help="modele")
parser.add_argument("taille", type=int, help="taille")
parser.add_argument("type_test", type=int, help="type_test")
args = parser.parse_args()


######
# Test Khi-2
######

# liste des extrémités des classes
def int_classe(f):
	k = int(5*math.log10(np.size(f)))
	data = np.array([x for x in f])
	Ext = [min(data)+(max(data)-min(data))*i/(1.0*k) for i in range(k+1)]
	return Ext


# liste du nombre d'occurences par classe
def tableau(f):
	classes = int_classe(f)
	E = np.array(f)
	res = []
	for i in range(0, np.size(classes)-1):
		if i == 0:
			res.append(np.size(E[np.where((E >= classes[i]) & (E <= classes[i+1]))]))
		elif i == np.size(classes)-1:
			res.append(np.size(E[np.where((E > classes[i]) & (E <= classes[i+1]))]))
		else:
			res.append(np.size(E[np.where((E > classes[i]) & (E <= classes[i+1]))]))
	return res


# liste des fréquences empiriques par classe
def freq_emp(f):
	nombre = tableau_regroupement(f)[1]
	res = []
	for i in nombre:
		res.append(i/len(f))
	return res


# liste des fréquences théoriques (H0 : loi de fonction de répartition fdr et de paramètres a et b)
def freq_theo(f, fdr, a, b):
	classes = tableau_regroupement(f)[0]
	res = []
	for i in range(0, len(classes)-1):
		res.append(abs(fdr(classes[i+1], a, b)-fdr(classes[i], a, b)))
	return res


# test du chi2 (ajustement à une loi de fonction de répartition fdr et de paramètres a et b à estimer) - variable continue
def chi2(f, fdr, a, b):
	f = np.array(f)
	tab = [np.size(f)*i for i in freq_emp(f)]
	theo = [np.size(f)*i for i in freq_theo(f, fdr, a, b)]
	res = 0
	for i in range(0, len(tab)):
		res = res + ((tab[i]-theo[i])**2)/(theo[i])
	return 1-(scipy.stats.chi2.cdf(res, len(tab)-2))


# regroupe les éventuelles classes à trop faible fréquence
def tableau_regroupement(f):
	tab_res = []
	E = tableau(f)
	classes = int_classe(f)
	classes_res = [classes[0]]
	acc = 0
	for i in range(1, len(classes)):
		if (E[i-1]+acc) >= 5:
			classes_res.append(classes[i])
			tab_res.append(E[i-1]+acc)
			acc = 0
		else:
			acc = acc+E[i-1]
	return (classes_res, tab_res)


######
# Test Khi-2 spécifique expo poly
######

# liste des fréquences théoriques (H0 : loi de fonction de répartition fdr et de paramètres a et b)
def freq_theo_epp(f, a, b):
	a.insert(0, b)
	classes = tableau_regroupement(f)[0]
	res = []
	for i in range(0, len(classes)-1):
		res.append(abs(fdr_expopoly(classes[i+1], a, b)-fdr_expopoly(classes[i], a, b)))
	del a[0]
	return res


# test du chi2 cas expopoly (ajustement à une loi de fonction de répartition fdr_expopoly et de paramètres a et b à estimer) - variable continue
def chi2_epp(f, a, b):
	f = np.array(f)
	tab = [np.size(f)*i for i in freq_emp(f)]
	theo = [np.size(f)*i for i in freq_theo_epp(f, a, b)]
	res = 0
	for i in range(0, len(tab)):
		res = res + ((tab[i]-theo[i])**2)/(theo[i])
	return 1-(scipy.stats.chi2.cdf(res, len(tab)-2))


########
# Test KS
########

def testks(data, loi, p1, p2):
	res = 0
	fdr_theo = fdr(loi)
	for k in data:
		b = abs(fdr_empirique(data, k)-fdr_theo(k, p1, p2))
		if b > res:
			res = b
	pval = 0
	for k in range(1, 3):
		pval = pval+(((-1)**(k+1))*np.exp(-2*k*k*np.size(data)*res*res))
	return 2*pval


def fdr_empirique(data, x):
	data = sorted(data)
	n = len(data)
	return sum([1 for i in range(n) if data[i] <= x])/(1.0*n)


########
# Test KS spécifique expopoly
########

def testks_epp(data, p1, p2):
	res = 0
	for k in data:
		b = abs(fdr_empirique(data, k)-fdr_expopoly(k, p1, p2))
		if b > res:
			res = b
	pval = 0
	for k in range(1, 3):
		pval = pval+(((-1)**(k+1))*np.exp(-2*k*k*np.size(data)*res*res))
	return 2*pval


#####
# Script
#####

warnings.filterwarnings("ignore")  # ignorer les warnings


# opération à effectuer selon la valeur de n
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
				nb_rand = 2*np.random.randint(1, 4999999)
				file = "../images/" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
				histo_discretes(array, nom=file)
				return nb_rand
			if (discretes_continues(array) == "continue"):
				classe = int(5*math.log10(n))
				nb_rand = 2*np.random.randint(1, 4999999)
				file = "../images/" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
				histo_Continue(array, classe, nom=file)
				return nb_rand
			else:
				return "Saisie invalide"
		elif (n == 8):
			global temp, va
			temp = max_vs_m1_epp(array, args.taille)
			va = []
			for i in range(1, np.size(temp)):
				va.append(round(temp[i], 5))
			return va
		elif (n == 9):
			return temp[0]
		elif (n == 10):
			temp = max_vs_m2_epp(array, args.taille)
			va = []
			for i in range(1, np.size(temp)):
				va.append(round(temp[i], 5))
			return va
		elif (n == 11):
			return temp[0]
		elif (n == 12):
			a = chi2_epp(array, va, temp[0])
			if np.isfinite(a):
				return round(a, 5)
			else:
				return 0
		elif (n == 13):
			a = testks_epp(array, va, temp[0])
			if (np.isfinite(a)):
				return round(a, 5)
			else:
				return 0
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
				nb_rand = 2*np.random.randint(1, 4999999)
				file = "../images/" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
				histo_discretes(array, nom=file)
				return nb_rand
			if (discretes_continues(array) == "continue"):
				classe = int(5*math.log10(n))
				nb_rand = 2*np.random.randint(1, 4999999)
				file = "../images/" + str(nb_rand) + ".png"  # le fichier est enregistré dans le dossier images situé dans le dossier parent à ~ (~ est le dossier où est exécuté le script)
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
		elif (n == 12):
			a = chi2(array, fdr(loi), temp[0], temp[1])
			if np.isfinite(a):
				return round(a, 5)
			else:
				return 0
		elif (n == 13):
			a = testks(array, loi, temp[0], temp[1])
			if (np.isfinite(a)):
				return round(a, 5)
			else:
				return 0
		else:
			return "Saisie invalide."


m = np.loadtxt(args.nom_fichier)

if discretes_continues(m) == "discrete":
	L = {"error": "error"}
else:
	if (args.type_test == 1):
		ntest = 12
	else:
		ntest = 13
	if (args.modele == 1):
		L = {"min": do_operation(m, 0, args.loi), "max": do_operation(m, 1, args.loi), "moy": do_operation(m, 2, args.loi), "var": do_operation(m, 3, args.loi), "ec": do_operation(m, 4, args.loi), "skew": do_operation(m, 5, args.loi), "kurt": do_operation(m, 6, args.loi), "hist": do_operation(m, 7, args.loi), "param_a": do_operation(m, 8, args.loi), "param_b": do_operation(m, 9, args.loi), "test_pvalue": do_operation(m, ntest, args.loi)}
	elif (args.modele == 2):
		L = {"min": do_operation(m, 0, args.loi), "max": do_operation(m, 1, args.loi), "moy": do_operation(m, 2, args.loi), "var": do_operation(m, 3, args.loi), "ec": do_operation(m, 4, args.loi), "skew": do_operation(m, 5, args.loi), "kurt": do_operation(m, 6, args.loi), "hist": do_operation(m, 7, args.loi), "param_a": do_operation(m, 10, args.loi), "param_b": do_operation(m, 11, args.loi), "test_pvalue": do_operation(m, ntest, args.loi)}

res = json.dumps(L, default=convert)  # appliquer convert si le nombre est un entier numpy
print(res)
