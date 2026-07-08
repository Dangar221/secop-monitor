KEYWORDS = [
    # IA
    "inteligencia artificial",
    "machine learning",
    "aprendizaje automático",
    "modelo de lenguaje",
    "llm",
    "ia generativa",
    "deep learning",
    # Transformación digital
    "transformación digital",
    "gobierno digital",
    "interoperabilidad",
    "automatización",
    "expediente electrónico",
    "gestión documental",
    # Software y desarrollo
    "software",
    "plataforma digital",
    "desarrollo web",
    "aplicación web",
    "ciberseguridad",
    # Datos
    "analítica de datos",
    "ciencia de datos",
    "big data",
    # Tecnología general
    "tecnología",
    "tecnologia",
    "sistemas de información",
    "infraestructura tecnológica",
]


def es_relevante(proceso):
    texto = " ".join([
        proceso.get("nombre_del_procedimiento", ""),
        proceso.get("descripci_n_del_procedimiento", ""),
    ]).lower()

    for keyword in KEYWORDS:
        if keyword in texto:
            return True
    return False