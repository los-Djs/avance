import numpy as np
import matplotlib.pyplot as plt

def funcion_fuente(nu, k):
    return nu/k

def calc_k_i():
    pass

def tao (x, k, i):
    x/2 
    pass

if __name__   == '__main__':
    ## data
    C_s = 7.8e-6
    alpha_line = 0
    nu = 200 #GHz frecuencia de observacion
    T = 293.15 # grados Kelvin
    theta = 300 * T 

    n = 0 #densidad de la nube, con 0 es que no hay nube
    K = 1.380649e-23 # constante de boltzmann joules por kelvin

    P = n*K*T

    alpha_h20 = (C_s * nu**2 * theta**3 * P ** 2) + alpha_line  ## aqui hay que calcular la opacidad del agua despejando la ecuacion

    ### opacidad
    k = 1/alpha_h20

    S_nu = funcion_fuente(nu, k)

    x = 100 #cm

    ## asumiendo que la temperatura es constante y no hay nube de agua
