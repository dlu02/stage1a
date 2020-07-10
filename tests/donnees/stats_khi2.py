import argparse
import numpy as np
import json
import matplotlib.pyplot as plt
import math
import scipy.stats
import warnings
from scipy.special import gamma, binom

parser = argparse.ArgumentParser()
parser.add_argument("nom_fichier", type=str, help="nom du fichier")
parser.add_argument("loi", type=str, help="loi")
parser.add_argument("modele", type=int, help="modele")
parser.add_argument("taille", type=int, help="taille")
args = parser.parse_args()

m = np.loadtxt(args.nom_fichier)
n = np.size(m)

###############################
# Construction de l'histogramme
###############################


def Mode_D(data):
	data = list(data)
	Dic = {}
	for x in sorted(data):
		Dic[x] = data.count(x)
	Valeurs = [t for t in Dic.keys()]
	Effectifs = [t for t in Dic.values()]
	n_max = max(Effectifs)
	return [x for x in Valeurs if Dic[x] == n_max]


###############################################################
# Tester si les données sont discrètes ou continues
###############################################################

def discretes_continues(data):
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


###############################################################
# nombre d'occurrences pour les données discrètes
###############################################################
def comptage_occurrences(data):
	data = sorted(data)
	Dic_compt = {}
	for valeur in data:
		Dic_compt[valeur] = data.count(valeur)
	return Dic_compt


###############################################################
# Histogramme des données discrètes
###############################################################

def histo_discretes(data, nom=None):
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
	# positions des extrémités des valeurs
	ax1.set_xticks(valeurs)
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
		plt.savefig("hist.png", dpi=400)
		plt.close()


###############################################################
# histogramme pour les Données Continues
###############################################################
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


def convert(n):  # pour convertir les entiers numpy en flottants usuels pour que le parse JSON fonctionne et envoie bien le tableau à PHP
	if isinstance(n, np.int64):
		return float(n)


# factorielle
def fact(n):
	if n <= 1:
		return 1
	else:
		return n*fact(n-1)


#################
# Estimation des paramètres
################

# Gradient
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


# fonction de calcul de la norme du gradient
def norme(vect):
	return np.dot(vect, vect)


# scipy fsolve
# contraintes
def contrainte1(x, M, ep):
	return 1e-6 - abs(ep(x)-np.mean(M))


def contrainte2(x, M, mom):
	return 1e-6 - abs(-mom(x)+mom_emp2(M))


def contrainte3(x, loi, M):
	mom3_c = mom3(loi)
	mom2_c = mom2(loi)
	esp_c = esp(loi)
	return (mom3_c(x)-3*esp_c(x)*mom2_c(x)-2*(esp_c(x)**3))*skewnessE(x, M)


# système d'équation à résoudre
def eq1_bis(x, M, logvs, esp, mom2):
	return [gradient((lambda y: logvs(y, M)), x)[0], gradient((lambda y: logvs(y, M)), x)[1], contrainte1(x, M, esp), contrainte2(x, M, mom2)]


def max_vs_m1(M, loi):
	ls = log_vs(loi)
	moy = esp(loi)
	mom2_f = mom2(loi)
	cons = [{'type': 'ineq', 'fun': (lambda x: contrainte2(x, M, mom2_f))}, {'type': 'ineq', 'fun': (lambda x: contrainte1(x, M, moy))}]
	res = []
	Rlist = []
	for k in range(0, 5):
		valeur_initiale = np.array([np.random.rand(), np.random.rand()])
		R = scipy.optimize.minimize((lambda x: ls(x, M)), valeur_initiale, tol=1e-6, options={'maxiter': 300}, constraints=cons).x
		res.append(norme(gradient((lambda y: ls(y, M)), R)))
		Rlist.append(R)
		if norme(gradient((lambda y: ls(y, M)), R)) < 1e-6:
			return R
	ind = res.index(min(res))
	return Rlist[ind]


def max_vs_m2(M, loi):
	cons = [{'type': 'ineq', 'fun': (lambda x: contrainte3(x, loi, M))}]
	ls = log_vs(loi)
	res = []
	Rlist = []
	for k in range(0, 20):
		valeur_initiale = np.array([np.random.rand(), np.random.rand()])
		R = scipy.optimize.minimize((lambda x: ls(x, M)), valeur_initiale, tol=1e-6, options={'maxiter': 300}, constraints=cons).x
		res.append(norme(gradient((lambda y: ls(y, M)), R)))
		Rlist.append(R)
		if norme(gradient((lambda y: ls(y, M)), R)) < 1e-6:
			return R
	ind = res.index(min(res))
	return Rlist[ind]


def mom_emp2(M):
	n = np.size(M)
	res = 0
	for i in range(n):
		res = res + M[i] * M[i]
	return res/n


########
# Log-vraisemblances
#######

def logvs_hyperexpo(x, M):  # x est un vecteur de R2 représentant les paramètres et M est un échantillon (x1,...,xn)
	res = 0
	c = (x[0] * x[1]) / (x[0] + x[1])
	for i in range(0, np.size(M)):
		res = res + np.log(c) + np.log(np.exp(-x[0] * M[i]) + np.exp(-x[1] * M[i]))
	return res


def logvs_burr(x, M):
	n = np.size(M)
	y = n * np.log(x[0] * x[1])
	res = 0
	for k in range(0, n):
		res = res + ((x[0]-1)*np.log(M[k])-(x[1]+1)*np.log(1+M[k]**(x[0])))
	return -y-res


def logvs_lomax(x, M):
	n = np.size(M)
	c = n*np.log(x[0]*(x[1]**(x[0])))
	res = 0
	for k in range(n):
		res = res+(x[0]+1)*np.log(x[1]+M[k])
	return -c+res


def logvs_weibull(x, M):
	n = np.size(M)
	c = n*np.log(x[1]/(x[0]**(x[1])))
	res = 0
	for k in range(n):
		res = res + ((x[1]-1)*np.log(M[k])-(M[k]**(x[1]))/(x[0]**(x[1])))
	return -c-res


def logvs_expoconvo(x, M):
	n = np.size(M)
	c = n*np.log(x[0]*x[1])-n*np.log(x[1]-x[0])
	res = 0
	for k in range(n):
		res = res+np.log(np.exp(-x[0]*M[k])-np.exp(-x[1]*M[k]))
	return -c-res


############
# Espérances ; moments d'ordre 2,3 ; moments centrés des lois
############

def esp_burr(x):
	return gamma(x[1]-(1/x[0]))*gamma(1+(1/x[0]))*(1/gamma(x[1]))


def mom2_burr(x):
	return gamma(x[1]-(2/x[0]))*gamma(1+(2/x[0]))*(1/gamma(x[1]))


def mom3_burr(x):
	return gamma(1+3/x[0])*gamma(x[1]-3/x[0])*(1/gamma(x[1]))


def momc_burr(x, k):
	res = 0
	for i in range(k+1):
		res = res + ((fact(k)*((-1)**i)*(esp_weibull(x)**(k-i))*gamma(1+i/x[0])*gamma(x[1]-i/x[0]))/(fact(i)*fact(k-i)*gamma(x[1])))
	return res


def esp_hyperexpo(x):
	return x[1]/(x[0]*(x[0]+x[1])) + x[0]/(x[1]*(x[0]+x[1]))


def mom2_hyperexpo(x):
	return (2*x[1]/(x[0]*x[0]*(x[0]+x[1])) + 2*x[0]/(x[1]*x[1]*(x[0]+x[1])))


def mom3_hyperexpo(x):
	return ((6*x[1])/((x[0]**3)*(x[0]+x[1])) + (6*x[0])/((x[1]**3)*(x[0]+x[1])))


def momc_hyperexpo(x, k):
	a, b = x
	res = 0
	for i in range(0, k+1):
		res = res + (((-1)**i)/fact(i))
	c1 = b/(a+b)
	c2 = a/(a+b)
	return res*((c1*fact(k))/(a**k)+(c2*fact(k))/(b**k))


def esp_lomax(x):
	return (x[1]/(x[0]-1))


def mom2_lomax(x):
	return (x[1]**x[1]*gamma(x[0]-2)*gamma(3))/(gamma(x[0]))


def mom3_lomax(x):
	return ((x[1]**3)*gamma(x[0]-3)*gamma(4))/(gamma(x[0]))


def momc_lomax(x, k):
	res = 0
	for i in range(k+1):
		res = res+((fact(k)*((-1)**i)*(esp_lomax(x)**(k-i))*(x[1]**i)*gamma(x[0]-i)*gamma(i+1))/(fact(i)*fact(k-i)*gamma(x[0])))
	return res


def esp_weibull(x):
	return x[0]*gamma(1+1/x[1])


def mom2_weibull(x):
	return x[0]*x[0]*gamma(1+2/x[1])


def mom3_weibull(x):
	return x[0]*x[0]*x[0]*gamma(1+3/x[1])


def momc_weibull(x, k):
	res = 0
	for i in range(k+1):
		res = res + ((fact(k)*((-1)**i)*(esp_weibull(x)**(k-i))*(x[0]**i)*gamma(1+i/x[1]))/(fact(i)*fact(k-i)))
	return res


def esp_expoconvo(x):
	if x[0] == x[1]:
		return 2/x[0]
	else:
		return 1/x[0]+1/x[1]


def mom2_expoconvo(x):
	if x[0] == x[1]:
		return 6/(x[0]*x[0])
	else:
		return ((2*x[1])/((x[0]**2)*(x[1]-x[0])) - (2*x[0])/((x[1]**2)*(x[1]-x[0])))


def mom3_expoconvo(x):
	if x[0] == x[1]:
		return 24/(x[0]**3)
	else:
		return ((6*x[1])/((x[0]**3)*(x[1]-x[0])) - (6*x[0])/((x[1]**3)*(x[1]-x[0])))


def momc_expoconvo(x, k):
	if (x[0] != x[1]):
		res = 0
		c1 = x[1]/(x[1]-x[0])
		c2 = x[0]/(x[1]-x[0])
		for i in range(k+1):
			res = res + ((fact(k)*((-1)**i)*(esp_expoconvo(x)**(k-i))*(fact(i)*c1/(x[0]**i)-c2*fact(i)/(x[1]**i)))/(fact(i)*fact(k-i)))
		return res
	else:
		res = 0
		for i in range(k+1):
			res = res + ((fact(k)*((-1)**i)*(esp_weibull(x)**(k-i))*fact(2+k-1))/(fact(i)*fact(k-i)*(x[0])**i))
		return res


#########
# Fonctions de répartition
#########

def fdr_burr(x, a, b):
	return 1 - (1 + x**a)**(-b)


def fdr_expoconvo(x, a, b):
	if a == b:
		return 1 - np.exp(-a*x)*(a*x+1)
	else:
		return 1 + (a/(b-a))*np.exp(-b*x)-(b/(b-a))*np.exp(-a*x)


def fdr_weibull(x, a, b):
	return 1 - np.exp(-(x/a)**b)


def fdr_hyperexpo(x, l1, l2):
	c = (l1*l2)/(l1+l2)
	return c*((1-np.exp(-l1*x))/l1 + (1-np.exp(-l2*x))/l2)


def fdr_lomax(x, a, b):
	return 1 - (1 + x/b)**(-a)

########
# choix fdr, var, esp, moments suivant lois
########


# fonctions de choix de la logvs suivant la loi
def log_vs(loi):
	if loi == "hyperexpo":
		return logvs_hyperexpo
	elif loi == "lomax":
		return logvs_lomax
	elif loi == "weibull":
		return logvs_weibull
	elif loi == "expo_poly":
		return logvs_expopoly
	elif loi == "burr":
		return logvs_burr
	elif loi == "expo_convo":
		return logvs_expoconvo


# choisir le moment 1 et 2 suivant la loi
def esp(loi):
	if loi == "hyperexpo":
		return esp_hyperexpo
	elif loi == "lomax":
		return esp_lomax
	elif loi == "weibull":
		return esp_weibull
	elif loi == "expo_poly":
		return esp_expopoly
	elif loi == "burr":
		return esp_burr
	elif loi == "expo_convo":
		return esp_expoconvo


def mom2(loi):
	if loi == "hyperexpo":
		return mom2_hyperexpo
	elif loi == "lomax":
		return mom2_lomax
	elif loi == "weibull":
		return mom2_weibull
	elif loi == "expo_poly":
		return mom2_expopoly
	elif loi == "burr":
		return mom2_burr
	elif loi == "expo_convo":
		return mom2_expoconvo


def varc(x, loi):
	m2 = mom2(loi)
	e = esp(loi)
	return (m2(x) - (e(x)**2))


def momc(loi):
	if loi == "hyperexpo":
		return momc_hyperexpo
	elif loi == "lomax":
		return momc_lomax
	elif loi == "weibull":
		return momc_weibull
	elif loi == "expo_poly":
		return momc_expopoly
	elif loi == "burr":
		return momc_burr
	elif loi == "expo_convo":
		return momc_expoconvo


def mom3(loi):
	if loi == "hyperexpo":
		return mom3_hyperexpo
	elif loi == "lomax":
		return mom3_lomax
	elif loi == "weibull":
		return mom3_weibull
	elif loi == "expo_poly":
		return mom3_expopoly
	elif loi == "burr":
		return mom3_burr
	elif loi == "expo_convo":
		return mom3_expoconvo


def fdr(loi):
	if loi == "hyperexpo":
		return fdr_hyperexpo
	elif loi == "lomax":
		return fdr_lomax
	elif loi == "weibull":
		return fdr_weibull
	elif loi == "expo_poly":
		return fdr_expopoly
	elif loi == "burr":
		return fdr_burr
	elif loi == "expo_convo":
		return fdr_expoconvo


# Skewness et kurtosis et contrainte d'optimisation pour le modèle 2
def skewnessT(x, loi):
	momc_c = momc(loi)
	esp_c = esp(loi)
	return (momc_c(x, 3)-3*esp_c(x)*varc(x, loi)-(esp_c(x))**3)/(varc(x, loi)**(3/2))


def skewnessE(x, M):
	n = np.size(M)
	res2 = 0
	res3 = 0
	moy = np.mean(M)
	for i in range(n):
		res2 = res2+(M[i]-moy)*(M[i]-moy)
	for j in range(n):
		res3 = res3+(M[i]-moy)*(M[i]-moy)*(M[i]-moy)
	return (res3/n)/((res2/n)**(3/2))


########
# cas particulier exponentielle polynomiale
#######
def fdr_expopoly(x, y, z):  # y est le vecteur de paramètres (b,a1,...,am), z argument inutile
	res = 0
	for k in range(1, np.size(y)):
		res = res+y[k]*fact(k)/(y[0]**(k+1))
	return cab(y)*res*(1-np.exp(-y[0]*x))


def logvs_expopoly(x, M):
	n = np.size(M)
	m = np.size(x)
	res = 0
	for k in range(1, m):
		res = res+(x[k]*fact(k)/(x[0]**(k+1)))
	res2 = 0
	res3 = 0
	for i in range(n):
		for k in range(1, m):
			res2 = res2+x[k]*(M[i])**k
		res3 = res3+np.log(res2)
	res4 = 0
	for i in range(n):
		res4 = res4+M[i]
	return n*np.log(res)+res2-x[0]*res4


def cab(x):  # coefficient C(a,b) x=(b,a1,...,am) de taille m+1
	res = 0
	for k in range(1, np.size(x)):
		res = res + ((x[k]*fact(k))/(x[0]**(k+1)))
	return 1/res


def esp_expopoly(x):
	cabval = cab(x)
	res = 0
	for k in range(1, np.size(x)):
		res = res+x[k]*fact(k+1)/(x[0]**(k+2))
	return cabval*res


def mom2_expopoly(x):
	cabval = cab(x)
	res = 0
	for k in range(1, np.size(x)):
		res = res+x[k]*fact(k+2)/(x[0]**(k+3))
	return cabval*res


def mom3_expopoly(x):
	cabval = cab(x)
	res = 0
	for k in range(1, np.size(x)):
		res = res+x[k]*fact(k+3)/(x[0]**(k+4))
	return cabval*res


def momi_expopoly(x, i):
	cabval = cab(x)
	res = 0
	for k in range(1, np.size(x)):
		res = res+x[k]*fact(k+i)/(x[0]**(k+i+1))
	return cabval*res


def momc_expopoly(x, k):
	res = 0
	esperance = esp_expopoly(x)
	for i in range(0, k+1):
		res = res + (binom(k, i)*(esperance**(k-i))*((-1)**i)*momi_expopoly(x, i))
	return res


def contrainte4(x):
	if x[0] > 0:
		res = 1
	else:
		res = 0
	for i in range(1, np.size(x)):
		if x[i] >= 0:
			res = res+1
	return res-(np.size(x))


def max_vs_m1_epp(M, m):
	ls = logvs_expopoly
	moy = esp_expopoly
	mom2_f = mom2_expopoly
	cons = [{'type': 'ineq', 'fun': (lambda x: contrainte2(x, M, mom2_f))}, {'type': 'ineq', 'fun': (lambda x: contrainte1(x, M, moy))}, {'type': 'eq', 'fun': (lambda x: contrainte4(x))}]
	res = []
	Rlist = []
	for k in range(0, 9):
		valeur_initiale = [np.random.rand()]
		for j in range(m):
			valeur_initiale.append(np.random.rand())
		valeur_initiale = np.array(valeur_initiale)
		R = scipy.optimize.minimize((lambda x: ls(x, M)), valeur_initiale, tol=1e-6, options={'maxiter': 300}, constraints=cons).x
		res.append(norme(gradient((lambda y: ls(y, M)), R)))
		Rlist.append(R)
		if norme(gradient((lambda y: ls(y, M)), R)) < 1e-6:
			return R
	ind = res.index(min(res))
	return Rlist[ind]


def max_vs_m2_epp(M, m):
	cons = [{'type': 'ineq', 'fun': (lambda x: contrainte3(x, "expo_poly", M))}, {'type': 'eq', 'fun': (lambda x: contrainte4(x))}]
	ls = logvs_expopoly
	res = []
	Rlist = []
	for k in range(0, 20):
		valeur_initiale = [np.random.rand()]
		for j in range(m):
			valeur_initiale.append(np.random.rand())
		valeur_initiale = np.array(valeur_initiale)
		R = scipy.optimize.minimize((lambda x: ls(x, M)), valeur_initiale, tol=1e-6, options={'maxiter': 300}, constraints=cons).x
		res.append(norme(gradient((lambda y: ls(y, M)), R)))
		Rlist.append(R)
		if norme(gradient((lambda y: ls(y, M)), R)) < 1e-6:
			return R
	ind = res.index(min(res))
	return Rlist[ind]


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
				histo_discretes(array, nom="hist")
				return "discrete"
			if (discretes_continues(array) == "continue"):
				classe = int(5*math.log10(n))
				histo_Continue(array, classe, nom="hist")
				return "continue"
			else:
				return "Saisie invalide"
		elif (n == 8):
			global temp
			temp = max_vs_m1_epp(array, args.taille)
			res = []
			for i in range(1, np.size(temp)):
				res.append(temp[i])
			return res
		elif (n == 9):
			return temp[0]
		elif (n == 10):
			temp = max_vs_m2_epp(array, args.taille)
			res = []
			for i in range(1, np.size(temp)):
				res.append(temp[i])
			return res
		elif (n == 11):
			return temp[0]
		elif (n == 12):
			return chi2(array, fdr(loi), temp, temp[1])
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
				histo_discretes(array, nom="hist")
				return "discrete"
			if (discretes_continues(array) == "continue"):
				classe = int(5*math.log10(n))
				histo_Continue(array, classe, nom="hist")
				return "continue"
			else:
				return "Saisie invalide"
		elif (n == 8):
			temp = max_vs_m1(array, loi)
			return temp[0]
		elif (n == 9):
			return temp[1]
		elif (n == 10):
			temp = max_vs_m2(array, loi)
			return temp[0]
		elif (n == 11):
			return temp[1]
		elif (n == 12):
			return chi2(array, fdr(loi), temp[0], temp[1])
		else:
			return "Saisie invalide."


####
# Script
####
if discretes_continues(m) == "discrete":
	L = {"error": "error"}
else:
	if (args.modele == 1):
		L = {"min": do_operation(m, 0, args.loi), "max": do_operation(m, 1, args.loi), "moy": do_operation(m, 2, args.loi), "var": do_operation(m, 3, args.loi), "ec": do_operation(m, 4, args.loi), "skew": do_operation(m, 5, args.loi), "kurt": do_operation(m, 6, args.loi), "hist": do_operation(m, 7, args.loi), "param_a": do_operation(m, 8, args.loi), "param_b": do_operation(m, 9, args.loi), "chi2_pvalue": do_operation(m, 12, args.loi)}
	elif (args.modele == 2):
		L = {"min": do_operation(m, 0, args.loi), "max": do_operation(m, 1, args.loi), "moy": do_operation(m, 2, args.loi), "var": do_operation(m, 3, args.loi), "ec": do_operation(m, 4, args.loi), "skew": do_operation(m, 5, args.loi), "kurt": do_operation(m, 6, args.loi), "hist": do_operation(m, 7, args.loi), "param_a": do_operation(m, 10, args.loi), "param_b": do_operation(m, 11, args.loi), "chi2_pvalue": do_operation(m, 12, args.loi)}

res = json.dumps(L, default=convert)  # appliquer convert si le nombre est un entier numpy
print(res)
