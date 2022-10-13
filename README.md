# Linking Biological Flocking with Turbulence (how birds, fish, bacteria and etc. move with fuel injectors, hurricanes, blood flow and etc.)

## Screenshots (Example Simulations)

[![E3-F8148-C-0619-4386-83-C8-F8822-B98-ACD6.jpg](https://i.postimg.cc/g0c8GFDR/E3-F8148-C-0619-4386-83-C8-F8822-B98-ACD6.jpg)](https://postimg.cc/rDbK9H7F)


## Introduction
Turbulence, organized chaos, has been a subject of study for hundreds of years. Fuel injectors, based on several factors ranging from ambient air to the pressure in the pipeline before ejection, can show turbulence after free expansion in laminar flow. However, as demonstrated by these programs, creating such a Python turbulence program with a low computation cost is challenging. 
As these simulations were being created, the fuel injector model was the first. Attempts to add turbulence phenomena were made, but it proved to be somewhat difficult to do so and match real turbulence statistics. The model thereafter ceased updates (at the moment is a simple particle engine that still reflects laminar flow and is useful for those purposes), and a new project was resumed—attempting to model turbulence with boids, the biological behavior of birds, fish, etc. Anything that "flocks." The first rendition of this code is given in this repository, open-source for all.
More factors like rotational momentum to model eddies at the mouth of the injector and vortexes in the later atomization stages of the droplets are yet to be added. Atomization will be an interesting thing to capture, if possible. Furthermore, pressure is captured in the fuel injector program but not the boid program—there are a couple working points that have been undertaken and will be complete soon.

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
