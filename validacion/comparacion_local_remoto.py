import pandas as pd



local = pd.read_csv("validacion/datos_18feb_local.csv")
remoto = pd.read_csv("validacion/datos_18feb_remoto.csv")
r = pd.read_csv("validacion/scores_r.csv", sep="\t")

join = local.set_index("name").join(other=remoto.set_index("name"), lsuffix= "_local" ,rsuffix="_remoto").set_index("codigo_remoto").join(other=r.set_index("Codigo"), rsuffix= "_r")
join["score_r"] = join["norm.HPC.score"].apply( lambda x :  10 - x)
print(join[["score_remoto", "score_local", "score_r"]])