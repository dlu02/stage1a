import matplotlib
import matplotlib.pyplot as plt
import numpy
import random

def densite_1param(a,f,x_max):
    nb_point=200
    #x_max de l'axe des x
    intervalle=[max(0,x_max)*i/(nb_point-1) for i in range(nb_point)]
    y=[f(t,a) for t in intervalle]  # densité
    return intervalle, y

def densite_2param(a,b,f,x_max):
    nb_point=200
    #x_max de l'axe des x
    intervalle=[max(0,x_max)*i/(nb_point-1) for i in range(nb_point)]
    y=[f(t,a,b) for t in intervalle]  # densité
    return intervalle, y

def fdr_inv_1param(param,fdr_Loi): ## déterminer la fonction de répartition réciproque numériquement (1 paramètre)
    import warnings
    warnings.filterwarnings("ignore")  # ignorer les warnings
    import scipy.optimize
    a=param[0]
    alpha=param[1]
    valeur_initiale=numpy.random.rand()
    R=scipy.optimize.fsolve(lambda x: fdr_Loi(x,a)-alpha,valeur_initiale)
    return  R[0]

def fdr_inv_2param(param,fdr_Loi): ## déterminer la fonction de répartition réciproque numériquement (2 paramètres)
    import warnings
    warnings.filterwarnings("ignore")  # ignorer les warnings
    import scipy.optimize
    a=param[0]
    b=param[1]
    alpha=param[2]
    valeur_initiale=numpy.random.rand()
    R=scipy.optimize.fsolve(lambda x: fdr_Loi(x,a,b)-alpha,valeur_initiale)
    return R[0]

## tracé de la densité  (1param)

def Axes_simple1(axe):
    axe.spines['top'].set_visible(False)
    axe.spines['right'].set_visible(False)
    axe.xaxis.set_ticks_position('bottom')
    axe.yaxis.set_ticks_position('left')

def trace_densite_1param(f,fdr_loi,var,titre):
    fig, ax = plt.subplots(figsize=(10,7))
    Axes_simple1(ax)
    # détermination de la borne sup de l'intervalle
    Axe_Max7=[]
    for a in var:
        Axe_Max7.append(fdr_inv_1param([a,0.98],fdr_loi))

    m7=max(Axe_Max7)

    for a in var:
        plt.plot(densite_1param(a,f,m7)[0],densite_1param(a,f,m7)[1],
                color=[random.random(),random.random(),random.random()],lw=3, label="$a={0}$".format(a))

    #font pour le titre du legend
    Leg=plt.legend(loc="best",ncol=2, shadow=True, title=titre,prop={'size':16}, fancybox=True)
    Leg.get_title().set_fontsize('15')

    plt.xlabel('$x$', fontsize=15)
    plt.ylabel('$f(x)$', fontsize=17)

    ax.get_legend().get_title().set_color("red")

    #plt.savefig("Loi_inf1.png", dpi=400)
    plt.show()

## tracé de la densité (2 param)
def trace_densite_2bparam(f,fdr_loi,param,var,titre):  # on fixe le deuxième paramètre et on fait varier le premier : param est la valeur du paramètre fixé et var est une liste de valeurs du paramètre à faire varier
    fig, ax = plt.subplots(figsize=(10,7))
    Axes_simple1(ax)
    # détermination de la borne sup de l'intervalle
    Axe_Max7=[]
    for a in var:
        Axe_Max7.append(fdr_inv_2param([a,param,0.98],fdr_loi))

    m7=max(Axe_Max7)

    for a in var:
        plt.plot(densite_2param(a,param,f,m7)[0],densite_2param(a,param,f,m7)[1],
                color=[random.random(),random.random(),random.random()],lw=3, label="$a={0}$".format(a))

    #font pour le titre du legend
    Leg=plt.legend(loc="best",ncol=2, shadow=True, title=titre,prop={'size':16}, fancybox=True)
    Leg.get_title().set_fontsize('15')

    plt.xlabel('$x$', fontsize=15)
    plt.ylabel('$f(x)$', fontsize=17)

    ax.get_legend().get_title().set_color("red")

    #plt.savefig("Loi_inf1.png", dpi=400)
    plt.show()

def trace_densite_2aparam(f,fdr_loi,param,var,titre): # on fixe le premier paramètre et on fait varier le deuxième : param est la valeur du paramètre fixé et var est une liste de valeurs du paramètre à faire varier
    fig, ax = plt.subplots(figsize=(10,7))
    Axes_simple1(ax)
    # détermination de la borne sup de l'intervalle
    Axe_Max7=[]
    for a in var:
        Axe_Max7.append(fdr_inv_2param([param,a,0.98],fdr_loi))

    m7=max(Axe_Max7)

    for a in var:
        plt.plot(densite_2param(param,a,f,m7)[0],densite_2param(param,a,f,m7)[1],
                color=[random.random(),random.random(),random.random()],lw=3, label="$b={0}$".format(a))

    #font pour le titre du legend
    Leg=plt.legend(loc="best",ncol=2, shadow=True, title=titre,prop={'size':16}, fancybox=True)
    Leg.get_title().set_fontsize('15')

    plt.xlabel('$x$', fontsize=15)
    plt.ylabel('$f(x)$', fontsize=17)

    ax.get_legend().get_title().set_color("red")

    #plt.savefig("Loi_inf1.png", dpi=400)
    plt.show()

#tracé densité simple

def trace_densite(f,fdr_loi,a,b):
    fig, ax = plt.subplots(figsize=(10,7))
    Axes_simple1(ax)

    # détermination de la borne sup de l'intervalle
    m7=fdr_inv_2param([a,b,0.98],fdr_loi)

    plt.plot(densite_2param(a,b,f,m7)[0],densite_2param(a,b,f,m7)[1],color=[random.random(),random.random(),random.random()],lw=3)

    plt.xlabel('$x$', fontsize=15)
    plt.ylabel('$f(x)$', fontsize=17)

    #plt.savefig("Loi_inf1.png", dpi=400)
    plt.show()

## tests
def lomax(x,a,b):
    return (a*(b**a))/((b+x)**(a+1))

def fdr_lomax(x,a,b):
    return 1-((1+(x/b))**(-a))

def densite_test(x,a):
    return (6*a*(numpy.exp(-a*x)-numpy.exp(-2*a*x)+numpy.exp(-3*a*x)))/5

def fdr_test(x,a):
    return 1-(1/5)*(6*numpy.exp(-a*x)-3*numpy.exp(-2*a*x)+2*numpy.exp(-3*a*x))

def fdr_weibull(x,a,b):
    return 1-numpy.exp(-(x**b)/(a**b))

def weibull(x,a,b):
    return (b/(a**b))*(x**(b-1))*numpy.exp(-(x**b)/(a**b))