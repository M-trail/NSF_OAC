Operational Guide
=================

This guide provides step-by-step instructions on how to run, customize, and analyze simulations using the CARLA and SUMO co-simulation environment.

Running a Basic Simulation
---------------------------

1. **Start CARLA Server**:

   Before running any simulation, ensure the CARLA server is up and running:

   .. code-block:: bash

      cd ~/carla
      ./CarlaUE4.sh -quality-level=Epic

   Leave this terminal open as the CARLA server will continue to run in the background.

2. **Prepare SUMO Scenario**:

   Navigate to the directory containing the SUMO scenario files:

   .. code-block:: bash

      cd ~/sumo-carla-co-simulation/scenarios

   Edit the SUMO configuration file (`.sumocfg`) to customize traffic settings if needed.

3. **Run Co-Simulation**:

   Execute the co-simulation script:

   .. code-block:: bash

      python3 run_co_simulation.py --scenario scenarios/sumo_scenario.sumocfg

   Monitor the output in the terminal for any errors or warnings.

Customizing Simulation Scenarios
--------------------------------

1. **Modify SUMO Configuration**:

   The SUMO configuration file (`.sumocfg`) controls various aspects of the simulation, such as traffic density, traffic lights, and routes. Edit this file to:

   - Adjust traffic flow.
   - Change vehicle types.
   - Modify traffic signal timings.

2. **Edit CARLA Scenario**:

   CARLA scenarios are defined in Python scripts that control the environment, weather, and vehicle behavior. Customize these scripts by editing:

   - Weather conditions (`carla.WeatherParameters`).
   - Spawn locations for vehicles and pedestrians.
   - Sensor configurations for autonomous vehicles.

3. **Combine Custom Scenarios**:

   You can combine custom SUMO and CARLA scenarios by ensuring the SUMO network aligns with the CARLA map. Use the `osmWebWizard.py` in SUMO to generate compatible road networks.

Analyzing Simulation Results
----------------------------

1. **Data Logging**:

   Both CARLA and SUMO can log data during the simulation. Ensure that logging is enabled:

   - For SUMO, use the `--summary-output` option in the `.sumocfg` file.
   - For CARLA, modify the Python script to save sensor data and vehicle trajectories.

2. **Visualization**:

   Use tools like `SUMO-GUI` to visualize traffic flow and inspect vehicle interactions.
   CARLA’s built-in visualization tools allow you to replay scenarios and inspect sensor data.

3. **Post-Processing**:

   Analyze the recorded data using Python or MATLAB for:

   - Vehicle trajectories.
   - Collision detection.
   - Traffic flow analysis.

   Generate plots and reports based on simulation results.

Troubleshooting
---------------

- **CARLA Server Crashes**: Ensure your GPU drivers are up to date and that your system has enough resources to handle high-fidelity simulations.
- **SUMO Traffic Issues**: Double-check the road network and vehicle routes in the SUMO configuration file for any inconsistencies.
- **Synchronization Issues**: If the co-simulation seems out of sync, adjust the time step configurations in both SUMO and CARLA to ensure they match.
