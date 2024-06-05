from io import BytesIO
import pandas as pd




equiv = {'COSING Ref No': 'COSING Ref No',
 'INCI name': 'INCI name',
 'INN name': 'INN name',
 'Ph. Eur. Name': 'Ph. Eur. Name',
 'CAS No': 'CAS No',
 'EC No': 'EC No',
 'NamexCas': 'NamexCas',
 'NamexEC': 'NamexEC',
 'NamexName': 'NamexName',
 'Mix': 'Mix',
 'Anexo.iii.name': 'Anexo.iii.name',
 'Anexo.iii.EC': 'Anexo.iii.EC',
 'Anexo.iii.CAS': 'Anexo.iii.CAS',
 'Chem/IUPAC Name / Description': 'Chem/IUPAC Name / Description',
 'nchar': 'nchar',
 'Synonyms.formatx': 'synonyms',
 '-': '-',
 'Name to Compare "Tool" (Risk databases)': 'actual_name',
 'Restriction': 'Restriction',
 'Function': 'Function',
 'Anexo.iii.Criteria': 'Anexo.iii.Criteria',
 'Info para Reporte': 'info_para_reporte',
 'Update Date': 'Update Date',
 'Observaciones': 'Observaciones',
 'Citas': 'cita',
 'Group.Cancer': 'Group.Cancer',
 'Ref.Cancer': 'Ref.Cancer',
 'Volume.Cancer': 'Volume.Cancer',
 'Year.Cancer': 'Year.Cancer',
 'Add Info.Cancer': 'Add Info.Cancer',
 'Add Info.Dev': 'Add Info.Dev',
 'Ref.Dev': 'Ref.Dev',
 'Group.Endoc': 'Group.Endoc',
 'Ref.Toxicity.Allergies': 'Ref.Toxicity.Allergies',
 'Add Info.Toxicity.Allergies': 'Add Info.Toxicity.Allergies',
 'Add Info.Total/partial use restrictions': 'Add Info.Total/partial use restrictions',
 'Ref.Endoc': 'Ref.Endoc',
 'Ref.Total/partial use restrictions': 'Ref.Total/partial use restrictions',
 'Ref.Env': 'Ref.Env',
 'Add Info.Env': 'Add Info.Env',
 'Cancer.Risk': 'cancer_risk',
 'Development.Risk': 'development_risk',
 'Allergies.Risk': 'allergies_risk',
 'Endocryne.Risk': 'endocryne_risk',
 'Prohibited.Risk': 'prohibited_risk',
 'Env.Risk': 'env_risk',
 'Total.Risk': 'total_risk'}


def convert(bytedata : bytes) -> bytes:
	df = pd.read_excel(BytesIO(bytedata))
	df.rename(columns=equiv, inplace = True)
	# df.to_csv("/home/gonik/Documents/git/goodvibes-org/gv_xml/pre_ingest/bpc_ingredientes_proc.csv")
	df.to_csv("/app/data/db_files/bpc_ingredientes_proc.csv")

	return df.to_string()