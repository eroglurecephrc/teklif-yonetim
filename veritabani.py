import sqlite3

def veritabani_olustur():
    conn = sqlite3.connect("veriler.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS musteriler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT NOT NULL,
            telefon TEXT,
            adres TEXT
        )
    """)
    conn.commit()
    conn.close()

def musteri_ekle(ad, telefon, adres):
    conn = sqlite3.connect("veriler.db")
    c = conn.cursor()
    c.execute("INSERT INTO musteriler (ad, telefon, adres) VALUES (?, ?, ?)", (ad, telefon, adres))
    conn.commit()
    conn.close()

def musterileri_getir():
    conn = sqlite3.connect("veriler.db")
    c = conn.cursor()
    c.execute("SELECT ad, telefon, adres FROM musteriler ORDER BY id DESC")
    veriler = c.fetchall()
    conn.close()
    return veriler
