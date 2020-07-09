import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("nombre_min", type=int, help="nombre minimum")
parser.add_argument("nombre_max", type=int, help="nombre maximum")
parser.add_argument("taille", type=int, help="taille")
parser.add_argument("nom_fichier", type=str, help="nom du fichier")
args = parser.parse_args()


f = open(args.nom_fichier, "w")
for k in range(1, args.taille + 1):
	a = random.randint(args.nombre_min, args.nombre_max)
	f.write(str(a))
	f.write("\n")
f.close()
