import tkinter as tk
from tkinter import ttk, messagebox
from veritabani import *
from pdf_export import teklif_pdf_olustur, siparis_pdf_olustur

class TeklifYonetimApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teklif Yönetim Sistemi")
        self.root.geometry("1000x600")

        self.tab_control = ttk.Notebook(self.root)

        self.tab_musteri = ttk.Frame(self.tab_control)
        self.tab_teklif = ttk.Frame(self.tab_control)
        self.tab_siparis = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_musteri, text="Müşteri Listesi")
        self.tab_control.add(self.tab_teklif, text="Teklif Şablonu")
        self.tab_control.add(self.tab_siparis, text="Sipariş Listesi")

        self.tab_control.pack(expand=1, fill='both')

        self.ekle_musteri_tab()
        self.ekle_teklif_tab()
        self.ekle_siparis_tab()

    # ---------------- Müşteri TAB --------------------
    def ekle_musteri_tab(self):
        frm = ttk.Frame(self.tab_musteri)
        frm.pack(pady=10)

        ttk.Label(frm, text="Ad Soyad").grid(row=0, column=0)
        ttk.Label(frm, text="Telefon").grid(row=0, column=1)
        ttk.Label(frm, text="Adres").grid(row=0, column=2)

        self.entry_ad = ttk.Entry(frm)
        self.entry_tel = ttk.Entry(frm)
        self.entry_adres = ttk.Entry(frm, width=50)

        self.entry_ad.grid(row=1, column=0, padx=5)
        self.entry_tel.grid(row=1, column=1, padx=5)
        self.entry_adres.grid(row=1, column=2, padx=5)

        ttk.Button(frm, text="Kaydet", command=self.musteri_kaydet).grid(row=1, column=3, padx=10)

        self.liste_musteri = ttk.Treeview(self.tab_musteri, columns=("ad", "telefon", "adres"), show="headings")
        self.liste_musteri.heading("ad", text="Ad Soyad")
        self.liste_musteri.heading("telefon", text="Telefon")
        self.liste_musteri.heading("adres", text="Adres")
        self.liste_musteri.pack(pady=20, fill='x')

        self.musteri_listele()

    def musteri_kaydet(self):
        ad = self.entry_ad.get()
        tel = self.entry_tel.get()
        adres = self.entry_adres.get()
        if ad:
            musteri_ekle(ad, tel, adres)
            self.entry_ad.delete(0, tk.END)
            self.entry_tel.delete(0, tk.END)
            self.entry_adres.delete(0, tk.END)
            self.musteri_listele()

    def musteri_listele(self):
        for i in self.liste_musteri.get_children():
            self.liste_musteri.delete(i)
        veriler = musterileri_getir()
        for v in veriler:
            self.liste_musteri.insert("", "end", values=v)

    # ---------------- Teklif TAB --------------------
    def ekle_teklif_tab(self):
        ttk.Label(self.tab_teklif, text="Teklif Metni").pack()
        self.teklif_text = tk.Text(self.tab_teklif, height=20)
        self.teklif_text.pack(fill='both', expand=True)

        ttk.Button(self.tab_teklif, text="PDF Olarak Kaydet", command=self.teklif_kaydet).pack(pady=10)

    def teklif_kaydet(self):
        icerik = self.teklif_text.get("1.0", tk.END).strip()
        if icerik:
            dosya = teklif_pdf_olustur(icerik)
            messagebox.showinfo("PDF", f"PDF oluşturuldu:\n{dosya}")

    # ---------------- Sipariş TAB --------------------
    def ekle_siparis_tab(self):
        ttk.Label(self.tab_siparis, text="Sipariş İçeriği").pack()
        self.siparis_text = tk.Text(self.tab_siparis, height=15)
        self.siparis_text.pack(fill='both', expand=True)

        ttk.Button(self.tab_siparis, text="PDF Olarak Kaydet", command=self.siparis_kaydet).pack(pady=10)

    def siparis_kaydet(self):
        icerik = self.siparis_text.get("1.0", tk.END).strip()
        if icerik:
            dosya = siparis_pdf_olustur(icerik)
            messagebox.showinfo("PDF", f"Sipariş PDF oluşturuldu:\n{dosya}")

# ---- ÇALIŞTIR ----
if __name__ == "__main__":
    from veritabani import veritabani_olustur
    veritabani_olustur()
    root = tk.Tk()
    app = TeklifYonetimApp(root)
    root.mainloop()
