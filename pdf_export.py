from fpdf import FPDF
from datetime import datetime
import os

def teklif_pdf_olustur(icerik, musteri_adi):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Fiyat Teklifi", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Müşteri: {musteri_adi}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='L')
    pdf.ln(10)

    for satir in icerik.split('\n'):
        try:
            pdf.cell(200, 8, txt=satir, ln=True)
        except:
            pdf.cell(200, 8, txt=satir.encode('latin-1', 'replace').decode('latin-1'), ln=True)

    dosya_adi = f"teklif_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(dosya_adi)
    return os.path.abspath(dosya_adi)

def siparis_pdf_olustur(icerik, tedarikci):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Sipariş Formu", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Tedarikçi: {tedarikci}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='L')
    pdf.ln(10)

    for satir in icerik.split('\n'):
        try:
            pdf.cell(200, 8, txt=satir, ln=True)
        except:
            pdf.cell(200, 8, txt=satir.encode('latin-1', 'replace').decode('latin-1'), ln=True)

    dosya_adi = f"siparis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(dosya_adi)
    return os.path.abspath(dosya_adi)
