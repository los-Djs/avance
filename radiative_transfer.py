import numpy as np
import matplotlib.pyplot as plt



## data
C_2 = 7.8e-6
alpha_line = 0
nu = 200 #GHz frecuencia de observacion
T = 293.15 # grados Kelvin
theta = 300 * T 

n = 0 #densidad de la nube, con 0 es que no hay nube
K = 1.380649e-23 # constante de boltzmann joules por kelvin

P = n*K*T

alpha_h20 = 1 ## aqui hay que calcular la opacidad del agua despejando la ecuacion


### opacidad
k = 1/alpha_h20


if __name__   == '__main__':
    pass

