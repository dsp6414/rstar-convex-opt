import cvxpy as cvx
import numpy as np

# Define variables
n = 3
k = 1.0
d = np.random.rand(n,n)
d_s = 0.5 * (d + d.T)

G = np.zeros((n,n))
G = k / d_s ** 3.5

# $\delta$ = np.identity(n)
δ = np.identity(n)
# S = G * $\delta$
S = G * δ
I = G - S

# $\sigma$ = 0.1 * np.ones(n)
σ = 0.1 * np.ones(n)
# $\gamma$ = 1.0
γ = 1.0
Pmax = 1.0

# Define optimisation variable
p = cvx.Variable(n)

# Define objective function
obj = cvx.Minimize(
      cvx.sum_entries(p))

# Define constraints
constraints = [p >= 0,
               # S * p - $\gamma$ * (I * p + $\sigma$) >= 0,
               S * p - γ * (I * p + σ) >= 0,
               p <= Pmax]

# Solve problem and print solution
prob = cvx.Problem(obj, constraints)
prob.solve()

print('Solution status = {0}'.format(prob.status))
print('Optimal solution = {0:.3f}'.format(prob.value))
if prob.status == 'optimal':
	for j in range(n):
		print('Power {0} = {1}'.format(j,p.value[j]))