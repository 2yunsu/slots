import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)
y1 = x
y2 = x**(1/2)

plt.plot(x, y2, label=r'Utility function, $U_M=E(x)^{1/2}$')
plt.plot(x, y1, label='Expected value of risky goods, n=1')
plt.xlabel('Price')
plt.ylabel('Utility')
plt.title('Utility function graph')
plt.legend()
plt.savefig('./graph/risk.png')