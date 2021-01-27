import numpy as np
import matplotlib.pyplot as plt

def funcion_fuente(nu, k):
    return nu/k


def tao (delta_x, k_i, k_i1 ):
    return (delta_x/2)*(k_i + k_i1) 

if __name__   == '__main__':
    ## data
    N = 10 #numero de iteraciones
    C_s = 7.8e-6
    alpha_line = 0
    nu = 200 #GHz frecuencia de observacion
    T = [293.15]*N # grados Kelvin equivale a 20 C
    theta = 300 * T 

    convertida = 0.017 *(1000/1000000) ## 0.017 es la densidad en kg/m3 pasar de kg/m3 a g/cm3 0.017/1000
    ro = [convertida] * N  #densidad de la nube en g/cm3 para 20 C , con 0 es que no hay nube 

    K = 1.380649e-23 # constante de boltzmann joules por kelvin

    P = ro*K*T

    alpha_h20 = (C_s * nu**2 * theta**3 * P ** 2) + alpha_line  ## aqui hay que calcular la opacidad del agua despejando la ecuacion

    ### opacidad
    k = 1/alpha_h20

    S_nu = funcion_fuente(nu, k)

    delta_x = 100 #cm


    k_n = [nu* alpha_h20 * (T_i/ro_i) for T_i, ro_i in zip(T,ro)]

    ## asumiendo que la temperatura y la densidad son constantantes
    I = []

    for i in range(N):
        pass
        # pass #aqui  ya va la cosa recursiva        


    
