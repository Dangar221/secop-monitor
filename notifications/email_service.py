import os
import smtplib
import sys
from datetime import date, datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.config import SMTP_HOST, SMTP_PORT

COLOR_PRIORIDAD = {
    "MUY ALTA": "#c0392b",
    "ALTA": "#e67e22",
    "MEDIA": "#b7950b",
    "BAJA": "#7f8c8d",
}


def _formatear_cierre(proceso):
    crudo = proceso.get("fecha_de_recepcion_de")
    if not crudo:
        return "Sin fecha", "#999", False

    fecha = datetime.fromisoformat(crudo.replace("Z", "+00:00")).date()
    dias_restantes = (fecha - date.today()).days
    texto = fecha.strftime("%d/%m/%Y")

    if dias_restantes < 0:
        return texto, "#999", False
    if dias_restantes <= 3:
        return texto, "#c0392b", True
    if dias_restantes <= 7:
        return texto, "#e67e22", False
    return texto, "#222", False


def _fila_html(resultado):
    proceso = resultado["proceso"]
    color = COLOR_PRIORIDAD.get(resultado["prioridad"], "#333")
    valor = int(proceso.get("precio_base") or 0)
    url = (proceso.get("urlproceso") or {}).get("url", "#")
    descripcion = (proceso.get("descripci_n_del_procedimiento") or "")[:150]
    cierre_texto, cierre_color, urgente = _formatear_cierre(proceso)
    cierre_html = f"{cierre_texto} ⚠" if urgente else cierre_texto

    return f"""
    <tr>
        <td style="padding:8px;border-bottom:1px solid #ddd;font-weight:bold;color:{color};white-space:nowrap;">{resultado['prioridad']}</td>
        <td style="padding:8px;border-bottom:1px solid #ddd;">{proceso.get('entidad', '')}</td>
        <td style="padding:8px;border-bottom:1px solid #ddd;">{descripcion}</td>
        <td style="padding:8px;border-bottom:1px solid #ddd;">{', '.join(resultado['coincidencias'])}</td>
        <td style="padding:8px;border-bottom:1px solid #ddd;white-space:nowrap;">${valor:,}</td>
        <td style="padding:8px;border-bottom:1px solid #ddd;font-weight:bold;color:{cierre_color};white-space:nowrap;">{cierre_html}</td>
        <td style="padding:8px;border-bottom:1px solid #ddd;"><a href="{url}">Ver proceso</a></td>
    </tr>"""


def construir_html(nuevos_con_puntaje):
    filas = "".join(_fila_html(r) for r in nuevos_con_puntaje)
    hoy = date.today().strftime("%d/%m/%Y")

    return f"""
    <html>
    <body style="font-family:Arial,Helvetica,sans-serif;color:#222;">
        <h2>SECOP II &mdash; {len(nuevos_con_puntaje)} procesos nuevos ({hoy})</h2>
        <table style="border-collapse:collapse;width:100%;font-size:14px;">
            <tr style="background:#2c3e50;color:white;text-align:left;">
                <th style="padding:8px;">Prioridad</th>
                <th style="padding:8px;">Entidad</th>
                <th style="padding:8px;">Descripci&oacute;n</th>
                <th style="padding:8px;">Coincidencias</th>
                <th style="padding:8px;">Valor</th>
                <th style="padding:8px;">Fecha l&iacute;mite</th>
                <th style="padding:8px;">Enlace</th>
            </tr>
            {filas}
        </table>
    </body>
    </html>
    """


def enviar_alerta(nuevos_con_puntaje, destinatarios):
    remitente = os.environ.get("EMAIL_USER")
    app_password = os.environ.get("EMAIL_APP_PASSWORD")

    if not remitente or not app_password:
        raise RuntimeError(
            "Faltan credenciales de correo: define EMAIL_USER y EMAIL_APP_PASSWORD como variables de entorno."
        )

    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = f"SECOP II: {len(nuevos_con_puntaje)} procesos nuevos - {date.today().strftime('%d/%m/%Y')}"
    mensaje["From"] = remitente
    mensaje["To"] = ", ".join(destinatarios)
    mensaje.attach(MIMEText(construir_html(nuevos_con_puntaje), "html"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(remitente, app_password)
        server.sendmail(remitente, destinatarios, mensaje.as_string())
