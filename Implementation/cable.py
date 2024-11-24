#This file implements the cable equation

import numpy as np

def update_voltage(V,I_ext,dx,Ra,Cm,g_passive,E_passive,dt):
    """
    Update voltage values across the dendrite using the cable equation.

    Parameters:
        V: Voltage array in mV for all segments.
        I_ext: External current array in nA.
        dx: segment length in microns.
        Ra: axial resistance in ohm*cm.
        Cm: Membrane capacitance in uF/cm^2.
        g_passive: Passive conductance in S/cm^2.
        E_passive: Passive reversal potential in mV.
        dt: Time step in ms.

    Returns:
        updated voltage array in mV.

    """
    #Axial Current
    dVdt= (1/(Ra*Cm)) * (
        (V[2:]-V[1:-1]) - (V[1:-1] - V[:-2])
                          )/ dx**2
    #Boundary Condition
    dVdt=np.pad(dVdt,(1,1),'constant', constant_values=0)
    #Leak current
    dVdt+=(g_passive*(E_passive-V))/Cm
    #Update Rule
    V_new=V+(dVdt+I_ext/Cm)*dt

    return V_new