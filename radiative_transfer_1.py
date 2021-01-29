import numpy as np
import math
import matplotlib.pyplot as plt

def plot(I, delta_x, N,save=False):
    paso = []
    acum = 0
    for i in range(N):
        paso.append(acum)
        acum += delta_x
        
    plt.plot( paso  , I,label = 'Simulacion Transferencia')
    plt.xlabel("Distancia (m)")
    plt.ylabel("Intensidad especifica")
    plt.title("Transferencia radiativa")
    plt.legend()
    plt.yscale('log')
    plt.xscale('log')
    plt.show()
    if save:
        plt.savefig('Images/radiative_transfer.png')
    
    
def tao (delta_x, k_i, k_i1 ):
    delta_x = delta_x/2
    k = (k_i + k_i1)
    bla = delta_x * k
    return  bla

#def funcion_fuente(nu, k):
#    return nu/k

def alpha_h20(c_s,nu,theta,p):
    return (c_s * (nu**2) * (theta**3) * (p**2))
 


if __name__   == '__main__':
    N = 100000 #numero de iteraciones
    C_s = 7.8e-6  #s^6 kg^2 m
    alpha_line = 0
    nu = 200e9 #Hz
    T = 293.15 # grados Kelvin equivale a 20 C
    theta = 300/T #adimensional

    ro = 0.6 # kg/m^3
    K = 1.380649e-23 # constante de boltzmann   m^2 kg s^-2 K^-1

    P = ro * K * T

    #alpha_h20 = 
    k = alpha_h20(C_s,nu,theta,P)


    delta_x = 100 #m

    k_n = nu* k * (T/ro)

    I = [200.0] #intensidad inicial
    for i in range(1,N):
        paso = i * delta_x
        aux1 = I[i-1]* math.exp(-1 * tao(delta_x, k_n, k_n))
        #print(aux1)

        I.append(aux1)    

    plot(I, delta_x, N, save=True)
