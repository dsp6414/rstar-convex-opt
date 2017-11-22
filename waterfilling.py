import cvxpy as cvx
import numpy as np

n = 3 # number of channels
P = 1 # total power available to allocate
x = cvx.Variable(n) # optimisation variable x
α = cvx.Parameter(n,sign='positive') # baseline paramter α 
α.value = [0.8,1.0,1.2]

# Define objective function
obj = cvx.Maximize(cvx.sum_entries
                  (cvx.log(α + x))
                  )

# Define constraints
constraints = [x >= 0,
               cvx.sum_entries(x) - P ==0]

# Solve problem
prob = cvx.Problem(obj, constraints)
prob.solve()

powers = np.asarray(x.value)

print('Solution status = {0}'.format(prob.status))
print('Optimal solution = {0:.3f}'.format(prob.value))
if prob.status == 'optimal':
  for j in range(n):
  	print('Power {0} = {1:.3f}'.format(j,powers[j][0]))
