# TurbulentBoids (Linking Biological Flocking with Turbulence) 

[![Turbulent-Boids-1.png](https://i.postimg.cc/XqDjnBQB/Turbulent-Boids-1.png)](https://postimg.cc/2LhRwypC)

Open-source Python software for building and running bio-turbulent studies. Visit TurbulentBoids.com


## Video

[![Linking Biological Flocking with Turbulence](https://img.youtube.com/vi/ImoDOyBzeKY/0.jpg)](https://www.youtube.com/watch?v=SFfnEDMSSqo "Linking Biological Flocking with Turbulence")


## Introduction
TTurbulence, organized chaos, has been a subject of study for hundreds of years. Fuel injectors, based on several factors ranging from ambient air to the pressure in the pipeline before ejection, can show turbulence after free expansion in laminar flow. It is plausible that a link between turbulence and biological flocking behavior could be found, as shown in these programs. We observe laminar flow in the normal fuel-injector program and turbulent flow in an enclosed space in the boid program. The boid program is based on Craig Reynolds' work on Boid Algorithms, where the boids all rely on three factors—separation, coherence, and alignment. And we see that these same properties could be applied to particle physics to simulate turbulence as a CFD would. 
The significance lies in understanding how our world could be more interconnected than we think. Flocking is omnipresent, as we see in bacteria movement, ant colonies, human mob behavior, bird murmurations, and schools of fish—turbulence exists everywhere, from airplanes to the very area this is being read from. And now, the TurbulentBoids software has demonstrated that there could be a link between the two.

## Fuel Injector Model
The Fuel Injector / Gas Particle Spray model provided features several factors available for modulation. Over time, the particles relax to a Maxwell-Boltzmann distribution (which is tracked and shown at the end of the simulation; the speed distribution graph given below is only an example. One can create more accurate distributions by altering input). Furthermore, number density standard deviation, mean squared dispersion, and the derivative halved of mean squared dispersion is tracked. These formulas are typically used in particle physics. The particle results align with realistic results with the correct parameters, such as those already provided.

## Flocking Behavior Model
The Flocking Behavior boid model features the same factors as the Gas Particle Spray model. The model is yet to be fully complete and needs realistic turbulent flows, but even simple simulations show hints of turbulence. As one changes the parameters, they will find they can simulate turbulent phenomena where the boids swirl back onto themselves. The point to be made is that the Gas Particle Spray model would require much more advanced and demanding codes, while the Boid model can achieve signs of turbulence with only some simple lines.

## Important Points
Part of both models is an array that loops through all the particles, obtains their position, and creates a graph that shows where the particles are concentrated for further analysis after experimentation. Much of the code used to track turbulent flows is already embedded within. Both codes have directions that allow for simple adjustments of only the parameters. The array is used to create more arrays for all other tracked factors.

Screenshots are automatically taken at the end of the simulation, but make sure the window is centered correctly (leave it untouched). Other controls for screenshots are given in the codes.

## Future

Perhaps the most exciting point is that boids, which show flocking behavior, can show a link between biology and turbulence. Hopefully, by early next year, the programs can be finalized with further developments to the code.

## Screenshots

### More Flocking Behavior Screenshots (Example Simulation)

[![Boid-Concentration-Quit-Graph.png](https://i.postimg.cc/RV5S2QZx/Boid-Concentration-Quit-Graph.png)](https://postimg.cc/s1mChWWT)
[![Boid-Mean-Squared-Dispersion-Graph.png](https://i.postimg.cc/dVQYKWMp/Boid-Mean-Squared-Dispersion-Graph.png)](https://postimg.cc/qzFYsxvx)
[![Boid-Concentration-Full-Graph.png](https://i.postimg.cc/4yRD2Pb8/Boid-Concentration-Full-Graph.png)](https://postimg.cc/5YpK6wrv)

### More Fuel Injector Screenshots (Example Simulation)

[![Gas-Particle-Concentration-Quit-Graph.png](https://i.postimg.cc/kXBGdXxW/Gas-Particle-Concentration-Quit-Graph.png)](https://postimg.cc/6yxtrKbQ)
[![Gas-Particle-Mean-Squared-Dispersion-Graph.png](https://i.postimg.cc/GmvccB9T/Gas-Particle-Mean-Squared-Dispersion-Graph.png)](https://postimg.cc/SnN0dx6m)
[![Gas-Particle-Speed-Distribution-Quit-Graph.png](https://i.postimg.cc/sXgy9wm5/Gas-Particle-Speed-Distribution-Quit-Graph.png)](https://postimg.cc/7Cdpq1pL)
