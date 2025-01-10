import streamlit as st
from productos import convert
import datetime
from ingredientes import convert as ing_convert
from dotenv import load_dotenv
import shutil
import subprocess
import requests
import streamlit as st
import pandas as pd
from google.cloud import storage
import os
st.set_page_config(
    page_title="BPC",
    page_icon="👋",
)
st.title(
	"GV XML Score Calculator"
)
st.session_state["sheet_ingredientes"] = "Ingredientes_Formatted_V1"
st.session_state["sheet_productos"] = "Productos"
load_dotenv(".env")

base_url = os.environ.get("REQUEST_URL")
productos = st.file_uploader("Base de datos de Productos")
if productos:
    st.write("Hoja por defecto `Productos`")
    change_sheet = st.button("Modificar", key="productos")
    if change_sheet:
        st.session_state.sheet_productos = st.text_input("Nombre de hoja")
        st.write(st.session_state.sheet_productos)
ingredientes = st.file_uploader("Base de datos de Ingredientes")
if ingredientes:
    st.write("Hoja por defecto `Ingredientes_Formatted_V1`")
    change_sheet_ing = st.button("Modificar", key = "ing")
    if change_sheet_ing:
        st.session_state.sheet_ingredientes = st.text_input("Nombre de hoja" )
        st.write(st.session_state.sheet_ingredientes)
if productos is not None and ingredientes is not None:
	with open(productos.name, "wb") as file:
		file.write(productos.getbuffer())
	with open(ingredientes.name, "wb") as file:
		file.write(ingredientes.getbuffer())
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
		try:
			sp = subprocess.check_output(["./excel-to-csv", f"{productos.name}", "-i", f"{ingredientes.name}" ,"-x",f"{st.session_state.sheet_productos}","-y",f"{st.session_state.sheet_ingredientes}", "home"], stderr=subprocess.STDOUT)
		except subprocess.CalledProcessError as err:
			st.write( err.stdout.decode("utf-8") )
		except Exception as e:
			st.write(e)
	
		shutil.copy("bpc_ingredientes_proc.csv", "data/db_files/bpc_ingredientes_proc.csv")
		shutil.copy("home_productos_proc.csv", "data/db_files/home_productos_proc.csv")
		shutil.copy("bpc_productos_proc_ingredientes.csv", "data/db_files/bpc_productos_proc_ingredientes.csv")
	
		st.write("Archivos digeridos exitosamente, corriendo scores")
		st.write("about to make request")

		if not update_run:
			response = requests.get(url = f"http://calculator:3000/solares")
			st.write("request made")
		else:
			response = requests.get(url = f"http://{base_url}:3000/update")
		file_location = response.content.decode()
		path = file_location.split("/data/share")[1]

		st.text(f"Archivos nuevos guardados en = {path}")
		st.link_button("resultados", f"https://xmls.goodvibes.work.gd/filebrowser/files{path}")
		st.subheader("EXITO")
