# Declare variables
I = np.zeros((n,m)) # interference power matrix
S = np.zeros((n,m)) # signal power matrix
delta = np.identity(n)
S = G * delta # using gains matrix G
I = G - S

# Declare optimisation variable
p = cvx.Variable(n)

# Define objective function
obj = cvx.Minimize(
      cvx.sum_entries(p))

# Declare constraints
constraints =    [p >= 0,
                  S*p-alpha*(I*p+sigma)>=0,
                  p <= Pmax]

# Solve problem
prob = cvx.Problem(obj, constraints)
prob.solve()
