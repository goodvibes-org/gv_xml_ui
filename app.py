from productos import convert
import datetime
from ingredientes import convert as ing_convert
from dotenv import load_dotenv
import os
import subprocess
import requests
import streamlit as st 
import pandas as pd
from google.cloud import storage
import os
st.title(
	"GV XML Score Calculator"
)


PRODUCTOS_BUCKET_PATH = "db/bpc_productos_proc.csv"
INGREDIENTES_BUCKET_PATH = "db/bpc_ingredientes_proc.csv"
PROD_ING_BUCKET_PATH = "db/bpc_productos_proc_ingredientes.csv"

load_dotenv(".env")
storage_client = storage.Client()
bucket = storage_client.bucket("edu-xml")
base_url = os.environ.get("REQUEST_URL")
productos = st.file_uploader("upload product database data") 
ingredientes = st.file_uploader("upload ingredient database data")
if productos is not None and ingredientes is not None:
	with open("BPC_Productos (1).xlsx", "wb") as file:
		file.write(productos.getbuffer())
	with open("BPC_Ingredientes.xlsx", "wb") as file:
		file.write(ingredientes.getbuffer())
	prod_blob = bucket.blob(PRODUCTOS_BUCKET_PATH)
	ing_blob = bucket.blob(INGREDIENTES_BUCKET_PATH)
	prod_ing_blob = bucket.blob(PROD_ING_BUCKET_PATH)
	
	st.write(
		f"""
		{productos.name} subido exitosamente\n
		{ingredientes.name} subido exitosamente\n

		"""
		)
	
	update_run = st.checkbox("update run")
	buti = st.button("RUN")
	if buti:
		st.subheader("Este comando tomará cierto tiempo, esperar hasta cartel EXITO")
		subprocess.run("./excel-to-csv")
		os.rename("bpc_ingredientes_proc.csv", "data/db_files/bpc_ingredientes_proc.csv")
		os.rename("bpc_productos_proc.csv", "data/db_files/bpc_productos_proc.csv")
		os.rename("bpc_productos_proc_ingredientes.csv", "data/db_files/bpc_productos_proc_ingredientes.csv")
		# prod = open(prod, "r")
		# ing_prod = open(ing_prod, "r")
		# ing = open(ing, "r")
		st.write("Archivos digeridos exitosamente, corriendo scores")
		
		print("Ingredientes")
		ing_blob.upload_from_filename("bpc_ingredientes_proc.csv")
		print("Productos")
		prod_blob.upload_from_filename("bpc_productos_proc.csv")
		print("Ingredientes de Productos")
		prod_ing_blob.upload_from_filename("bpc_productos_proc_ingredientes.csv")
		
		
		# payload = {
		# 	"prod_data" : prod,
		# 	"prod_ing_data": ing_prod,
		# 	"ing_data": ing
		# }
		st.write("about to make request")
		# with open("jsondump.json", "w") as file:
			# json.dump(payload,file)
		# response = requests.post(url= "http://localhost:3000/first_run_bytes", json = payload).content.decode()
		if not update_run:
			response = requests.get(url = f"http://calculator:3000/")
			st.write("request made")
		else:
			response = requests.get(url = f"http://{base_url}:3000/update")
		st.text(f"Archivos nuevos guardados en = {response.content.decode()}")
		st.link_button("resultados", "http=//{base_url}:8080")
		st.subheader("EXITO")
