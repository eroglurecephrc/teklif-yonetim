import sqlite3
from datetime import datetime

class Veritabani:
    def __init__(self):
        self.baglanti = sqlite3.connect("veritabani.db")
        self.imlec = self.baglanti.cursor()
        self.tablo_olustur()

    def tablo_olustur(self):
        self.imlec.execute("""
            CREATE TABLE IF NOT EXISTS musteriler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad TEXT NOT NULL,
                tarih TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.baglanti.commit()

    def musteri_ekle(self, ad):
        self.imlec.execute("INSERT INTO musteriler (ad, tarih) VALUES (?, ?)", (ad, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.baglanti.commit()

    def musteri_guncelle(self, musteri_id, yeni_ad):
        self.imlec.execute("UPDATE musteriler SET ad=? WHERE id=?", (yeni_ad, musteri_id))
        self.baglanti.commit()

    def musteri_sil(self, musteri_id):
        self.imlec.execute("DELETE FROM musteriler WHERE id=?", (musteri_id,))
        self.baglanti.commit()

    def musteri_listele(self):
        self.imlec.execute("SELECT id, ad FROM musteriler ORDER BY tarih DESC")
        return self.imlec.fetchall()

    def kapat(self):
        self.baglanti.close()
