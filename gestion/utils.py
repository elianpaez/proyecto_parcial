import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

def generar_pdf_alumno(alumno):

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    p.setFont("Helvetica-Bold", 16)
    p.drawString(1 * inch, 10 * inch, "Reporte Oficial del Alumno")

    p.line(1 * inch, 9.8 * inch, 7.5 * inch, 9.8 * inch)

    p.setFont("Helvetica", 12)
    p.drawString(1 * inch, 9.5 * inch, f"Nombre: {alumno.nombre} {alumno.apellido}")
    p.drawString(1 * inch, 9.2 * inch, f"Email de Contacto: {alumno.email}")
    p.drawString(1 * inch, 8.9 * inch, f"Creado por Usuario: {alumno.creado_por.username}")
    p.drawString(1 * inch, 8.6 * inch, f"Nota Promedio: {alumno.nota_promedio}")

    p.setFont("Helvetica-Oblique", 10)
    p.drawString(1 * inch, 1 * inch, "Documento generado automáticamente por el sistema.")

    p.showPage()
    p.save()
    
    pdf_content = buffer.getvalue()
    buffer.close()
    
    return pdf_content