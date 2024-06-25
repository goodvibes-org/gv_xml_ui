import pandas as pd 
import matplotlib.pyplot as plt


EDU_DF_PATH = "scores_edu.csv"
R_DF_PATH = "scores_r.csv"

edu = pd.read_csv(EDU_DF_PATH)
r = pd.read_csv(R_DF_PATH, sep = "\t")


# Acá asumo que `norm.HPC.score` es el 10 + score
join = edu.set_index("codigo").join(r.set_index("Codigo"), lsuffix = "edu",rsuffix= "r")
join["norm.HPC.score"] = join["norm.HPC.score"].apply( lambda x :  10 - x)
join["diferencia"] = join["score"] - join["norm.HPC.score"]
df = join[[ "name", "score", "norm.HPC.score", "diferencia", "numero_ingredientes"]]
df.to_csv("comparacion.csv")

fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize = (40, 10))
join.to_csv("datos_todos.csv")
ax[0].hist(df.diferencia, bins = 50)
ax[0].set_xlabel("Diferencia entre puntaje Edu - R")
ax[0].set_ylabel("Instancias")
# plt.savefig("diferencias.png")
# plt.show()
ax[1].hist(df.score, bins = 50 , alpha = .5, label= "Edu")
ax[1].hist(df["norm.HPC.score"], bins = 50 , alpha = .5, label = "R")
ax[1].legend()
ax[1].set_xlabel("Puntaje")
ax[1].set_ylabel("Instancias")

ax[2].scatter(df.diferencia, df.numero_ingredientes)
ax[2].set_xlabel("diferencia entre puntaje Edu - R")
ax[2].set_ylabel("Cantidad de Ingredientes")

plt.savefig("con_correccion_de_puntajes.png")
plt.show()


