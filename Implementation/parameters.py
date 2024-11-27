import numpy as np

#-----------Define Spatial parameters-------
L=500 #Length in microns
diameter=10 #diameter in microns
segment=500 #Number of segemets

#Segment Length
dx=L/(segment-1)
#Position array along dendrites
x=np.linspace(0,L,segment)


#---------Define Cable properties----------
Ra=100 #Axial resistance in ohm*cm
Cm=1 #Membrane capacitance in uF/cm^2
g_passive=0.001 #Passive conductance in S/cm^2
E_passive=-65 #Passive reversal potential in mV

#---------Define Simulation time parameters--------
dt=0.1 #Time step in ms
t_max=2000 #Maximum simulation duration in ms
time=np.arange(0,t_max,dt)#time array

τ_m = Cm / g_passive   # Membrane time constant in ms (10 ms)
λ_m = 0.28             # Length constant in cm (calculated) #Length in cm, which characterizes the spatial scale of voltage changes along the cable

# print(
#     L,diameter,segment,dx,x,Ra,Cm,g_passive,E_passive,
#     dt,t_max,time
# )