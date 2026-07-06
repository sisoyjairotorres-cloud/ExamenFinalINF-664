import json
import yaml

with open('datos.json', 'r', encoding='utf-8') as archivo_json:
    datos = json.load(archivo_json)

for clave, valor in datos.items():
    print(f"{clave}: {valor}")

datos_yaml = yaml.dump(datos, allow_unicode=True, default_flow_style=False)
print(datos_yaml)