#------------------------------ Define Spatial Parameters----------------------------------

import numpy as np

L=100 # Length in microns
diameter=10 #diameter in microns
segment=500 #number of segments

#Segment Length
dx=L/(segment-1)
#Position along dendrites in array
x=np.linspace(0,L,segment)

#------------------------------------- Define Cable Properties-------------------------
#Axial resistance ( R_a ) is implicitly included in the spatial derivative term through the length constant ( λ_m ), 
# which characterizes how voltage changes propagate along the neurite#
Cm=1.0 # Membrane capacitance in uF/cm^2
g_passive=0.0003 # Passive conductance in S/cm^2
E_passive=-70 #Passive reversal potential in mV

#------------------------------------ Define Simulation Time Parameters---------------------
dt=0.05 #Time step in ms
t_max=3000 # Maximum simulation duration in ms
time=np.arange(0, t_max, dt) #array of time

τ_m= Cm/g_passive #Membrane time constant in ms
λ_m= 0.4 # Length constant in cm

#--------------------------------------Initial Voltage------------------------------
V=np.full(segment, E_passive) #start with restng potential

#----------------------------------Define current injection parameters---------------------
I_source=[(100,30),(300,-40)] #List of (segemnt index, amplitude in nA )
t_start, t_end=50, 150 # start and end time of current injection

