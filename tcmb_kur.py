import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def get_tcmb_kurlar():
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"
    try:
        response = requests.get(url)
        response.encoding = 'utf-8'
        xml_data = ET.fromstring(response.text)

        kur_listesi = {}
        for currency in xml_data.findall("Currency"):
            kod = currency.get("CurrencyCode")
            isim = currency.find("Isim").text
            alis = currency.find("ForexBuying").text
            satis = currency.find("ForexSelling").text
            kur_listesi[kod] = {
                "isim": isim,
                "alis": float(alis.replace(",", ".")) if alis else 0.0,
                "satis": float(satis.replace(",", ".")) if satis else 0.0
            }

        return kur_listesi
    except Exception as e:
        print("Kur bilgileri alınamadı:", e)
        return None

# Test etmek istersen:
if __name__ == "__main__":
    kurlar = get_tcmb_kurlar()
    if kurlar:
        for kod, detay in kurlar.items():
            print(f"{kod} - {detay['isim']}: Alış: {detay['alis']}, Satış: {detay['satis']}")
