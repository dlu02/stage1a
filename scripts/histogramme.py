import numpy as np
import matplotlib.pyplot as plt

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
		plt.savefig(nom, dpi=400)
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
		plt.savefig(nom, dpi=400)
		plt.close()
