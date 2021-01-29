# Radiative Transfer

## Authors:

* ### Fonseca Márquez Pablo Francisco fonseking21@gmail.com
* ### Ceja Cruz Eduardo Manuel lalitoceja@gmail.com
* ### García Olivo Brian Kalid briankalid2000@gmail.com

## Introduction:

Radiative Transfer is the theory of the physical phenomenon of energy transfer in the form of electromagnetic radiation. The propagation of the radiation through a medium is affected by the absorption and the emission of it as well as the wavelenght that its going through. That's what it's described in the radiative transfer equcation. This equation has a wide variety of applications, including asytophysics, optics, atmospheric sicence, among others.


## Goal:
Our goal is to implement the radiative transfer model for a few simple controlled cases, succesfully. For this, we are going to solve the radiative transfer equation, but in its discretized form for simplicity. 


# Methodology:

The discretized form is the following:


<!--- $$I_{i+1} = I_i e^{-\tau} + S_{\nu}(I_{i+1})(1-e^{-\tau})$$-->
<!---<img src="https://latex.codecogs.com/svg.latex?\Large&space;I_{i+1}=I_{i}e^{-\tau}+S_{\nu}(I_{i})(1-e^{-\tau})" title="" />-->

<img src="https://latex.codecogs.com/svg.latex?\Large&space;I_{i+1}=I_{i}e^{-\tau}+S_{\nu}(1-e^{-\tau})" title="" />

Where <img src="https://latex.codecogs.com/svg.latex?\Large&space;\tau" title="" /> is defined as

<!---\frac{\delta x}{2}(k_i + k_{i + 1})-->

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{\Delta{x}}{2}{(k_i+k_{i+1})" title="dt"/>

<!---and $k = \nu f T/\ro$  where $f$ is the value of the ~~something i don't remeber~~, $T$ is a vector of size n  with the temperature at each step and $\ro$ is another vector of the same size with the density.-->


and  <img src="https://latex.codecogs.com/svg.latex?\normalsize&space;k=\nu{\alpha_{H_2O}}\frac{T}{{\rho}}" title=""/>   where <img src="https://latex.codecogs.com/svg.latex?\normalsize&space;\alpha_{H_2O}" title="" />  is the opacity value of the medium/material, in this case water vapor, it is going through, <img src="https://latex.codecogs.com/svg.latex?\normalsize&space;T" title="" /> is a vector of size n  with the temperature at each step and <img src="https://latex.codecogs.com/svg.latex?\normalsize&space;\rho" title="" /> is another vector of the same size with the density.


## Data Source:

In order to achieve this project, there is no need for real data, using only the initial conditions is enough. The initial condition we considered are the following:

* Sv = 0 Water vapor does not emit its own light, which makes this variable equal to zero
* alpha_line = 0 
* Cs = 7.8e-6 s^6 kg^2 m
* nu = 200 GHz
* K = 1.380649e-23 m^2 kg s^-2 K^-1 Boltzman constant
* N = 100000 number of iterations
* T is the temperature in K
* alpha_h20 is the opacity of water derivated  from the following ecuation [Rosenkranz, 1990][6]:

Which resulted in this  equation:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;{\alpha_{H_2O}}=({C_s}{\nu^{2}}{\theta^{3}}{P_{H_2O}^{2}})+\alpha_{line}" title="alphah2o"/>

* theta = 300/T wich it's dimensionless and T is the temperature

* P_H2O is the pressure of  water vapor calculated by: <img src="https://latex.codecogs.com/svg.latex?\normalsize&space;P = \rho K T" title="" /> 

This is because the opacity for a certain frecunecy is dependant on the thermodynamic conditions of the medium that it's traversing. For this case, we are going to asume that the density and temperature of the water vapor are constant.
## Diagram:

GOAL: Calculate how far in meters the spotlight's radiation reaches within or outside water vapor.  
Water vapor is affected by temperature and density (K) which change spotlight's radiation distance; in this case temperature and density are taken as constants. Our
task is to create a model in order to achieve the *GOAL* with any temperature.

![Diagrama1_3](https://user-images.githubusercontent.com/60753156/105610443-2c41d200-5d75-11eb-8c14-06c8ace41345.png)


# Instructions

To run this proyect, yo first need to clone the repository using 
```
git clone https://github.com/los-Djs/avance
``` 
and then if you need, install the dependencies for the proyect by executing
```
 pip install -r requirements.txt
```
To run the script, run
```sh
python3 radiative_transfer_1.py
```


# Results:

This a graph generated in a logarithm scale:

![Plot](/Images/Figure_1.png)
![Plot](/Images/Figure_1F.png) 
<!-- aqui pon la imagen que genera kalid -->

## Software Tools:

Below, we are going to list the Python libraries needed:

* Python 3
* NumPy == 1.19.2
* Matplotlib == 3.3.2
* Pandas == 1.1.3


## Conclusions:

We observe that the water vapor absorbs the 200GHz that it is emitting from the source. It is seen in our graphic, when the light enters the water vapor its intensity is decreasing drastically.

# References:
[1] Rouan, D. (2011). Radiative Transfer. Encyclopedia of Astrobiology, 1410–1413. https://doi.org/10.1007/978-3-642-11274-4_1336 

[2] Wikipedia Contributors. (2020, December 23). Radiative transfer. Retrieved January 8, 2021, from Wikipedia website: https://en.wikipedia.org/wiki/Radiative_transfer

[3] Radiative Transfer Equation - an overview | ScienceDirect Topics. (2013). Retrieved January 8, 2021, from Sciencedirect.com website: https://www.sciencedirect.com/topics/engineering/radiative-transfer-equation

[4] Radiative Transfer - an overview | ScienceDirect Topics. (2017). Retrieved January 8, 2021, from Sciencedirect.com website: https://www.sciencedirect.com/topics/earth-and-planetary-sciences/radiative-transfer

[5] Engineering ToolBox, (2004). Water Vapor and Saturation Pressure in Humid Air. [online] Available at: https://www.engineeringtoolbox.com/water-vapor-saturation-pressure-air-d_689.html [Accessed 26 January. 2021].

[6] Rosenkranz, P. W. (1998). Water vapor microwave continuum absorption: A comparison of measurements and models. Radio Science, 33(4), 919–928. https://doi.org/10.1029/98rs01182 [Accessed 27 January. 2021].
