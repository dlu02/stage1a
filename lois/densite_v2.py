import matplotlib.pyplot as plt
import numpy
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a", type=float, help="a")
parser.add_argument("b", type=float, help="b")
parser.add_argument("loi", type=int, help="loi")
args = parser.parse_args()


# fonction de sélection de l'opération à effectuer
def do_operation():
    if (args.loi == 0):
        trace_densite(hyperexpo, fdr_hyperexpo, args.a, args.b)
    elif (args.loi == 1):
        trace_densite(lomax, fdr_lomax, args.a, args.b)
    elif (args.loi == 2):
        trace_densite(weibull, fdr_weibull, args.a, args.b)
    elif (args.loi == 3):
        trace_densite(burr, fdr_burr, args.a, args.b)
    elif (args.loi == 4):
        trace_densite(expo_convo, fdr_expoconvo, args.a, args.b)


# def densite_1param(a,f,x_max):
#     nb_point=200
#     #x_max de l'axe des x
#     intervalle=[max(0,x_max)*i/(nb_point-1) for i in range(nb_point)]
#     y=[f(t,a) for t in intervalle]  # densité
#     return intervalle, y

def densite_2param(a, b, f, x_max):
    nb_point = 200
    # x_max de l'axe des x
    intervalle = [max(0, x_max)*i/(nb_point-1) for i in range(nb_point)]
    y = [f(t, a, b) for t in intervalle]  # densité
    return intervalle, y

# def fdr_inv_1param(param,fdr_Loi): ## déterminer la fonction de répartition réciproque numériquement (1 paramètre)
#     import warnings
#     warnings.filterwarnings("ignore")  # ignorer les warnings
#     import scipy.optimize
#     a=param[0]
#     alpha=param[1]
#     valeur_initiale=numpy.random.rand()
#     R=scipy.optimize.fsolve(lambda x: fdr_Loi(x,a)-alpha,valeur_initiale)
#     return  R[0]


def fdr_inv_2param(param, fdr_Loi):  # déterminer la fonction de répartition réciproque numériquement (2 paramètres)
    import warnings
    warnings.filterwarnings("ignore")  # ignorer les warnings
    import scipy.optimize
    a = param[0]
    b = param[1]
    alpha = param[2]
    valeur_initiale = numpy.random.rand()
    R = scipy.optimize.fsolve((lambda x: fdr_Loi(x, a, b)-alpha), valeur_initiale)
    return R[0]

# tracé de la densité  (1param)
# def trace_densite_1param(f,fdr_loi,var,titre):
#     fig, ax = plt.subplots(figsize=(10,7))
#     Axes_simple1(ax)
#     # détermination de la borne sup de l'intervalle
#     Axe_Max7=[]
#     for a in var:
#         Axe_Max7.append(fdr_inv_1param([a,0.98],fdr_loi))
#
#     m7=max(Axe_Max7)
#
#     for a in var:
#         plt.plot(densite_1param(a,f,m7)[0],densite_1param(a,f,m7)[1],
#                 color=[random.random(),random.random(),random.random()],lw=3, label="$a={0}$".format(a))
#
#     #font pour le titre du legend
#     Leg=plt.legend(loc="best",ncol=2, shadow=True, title=titre,prop={'size':16}, fancybox=True)
#     Leg.get_title().set_fontsize('15')
#
#     plt.xlabel('$x$', fontsize=15)
#     plt.ylabel('$f(x)$', fontsize=17)
#
#     ax.get_legend().get_title().set_color("red")
#
#     #plt.savefig("Loi_inf1.png", dpi=400)
#     plt.show()


# tracé de la densité (2 param)
def Axes_simple1(axe):
    axe.spines['top'].set_visible(False)
    axe.spines['right'].set_visible(False)
    axe.xaxis.set_ticks_position('bottom')
    axe.yaxis.set_ticks_position('left')


def trace_densite(f, fdr_loi, a, b):
    fig, ax = plt.subplots(figsize=(10, 7))
    Axes_simple1(ax)
    # détermination de la borne sup de l'intervalle
    m7 = fdr_inv_2param([a, b, 0.98], fdr_loi)
    plt.plot(densite_2param(a, b, f, m7)[0], densite_2param(a, b, f, m7)[1], color=[random.random(), random.random(), random.random()], lw=3)
    plt.xlabel('$x$', fontsize=15)
    plt.ylabel('$f(x)$', fontsize=17)
    plt.savefig("densite.png", dpi=400)
    plt.close()


####
# lois
####

def lomax(x, a, b):
    return (a*(b**a))/((b+x)**(a+1))


def fdr_lomax(x, a, b):
    return 1-((1+(x/b))**(-a))


def fdr_weibull(x, a, b):
    return 1-numpy.exp(-(x**b)/(a**b))


def weibull(x, a, b):
    return (b/(a**b))*(x**(b-1))*numpy.exp(-(x**b)/(a**b))


def hyperexpo(x, l1, l2):
    return ((l1*l2)/(l1+l2))*(numpy.exp(-l1*x)+numpy.exp(-l2*x))


def fdr_hyperexpo(x, l1, l2):
    return ((l1*l2)/(l1+l2))*((1-numpy.exp(-l1*x))/l1 + (1-numpy.exp(-l2*x))/l2)


def burr(x, a, b):
    return (a*b*(x**(a-1)))/((1+(x**a))**(b+1))


def fdr_burr(x, a, b):
    return 1-((1+(x**a))**(-b))


def expo_convo(x, a, b):
    if a == b:
        return a*a*x*numpy.exp(-a*x)
    else:
        c = (a*b)/(b-a)
        return c*(numpy.exp(-a*x)+numpy.exp(-b*x))


def fdr_expoconvo(x, a, b):
    if a == b:
        return 1-numpy.exp(-a*x)*(a*x+1)
    else:
        return 1 + (a/(b-a))*numpy.exp(-b*x) - (b/(b-a))*numpy.exp(-a*x)


# exécution du script
do_operation()
