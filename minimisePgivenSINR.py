import cvxpy as cvx
import numpy as np

np.random.seed(100)

# Define variables
n = 3 # number of transmitters = receivers
A = 0.025 # uniform receiver coefficient
Δ = np.identity(n) # identity matrix
# unwanted transmitters d∈U[0,1] from receivers
d_unpair = np.random.rand(n,n)
# desired transmitters d∈0.2B[2,2] from receivers
d_pair = np.random.beta(2,2,size=n)*0.20 
 # make the matrix symmetric
d = np.tril(d_unpair) + np.tril(d_unpair, -1).T-np.diag(d_unpair)*Δ + d_pair*Δ

G = np.zeros((n,n)) # gain matrix G
G = A / d ** 3.5
S_hat = G * Δ # signal potential matrix
I_hat = G - S_hat # interference potential matrix

σ = 5.0 * np.ones(n)
γ = 1.0 # minimum acceptable SINR
Pmax = 1.0 # total power for each transmitter

# Define optimisation variable as the transmitter powers
p = cvx.Variable(n)

# Define objective function as the total power
obj = cvx.Minimize(cvx.sum(p))

# Define constraints
constraints = [p >= 0,
              S_hat * p - γ * (I_hat * p + σ) >= 0,
              p <= Pmax]

# Solve problem and print solution
prob = cvx.Problem(obj, constraints)
prob.solve()
powers = np.asarray(p.value)

print('Solution status = {0}'.format(prob.status))
print('Optimal solution = {0:.3f}'.format(prob.value))
if prob.status == 'optimal':
  for j in range(n):
  	print('Power {0} = {1:.3f}'.format(j,powers[j][0]))
