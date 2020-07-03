import argparse
import random
import numpy as np
import json
import matplotlib.pyplot as plt
import math
import scipy.stats
import warnings

parser = argparse.ArgumentParser()
parser.add_argument("nom_fichier", type=str, help="nom du fichier")
parser.add_argument("loi", type=str, help="loi")
args = parser.parse_args()

m=np.loadtxt(args.nom_fichier)
n=np.size(m)

#### Librairie de fonctions
###############################################################
# Mode(s) pour les données discrètes
###############################################################

def Mode_D(data):
	data=list(data)
	Dic={}
	for x in sorted(data):
		Dic[x]=data.count(x)
	Valeurs=[t for t in Dic.keys()]
	Effectifs=[t for t in Dic.values()]
	n_max=max(Effectifs)
	return [x for x in Valeurs if Dic[x]==n_max]


###############################################################
# Tester si les données sont discrètes ou continues
###############################################################

def discretes_continues(data):
	data=[x for x in data]
	dic_donnees={}
	for x in sorted(data):
		dic_donnees[x]=data.count(x)

	valeurs=[k for k in dic_donnees.keys()]
	effectifs=[v for v in dic_donnees.values()]

	# test
	if max(effectifs) >1:
		return "discrete"
	else:
		return "continue"

###############################################################
# nombre d'occurrences pour les données discrètes
###############################################################
def comptage_occurrences(data):
	data=sorted(data)
	Dic_compt={}
	for valeur in data:
		Dic_compt[valeur]=data.count(valeur)
	return Dic_compt


###############################################################
# Histogramme des données discrètes
###############################################################

def histo_discretes(data,nom=None):

	# nom : le nom (sans extension)  pour la figure

	import datetime
	import numpy
	import matplotlib.pyplot as plt

	plt.rcParams['hatch.color'] = [0.9,0.9,0.9]


	D=comptage_occurrences(data)
	valeurs=[k for k in D.keys()]
	effectifs=[v for v in D.values()]

	i_mode=numpy.argmax(effectifs)  # indice max
	### multi_mode
	indice_mode=[i for i in range(len(effectifs)) if effectifs[i]==effectifs[i_mode]]

	fig1 = plt.figure(figsize=(10,7))
	ax1 =fig1.add_subplot(111)
	# cacher le cadre (haut,bas , à gauche)
	ax1.spines['top'].set_visible(False)
	ax1.spines['right'].set_visible(False)
	ax1.spines['left'].set_visible(False)
	##
	ax1.xaxis.set_ticks_position('bottom')
	ax1.yaxis.set_ticks_position('left')

	ax1.set_yticks([])

	ax1.set_xticks(valeurs)  ## positions des extrémités des valeurs
	ax1.set_xticklabels(valeurs ,fontsize=10, rotation=25)
	ax1.set_xlabel("Valeurs",fontsize=13)
	ax1.set_ylabel("Effectifes",fontsize=13)

	for k in range(len(valeurs)):
		if k not in indice_mode:
			plt.bar(valeurs[k], height= effectifs[k],edgecolor="white")
		else:
			plt.bar(valeurs[k], height= effectifs[k],edgecolor="white",color = [0.15,0.15,0.85],hatch="X", lw=1., zorder = 0)
		for i in range(len(valeurs)):
			ax1.text(valeurs[i], effectifs[i], "%d"%(effectifs[i]),fontsize=9,horizontalalignment='center',verticalalignment='bottom',style='italic')

	# le nom de la figure va  porter la date du jour de création
	# aujourdhui=datetime.datetime.today()
	# jour="{}{}{}".format(aujourdhui.timetuple()[2],aujourdhui.timetuple()[1],aujourdhui.timetuple()[0])

	if nom is None:
		plt.show()
	else:
		# nom_fig="{}_histo_{}.png".format(nom,jour)
		# print(nom_fig)
		# plt.savefig(nom_fig, format="png")
		plt.savefig("hist.png",dpi=400)
		plt.close()


###############################################################
# histogramme pour les Données Continues
###############################################################

def histo_Continue(data,k,nom=None):
	# k=nombre de classes
	# nom : le nom (sans extension)  pour la figure

	import datetime
	import numpy
	import matplotlib.pyplot as plt

	plt.rcParams['hatch.color'] = [0.9,0.9,0.9] # hachure


	data=numpy.array([x for x in data])
	Ext=[min(data)+(max(data)-min(data))*i/(1.0*k) for i in range(k+1)]

	C=[0.5*(Ext[i]+Ext[i+1]) for i in range(k)]  # Centres des classes

	NN=[] # Effectifs des classes
	for i in range(k):
		NN.append(((Ext[i] <= data) & (data<=Ext[i+1])).sum())

	# pour la classe modale
	indice_max=[i for i in range(k) if NN[i]==numpy.max(NN)]

	TT=[str("{:.4f}".format(t)) for t in Ext]  ## pour afficher les extrémités des classes

	CC=[str("{:.4f}".format(t)) for t in C]    ## pour afficher les centres des classes


	fig = plt.figure(figsize=(10,7))
	ax1 = fig.add_subplot(111)
	# cacher le cadre
	ax1.spines['right'].set_visible(False)
	ax1.spines['top'].set_visible(False)
	ax1.spines['left'].set_visible(False)
	ax1.xaxis.set_ticks_position('bottom')

	ax1.set_yticks([])
	largeur=Ext[1]-Ext[0]  #  largeur des classes

	for i in range(k):
		if i in indice_max:
			ax1.bar(C[i], NN[i],largeur,  color = [0.15,0.15,0.80], edgecolor="white", hatch="/",lw=1., zorder = 0,alpha=0.9)
		else:
			ax1.bar(C[i], NN[i],largeur, align='center', edgecolor="white")

		ax1.text(C[i], NN[i], "%d"%(NN[i]),fontsize=8, style='italic',horizontalalignment='center',verticalalignment='bottom')


	#ax1.set_xticks(C)      ## positions des centres
	ax1.set_xticks(Ext)  ## positions des extrémités des classes

	ax1.set_xticklabels(TT ,fontsize=8, rotation=45)
	#ax1.set_xticklabels(CC ,fontsize=8, rotation=45)


	ax1.set_xlim(numpy.min(data)-0.75*largeur, numpy.max(data)+0.75*largeur)
	ax1.set_ylim(0.0, numpy.max(NN)+3.0)
	ax1.set_xlabel("Valeurs",fontsize=12)
	ax1.set_ylabel("Effectifs",fontsize=14)

	# le nom de la figure va  porter la date du jour de création
	# aujourdhui=datetime.datetime.today()
	# jour="{}{}{}".format(aujourdhui.timetuple()[2],aujourdhui.timetuple()[1],aujourdhui.timetuple()[0])

	if nom is None:
		plt.show()
	else:
		# nom_fig="{}_histo_{}.png".format(nom,jour)
		# print(nom_fig)
		# plt.savefig(nom_fig, format="png")
		plt.savefig("hist.png",dpi=400)
		plt.close()


def do_operation(array,n,log_vs):
	if (n==0):
		return round(np.amin(array),5)
	elif (n==1):
		return round(np.amax(array),5)
	elif (n==2):
		return round(np.mean(array),5)
	elif (n==3):
		return round(np.var(array),5)
	elif (n==4):
		return round(np.std(array),5)
	elif (n==5):
		return round(skewness(array),5)
	elif (n==6):
		return round(kurtosis(array),5)
	elif (n==7):
		if (discretes_continues(array)=="discrete"):
			histo_discretes(array,nom="hist")
			return "discrete"
		if (discretes_continues(array)=="continue"):
			classe=int(5*math.log10(n))
			histo_Continue(array,classe,nom="hist")
			return "continue"
		else:
			return "Saisie invalide"
	elif (n==8):
		global temp
		temp=max_vs_m1(array,log_vs)
		return temp[0]
	elif (n==9):
		return temp[1]
	else:
		return "Saisie invalide."


def Moment_r(data,r):
	fonc_r= lambda x : x**r
	S=np.sum(fonc_r(data))
	return S/(1.0*np.size(data))

def Moment_cr(data,r):
	m=Moment_r(data,1)
	fonc_r= lambda x : (x-m)**r
	S=np.sum(fonc_r(data))
	return S/(1.0*np.size(data))

def skewness(array):
	return (Moment_cr(array,3)/(Moment_cr(array,2)**(3/2)))

def kurtosis(array):
	return (Moment_cr(array,4)/(Moment_cr(array,2)**2)-3)

def convert(n): # pour convertir les entiers numpy en flottants usuels pour que le parse JSON fonctionne et envoie bien le tableau à PHP
	if isinstance(n,np.int64):
		return float(n)

#################Estimation des paramètres

#liste des logvs des lois
def logvs_hyperexpo(x,M): # x est un vecteur de R2 représentant les paramètres et M est un échantillon (x1,...,xn)
    res=0
    c=(x[0]*x[1])/(x[0]+x[1])
    for i in range(0,np.size(M)):
        res=res+np.log(c*(np.exp(-x[0]*M[i])+np.exp(-x[1]*M[i])))
    return res
#

##Liste des moments 1 et 2 des lois
def mom1_hyperexpo(x):
	return ((x[1]/(x[0]*(x[0]+x[1])) + x[0]/(x[1]*(x[0]+x[1]))))

def mom2_hyperexpo(x):
	return ((2*x[1]/(x[0]*x[0]*(x[0]+x[1])) + 2*x[0]/(x[1]*x[1]*(x[0]+x[1]))))
##

#fonctions usuelles pour le modèle 1
# def grad_logvs(x,M,log_vs):
#     return gradient(lambda y: logvs(y,M),x)

# def max_vs(M):
#     valeur_initiale=np.array([np.random.rand(),np.random.rand()])
#     print(valeur_initiale)
#     R=scipy.optimize.root(lambda x: grad_logvs_hyperexpo(x,M),valeur_initiale)
#     return R

def contrainteE(x,M,mom1):
    return (mom1(x)-np.mean(M))

def contrainteE2(x,M,mom2):
    return (mom2(x)-mom_emp2(M))

def mom_emp2(M):
    n=np.size(M)
    res=0
    for i in M:
        res=res+i*i
    return res/n
#

#choisir la fonction logvs suivant la loi
def log_vs(loi):
	if loi=="hyperexpo":
		return logvs_hyperexpo
	elif loi=="lomax":
		return logvs_lomax
	elif loi=="weibull":
		return logvs_weibull
	elif loi=="expo_poly":
		return logvs_expopoly
	elif loi=="burr":
		return logvs_burr
	elif loi=="expo_convo":
		return logvs_expoconvo

#choisir le moment 1 et 2 suivant la loi
def mom(loi):
	if loi=="hyperexpo":
		return (mom1_hyperexpo,mom2_hyperexpo)
	elif loi=="lomax":
		return (mom1_lomax,mom2_lomax)
	elif loi=="weibull":
		return (mom1_weibull,mom2_weibull)
	elif loi=="expo_poly":
		return (mom1_expopoly,mom2_expopoly)
	elif loi=="burr":
		return (mom1_burr,mom2_burr)
	elif loi=="expo_convo":
		return (mom1_expoconvo,mom2_expoconvo)

#système d'équation à résoudre
def eq1(x,M,loi):
	logvs=log_vs(loi)
	moment=mom(loi)
	return [gradient((lambda y: logvs(y,M)),x)[0],gradient((lambda y: logvs(y,M)),x)[1],contrainteE(x,M,moment[0]),contrainteE2(x,M,moment[1])]

def max_vs_m1(M,loi):
    valeur_initiale=np.array([np.random.rand()*3,np.random.rand()*3,0,0])
    R=scipy.optimize.fsolve(lambda x: eq1(x,M,loi),valeur_initiale)
    return R

### Gradient
def derivee_num(fonction,x0,i,h=1e-06):
    a=np.zeros(np.size(x0))
    a[i]=1
    return (fonction(x0+0.5*h*a)-fonction(x0-0.5*h*a))/h


def gradient(fonction,point):
    res=np.array([])
    for k in range(0,np.size(point)):
        a=derivee_num(fonction,point,k,1e-06)
        res=np.append(res,a)
    return res
##############

warnings.filterwarnings("ignore")  # ignorer les warnings

L={"min":do_operation(m,0,args.loi),"max":do_operation(m,1,args.loi),"moy":do_operation(m,2,args.loi),"var":do_operation(m,3,args.loi),"ec":do_operation(m,4,args.loi),"skew":do_operation(m,5,args.loi),"kurt":do_operation(m,6,args.loi),"hist":do_operation(m,7,args.loi),"param_a":do_operation(m,8,args.loi),"param_b":do_operation(m,9,args.loi)} #dictionnaire des valeurs à calculer

res=json.dumps(L,default=convert) #appliquer convert si le nombre est un entier numpy
print(res)
