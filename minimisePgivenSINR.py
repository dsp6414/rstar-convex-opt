import cvxpy as cvx
import numpy as np

feasibility_count = 0
total_power = 0

for i in range(5000):
  np.random.seed(i)

  # Define variables
  n = 3 # number of transmitters = number of receivers
  k = 0.025 # receiver coefficient, assume uniform
  δ = np.identity(n) # identity matrix
  d = np.random.rand(n,n) # transmitters placed distance d∈U[0,1] from receivers
  d_diag = np.random.beta(2,2,size=n)*0.20
  d = np.tril(d) + np.tril(d, -1).T-np.diag(d)*δ+d_diag*δ # make the matrix symmetric with smaller diagonal elements
  # print(d)

  G = np.zeros((n,n)) # gain matrix G
  G = k / d ** 3.5

  # print(G)

  S = G * δ # desired signal matrix
  I = G - S # interference matrix

  σ = 5.0 * np.ones(n)
  γ = 1.0 # minimimum acceptable SINR
  Pmax = 1.0 # total power for the n transmitters

  # Define optimisation variable
  p = cvx.Variable(n)

  # Define objective function
  obj = cvx.Minimize(cvx.sum_entries(p))

  # Define constraints
  constraints = [p >= 0,
                 S * p - γ * (I * p + σ) >= 0,
                 p <= Pmax]

  # Solve problem and print solution
  prob = cvx.Problem(obj, constraints)
  prob.solve()
  powers = np.asarray(p.value)

  # print('Solution status = {0}'.format(prob.status))
  # print('Optimal solution = {0:.3f}'.format(prob.value))
  # if prob.status == 'optimal':
  # 	for j in range(n):
  # 		print('Power {0} = {1:.3f}'.format(j,powers[j][0]))

  if prob.status == 'optimal':
    feasibility_count += 1
    total_power += p.value

print(feasibility_count)
print(total_power/feasibility_count)