import numpy as np
from scipy.special import gamma, binom


# factorielle
def fact(n):
	if n <= 1:
		return 1
	else:
		return n*fact(n-1)


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
# densités des lois
########

def lomax(x, a, b):
	return (a*(b**a))/((b+x)**(a+1))


def weibull(x, a, b):
	return (b/(a**b))*(x**(b-1))*np.exp(-(x**b)/(a**b))


def hyperexpo(x, l1, l2):
	return ((l1*l2)/(l1+l2))*(np.exp(-l1*x)+np.exp(-l2*x))


def burr(x, a, b):
	return (a*b*(x**(a-1)))/((1+(x**a))**(b+1))


def expo_convo(x, a, b):
	if a == b:
		return a*a*x*np.exp(-a*x)
	else:
		c = (a*b)/(b-a)
		return c*(np.exp(-a*x)+np.exp(-b*x))


########
# cas particulier exponentielle polynomiale
#######

def expo_poly(x, a, b):
	res = 0
	for k in range(0, np.size(a)):
		res = res+a[k]*(x**k)
	return cab3(a, b)*res*np.exp(-b*x)


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


def cab3(a, b):  # coefficient C(a,b) où a est la liste (a1,...,am)
	res = 0
	for k in range(1, np.size(a)+1):
		res = res+((a[k-1]*fact(k))/(b**(k+1)))
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


# cas où a est un unique réel
def cab2(a, b):
	return (b*b)/a


def expo_poly2(x, a, b):
	return cab2(a, b)*a*x*np.exp(-b*x)


def fdr_expopoly2(x, a, b):
	return cab2(a, b)*a*(1-np.exp(-b*x))/(b*b)
