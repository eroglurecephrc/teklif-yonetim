import sqlite3
from datetime import datetime

# Veritabanını oluştur ve bağlantıyı al
def veritabani_baglan():
    conn = sqlite3.connect("veritabani.db")
    return conn

# Tabloları oluştur
def veritabani_olustur():
    conn = veritabani_baglan()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS musteriler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad TEXT NOT NULL,
        adres TEXT,
        telefon TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teklifler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        musteri_id INTEGER,
        tarih TEXT,
        icerik TEXT,
        FOREIGN KEY(musteri_id) REFERENCES musteriler(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS siparisler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tedarikci TEXT,
        icerik TEXT,
        tarih TEXT
    )
    """)

    conn.commit()
    conn.close()

# Müşteri ekle
def musteri_ekle(ad, adres, telefon, email):
    conn = veritabani_baglan()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO musteriler (ad, adres, telefon, email) VALUES (?, ?, ?, ?)",
                   (ad, adres, telefon, email))
    conn.commit()
    conn.close()

# Müşteri sil
def musteri_sil(musteri_id):
    conn = veritabani_baglan()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM musteriler WHERE id=?", (musteri_id,))
    conn.commit()
    conn.close()

# Müşteri güncelle
def musteri_guncelle(musteri_id, ad, adres, telefon, email):
    conn = veritabani_baglan()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE musteriler 
        SET ad=?, adres=?, telefon=?, email=? 
        WHERE id=?
    """, (ad, adres, telefon, email, musteri_id))
    conn.commit()
    conn.close()

# Müşteri listesini al
def musterileri_getir():
    conn = veritabani_baglan()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM musteriler")
    musteriler = cursor.fetchall()
    conn.close()
    return musteriler

# Teklif ekle
def teklif_ekle(musteri_id, icerik):
    conn = veritabani_baglan()
    cursor = conn.cursor()
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO teklifler (musteri_id, tarih, icerik) VALUES (?, ?, ?)",
                   (musteri_id, tarih, icerik))
    conn.commit()
    conn.close()

# Sipariş ekle
def siparis_ekle(tedarikci, icerik):
    conn = veritabani_baglan()
    cursor = conn.cursor()
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO siparisler (tedarikci, icerik, tarih) VALUES (?, ?, ?)",
                   (tedarikci, icerik, tarih))
    conn.commit()
    conn.close()
