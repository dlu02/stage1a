import numpy as np


def convert(n):  # pour convertir les entiers numpy en flottants usuels pour que le parse JSON fonctionne et envoie bien le tableau à PHP
    if isinstance(n, np.int64):
        return float(n)


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


def mom_emp2(M):
    n = np.size(M)
    res = 0
    for i in range(n):
        res = res + M[i] * M[i]
    return res/n
