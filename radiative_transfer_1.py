import numpy as np
import matplotlib.pyplot as plt

def plot(I, delta_x, N):
    paso = []
    acum = 0
    for i in range(N):
        paso.append(acum)

    plt.plot(I)
    pass


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
    nu = 200 #GHz
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

    for i in range(1,N):
        
        # S_nu = funcion_fuente(nu, k)

        aux1 = I[i-1]* np.exp(- tao(delta_x, k_n[i-1], k_n[i]))
        aux2 = S_nu * (1- np.exp(- tao(delta_x, k_n[i-1], k_n[i])))

        print(aux1, aux2)

        I.append(aux1 + aux2)    
