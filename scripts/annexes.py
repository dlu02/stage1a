import numpy


def convert(n):  # pour convertir les entiers numpy en flottants usuels pour que le parse JSON fonctionne et envoie bien le tableau à PHP
    if isinstance(n, numpy.int64):
        return float(n)
