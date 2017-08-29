import numpy as np
from functions import *
from argparse import ArgumentParser
from matplotlib import pyplot as plt

# Fixed Step Size Updates
def update(cur_point, lr, func):
	gradients = {'quad'		: grad_quad,
		     'log_reg'		: grad_log_reg,
		     'himmelblaus'	: grad_himmelblaus,
		     'rosenbrock'	: grad_rosenbrock
		    }
	updt	= cur_point - lr*gradients[func](*cur_point)
	return updt
			
# Argument parser for arguments
parser	= ArgumentParser()
parser.add_argument('--func_name', required=True, help='quad | log_reg | himmelblaus | rosenbrock')
parser.add_argument('--init_type', required=True, help='rand | static')
opt	= parser.parse_args()

# Set initial point
if opt.init_type == 'rand':
	xs	= np.random.uniform(low=-6, high=6, size=2)

elif opt.init_type == 'static':
	xs	= np.array([2, 3])
	
plt.subplot(111)
plt.xlabel('$x$', size=20)
plt.ylabel('$y$', size=20)

if opt.func_name == 'quad':
	levels	= np.linspace(0, 110, 88)
	xmin, xmax, xstep	= -6, 6, 0.05
	ymin, ymax, ystep	= -6, 6, 0.05
	X, Y	= np.meshgrid(np.arange(xmin, xmax + xstep, xstep), np.arange(ymin, ymax + ystep, ystep))
	Z	= quad(X, Y)

elif opt.func_name == 'log_reg':
	levels	= np.linspace(0, 265, 212)
	xmin, xmax, xstep	= -6, 6, 0.05
	ymin, ymax, ystep	= -6, 6, 0.05
	X, Y	= np.meshgrid(np.arange(xmin, xmax + xstep, xstep), np.arange(ymin, ymax + ystep, ystep))
	Z	= log_reg(X, Y)

elif opt.func_name == 'himmelblaus':
	levels	= np.linspace(0, 220, 176)
	xmin, xmax, xstep	= -6, 6, 0.05
	ymin, ymax, ystep	= -6, 6, 0.05
	X, Y	= np.meshgrid(np.arange(xmin, xmax + xstep, xstep), np.arange(ymin, ymax + ystep, ystep))
	Z	= himmelblaus(X, Y)

elif opt.func_name == 'rosenbrock':
	levels	= np.linspace(0, 50, 40)
	xmin, xmax, xstep	= -3, 3, 0.0025
	ymin, ymax, ystep	= -6, 6, 0.05
	X, Y	= np.meshgrid(np.arange(xmin, xmax + xstep, xstep), np.arange(ymin, ymax + ystep, ystep))
	Z	= rosenbrock(X, Y)

plt.contour(X, Y, Z, levels=levels, cmap=plt.cm.jet)

for i in range(0, 1000):
	plt.plot(*xs, 'k.', markersize=5)
	xs	= update(xs, 1/(i+1), opt.func_name)
	plt.title('Iteration ${0}$ Learning Rate: ${1}$ Current Point: $({2}, {3})$'.format(i+1, round(1/(i+1), 5), round(xs[0], 5), round(xs[1], 5)), size=20)
	plt.pause(0.0001)
plt.show()
