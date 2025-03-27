#This file implements the cable equation

import numpy as np

def update_voltage_eq1(V,I_ext,dx,Ra,τ_m,λ_m,Cm,g_passive,E_passive,dt):
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
    if dx <= 0 or Ra <= 0 or Cm <= 0 or g_passive < 0 or dt <= 0:
        raise ValueError("Invalid parameter values. Please check the inputs.")
    # #Axial Current
    # dVdt= (1/(Ra*Cm)) * (
    #     (V[2:]-V[1:-1]) - (V[1:-1] - V[:-2])
    #                       )/ dx**2
   
    # #Leak current
    # dVdt+=(g_passive*(E_passive-V))/Cm
    # #Update Rule
    # V_new=V+(dVdt+I_ext/Cm)*dt

    # Calculate membrane current
    # I_membrane = g_passive * (V - E_passive)

    # # Calculate second spatial derivative
    # d2Vdx2 = (V[2:] - 2 * V[1:-1] + V[:-2]) / dx**2
    # d2Vdx2 = np.pad(d2Vdx2, (1, 1), 'constant', constant_values=0)  # Pad with zeros

    # # Clip extreme values to avoid overflow
    # # d2Vdx2 = np.clip(d2Vdx2, -1e3, 1e3)
    # # Update voltage using the cable equation
    # dVdt = (1 / τ_m) * (((λ_m)**2 * d2Vdx2) - V + (τ_m * I_ext))

    # # dVdt = np.clip(dVdt, -1e3, 1e3)  # Prevent extreme voltage changes

    # V_new = V + dVdt * dt

    #---------New------
    # Calculate second spatial derivative
    d2Vdx2 = (V[2:] - 2 * V[1:-1] + V[:-2]) / dx**2
    d2Vdx2 = np.pad(d2Vdx2, (1, 1), 'edge')  # Use edge padding instead of zeros

    # Membrane current
    I_membrane = g_passive * (V-E_passive)  # Correct sign

    # Update voltage using the cable equation
    dVdt = (1 / τ_m) * (((λ_m)**2 * d2Vdx2) - V + (I_ext / Cm))  # Fixed external current term

    V_new = V + dVdt * dt


    # Ensure V remains finite
    if np.any(np.isnan(V_new)) or np.any(np.isinf(V_new)):
        raise RuntimeError("Voltage values became invalid. Check parameters.")


    return V_new,I_membrane