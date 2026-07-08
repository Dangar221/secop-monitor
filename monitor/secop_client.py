import requests
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.config import API_URL, LIMITE_PROCESOS, ESTADOS_ACTIVOS

def obtener_procesos():
    # Construir filtro de estados con SoQL
    estados_filtro = " OR ".join(
        [f"estado_resumen='{e}'" for e in ESTADOS_ACTIVOS]
    )

    params = {
        "$limit": LIMITE_PROCESOS,
        "$where": estados_filtro,
        "$order": "id_del_proceso DESC",
    }

    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()