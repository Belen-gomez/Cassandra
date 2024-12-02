import json

# Función para corregir el formato del archivo JSON
def corregir_json_malformado(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as file:
        # Leemos el contenido del archivo
        content = file.read()

    # Aquí asumimos que los objetos están mal formados y los vamos a corregir
    # Reemplazamos el final de un objeto con la falta de coma entre objetos
    # Esto reemplaza los '}{' por '},{' para insertar las comas
    content_corregido = content.replace("} ", '},')

    # Intentamos cargar el contenido corregido para asegurarnos que es un JSON válido
    try:
        # Intentamos cargar el JSON
        json_data = json.loads(f'[{content_corregido}]')  # Convertimos a lista para validarlo
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el archivo JSON: {e}")
        return
    
    # Guardamos el archivo JSON corregido
    with open(archivo_salida, 'w') as file:
        # Volcamos el JSON corregido con una buena indentación
        json.dump(json_data, file, indent=4)

    print(f"El archivo JSON ha sido corregido y guardado como '{archivo_salida}'")

# Llamada a la función con los nombres de los archivos
corregir_json_malformado('sample.json', 'archivo_corregido2.json')
