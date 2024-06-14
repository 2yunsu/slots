import numpy as np

import matplotlib.pyplot as plt

for i in range(4):
    x = np.linspace(0, 1, 100)
    y1 = x
    y2 = x**(1/(i+2))
    plt.plot(x, y2, label=r'Utility function, $U_M=E(x)^{{1/{}}}$'.format(i+2))

plt.plot(x, y1, label=r'Expected value of risky goods, $U_M=E(x)^{1}$')
plt.xlabel('Price')
plt.ylabel('Utility')
plt.title('Utility function graph')
plt.legend()
plt.savefig('./graph/risk_per_sqaure_root.png')