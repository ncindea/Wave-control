import numpy as np

# This module contains a 2D Gauss Quadrature Rule and a 1D Gauss Quadrature Rule

# The 2D Quadrature Rule is a 19 points rule over the reference triangle used by A. Meyer
# in reference [1]. It was obtained using the MATLAB software developed by  John Burkardt,
# available at
# https://people.sc.fsu.edu/~jburkardt/m_src/triangle_dunavant_rule/triangle_dunavant_rule.html
# It is stored as a 19x3 matrix called 'gaussRule2D'.

# The 1D Quadrature Rule is a six points quadrature rule over the interval [-1,1]

# Referencees:
#
# [1]:
# Author: Arnd Meyer
# Title: A simplified calculation of reduced HCT-basis in FE context
# Journal: Computational Methods in Applied Mathematics

#


### 2D Quadrature Rule
# 1st and 2nd columns are xy-coordinates of gaussian points, 3rd column is weight
gaussRule2D = np.array([
[0.33333333333333298176270886870042886584997177124023, 0.33333333333333298176270886870042886584997177124023, 0.09713579628279900290976911492180079221725463867188 ],
[0.02063496160252499891929467423778987722471356391907, 0.48968251919873800881433112408558372408151626586914, 0.03133470022713900210442616867112519685178995132446 ],
[0.48968251919873800881433112408558372408151626586914, 0.48968251919873800881433112408558372408151626586914, 0.03133470022713900210442616867112519685178995132446 ],
[0.48968251919873800881433112408558372408151626586914, 0.02063496160252499891929467423778987722471356391907, 0.03133470022713900210442616867112519685178995132446 ],
[0.12582081701412700658337939785269554704427719116211, 0.43708959149293702406424699802300892770290374755859, 0.07782754100477400072133349340219865553081035614014 ],
[0.43708959149293702406424699802300892770290374755859, 0.43708959149293702406424699802300892770290374755859, 0.07782754100477400072133349340219865553081035614014 ],
[0.43708959149293702406424699802300892770290374755859, 0.12582081701412700658337939785269554704427719116211, 0.07782754100477400072133349340219865553081035614014 ],
[0.62359292876193495036574176992871798574924468994141, 0.18820353561903299666191458072717068716883659362793, 0.07964773892720999892702593569993041455745697021484 ],
[0.18820353561903299666191458072717068716883659362793, 0.18820353561903299666191458072717068716883659362793, 0.07964773892720999892702593569993041455745697021484 ],
[0.18820353561903299666191458072717068716883659362793, 0.62359292876193495036574176992871798574924468994141, 0.07964773892720999892702593569993041455745697021484 ],
[0.91054097321109495055679872166365385055541992187500, 0.04472951339445299656638610485970275476574897766113, 0.02557767565869800002742451283666014205664396286011 ],
[0.04472951339445299656638610485970275476574897766113, 0.04472951339445299656638610485970275476574897766113, 0.02557767565869800002742451283666014205664396286011 ],
[0.04472951339445299656638610485970275476574897766113, 0.91054097321109495055679872166365385055541992187500, 0.02557767565869800002742451283666014205664396286011 ],
[0.03683841205473600138864398445548431482166051864624, 0.22196298916076601104307997047726530581712722778320, 0.04328353937728900147074995174989453516900539398193 ],
[0.22196298916076601104307997047726530581712722778320, 0.74119859878449800838495775678893551230430603027344, 0.04328353937728900147074995174989453516900539398193 ],
[0.74119859878449800838495775678893551230430603027344, 0.03683841205473600138864398445548431482166051864624, 0.04328353937728900147074995174989453516900539398193 ],
[0.22196298916076601104307997047726530581712722778320, 0.03683841205473600138864398445548431482166051864624, 0.04328353937728900147074995174989453516900539398193 ],
[0.74119859878449800838495775678893551230430603027344, 0.22196298916076601104307997047726530581712722778320, 0.04328353937728900147074995174989453516900539398193 ],
[0.03683841205473600138864398445548431482166051864624, 0.74119859878449800838495775678893551230430603027344, 0.04328353937728900147074995174989453516900539398193 ]])

### 1D Quadrature Rule
# 1st column are the gaussian points in in the interval [-1,1], 2nd column stores the weights
gaussRule1D = np.array([
    [ 0.6612093864662645, 0.3607615730481386],
    [-0.6612093864662645, 0.3607615730481386],
    [-0.2386191860831969, 0.4679139345726910],
    [ 0.2386191860831969, 0.4679139345726910],
    [-0.9324695142031521, 0.1713244923791704],
    [ 0.9324695142031521, 0.1713244923791704]])
