import requests
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from filters.keywords import KEYWORDS, es_relevante
from database.tracker import inicializar, filtrar_nuevos, marcar_todos_vistos

BASE_URL = "https://www.datos.gov.co/resource/p6dx-8zbt.json"

def obtener_procesos(limit=200):
    params = {
        "$limit": limit,
        "$order": "id_del_proceso DESC",
    }
    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def correr_monitor():
    inicializar()

    print("Consultando SECOP II...")
    procesos = obtener_procesos()
    print(f"Obtenidos  : {len(procesos)}")

    relevantes = [p for p in procesos if es_relevante(p)]
    print(f"Relevantes : {len(relevantes)}")

    nuevos = filtrar_nuevos(relevantes)
    print(f"Nuevos     : {len(nuevos)}")

    if not nuevos:
        print("\nSin procesos nuevos.")
        return

    print("\n=== PROCESOS NUEVOS ===")
    for p in nuevos:
        print("---")
        print("Entidad:", p.get("entidad"))
        print("Desc   :", p.get("descripci_n_del_procedimiento", "")[:120])
        print("Valor  :", p.get("precio_base"))
        print("URL    :", p.get("urlproceso", {}).get("url"))

    marcar_todos_vistos(nuevos)
    print(f"\n✓ {len(nuevos)} procesos marcados como vistos.")


if __name__ == "__main__":
    correr_monitor()