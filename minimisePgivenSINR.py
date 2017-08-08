import cvxpy as cvx
import numpy as np

n = 3
k = 1
d = np.random.rand(n,n)
d_s = 0.5*(d+d.T)

G = np.zeros((n,n))
G = k/d_s**3.5

# Define variables
$\delta$ = np.identity(n)
S = G * $\delta$
I = G - S

sigma = 0.1*np.ones(n)
gamma = 1
Pmax = 1

# Define optimisation variable
p = cvx.Variable(n)

# Define objective function
obj = cvx.Minimize(
      cvx.sum_entries(p))

# Define constraints
constraints = [p >= 0,
               S * p - $\gamma$ * (I * p + $\sigma$) >= 0,
               p <= Pmax]

# Solve problem and print solution
prob = cvx.Problem(obj, constraints)
prob.solve()
print("Solution status = %s"%(prob.status))
print("Optimal solution = %s"%(prob.value))
print("Power settings = %s"%(p.value))