- The Ben Moseley example estimates u(t), size 1 input (time), size 1 output (u(t)).  For say a 2D diffusion equation u(x, y, t), then the input is size 3 (x, y, and t) and the output is still size 1 scalar (u(x, y, t)).  I suppose it's possible to have the output be a vector field too, instead of just a scalar.  Such a flow equations/stresses etc.

- Forward modelling:  PINN vs Euler/RK (see notes in my notebook).  Autograd saves us from needed to derive the finite difference integration formulas?

- PINN for eigenvalue equations?  Suppose the Schrodinger equation in a box potential.

- Perturbation theory with PINNs

- Can you learn the Green’s function for a PDE and use it as the kernel to solve general problems related to that PDE?

- Can physics-informed NN be used to exploit Green’s functions also?

- 