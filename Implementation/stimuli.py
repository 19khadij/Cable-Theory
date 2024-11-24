# This file defines the function to handle external current sources.

import numpy as np

def generate_stimuli(t,t_start,t_end,I_source,segment):
    """
    Generate external current array for the simulation.

    Parameters:
        t:Current time in ms.
        t_start:Start time of simulation in ms.
        t_end:End time of simulation in ms.
        I_source: List of (segemnent index, amplitude in nA).
        segment: Number of segments.

    Returns:
        np.ndarray: External current array for all segments.
    """

    I_ext=np.zeros(segment)

    if t_start<=t<=t_end:
        for idx, amp in I_source:
            I_ext[idx]+=amp
    return I_ext
