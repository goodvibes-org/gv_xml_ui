using CSV, DataFrames, Plots, GLM, StatsPlots, GR
gr()
println(pwd())
solares_r = CSV.File("validacion/BPC_Scores_Solares.tsv", delim = '\t') |> DataFrame
solares_r = solares_r[begin:end-1, :]
solares_r."norm.HPC.score" = parse.(Float64,solares_r."norm.HPC.score")
solares_edu = CSV.File("validacion/solares_edu_por_bpc.csv") |> DataFrame
joined = innerjoin(solares_edu, solares_r, on = :name => :Descripcion)
rename!(joined, Dict("norm.HPC.score" => "rscore" ))
model = lm(@formula(score ~ rscore), joined)
yhat = predict(model, joined)

pl = @df joined Plots.scatter(:rscore, :score, label = "data")
Plots.plot!(joined.rscore, yhat, label = "model")