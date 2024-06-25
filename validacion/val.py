import pandas as pd 
import matplotlib.pyplot as plt


EDU_DF_PATH = "scores_edu.csv"
R_DF_PATH = "scores_r.csv"

edu = pd.read_csv(EDU_DF_PATH)
r = pd.read_csv(R_DF_PATH, sep = "\t")

join = edu.set_index("codigo").join(r.set_index("Codigo"), lsuffix = "edu",rsuffix= "r")
print(join)
join["norm.HPC.score"] = join["norm.HPC.score"].apply( lambda x :  10 - x)
print(join[["score", "norm.HPC.score"]])
join["diferencia"] = join["score"] - join["norm.HPC.score"]
print(join.columns)
df = join[[ "name", "score", "norm.HPC.score", "diferencia"]]
plt.hist(df.diferencia, bins = 50)
plt.xlabel("Diferencia entre puntaje Edu - R")
plt.ylabel("Instancias")
plt.show()
plt.hist(df.score, bins = 50 , alpha = .5, label= "Edu")
plt.hist(df["norm.HPC.score"], bins = 50 , alpha = .5, label = "R")
plt.legend()
plt.show()
# print(join["norm.HPC.score"].astype(float))
# print(edu)
# print(r)