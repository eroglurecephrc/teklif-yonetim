import tkinter as tk
from tkinter import ttk, messagebox
from uuid import uuid4

class Uygulama:
    def __init__(self, root):
        self.root = root
        self.root.title("Teklif Yönetim Sistemi")
        self.root.geometry("1000x600")

        self.tab_control = ttk.Notebook(self.root)
        self.tabs = {}

        # Sekmeleri oluştur
        for isim in ["Müşteriler", "Teklifler", "Maliyet", "Sipariş"]:
            sekme = ttk.Frame(self.tab_control)
            self.tab_control.add(sekme, text=isim)
            self.tabs[isim] = sekme

        self.tab_control.pack(expand=1, fill='both')

        # Her sekme için içerik
        self.veri = {
            "Müşteriler": [],
            "Teklifler": [],
            "Maliyet": [],
            "Sipariş": []
        }

        for isim in self.tabs:
            self.ekle_tablo(self.tabs[isim], isim)

    def ekle_tablo(self, sekme, tablo_adi):
        frame = ttk.Frame(sekme)
        frame.pack(fill='both', expand=True, padx=10, pady=10)

        kolonlar = {
            "Müşteriler": ["ID", "Adı", "Telefon", "Adres"],
            "Teklifler": ["ID", "Müşteri", "Konu", "Tutar"],
            "Maliyet": ["ID", "Kalem", "Adet", "Birim", "Toplam"],
            "Sipariş": ["ID", "Tedarikçi", "Ürün", "Adet", "Tutar"]
        }

        self.tree = ttk.Treeview(frame, columns=kolonlar[tablo_adi], show="headings", height=15)
        for col in kolonlar[tablo_adi]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Alt form - giriş alanları
        form_frame = ttk.Frame(sekme)
        form_frame.pack(fill='x', padx=10)

        entries = []
        for col in kolonlar[tablo_adi][1:]:
            ttk.Label(form_frame, text=col).pack(side="left")
            ent = ttk.Entry(form_frame, width=15)
            ent.pack(side="left", padx=5)
            entries.append(ent)

        def ekle():
            veri = [str(uuid4())[:8]] + [e.get() for e in entries]
            self.tree.insert('', 'end', values=veri)
            self.veri[tablo_adi].append(veri)
            for e in entries:
                e.delete(0, tk.END)

        def sil():
            secilen = self.tree.selection()
            for item in secilen:
                self.tree.delete(item)

        def guncelle():
            secilen = self.tree.selection()
            if not secilen:
                return
            yeni = [self.tree.item(secilen[0])['values'][0]] + [e.get() for e in entries]
            self.tree.item(secilen[0], values=yeni)

        btn_frame = ttk.Frame(sekme)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Ekle", command=ekle).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Güncelle", command=guncelle).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Sil", command=sil).pack(side="left", padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = Uygulama(root)
    root.mainloop()
