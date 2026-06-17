import numpy as np
import matplotlib.pyplot as plt

# Cargar datos
data = np.loadtxt("../sample_data/hydrobase-rho.maximum.asc")

# Columnas: iteración, tiempo, valor
t = data[:,1]
rho_max = data[:,2]

plt.figure(figsize=(8,5))
plt.plot(t, rho_max, color="purple", linewidth=2)

plt.xlabel("Time [M]")
plt.ylabel(r"Maximum density $\rho$")
plt.title("Maximum density vs time (TOV star)")
plt.grid(True)

plt.tight_layout()
plt.savefig("../figures/rho_max_vs_time.png", dpi=300)

print("Figure saved in ../figures/")
