# Radiative Transfer

## Authors:

* ### Fonseca Márquez Pablo Francisco fonseking21@gmail.com
* ### Ceja Cruz Eduardo Manuel lalitoceja@gmail.com
* ### García Olivo Brian Kalid briankalid2000@gmail.com

## Issue:

We all have some source of light in our house that feels warm, but have we ever wondered why or how? Well, in order to answer this question, we are going yo develop our project with help of radiative transfer.

## Model:

Radiative Transfer, is the physical phenomenon of energy transfer in the form of electromagnetic radiation.
The progragation of radiation through a medium is affected by abosrption, emission, and scattering processes. It's basically how energy interacts with the matter through which this is transfered.


## Goal:
Our goal is to implement the radiative transfer model for a few simple controlled cases succesfully. For this, we are going to solve the radiative transfer equation, but in it's discretized form for simplicity. The discretized form is the following:


<!--- $$I_{i+1} = I_i e^{-\tau} + S_{\nu}(I_{i+1})(1-e^{-\tau})$$-->
<img src="https://latex.codecogs.com/svg.latex?\Large&space;I_{i+1}=I_{i}e^{-\tau}+S_{\nu}(I_{i+1})(1-e^{-\tau})" title="" />


Where <img src="https://latex.codecogs.com/svg.latex?\Large&space;\tau" title="" /> is defined as

<!---\frac{\delta x}{2}(k_i + k_{i + 1})-->

<img src="https://latex.codecogs.com/svg.latex?\Large&space;\frac{\Delta{x}} {2}(k_i+k_{i+1})" title="dt"/>

<!---and $k = \nu f T/\ro$  where $f$ is the value of the ~~something i don't remeber~~, $T$ is a vector of size n  with the temperature at each step and $\ro$ is another vector of the same size with the density.-->


and  <img src="https://latex.codecogs.com/svg.latex?\normalsize&space;k=\nu{f}{\frac{T}{\rho}}" title=""/>   where <img src="https://latex.codecogs.com/svg.latex?\normalsize&space;f" title="" />  is the opacity value of the medium/material it is going thru, <img src="https://latex.codecogs.com/svg.latex?\normalsize&space;T" title="" /> is a vector of size n  with the temperature at each step and <img src="https://latex.codecogs.com/svg.latex?\normalsize&space;\rho" title="" /> is another vector of the same size with the density.


## Software Tools:

Below, we are going to list the python libraries we are going to need:

1. Python 3
2. Numpy
3. Matplotlib

## Data source:

For this proyect, there is no need fore real data, using the initial conditions is enough.0

## Diagram:

GOAL: Calculate how far in cm the spotlight's radiation reaches within or outside water steam.  
Water steam is affected by temperature (°C) which changes spotlight's radiation distance; our
task is to create a model in order to achieve the *GOAL* with any temperature.

![Diagrama1_3](https://user-images.githubusercontent.com/60753156/105610443-2c41d200-5d75-11eb-8c14-06c8ace41345.png)


## References:
[1] Rouan, D. (2011). Radiative Transfer. Encyclopedia of Astrobiology, 1410–1413. https://doi.org/10.1007/978-3-642-11274-4_1336 

[2] Wikipedia Contributors. (2020, December 23). Radiative transfer. Retrieved January 8, 2021, from Wikipedia website: https://en.wikipedia.org/wiki/Radiative_transfer

[3] Radiative Transfer Equation - an overview | ScienceDirect Topics. (2013). Retrieved January 8, 2021, from Sciencedirect.com website: https://www.sciencedirect.com/topics/engineering/radiative-transfer-equation

[4] Radiative Transfer - an overview | ScienceDirect Topics. (2017). Retrieved January 8, 2021, from Sciencedirect.com website: https://www.sciencedirect.com/topics/earth-and-planetary-sciences/radiative-transfer


