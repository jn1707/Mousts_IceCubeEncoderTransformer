# Visualize Beta distribution 

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# Generate a grid of x values
x = np.linspace(0, 1, 200)

# Make the plots

plt.figure(figsize=(12, 6))

plt.subplot(121)

# Compute the corresponding probability density function
for i in range(1, 6):
    # Choose random values for a and b
    a = np.random.randint(1, 10)
    b = np.random.randint(1, 10)
    pdf = stats.beta.pdf(x, a, b)
    plt.plot(x, pdf, label=f'Beta({a}, {b})')
    plt.fill_between(x, pdf, alpha=0.1)

a = 1
b = 2
pdf = stats.beta.pdf(x, a, b)
plt.plot(x, pdf, label=f'Beta({a}, {b})')
plt.title('Probability Density Function')
plt.xlabel('x')
plt.ylabel('pdf')
plt.legend()

plt.subplot(122)
plt.plot(x, stats.beta.cdf(x, a, b), label=f'Beta({a}, {b})')
plt.title('Cumulative Distribution Function')
plt.xlabel('x')
plt.ylabel('cdf')
plt.legend()

plt.show()
