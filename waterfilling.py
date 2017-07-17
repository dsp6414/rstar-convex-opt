# Define variable (x) & parameter (a) with total power to allocate (sum_x) and number of channels (n).
x = cvx.Variable(n)
alpha = cvx.Parameter(n,sign='positive')
alpha.value = a

# Define objective function
obj = cvx.Maximize(cvx.sum_entries
                  (cvx.log(α + x))
                  )

# Define constraints
constraints = [x >= 0,
               cvx.sum_entries(x) - sum_x ==0]

# Solve problem
prob = cvx.Problem(obj, constraints)
prob.solve()
