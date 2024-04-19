import json

ruta_archivo = '/home/devasc/labs/devnet-src/parsing/myfile.json'

with open(ruta_archivo, 'r') as ourjson:
	json_file=json.load(ourjson)
print(json_file)
