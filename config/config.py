# API
API_URL = "https://www.datos.gov.co/resource/p6dx-8zbt.json"
LIMITE_PROCESOS = 500
DIAS_HACIA_ATRAS = 3

# Filtros
ESTADOS_ACTIVOS = [
    "Presentación de oferta",
    "Fase de ofertas",
    "Presentación de observaciones",
]

KEYWORDS = [
    ("inteligencia artificial", 10),
    ("machine learning", 10),
    ("aprendizaje automático", 10),
    ("modelo de lenguaje", 10),
    ("llm", 10),
    ("ia generativa", 10),
    ("deep learning", 10),
    ("interoperabilidad", 8),
    ("transformación digital", 8),
    ("gobierno digital", 8),
    ("govtech", 8),
    ("automatización", 6),
    ("analítica de datos", 6),
    ("ciencia de datos", 6),
    ("expediente electrónico", 5),
    ("desarrollo web", 5),
    ("aplicación web", 5),
    ("ciberseguridad", 5),
    ("plataforma digital", 5),
    ("big data", 5),
    ("gestión documental", 4),
    ("software", 4),
    ("tecnología", 2),
    ("tecnologia", 2),
    ("sistemas de información", 2),
    ("infraestructura tecnológica", 2),
    ("soporte técnico", 2),
]

# Email
EMAIL_DESTINATARIOS = ["dannav@estadox.com"]
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587