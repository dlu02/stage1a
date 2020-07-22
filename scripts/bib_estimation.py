import numpy as np
import scipy.stats
from annexes import mom_emp2
from lois_theo import log_vs, esp, mom2, varc, momc, mom3, logvs_expopoly, mom2_expopoly, esp_expopoly


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
	for k in range(0, 10):
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
	for k in range(0, 10):
		valeur_initiale = np.array([np.random.rand(), np.random.rand()])
		R = scipy.optimize.minimize((lambda x: ls(x, M)), valeur_initiale, tol=1e-6, options={'maxiter': 300}, constraints=cons).x
		res.append(norme(gradient((lambda y: ls(y, M)), R)))
		Rlist.append(R)
		if norme(gradient((lambda y: ls(y, M)), R)) < 1e-6:
			return R
	ind = res.index(min(res))
	return Rlist[ind]


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


def contrainte4(x):
	if x[0] > 0:
		res = 1
	else:
		res = 0
	for i in range(1, np.size(x)):
		if x[i] >= 0:
			res = res+1
	return res-(np.size(x))

####
# Cas particulier exponentielle polynomiale
###


def max_vs_m1_epp(M, m):
	ls = logvs_expopoly
	moy = esp_expopoly
	mom2_f = mom2_expopoly
	cons = [{'type': 'ineq', 'fun': (lambda x: contrainte2(x, M, mom2_f))}, {'type': 'ineq', 'fun': (lambda x: contrainte1(x, M, moy))}, {'type': 'eq', 'fun': (lambda x: contrainte4(x))}]
	res = []
	Rlist = []
	for k in range(0, 10):
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
	for k in range(0, 10):
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
