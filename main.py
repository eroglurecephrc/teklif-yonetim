import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from utils.pdf_export import teklif_pdf_olustur, siparis_pdf_olustur
from utils.tcmb_kur import get_tcmb_kurlar
from veritabani import tablo_olustur, musteri_ekle, musteri_listele, musteri_sil, musteri_guncelle

class TeklifUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Teklif ve Sipariş Yönetimi")
        self.root.geometry("1000x600")

        # Veritabanı tablolarını oluştur
        tablo_olustur()

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
        frame = ttk.LabelFrame(self.tab_musteri, text="Yeni Müşteri Ekle")
        frame.pack(padx=10, pady=10, fill='x')

        ttk.Label(frame, text="Adı:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_ad = ttk.Entry(frame, width=30)
        self.entry_ad.grid(row=0, column=1)

        ttk.Label(frame, text="Telefon:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_telefon = ttk.Entry(frame, width=30)
        self.entry_telefon.grid(row=1, column=1)

        ttk.Label(frame, text="Adres:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_adres = ttk.Entry(frame, width=30)
        self.entry_adres.grid(row=2, column=1)

        ttk.Button(frame, text="Ekle", command=self.musteri_kaydet).grid(row=3, column=0, pady=10)
        ttk.Button(frame, text="Güncelle", command=self.musteri_guncelle).grid(row=3, column=1, pady=10)
        ttk.Button(frame, text="Sil", command=self.musteri_sil).grid(row=3, column=2, pady=10)

        self.tree_musteri = ttk.Treeview(self.tab_musteri, columns=("ID", "Ad", "Telefon", "Adres"), show="headings")
        self.tree_musteri.heading("ID", text="ID")
        self.tree_musteri.heading("Ad", text="Ad")
        self.tree_musteri.heading("Telefon", text="Telefon")
        self.tree_musteri.heading("Adres", text="Adres")
        self.tree_musteri.pack(fill='both', expand=True, padx=10, pady=10)
        self.tree_musteri.bind("<<TreeviewSelect>>", self.musteri_secildi)

        self.musterileri_yukle()

    def musteri_kaydet(self):
        ad = self.entry_ad.get().strip()
        telefon = self.entry_telefon.get().strip()
        adres = self.entry_adres.get().strip()

        if not ad:
            messagebox.showwarning("Eksik Bilgi", "Müşteri adı zorunludur.")
            return

        musteri_ekle(ad, telefon, adres)
        self.musterileri_yukle()
        self.temizle_giris()

    def musteri_guncelle(self):
        secim = self.tree_musteri.selection()
        if not secim:
            messagebox.showwarning("Seçim Yok", "Lütfen bir müşteri seçin.")
            return

        id = self.tree_musteri.item(secim)["values"][0]
        yeni_ad = self.entry_ad.get()
        yeni_tel = self.entry_telefon.get()
        yeni_adr = self.entry_adres.get()
        musteri_guncelle(id, yeni_ad, yeni_tel, yeni_adr)
        self.musterileri_yukle()
        self.temizle_giris()

    def musteri_sil(self):
        secim = self.tree_musteri.selection()
        if not secim:
            messagebox.showwarning("Seçim Yok", "Lütfen bir müşteri seçin.")
            return

        id = self.tree_musteri.item(secim)["values"][0]
        musteri_sil(id)
        self.musterileri_yukle()
        self.temizle_giris()

    def musteri_secildi(self, event):
        secim = self.tree_musteri.selection()
        if not secim:
            return
        secilen = self.tree_musteri.item(secim)["values"]
        self.entry_ad.delete(0, tk.END)
        self.entry_ad.insert(0, secilen[1])
        self.entry_telefon.delete(0, tk.END)
        self.entry_telefon.insert(0, secilen[2])
        self.entry_adres.delete(0, tk.END)
        self.entry_adres.insert(0, secilen[3])

    def musterileri_yukle(self):
        for i in self.tree_musteri.get_children():
            self.t
