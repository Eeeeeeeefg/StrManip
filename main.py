from webcrawler import Crawler

c = Crawler()

c.link_add("GIRM", "https://www.vatican.va/roman_curia/congregations/ccdds/documents/rc_con_ccdds_doc_20030317_ordinamento-messale_en.html")
c.link_add("Sacrosanctum Concillium", "https://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19631204_sacrosanctum-concilium_en.html")
c.link_add()
c.scrape()
output = c.soupify()
for i in output.items():
    with open(i[0], "w", encoding='utf-8') as f:
        f.write(i[1].get_text())