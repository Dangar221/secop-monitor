import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from monitor.secop_client import obtener_procesos
from filters.keywords import filtrar_y_ordenar
from database.tracker import inicializar, filtrar_nuevos, marcar_todos_vistos


def correr_monitor():
    inicializar()

    print("Consultando SECOP II...")
    procesos = obtener_procesos()
    print(f"Obtenidos  : {len(procesos)}")

    relevantes = filtrar_y_ordenar(procesos)
    print(f"Relevantes : {len(relevantes)}")

    nuevos = filtrar_nuevos([r["proceso"] for r in relevantes])
    print(f"Nuevos     : {len(nuevos)}")

    if not nuevos:
        print("\nSin procesos nuevos.")
        return

    ids_nuevos = {p.get("id_del_proceso") for p in nuevos}
    nuevos_con_puntaje = [r for r in relevantes if r["proceso"].get("id_del_proceso") in ids_nuevos]

    print("\n=== PROCESOS NUEVOS ===")
    for r in nuevos_con_puntaje:
        p = r["proceso"]
        print("---")
        print(f"Prioridad     : {r['prioridad']}")
        print(f"Coincidencias : {', '.join(r['coincidencias'])}")
        print(f"Entidad       : {p.get('entidad')}")
        print(f"Estado        : {p.get('estado_resumen')}")
        print(f"Desc          : {p.get('descripci_n_del_procedimiento', '')[:120]}")
        print(f"Valor         : ${int(p.get('precio_base', 0)):,}")
        print(f"URL           : {p.get('urlproceso', {}).get('url')}")

    marcar_todos_vistos(nuevos)
    print(f"\n{len(nuevos)} procesos marcados como vistos.")


if __name__ == "__main__":
    correr_monitor()