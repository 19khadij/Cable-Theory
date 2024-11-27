# Cable-Theory

This project simulates the voltage propagation across a dendrite using the cable equation. The implementation calculates the voltage distribution across the dendrite at each time step, taking into account the axial current, boundary conditions, and passive conductance properties. The simulation also includes an external current injection at specific segments of the dendrite over a defined time period.

# Overview
Files
cable.py - Contains the implementation of the update_voltage function, which computes the voltage changes across segments of the dendrite based on the cable equation.
stimuli.py - Defines the generate_stimuli function, which models the external current injection into the dendrite at specified times and segments.
parameters.py - Contains all the necessary physical parameters and constants for the simulation, such as segment length, axial resistance, membrane capacitance, and passive reversal potential.
main.py - Runs the simulation, collects voltage data at different time points, and generates visualizations of the voltage profile along the dendrite.

# Installation
To run this simulation, you will need Python 3 and the following packages:

-numpy
-matplotlib

# Key Simulation Outputs
-Voltage Profile Over Time: The simulation calculates the voltage at each segment for each time step.
-Temporal Dynamics: The voltage evolution is plotted for selected segments over time.
-How to Run the Simulation
-Ensure you have the required Python packages installed (numpy, matplotlib).
-Save the code for each file (cable.py, stimuli.py, parameters.py, main.py).
-Run main.py to start the simulation and generate voltage plots.


# Conclusion
This simulation provides insight into how electrical signals propagate along a dendrite in response to external current injections. The cable equation is used to model the changes in membrane potential across multiple segments of the dendrite.
