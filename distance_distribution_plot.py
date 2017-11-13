import numpy as np
import matplotlib.pylab as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.stats import beta

a = 2
b = 2
x = np.linspace(0,1,1000)
u = np.ones(len(x))
u[0] = 0
u[-1] = 0

with PdfPages('distance_distributions.pdf') as pdf:
	plt.plot(0.2*x,5*beta.pdf(x, a, b), label="Paired Distribution")
	plt.plot(x,u, label="Unpaired Distribution")
	plt.xlabel("Distance, $d$")
	plt.ylabel("Probability Density")
	plt.legend(loc="best")
	pdf.savefig(bbox_inches="tight")