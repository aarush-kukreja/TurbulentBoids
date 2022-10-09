# Boid and Gas Particle Spray Simulations

Turbulence, organized chaos, has been a subject of study for hundreds of years. Fuel ejectors, based on several factors ranging from ambient air to the pressure in the pipeline before ejection, can show turbulence after free expansion in laminar flow. However, as demonstrated by these programs, it is difficult to create such a Python turbulence program with a low cost of computation. 

The Gas Particle Spray model provided features several factors available for modulation. Over time, the particles relax to a Maxwell-Boltzmann distribution (which is tracked and shown at the end of the simulation). Furthermore, number density standard deviation, mean squared dispersion, and the derivative halved of mean squared dispersion is tracked. These formulas are typically used in particle physics. With the correct parameters, such as the ones already provided, the particle results align with realistic results.

The Boid model features the same factors as the Gas Particle Spray model. The model is yet to be fully complete, needed realsitic turbulent flows, but even simple simulations show hints of turbulence. As one changes the parameters, they will find that they can simulate turbulent phenomena where the boids swirl back onto themselves. The point to be made is that the Gas Particle Spray model would require much more advanced and demanding codes, while the Boid model is able to achieve signs of turbulence with only some simple lines.

Part of both models is an array that loops through all the particles, obtains their position, and creates a graph that shows where the particles are concentrated for further analysis after experimentation. Much of the code that would be used to track turbulent flows is already embedded within. Both codes have directions that allow for simple adjustments of only the parameters.

Screenshots are automatically taken at the end of the simulation, but make sure the window is properly centered (leave it untouched). Other controls for screenshots are given in the codes.

Perhaps the most interesting point is that boids, which show flocking behavior, can show a link between biology and turbulence. With further developments to the code, hopefully by early next year, the codes can be finalized.
## Screenshots

![alt text](https://ibb.co/k2WNXqM)
![alt text](https://ibb.co/hW74hY5)
![alt text](https://ibb.co/XxFfC3V)
![alt text](https://ibb.co/ZLY9Ft2)
## Author

[@aarushkukreja](https://github.com/aarushkukreja)
