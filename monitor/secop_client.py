import requests
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.config import API_URL, LIMITE_PROCESOS, ESTADOS_ACTIVOS

def obtener_procesos():
    # Construir filtro de estados con SoQL
    estados_filtro = " OR ".join(
        [f"estado_resumen='{e}'" for e in ESTADOS_ACTIVOS]
    )

    # id_del_proceso se ordena como texto, no como número: un ID de 8 dígitos
    # ("10347391") queda por detrás de uno de 7 ("9999999") al ordenar DESC,
    # así que nunca se veían los procesos realmente recientes. Se ordena por
    # fecha de publicación real en su lugar, excluyendo nulos (si no, Postgres
    # pone los nulos primero en un ORDER BY ... DESC).
    where = f"({estados_filtro}) AND fecha_de_publicacion_del IS NOT NULL"

    params = {
        "$limit": LIMITE_PROCESOS,
        "$where": where,
        "$order": "fecha_de_publicacion_del DESC",
    }

    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()