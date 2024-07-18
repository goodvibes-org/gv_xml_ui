from productos import convert
import datetime
from ingredientes import convert as ing_convert
from dotenv import load_dotenv
import os
import requests
import streamlit as st 
import pandas as pd
from google.cloud import storage
st.title(
	"GV XML Score Calculator"
)


PRODUCTOS_BUCKET_PATH = "db/productos.csv"
INGREDIENTES_BUCKET_PATH = "db/ingredientes.csv"
PROD_ING_BUCKET_PATH = "db/prod_ingredientes.csv"

load_dotenv(".env")
storage_client = storage.Client()
bucket = storage_client.bucket("edu-xml")
base_url = os.environ.get("REQUEST_URL")
productos = st.file_uploader("upload product database data") 
ingredientes = st.file_uploader("upload ingredient database data")
if productos is not None and ingredientes is not None:
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
		ing = ing_convert(ingredientes.read())
		prod, ing_prod = convert(productos.read())
		st.write("Archivos digeridos exitosamente, corriendo scores")
		
		print("Ingredientes")
		ing_blob.upload_from_string(ing, "text/csv")
		print("Productos")
		prod_blob.upload_from_string(prod, "text/csv")
		print("Ingredientes de Productos")
		prod_ing_blob.upload_from_string(ing_prod, "text/csv")
		
		payload = {
			"prod_data" : prod,
			"prod_ing_data": ing_prod,
			"ing_data": ing
		}
		st.write("about to make request")
		# with open("jsondump.json", "w") as file:
			# json.dump(payload,file)
		# response = requests.post(url= "http://localhost:3000/first_run_bytes", json = payload).content.decode()
		# if not update_run:
		# 	response = requests.get(url = f"http://{base_url}:3000/")
		# else:
		# 	response = requests.get(url = f"http://{base_url}:3000/update")
		# st.text(f"Archivos nuevos guardados en = {response.content.decode()}")
		st.link_button("resultados", "http=//{base_url}:8080")
		st.subheader("EXITO")
