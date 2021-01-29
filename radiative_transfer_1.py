import numpy as np
import math
import matplotlib.pyplot as plt


import pandas as pd



def plot(I,N,T,delta_x):
    paso = []
    acum = 0
    for i in range(N):
        paso.append(acum)
        acum += delta_x
     
    T=[T]
    df=pd.DataFrame(I,index=paso,columns=T)
    figure, axes = plt.subplots(2,1)

    ax=df.plot(ax=axes[0],title='Escala Normal')

    ax.axvline(100*delta_x,color='r',ls='dotted')
    ax.axvline(10000*delta_x,color='r',ls='dotted')
    ax.axvspan(100*delta_x,10000*delta_x,alpha=0.25)

    ax.annotate('Water \n vapor',
            xy=(160, 400), xycoords='figure points',
            fontsize=14)




    ax_1=df.plot(loglog=True,ax=axes[1],title='Escala Logaritmica')

    ax_1.axvline(100*delta_x,color='r',ls='dotted')
    ax_1.axvline(10000*delta_x,color='r',ls='dotted')
    ax_1.axvspan(100*delta_x,10000*delta_x,alpha=0.25)

    plt.annotate('Water \n vapor',
            xy=(520, 175), xycoords='figure points',
            fontsize=14)




    
def tao (delta_x, k_i, k_i1 ):
    delta_x = delta_x/2
    k = (k_i + k_i1)
    bla = delta_x * k
    return  bla


#def funcion_fuente(nu, k):
#    return nu/k


def alpha_h20(c_s,nu,theta,p):
    return (c_s * (nu**2) * (theta**3) * (p**2))
 

def func_P(ro,k,t):
    return ro*k*t


if __name__   == '__main__':
    N = 100000 #numero de iteraciones
    C_s = 7.8e-6  #s^6 kg^2 m
    alpha_line = 0
    nu = 200e9 #Hz
    T=293.15
    ro = 0.6 # kg/m^3
    K = 1.380649e-23 # constante de boltzmann   m^2 kg s^-2 K^-1

    delta_x = 100 #m

    I=[]
 


    theta = 300/T #adimensional

    P = func_P(ro,K,T)

    k = alpha_h20(C_s,nu,theta,P)


    k_n = nu* k * (T/ro)

    I = [200.0] #intensidad inicial
    for i in range(1,N):
        if i>=100 and i<=10000:
            paso = i * delta_x
            aux1 = I[i-1]*math.exp(-1*tao(delta_x,k_n,k_n))

        else:
            aux1=I[i-1]

        I.append(aux1)    



    plot(I,N,T,delta_x)
 
    

    plt.savefig('Images/radiative_transfer.png')

    plt.show()

