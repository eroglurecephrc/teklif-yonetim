import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def get_tcmb_kurlar():
    try:
        url = "https://www.tcmb.gov.tr/kurlar/today.xml"
        response = requests.get(url)
        response.encoding = "utf-8"
        tree = ET.ElementTree(ET.fromstring(response.text))
        root = tree.getroot()

        kurlar = {}
        for currency in root.findall("Currency"):
            kod = currency.get("CurrencyCode")
            if kod in ["USD", "EUR", "GBP"]:
                try:
                    kur = currency.find("ForexSelling").text.replace(",", ".")
                    kurlar[kod] = float(kur)
                except:
                    continue

        return kurlar
    except Exception as e:
        print(f"TCMB kurlarını alırken hata oluştu: {e}")
        return {}
