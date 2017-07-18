# Define variables
delta = np.identity(n)
S = G * delta
I = G - S

# Define optimisation variable
p = cvx.Variable(n)

# Define objective function
obj = cvx.Minimize(
      cvx.sum_entries(p))

# Define constraints
constraints = [p >= 0,
               S * p - $\alpha$ * (I * p + $\sigma$) >= 0,
               p <= Pmax]

# Solve problem
prob = cvx.Problem(obj, constraints)
prob.solve()