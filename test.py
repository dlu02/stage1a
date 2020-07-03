m=np.loadtxt("test.txt",unpack=True)

def Moment_r(data,r):
    import functools
    fonc_r= lambda x : x**r
    S=np.sum(fonc_r(data))
    return S/(1.0*np.size(data))

def Moment_cr(data,r):
    import functools
    m=Moment_r(data,1)
    fonc_r= lambda x : (x-m)**r
    S=np.sum(fonc_r(data))
    return S/(1.0*np.size(data))

def skewness(array,i):
    return Moment_cr(array[i],3)/(Moment_cr(array[i],2)**(3/2))

def kurtosis(array,i):
    return (Moment_cr(array[i],4)/(Moment_cr(array[i],2)**2)-3)