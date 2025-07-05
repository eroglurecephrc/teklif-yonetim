import sqlite3

class Veritabani:
    def __init__(self, db_adi="veritabani.db"):
        self.conn = sqlite3.connect(db_adi)
        self.cursor = self.conn.cursor()
        self.tablolari_olustur()

    def tabloları_var_mi(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return self.cursor.fetchall()

    def tabloları_olustur(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS musteriler (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ad TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def musteri_ekle(self, ad):
        self.cursor.execute("INSERT INTO musteriler (ad) VALUES (?)", (ad,))
        self.conn.commit()

    def musteri_listele(self):
        self.cursor.execute("SELECT * FROM musteriler")
        return self.cursor.fetchall()

    def musteri_guncelle(self, musteri_id, yeni_ad):
        self.cursor.execute("UPDATE musteriler SET ad = ? WHERE id = ?", (yeni_ad, musteri_id))
        self.conn.commit()

    def musteri_sil(self, musteri_id):
        self.cursor.execute("DELETE FROM musteriler WHERE id = ?", (musteri_id,))
        self.conn.commit()

    def baglantiyi_kapat(self):
        self.conn.close()
