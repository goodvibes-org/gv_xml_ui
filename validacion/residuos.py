import pandas as pd
import matplotlib.pyplot as plt

cc = pd.read_csv("comparacion.csv")
sc = pd.read_csv("comparacion_sin_corr.csv")

plt.scatter(range(len(cc)), cc.diferencia, label = "con correccion", alpha=.5)
plt.scatter(range(len(sc)), sc.diferencia, label = "sin correccion", alpha=.5)
plt.xlabel("producto n")
plt.ylabel("diferencia")
plt.legend()
plt.savefig("residuos.png")
plt.show()