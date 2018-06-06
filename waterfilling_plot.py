import matplotlib as mp
import matplotlib.pylab as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

# mp.rc('font', family = 'serif', serif = 'cmr10')
mp.rcParams['mathtext.fontset'] = 'cm'
mp.rcParams.update({'font.size': 16})

n=3
α = np.array([0.8,1.0,1.2])
X = np.array([8/15,5/15,2/15])
with PdfPages('water_filling_plot.pdf') as pdf:
	axis = np.arange(0.5,n+1.5,1)
	index = axis+0.5
	# X = np.asarray(x).flatten()
	Y = α + X

	# to include the last data point as a step, we need to repeat it
	A = np.concatenate((α,[α[-1]]))
	X = np.concatenate((X,[X[-1]]))
	Y = np.concatenate((Y,[Y[-1]]))

	plt.xticks(index)
	plt.xlim(0.5,n+0.5)
	plt.ylim(0,1.5)
	plt.step(axis,A,where='post',label =r'$\alpha$',lw=2)
	plt.step(axis,Y,where='post',label=r'$\alpha + x$',lw=2)
	plt.legend(loc='lower right')
	plt.xlabel('channel number')
	plt.ylabel('power level')
	pdf.savefig(bbox_inches='tight')