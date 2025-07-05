import sqlite3

# Veritabanı bağlantısı
def veritabani_baglan():
    conn = sqlite3.connect("veri.db")
    return conn

# Veritabanı tablolarını oluştur
def tablo_olustur():
    conn = veritabani_baglan()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS musteriler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT NOT NULL,
            telefon TEXT,
            adres TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teklifler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            musteri_id INTEGER,
            icerik TEXT,
            tarih TEXT,
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
def musteri_ekle(ad, telefon, adres):
    conn = veritabani_baglan()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO musteriler (ad, telefon, adres) VALUES (?, ?, ?)", (ad, telefon, adres))
    conn.commit()
    conn.close()

# Müşteri listesini getir
def musteri_listele():
    conn = veritabani_baglan()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM musteriler")
    sonuc = cursor.fetchall()
    conn.close()
    return sonuc

# Müşteri güncelle
def musteri_guncelle(id, yeni_ad, yeni_telefon, yeni_adres):
    conn = veritabani_baglan()
    cursor = conn.cursor()
    cursor.execute("UPDATE musteriler SET ad=?, telefon=?, adres=? WHERE id=?", (yeni_ad, yeni_telefon, yeni_adres, id))
    conn.commit()
    conn.close()

# Müşteri sil
def musteri_sil(id):
    conn = veritabani_baglan()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM musteriler WHERE id=?", (id,))
    conn.commit()
    conn.close()
