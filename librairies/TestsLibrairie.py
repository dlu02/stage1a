
from Librairie_version16062020 import*

import numpy
data=numpy.random.poisson(11,29)

print("data :",data)

print("les données sont :",discretes_continues(data))

print("***"*20)

# nombre d'occurrences

print(comptage_occurrences(data))


print("***"*20)
# Histogramme des données discrètes
###############################################################

# test pour uniquement visualiser l'histogramme
# histo_discretes(data)

print(" la figure testDiscrete_histo_....png va  être crée dans le répertoitre")

histo_discretes(data,"testDiscrete")


print("***"*20)
# Histogramme des données discrètes
###############################################################


data1=numpy.random.gamma(3,6,189) # loi gamma(3,1/6) , taille=189

# test pour uniquement visualiser l'histogramme
#nombre de classes=13
#histo_Continue(data1,13)


print(" la figure testContinue_histo_....png va  être crée dans le répertoitre")

#nombre de classes=13
histo_Continue(data1,13,nom="testContinue")
