import requests
import xml.etree.ElementTree as ET
from datetime import datetime

def get_tcmb_kurlar():
    today = datetime.now().strftime("%d/%m/%Y")
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        xml_data = ET.fromstring(response.content)

        dolar = xml_data.find("Currency[@Kod='USD']/BanknoteSelling").text
        euro = xml_data.find("Currency[@Kod='EUR']/BanknoteSelling").text

        return {
            "Tarih": today,
            "Dolar": f"{float(dolar):.2f} TL",
            "Euro": f"{float(euro):.2f} TL"
        }
    except Exception as e:
        return {
            "Hata": str(e),
            "Tarih": today,
            "Dolar": "--",
            "Euro": "--"
        }
