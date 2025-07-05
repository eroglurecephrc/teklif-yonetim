import sqlite3
from datetime import datetime

class Veritabani:
    def __init__(self, db_adi="veriler.db"):
        self.conn = sqlite3.connect(db_adi)
        self.cursor = self.conn.cursor()
        self.tablolari_olustur()

    def tablolari_olustur(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS musteriler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS teklifler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                musteri_id INTEGER,
                icerik TEXT,
                tarih TEXT,
                FOREIGN KEY (musteri_id) REFERENCES musteriler(id)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS siparisler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tedarikci TEXT,
                icerik TEXT,
                tarih TEXT
            )
        """)
        self.conn.commit()

    def musteri_ekle(self, ad):
        self.cursor.execute("INSERT INTO musteriler (ad) VALUES (?)", (ad,))
        self.conn.commit()

    def musteri_listele(self):
        self.cursor.execute("SELECT id, ad FROM musteriler")
        return self.cursor.fetchall()

    def musteri_guncelle(self, musteri_id, yeni_ad):
        self.cursor.execute("UPDATE musteriler SET ad = ? WHERE id = ?", (yeni_ad, musteri_id))
        self.conn.commit()

    def teklif_ekle(self, musteri_id, icerik):
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO teklifler (musteri_id, icerik, tarih) VALUES (?, ?, ?)", (musteri_id, icerik, tarih))
        self.conn.commit()

    def siparis_ekle(self, tedarikci, icerik):
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("INSERT INTO siparisler (tedarikci, icerik, tarih) VALUES (?, ?, ?)", (tedarikci, icerik, tarih))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
