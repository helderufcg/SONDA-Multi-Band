# SONDA MULTI-BAND
---
## About
  ### This project improves the open-source software SONDA to consider simulations involving multiband systems, their characteristics and penalties.
  ### In order to successfully adapt the SONDA simulator to Mult-band optical networks, the project considers the attenuation as a function of frequency in two different fibers: G652.A and G652.D. Furthermore,  it was also taken in consideration the noise figure as a function of the frequency in two different amplifiers: TDFA  (S-Band) and EDFA (C and L Bands), meanwhile the O and E bands amplifiers' (BDFA and PDFA, respectively) noise figures are still considered constant, for now.
  ### Regarding the multiband optical networks' penalties, the project accounts the ASE-noise (Amplified Spontaneous Emission noise) for now,  considering devices such as transmitters, receivers, switches, multiplexers and demultiplexers.
---
## SONDA - Simulator for Optical Network Design and Analysis
  ### SONDA is an open-source python software for simulating and analyzing optical networks.
  ### The software considers WDM and EON networks, in addition to having a simulation version for SDM networks.
  ### Link to the SONDA: https://github.com/helderufcg/SONDA
  ### Link to the SONDA-SDM version: https://github.com/GuerraJr/SONDA-SDM
---
## Flowchart
  ### Flowchart of the SONDA Multi-Band call request process:
  <p align="center">
  <img height="600" src="To readme/Fluxograma SONDA MB 1.0.png">
  
---
## Libs
  ### Required libraries:
1. Numpy
2. Scipy
3. MatPlotLib]
4. Pandas
5. Networkx
6. Dill
7. Pyqt5
8. Mysql.connector
9. Mysqlclient
10. Prettytable
---
## References
  ### Attenuation curves as a function of frequency for two types of fiber (G652.A and G652.D): https://www.fiberoptics4sale.com/blogs/archive-posts/95052294-optical-fiber-attenuation
  ### TDFA noise figure curve for the S-band as a function of frequency: 2020Correia
  ### EDFA noise figure curve for the C-band as a function of frequency: 2022D_Amico
  ### EDFA noise figure curve for the L-band as a function of frequency: 2021Correia-1
  ### PDFA (O-Band) and BDFA (E-Band) noise figure: 2019Ferrari
---
## Contact
  ### Email: ademar.santos@ee.ufcg.edu.br
---
