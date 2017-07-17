# n is the number of different input values
# m is the number of different output values
# x is probability distribution of the input signal X(t)
x = cvx.Variable(rows=n,cols=1)
# y is the probability distribution of the output signal Y(t)
# P is the channel transition matrix
y = P*x
# I is the mutual information between x and y
c = np.sum(P*np.log2(P),axis=0)
I = c*x + cvx.sum_entries(cvx.entr(y))
# Channel capacity maximised by maximising the mutual information
obj = cvx.Minimize(-I)
constraints = [cvx.sum_entries(x) == sum_x,x >= 0]
# Form and solve problem
prob = cvx.Problem(obj,constraints)
prob.solve()

