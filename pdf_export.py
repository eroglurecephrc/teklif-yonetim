from fpdf import FPDF
import os
from datetime import datetime

def teklif_pdf_olustur(teklif_icerik, musteri_adi):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="TEKLİF FORMU", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Müşteri: {musteri_adi}", ln=2, align="L")
    pdf.ln(10)

    for satir in teklif_icerik.split("\n"):
        pdf.cell(200, 8, txt=satir.encode('latin-1', 'replace').decode('latin-1'), ln=1)

    klasor = "pdfler"
    os.makedirs(klasor, exist_ok=True)
    dosya_adi = os.path.join(klasor, f"teklif_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
    pdf.output(dosya_adi)
    return dosya_adi

def siparis_pdf_olustur(siparis_icerik, tedarikci_adi):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="SİPARİŞ FORMU", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Tedarikçi: {tedarikci_adi}", ln=2, align="L")
    pdf.ln(10)

    for satir in siparis_icerik.split("\n"):
        pdf.cell(200, 8, txt=satir.encode('latin-1', 'replace').decode('latin-1'), ln=1)

    klasor = "pdfler"
    os.makedirs(klasor, exist_ok=True)
    dosya_adi = os.path.join(klasor, f"siparis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
    pdf.output(dosya_adi)
    return dosya_adi
