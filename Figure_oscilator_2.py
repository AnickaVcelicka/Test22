import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1
UD = 0.2 * np.sqrt(4* m * k)
CRI = np.sqrt(4* m * k)
OD = 2 * np.sqrt(4* m * k)

x = np.linspace(0, 10, 100)
Freq = np.sqrt(k / m) 
RF = -(OD / (2 * m)) + np.sqrt((OD / (2 * m) )**2 - Freq**2)
FR = -(OD / (2 * m)) - np.sqrt((OD / (2 * m))**2 - Freq**2)

AUD = np.exp(-UD / (2 * m) * x) * np.cos((Freq**2 -UD / (2 * m) ) * x)
ACRI = np.exp(-CRI / (2 * m) * x) * (1 + x)

AOD = (np.exp(RF * x) + np.exp(FR * x)) / 2

plt.title("Dependance of the damping coefficient on the amplitude of oscilation")
plt.xlabel("Time, t [s]")
plt.ylabel("Amplitude, A [m]") 
plt.plot(x, AUD, label="Underdamping", color="red")
plt.plot(x, ACRI, label="Critical damping", color="blue")
plt.plot(x, AOD, label="Overdamping", color="green")
plt.legend()
plt.grid()
plt.savefig('plot_test2.png')
plt.show()
