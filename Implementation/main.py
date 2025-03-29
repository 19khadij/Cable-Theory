#---main
import numpy as np
import matplotlib.pyplot as plt

#import Files
from parameters import *
from stimuli import generate_stimuli
from cable import update_voltage_eq1

#Store voltage profiles over time
V_history=[]


# I_history=[]
#Stimulation Loop
for t in time:
    I_ext=generate_stimuli(t,t_start,t_end, I_source,segment)
    V,I=update_voltage_eq1(V,I_ext,dx,τ_m,λ_m,Cm,g_passive,E_passive,dt)
    V_history.append(V.copy())
    # I_history.append(I.copy())
# print(f"Total number of steps in V_history: {len(V_history)}")
# print(f"Membrane Current: {V_history}" )
# print(f"Membrane Current: {I_history}")

# Convert V_history to a numpy array for easier indexing
V_history = np.array(V_history)


# Plot voltage profiles at different times
plt.figure(figsize=(10, 6))
time_to_plot = [0, 50, 100, 150, 200]  # time in ms
for t_idx in time_to_plot:
    plt.plot(x, V_history[int(t_idx / dt)], label=f"t={t_idx} ms")

plt.xlabel("Distance (microns)")
plt.ylabel("Voltage (mV)")
plt.title("Voltage Profiles over Time")
plt.legend()
plt.grid()
plt.show()

# Plot temporal dynamics at selected locations
plt.figure(figsize=(10, 6))
segment_to_plot = [50, 100, 400]
for seg in segment_to_plot:
    plt.plot(time, V_history[:, seg], label=f"Segment {seg}")

plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.title("Voltage over Time at Selected Segments")
plt.axhline(0, color='gray', linestyle='--')  # Add a line at 0 mV for reference
plt.legend()
plt.grid()
plt.show()