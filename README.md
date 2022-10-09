# Boid and Gas Particle Spray Simulations

Turbulence, organized chaos, has been a subject of study for hundreds of years. Fuel ejectors, based on several factors ranging from ambient air to the pressure in the pipeline before ejection, can show turbulence after free expansion in laminar flow. However, as demonstrated by these programs, it is difficult to create such a Python turbulence program with a low cost of computation. 

The Gas Particle Spray model provided features several factors available for modulation. Over time, the particles relax to a Maxwell-Boltzmann distribution (which is tracked and shown at the end of the simulation; the speed distribution graph given below is only an example, one can create more accurate distributions by altering input). Furthermore, number density standard deviation, mean squared dispersion, and the derivative halved of mean squared dispersion is tracked. These formulas are typically used in particle physics. With the correct parameters, such as the ones already provided, the particle results align with realistic results.

The Boid model features the same factors as the Gas Particle Spray model. The model is yet to be fully complete, needed realsitic turbulent flows, but even simple simulations show hints of turbulence. As one changes the parameters, they will find that they can simulate turbulent phenomena where the boids swirl back onto themselves. The point to be made is that the Gas Particle Spray model would require much more advanced and demanding codes, while the Boid model is able to achieve signs of turbulence with only some simple lines.

Part of both models is an array that loops through all the particles, obtains their position, and creates a graph that shows where the particles are concentrated for further analysis after experimentation. Much of the code that would be used to track turbulent flows is already embedded within. Both codes have directions that allow for simple adjustments of only the parameters. The array is used to create more arrays for all other tracked factors.

Screenshots are automatically taken at the end of the simulation, but make sure the window is properly centered (leave it untouched). Other controls for screenshots are given in the codes.

Perhaps the most interesting point is that boids, which show flocking behavior, can show a link between biology and turbulence. With further developments to the code, hopefully by early next year, the codes can be finalized.
## Screenshots

[![Gas-Particle-Simulation-Quit.png](https://i.postimg.cc/brMzvkQk/Gas-Particle-Simulation-Quit.png)](https://postimg.cc/N26hJyCj)
[![Gas-Particle-Concentration-Quit-Graph.png](https://i.postimg.cc/kXBGdXxW/Gas-Particle-Concentration-Quit-Graph.png)](https://postimg.cc/6yxtrKbQ)
[![Gas-Particle-Mean-Squared-Dispersion-Graph.png](https://i.postimg.cc/GmvccB9T/Gas-Particle-Mean-Squared-Dispersion-Graph.png)](https://postimg.cc/SnN0dx6m)
[![Gas-Particle-Speed-Distribution-Quit-Graph.png](https://i.postimg.cc/sXgy9wm5/Gas-Particle-Speed-Distribution-Quit-Graph.png)](https://postimg.cc/7Cdpq1pL)

[![Boid-Simulation-Quit.png](https://i.postimg.cc/hvQkpwdQ/Boid-Simulation-Quit.png)](https://postimg.cc/64wbQMzB)
[![Boid-Concentration-Quit-Graph.png](https://i.postimg.cc/RV5S2QZx/Boid-Concentration-Quit-Graph.png)](https://postimg.cc/s1mChWWT)
## Author
[![Boid-Mean-Squared-Dispersion-Graph.png](https://i.postimg.cc/dVQYKWMp/Boid-Mean-Squared-Dispersion-Graph.png)](https://postimg.cc/qzFYsxvx)
[![Boid-Concentration-Full-Graph.png](https://i.postimg.cc/4yRD2Pb8/Boid-Concentration-Full-Graph.png)](https://postimg.cc/5YpK6wrv)

[@aarushkukreja](https://github.com/aarushkukreja)
