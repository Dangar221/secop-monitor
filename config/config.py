# API
API_URL = "https://www.datos.gov.co/resource/p6dx-8zbt.json"
LIMITE_PROCESOS = 500

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
    ("transformación digital", 7),
    ("gobierno digital", 7),
    ("automatización", 6),
    ("interoperabilidad", 5),
    ("expediente electrónico", 5),
    ("gestión documental", 4),
    ("software", 5),
    ("desarrollo web", 5),
    ("aplicación web", 5),
    ("ciberseguridad", 5),
    ("plataforma digital", 5),
    ("analítica de datos", 6),
    ("ciencia de datos", 6),
    ("big data", 5),
    ("tecnología", 3),
    ("tecnologia", 3),
    ("sistemas de información", 3),
    ("infraestructura tecnológica", 3),
    ("soporte técnico", 2),
]

# Email
EMAIL_DESTINATARIOS = ["secop@estadox.com"]
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587