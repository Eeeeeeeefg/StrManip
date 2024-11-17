import requests
from bs4 import BeautifulSoup
f = "GIRM.txt"
r = requests.get("https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_en.html")
with open(f, "w", encoding='utf-8') as nF:
    soup = BeautifulSoup(r.text, features="html.parser")
    nF.write(soup.get_text())