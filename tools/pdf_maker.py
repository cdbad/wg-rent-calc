from reportlab.pdfgen import canvas 
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from uuid import uuid1

def make_pdf(table_data: list, name: str, kaltmiete: float):
    file_name = f'output/{str(uuid1())}.pdf' # change to name
    doc_title = f'{name.upper()} costs'
    text_lines = [
        name,
        f'Ganze Kaltmiete: {kaltmiete}',
    ]
    
    pdf = canvas.Canvas(file_name)
    pdf.setTitle(doc_title)
    
    # text
    text = pdf.beginText(40, 800)
    
    for line in text_lines:
        text.textLine(line)
    
    pdf.drawText(text)

    # table
    table = Table(table_data,
                  colWidths=[100] * len(table_data[0]),
                  rowHeights=20)
    
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.transparent),
        ('BACKGROUND', (0, 0), (0, -1), colors. transparent),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (1, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)

    table.wrapOn(pdf, 40, 500)
    table.drawOn(pdf, 40, 500)

    pdf.save()

if __name__ == '__main__':
    make_pdf()
