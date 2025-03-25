
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
    page_title="Home",
    page_icon="👋",
)

st.title(
	"GV XML Score Calculator"
)
st.sidebar.success("Seleccionar la base de datos a procesar")
