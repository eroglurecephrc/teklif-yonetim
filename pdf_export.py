from fpdf import FPDF
from datetime import datetime
import os

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "TEKLİF / SİPARİŞ BELGESİ", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Sayfa {self.page_no()}", align="C")

def teklif_pdf_olustur(teklif_metin, musteri_adi):
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M")
    dosya_adi = f"Teklif_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    pdf.cell(0, 10, f"Müşteri: {musteri_adi}", ln=True)
    pdf.cell(0, 10, f"Tarih: {tarih}", ln=True)
    pdf.ln(10)
    pdf.multi_cell(0, 10, teklif_metin)

    pdf.output(dosya_adi)
    return dosya_adi

def siparis_pdf_olustur(siparis_metin, tedarikci_adi):
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M")
    dosya_adi = f"Siparis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=11)

    pdf.cell(0, 10, f"Tedarikçi: {tedarikci_adi}", ln=True)
    pdf.cell(0, 10, f"Tarih: {tarih}", ln=True)
    pdf.ln(10)
    pdf.multi_cell(0, 10, siparis_metin)

    pdf.output(dosya_adi)
    return dosya_adi
