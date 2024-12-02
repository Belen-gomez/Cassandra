import json
import re
from datetime import datetime

# Ruta del archivo JSON original
input_file = "archivo_corregido2.json"
output_file = "sample_limpio.json"

# Función para limpiar y transformar fechas
def clean_date(date_str, pattern_in, pattern_out):
    try:
        return datetime.strptime(date_str, pattern_in).strftime(pattern_out)
    except ValueError:
        return None


# Carga y transforma el JSON
with open(input_file, "r") as file:
    data = json.load(file)

for record in data:
    # Transformar fechas simples
    if "dump date" in record:
        record["dump date"] = clean_date(record["dump date"], "%d/%m/%y", "%Y-%m-%d")
    
    # Transformar fechas complejas en "vehicle"
    if "vehicle" in record:
        if "roadworthiness" in record["vehicle"]:
            roadworthiness = record["vehicle"]["roadworthiness"]
            if isinstance(roadworthiness, list):
                # Si es una lista, transformar cada elemento
                for item in roadworthiness:
                    if "MOT date" in item:
                        item["MOT date"] = clean_date(item["MOT date"], "%d/%m/%Y", "%Y-%m-%d")
            elif isinstance(roadworthiness, str):
                # Si es una fecha en formato string, transformarla directamente
                record["vehicle"]["roadworthiness"] = clean_date(record["vehicle"]["roadworthiness"], "%d/%m/%Y", "%Y-%m-%d")
    
    # Transformar fechas en "Record"
    if "Record" in record:
        if "date" in record["Record"]:  
            record["Record"]["date"] = clean_date(record["Record"]["date"], "%d/%m/%Y", "%Y-%m-%d")
    
    # Transformar fechas en "Speed ticket"
    if "Speed ticket" in record:
        if "Issue date" in record["Speed ticket"]:
            record["Speed ticket"]["Issue date"] = clean_date(record["Speed ticket"]["Issue date"], "%d/%m/%Y", "%Y-%m-%d")
        if "Pay date" in record["Speed ticket"]:
            record["Speed ticket"]["Pay date"] = clean_date(record["Speed ticket"]["Pay date"], "%d/%m/%Y", "%Y-%m-%d")
    record["vehicle"]["Owner"]["Birthdate"] = clean_date(record["vehicle"]["Owner"]["Birthdate"], "%d/%m/%Y", "%Y-%m-%d")
    record["vehicle"]["Driver"]["Birthdate"] = clean_date(record["vehicle"]["Driver"]["Birthdate"], "%d/%m/%Y", "%Y-%m-%d")
    record["vehicle"]["Driver"]["driving license"]["date"] = clean_date(record["vehicle"]["Driver"]["driving license"]["date"], "%d/%m/%Y", "%Y-%m-%d")
    if "Speed ticket" in record:
        record["Speed ticket"]["Debtor"]["Birthdate"] = clean_date(record["Speed ticket"]["Debtor"]["Birthdate"], "%d/%m/%Y", "%Y-%m-%d")
    if "Stretch ticket" in record:
        record["Stretch ticket"]["Debtor"]["Birthdate"] = clean_date(record["Stretch ticket"]["Debtor"]["Birthdate"], "%d/%m/%Y", "%Y-%m-%d")
        record["Stretch ticket"]["previous rec"]["date"] = clean_date(record["Stretch ticket"]["previous rec"]["date"], "%d/%m/%Y", "%Y-%m-%d")
    if "Clearance ticket" in record:
        record["Clearance ticket"]["Debtor"]["Birthdate"] = clean_date(record["Clearance ticket"]["Debtor"]["Birthdate"], "%d/%m/%Y", "%Y-%m-%d")
        record["Clearance ticket"]["previous car"]["date"] = clean_date(record["Clearance ticket"]["previous car"]["date"], "%d/%m/%Y", "%Y-%m-%d")

        
   

# Guardar el JSON limpio
with open(output_file, "w") as file:
    json.dump(data, file, indent=4)

print(f"Archivo transformado guardado en {output_file}")
