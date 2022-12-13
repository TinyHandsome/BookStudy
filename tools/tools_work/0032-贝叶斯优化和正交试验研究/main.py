import numpy as np
import matplotlib.pyplot as plt
from skopt import gp_minimize
from skopt.optimizer import Optimizer

np.random.seed(237)

noise_level = 0.1


def f(x, noise_level=noise_level):
    return np.sin(5 * x[0]) * (1 - np.tanh(x[0] ** 2)) + np.random.randn() * noise_level


# x = np.linspace(-2, 2, 400).reshape(-1, 1)
# fx = [f(x_i, noise_level=0.0) for x_i in x]
# plt.plot(x, fx, "r--", label="True (unknown)")
# plt.fill(np.concatenate([x, x[::-1]]),
#          np.concatenate(([fx_i - 1.9600 * noise_level for fx_i in fx],
#                          [fx_i + 1.9600 * noise_level for fx_i in fx[::-1]])),
#          alpha=.2, fc="r", ec="None")
# plt.legend()
# plt.grid()
# plt.show()

x0 = [[-1], [0], [1]]
y0 = [f(x_temp) for x_temp in x0]
# print(y0)

# res = gp_minimize(f,  # the function to minimize
#                   [(-2.0, 2.0)],  # the bounds on each dimension of x
#                   acq_func="EI",  # the acquisition function
#                   n_calls=5,  # the number of evaluations of f
#
#                   # 这个函数已经被弃用了，现在用是n_initial_points
#                   # n_random_starts=0,  # the number of random initialization points
#                   n_initial_points=0,
#
#                   x0=x0,
#                   y0=y0,
#
#                   # verbose=True,
#                   noise=0.1 ** 2,  # the noise level (optional)
#                   random_state=1234)  # the random seed
#
# print(res)


optimizer = Optimizer(
    [(-2.0, 2.0)],
    acq_func="EI",
    n_initial_points=0,
    random_state=1234
)
result = optimizer.tell(x0, y0)
# next_x = optimizer.ask(n_points=None)
next_x = optimizer._ask()
print(next_x)


'''
For further inspection of the results, attributes of the res named tuple provide the following information:

x [float]: location of the minimum.
fun [float]: function value at the minimum.
models: surrogate models used for each iteration.
x_iters [array]: location of function evaluation for each iteration.
func_vals [array]: function value for each iteration.
space [Space]: the optimization space.
specs [dict]: parameters passed to the function.
rng [RandomState instance]: State of the random state
'''
