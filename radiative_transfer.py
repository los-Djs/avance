import numpy as np
import matplotlib.pyplot as plt

def funcion_fuente(nu, k):
    return nu/k


def tao (delta_x, k_i, k_i1 ):
    return (delta_x/2)*(k_i + k_i1) 

if __name__   == '__main__':
    ## data
    N = 10 #numero de iteraciones
    C_s = 7.8e-6 #(dB/km)/(GHz kPa)
    alpha_line = 0
    nu = 2e11 #Hz frecuencia de observacion
    T = [293.15]*N # grados Kelvin equivale a 20 C
    theta = 300/T[0]

    convertida = 0.017/1000 ## 0.017 es la densidad en kg/m^3 pasar de kg/m^3 a g/cm^3 0.017/1000
    ro = [convertida] * N  #densidad de la nube en g/cm^3 para 20 C , con 0 es que no hay nube 

    K = 1.380649e-23 # (m^2 kg s^-2 K^-1)

    P = convertida*K*T[0]

    alpha_h20 = (C_s * (nu**2) * (theta**3) * (P ** 2)) + alpha_line  ## aqui hay que calcular la opacidad del agua despejando la ecuacion

    ### opacidad
    k = 1/alpha_h20

    S_nu = funcion_fuente(nu, k)

    delta_x = 1 #m


    k_n = [nu* k * (T_i/ro_i) for T_i, ro_i in zip(T,ro)]
    print(k_n)
    print(ro)

    ## asumiendo que la temperatura y la densidad son constantantes
    I = [200] #intensidad inicial del foco

    for i in range(1,N):
        # if i == 1:
            # coso = np.exp(- tao(delta_x, k_n[i-1], k_n[i]))    
        # else: 
        aux1 = I[i-1]* np.exp(- tao(delta_x, k_n[i-1], k_n[i]))
        aux2 = S_nu * (1- np.exp(- tao(delta_x, k_n[i-1], k_n[i])))

        print(aux1, aux2)

        I.append(aux1 + aux2)
        # pass #aqui  ya va la cosa recursiva        

    print(I)

    
