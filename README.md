# Stochastic Simulation Platform for Assessing Safety Performance of Autonomous Vehicles in Winter Seasons
## Documentation

For detailed documentation, please visit: [NSF OAC Documentation](https://nsf-oac.readthedocs.io/en/latest/)

# Project Overview

This multidisciplinary research project aims to develop an advanced cyberinfrastructure toolkit that significantly improves algorithms in simulation and enhances fundamental knowledge in computing. The focus of the project is to create a stochastic simulation platform capable of thoroughly evaluating the capabilities of Autonomous Vehicles' (AVs) Automated Driving Systems (ADS), especially under adverse winter driving conditions.

The motivation behind this research is to build a reliable tool that can accurately model stochastic vehicle behaviors, study vehicle dynamics, and predict potential AV safety risks when faced with icy or snowy road conditions. This is crucial for ensuring the safety and reliability of AVs before widespread implementation.

## Key Objectives

- **Physics-Regularized Modeling**: Leverage the principles of physics through a Physics Regularized Gaussian Process (PRGP) model to enhance the machine learning process used for simulating vehicle interactions on icy/snowy roads.
  
- **Crash Risk Prediction**: Predict both multi-vehicle and single-vehicle crash probabilities in mixed traffic environments by integrating the traffic simulation model with a new vehicle dynamics model, accounting for the complexities of winter driving conditions.
  
- **Safety Assessment**: Conduct comprehensive safety assessments of AV performance on icy and snowy pavement by analyzing stochastic vehicle motions and the corresponding risk factors. 
<p align="center">
  <img src="Picture/VehicleForces_page_1.png" width="400">
  <img src="Picture/PRGP_page_1.png" width="400">
</p>

- **Open-Source Platform Development**: Integrate the developed models into an open-source software package with extensive documentation and numerous application cases. The goal is to create a public, cloud-based platform that is easily accessible and capable of incorporating new data streams for continuous model improvement.
<p align="center">
  <img src="Picture/ResearchOverview_page_1.png" width="800">
</p>

## Research Thrusts

To overcome the challenges associated with assessing AV safety in winter driving conditions, the project will focus on the following research thrusts:

- **Thrust 1: Stochastic Simulation with Vehicle Behavioral Modeling**  
  Using vehicle trajectories and pavement ice/snow patterns obtained from roadside videos as the training dataset, a novel microscopic model will be designed to simulate Human Vehicle (HV) behaviors on icy/snowy roads using the **Physics Regularized Gaussian Process (PRGP)** technique.

- **Thrust 2: AV Safety Assessment with Vehicle Dynamic Modeling**  
  By studying vehicle dynamic factors that affect AVs' safety performance on slippery roads, an efficient, reliable, and accurate model will be developed to predict the crash risks of AVs in a mixed HV-AV environment under adverse driving conditions.

- **Thrust 3: Platform Development with Incremental Online Learning**  
  The models and algorithms will be integrated into an open-source software package, with comprehensive documentation and numerous application cases. The expected deliverable is a public cloud-based service that is easy to access and capable of adopting new data streams from users for ongoing model improvement.

- **Thrust 4: Validation and Transition-to-Practice Plan**  
  Validation will first be conducted using field data collected in Utah. The transition-to-practice plan includes:  
  1. Connecting the platform to the existing federal cyberinfrastructure, CARMA, to ensure research sustainability.  
  2. Testing the simulation platform with the operating autonomous shuttles of the CARS Lab at Wayne State University.  
  3. Deploying this simulation platform to AV testbeds for broader application.

## Broader Impacts

The expected outcomes of this project include a public cloud-based simulation platform that not only facilitates the assessment of AV safety in winter conditions but also serves as a valuable resource for the broader AV research community. By validating the models with real-world data and integrating them with existing automated driving systems, this project aims to ensure the practical applicability and sustainability of the developed toolkit.

Additionally, this research has the potential to impact other scientific and engineering fields, such as physics-supported artificial intelligence, smart and autonomous systems, and any research domain that relies on simulated data for critical evaluations.

## Introduction to CARLA

[CARLA](http://carla.org/) is an open-source simulator for autonomous driving research. It provides a highly flexible platform where you can test and validate autonomous vehicle (AV) models in realistic urban environments. CARLA supports the development, training, and validation of autonomous driving systems, with a variety of features including:

<p align="center">
  <img src="Picture/carla.jpg" width="200" alt="CARLA Environment">
</p>

- **Highly Realistic 3D Environment**: CARLA provides a high-fidelity simulation environment with a variety of urban and rural settings, complete with buildings, vehicles, pedestrians, and weather conditions.
- **Flexible API**: The CARLA Python API allows for easy integration with different autonomous driving stacks, enabling control of vehicles, sensors, and the environment programmatically.
- **Open Source and Extensible**: CARLA is open-source and highly extensible, allowing researchers to modify and add new features according to their needs.

### Key Features

<p align="center">
  <img src="Picture/lidar_point_cloud.jpg" width="400" alt="CARLA Sensors">
  <img src="Picture/fog01.gif" width="400" alt="Dynamic Weather in CARLA">
</p>

- **Multiple Sensors**: CARLA supports a wide range of sensors, including cameras, LiDARs, radars, and GNSS, which can be used to gather data or for real-time vehicle control.
- **Dynamic Weather**: The simulator allows for dynamic changes in weather and lighting, which is crucial for testing AV systems under different conditions.
- **Scenario Runner**: CARLA includes a Scenario Runner module to create complex driving scenarios for testing AVs, including multi-agent interactions and challenging driving conditions.

### Getting Started

To get started with CARLA, you can visit the [official documentation](https://carla.readthedocs.io/)&[NSF_OAC project documentation](https://nsf-oac.readthedocs.io/en/latest/) and follow the installation instructions. 

### Applications

CARLA is widely used in autonomous driving research, particularly in areas like:

- **Reinforcement Learning**: Training autonomous driving models using reinforcement learning algorithms.
- **Perception**: Testing and validation of perception systems for obstacle detection, traffic sign recognition, and more.
- **Planning and Control**: Developing and testing path planning and vehicle control algorithms in a safe and controlled environment.

### Resources
- [UMD NSF_OAC Project Group](https://nsf-oac.readthedocs.io/en/latest/)
- [CARLA GitHub Repository](https://github.com/carla-simulator/carla)
- [CARLA Documentation](https://carla.readthedocs.io/)
- [CARLA Discord Community](https://discord.gg/carla-simulator)


## Introduction to SUMO

[SUMO (Simulation of Urban MObility)](https://www.eclipse.org/sumo/) is an open-source, highly portable, microscopic, and continuous traffic simulation package designed to handle large road networks. SUMO allows researchers and developers to simulate how traffic evolves on real-world and fictional road networks, supporting a wide range of applications in traffic engineering, urban planning, and autonomous driving.

<p align="center">
  <img src="Picture/sumo_simulation.jpg" width="200" alt="SUMO Simulation">
</p>

- **Microscopic Traffic Simulation**: SUMO simulates individual vehicle behavior, including lane changing, traffic light handling, and other complex interactions, allowing for detailed studies of traffic dynamics.
- **Multi-Modal Traffic Support**: In addition to vehicles, SUMO can simulate pedestrians, bicycles, and public transportation, providing a comprehensive view of urban mobility.
- **Open Source and Extensible**: SUMO is open-source and supports custom models and extensions, making it a versatile tool for traffic simulation research.

### Key Features

<p align="center">
  <img src="Picture/sumo_network_editor.jpg" width="400" alt="SUMO Network Editor">
  <img src="Picture/sumo_vehicle_scenario.jpg" width="400" alt="SUMO Vehicle Scenario">
</p>

- **Flexible Network Import**: SUMO can import road networks from various sources, including OpenStreetMap (OSM), and allows users to define custom road networks using XML-based configuration files.
- **Traffic Demand Modeling**: SUMO provides tools for generating and simulating traffic demand, including vehicle routes, traffic lights, and other network elements.
- **Multi-Vehicle Integration**: SUMO can be used in conjunction with other simulators like CARLA for co-simulation, enabling comprehensive studies of autonomous vehicles in realistic traffic scenarios.

### Getting Started

To get started with SUMO, you can visit the [official documentation](https://sumo.dlr.de/docs/) and follow the installation instructions. The SUMO community also provides a variety of tutorials and examples to help you learn how to use the simulator effectively.

### Applications

SUMO is widely used in traffic research and autonomous driving studies, particularly in areas like:

- **Traffic Flow Optimization**: Analyzing and optimizing traffic flow on urban road networks to reduce congestion and improve efficiency.
- **Autonomous Vehicle Testing**: Simulating complex traffic scenarios to test and validate autonomous vehicle behavior in a controlled environment.
- **Urban Planning**: Supporting urban planners and engineers in designing more efficient and sustainable transportation systems.

### Resources
- [SUMO GitHub Repository](https://github.com/eclipse/sumo)
- [SUMO Documentation](https://sumo.dlr.de/docs/)
- [SUMO User Community](https://sumo.dlr.de/wiki/Main_Page)




## Demo
Dynamic weather and road friction changes in the CARLA Sumo Co-simulation Environment
<p align="center">
  <img src="Picture/2024-08.gif" width="800">
</p>

## Snowy Vehicle Trajectory Data
The snowy dataset was collected by the team at the I-695 highway segment in Baltimore, Maryland, United States on 01/15/2024 using a drone. A total of 50 minutes of video footage was captured in 4K resolution at 30 frames per second and subsequently processed into vehicle trajectory data.
<p align="center">
  <img src="Picture/Trajectory.gif" width="800">
</p>

## Publications
1. **Azin Bahar, Yang Xianfeng (Terry), Marković Nikola, Liu Mingxi** - "Infrastructure enabled and electrified automation: Charging facility planning for cleaner smart mobility" - Transportation Research Part D: Transport and Environment, 2021. [DOI: 10.1016/j.trd.2021.103079](https://doi.org/10.1016/j.trd.2021.103079)
2. **Zhang Huijie, Li Pu, Liu Xiaobai, Yang Xianfeng, An Li** - "An Iterative Semi-Supervised Approach with Pixel-wise Contrastive Loss for Road Extraction in Aerial Images" - ACM Transactions on Multimedia Computing Communications and Applications, 2023. [DOI: 10.1145/3606374](https://doi.org/10.1145/3606374)
3. **Wang Qinzheng, Gong Yaobang, Yang Xianfeng** - "Connected automated vehicle trajectory optimization along signalized arterial: A decentralized approach under mixed traffic environment" - Transportation Research Part C: Emerging Technologies, 2022. [DOI: 10.1016/j.trc.2022.103918](https://doi.org/10.1016/j.trc.2022.103918)

## People
### Dr. Xianfeng Terry Yang
Dr. Yang is an Assistant Professor (Transportation Engineering) in the Department of Civil & Environmental Engineering at the University of Maryland College Park. Dr. Yang received his Ph.D. and M.S. degrees in Civil Engineering from the University of Maryland College Park and his B.S. degree in Civil Engineering from Tsinghua University. Prior to joining UMD, Dr. Yang was an Assistant Professor at the University of Utah.

Dr. Yang's current research areas include machine learning for transportation modeling, traffic operations with connected automated vehicles, traffic safety, transportation equity, transportation planning, etc. He is the recipient of the prestigious NSF CAREER award in 2021. He has published over 100 peer-reviewed research articles in journals and conferences. He is currently an editorial board member of Transportation Research Part C, the Associate Editor of ASCE Journal of Urban Planning and Development and IEEE OJ-Intelligent Transportation Systems, and the Handling Editor of TRB Transportation Research Record. He is also the Chair of INFORMS JST ITS committee and the Secretary of the ASCE Artificial Intelligence committee. He is an appointed member of two TRB standing committees (ACP25-Traffic Signal Systems and AMR20-Disaster Response, Emergency Evacuations, and Business Continuity). He serves as a panelist of NSF, NCHRP, and multiple USDOT University Transportation Centers.

**Contact Information:**
- Email: xtyang@umd.edu
- Phone: 301-405-2881
- [Website](https://cee.umd.edu/clark/faculty/1706/Xianfeng-Terry-Yang)
- Department of Civil and Environmental Engineering, University of Maryland

## Simulator and Resources
- **Winter Season Autonomous Vehicle Safety Performance Simulation Platform**
  - ADS Submission
  - Co-simulation 
  - Download

## News and Media
Stay tuned for updates on our research progress and upcoming publications.

## Contact
For more information or to get involved, please contact:

**Principal Investigator:**
Dr. Xianfeng Terry Yang
- A. James Clark School of Engineering, Civil and Environmental Engineering
- 3244 Jeong H. Kim Engineering Building
- Tel: 301-405-2881
- Email: xtyang@umd.edu

## Instructions for Building Customized Simulation
- Download the Calibrated Co-Simulation
- Submit Your Request [Here]

---
© 2024 Autonomous Vehicle Safety Performance Simulation Project
