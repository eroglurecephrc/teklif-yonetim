import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from utils.pdf_export import teklif_pdf_olustur, siparis_pdf_olustur
from utils.tcmb_kur import get_tcmb_kurlar
from veritabani import Veritabani

class TeklifUygulamasi:
    def __init__(self, root):
        self.db = Veritabani()
        self.root = root
        self.root.title("Teklif ve Sipariş Yönetimi")
        self.root.geometry("1000x600")

        self.tab_control = ttk.Notebook(self.root)
        self.tab_musteri = ttk.Frame(self.tab_control)
        self.tab_teklif = ttk.Frame(self.tab_control)
        self.tab_siparis = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_musteri, text='Müşteri Kartları')
        self.tab_control.add(self.tab_teklif, text='Teklif Oluştur')
        self.tab_control.add(self.tab_siparis, text='Sipariş Formu')
        self.tab_control.pack(expand=1, fill='both')

        self.ekle_musteri_tab()
        self.ekle_teklif_tab()
        self.ekle_siparis_tab()

    def ekle_musteri_tab(self):
        frame = ttk.Frame(self.tab_musteri)
        frame.pack(pady=10)

        ttk.Label(frame, text="Müşteri Adı:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_musteri = ttk.Entry(frame, width=40)
        self.entry_musteri.grid(row=0, column=1)
        ttk.Button(frame, text="Kaydet", command=self.musteri_kaydet).grid(row=0, column=2, padx=10)

        self.musteri_tree = ttk.Treeview(self.tab_musteri, columns=("id", "ad"), show="headings")
        self.musteri_tree.heading("id", text="ID")
        self.musteri_tree.heading("ad", text="Müşteri Adı")
        self.musteri_tree.pack(fill="both", expand=True)
        self.musteri_tree.bind("<Double-1>", self.musteri_duzenle)

        self.musteri_yenile()

    def musteri_kaydet(self):
        ad = self.entry_musteri.get()
        if ad:
            self.db.musteri_ekle(ad)
            self.musteri_yenile()
            self.entry_musteri.delete(0, tk.END)

    def musteri_yenile(self):
        for row in self.musteri_tree.get_children():
            self.musteri_tree.delete(row)
        for musteri in self.db.musteri_listele():
            self.musteri_tree.insert("", "end", values=musteri)

    def musteri_duzenle(self, event):
        secilen = self.musteri_tree.selection()
        if not secilen:
            return
        item = self.musteri_tree.item(secilen)
        musteri_id, musteri_ad = item['values']

        yeni_ad = tk.simpledialog.askstring("Düzenle", "Yeni müşteri adı:", initialvalue=musteri_ad)
        if yeni_ad:
            self.db.musteri_guncelle(musteri_id, yeni_ad)
            self.musteri_yenile()

    def ekle_teklif_tab(self):
        ttk.Label(self.tab_teklif, text="Teklif Kalemleri (örnek)").pack(pady=5)
        self.text_teklif = tk.Text(self.tab_teklif, height=15)
        self.text_teklif.pack()
        ttk.Button(self.tab_teklif, text="PDF Kaydet", command=self.teklif_kaydet).pack(pady=10)

    def ekle_siparis_tab(self):
        ttk.Label(self.tab_siparis, text="Tedarikçi Adı:").pack(pady=5)
        self.entry_tedarikci = ttk.Entry(self.tab_siparis, width=40)
        self.entry_tedarikci.pack()
        ttk.Label(self.tab_siparis, text="Malzeme / Ölçü / Adet").pack(pady=5)
        self.text_siparis = tk.Text(self.tab_siparis, height=10)
        self.text_siparis.pack()
        ttk.Button(self.tab_siparis, text="Siparişi PDF Kaydet", command=self.siparis_kaydet).pack(pady=10)

    def teklif_kaydet(self):
        teklif = self.text_teklif.get("1.0", tk.END).strip()
        musteri_adi = self.entry_musteri.get() or "Musteri"
        dosya_adi = teklif_pdf_olustur(teklif, musteri_adi)
        messagebox.showinfo("Teklif", f"PDF olarak kaydedildi:\n{dosya_adi}")

    def siparis_kaydet(self):
        siparis = self.text_siparis.get("1.0", tk.END).strip()
        tedarikci = self.entry_tedarikci.get() or "Tedarikci"
        dosya_adi = siparis_pdf_olustur(siparis, tedarikci)
        messagebox.showinfo("Sipariş", f"PDF olarak kaydedildi:\n{dosya_adi}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TeklifUygulamasi(root)
    root.mainloop()
