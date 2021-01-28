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
    plt.show()
    if save:
        plt.savefig('radiative_transfer.png')
    
    
def tao (delta_x, k_i, k_i1 ):
    delta_x = delta_x/2
    k = (k_i + k_i1)
    bla = delta_x * k
    return  bla

def funcion_fuente(nu, k):
    return nu/k


if __name__   == '__main__':
    N = 10 #numero de iteraciones
    C_s = 7.8e-6  #s^6 kg^2 m
    alpha_line = 0
    nu = 200e9 #Hz
    T = [293.15]*N # grados Kelvin equivale a 20 C
    theta = 300/T[0] #adimensional

    ro = [0.6] * N # kg/m^3
    K = 1.380649e-23 # constante de boltzmann   m^2 kg s^-2 K^-1

    P = ro[0] * K * T[0]

    alpha_h20 = (C_s * (nu**2) * (theta**3) * (P**2)) + alpha_line

    k = alpha_h20

    S_nu = funcion_fuente(nu, k)

    delta_x = 1 #m

    k_n = [nu* k * (T_i/ro_i) for T_i, ro_i in zip(T,ro)]

    I = [0.0] #intensidad inicial
    for i in range(1,N):
        paso = i * delta_x
        aux1 = I[i-1]* math.exp(-1 * tao(delta_x, k_n[i-1], k_n[i]))
        aux2 = S_nu * (1 - math.exp(-1 * tao(delta_x, k_n[i-1], k_n[i])))

        # S_nu = funcion_fuente(nu, k)
        print(aux1, aux2)

        I.append(aux1 + aux2)    

    plot(I, delta_x, N)