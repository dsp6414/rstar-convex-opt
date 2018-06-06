import numpy as np
import matplotlib.pylab as plt
import matplotlib as mp
from matplotlib.backends.backend_pdf import PdfPages
from scipy.stats import beta

# mp.rc('font', family = 'serif', serif = 'cmr10')
mp.rcParams['mathtext.fontset'] = 'cm'
mp.rcParams.update({'font.size': 16})

a = 2
b = 2
x = np.linspace(0,1,1000)
u = np.ones(len(x))
u[0] = 0
u[-1] = 0

with PdfPages('distance_distributions.pdf') as pdf:
	plt.plot(0.2*x,5*beta.pdf(x, a, b), label="paired distribution")
	plt.plot(x,u, label="unpaired distribution")
	plt.xlabel("distance, $d$")
	plt.ylabel("probability density")
	plt.legend(loc="best")
	pdf.savefig(bbox_inches="tight")