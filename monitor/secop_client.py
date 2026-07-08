import requests
from pprint import pprint

BASE_URL = "https://www.datos.gov.co/resource/p6dx-8zbt.json"

def obtener_procesos(limit=5):
    params = {
        "$limit": limit,
        "$order": "fecha_de_publicacion_del DESC",
    }
    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    procesos = obtener_procesos(limit=5)
    
    print("=== COLUMNAS DEL DATASET ===")
    for key in procesos[0].keys():
        print(key)
    
    print("\n=== PRIMER REGISTRO COMPLETO ===")
    pprint(procesos[0])