import urllib.request
from xml.dom import minidom


url = "http://www.cbr.ru/scripts/XML_daily.asp"


webFile = urllib.request.urlopen(url)
data = webFile.read()


UrlSplit = url.split("/")[-1]
ExtSplit = UrlSplit.split(".")[1]
FileName = UrlSplit.replace(ExtSplit, "xml")

with open(FileName, "wb") as localFile:
    localFile.write(data)

webFile.close()

# Парсинг xml и запись данных в файл
doc = minidom.parse(FileName)

# Извлечение даты
root = doc.getElementsByTagName("ValCurs")[0]
# date = "Текущий курс валют ЦБ РФ на {date}г. \n".format(date=root.getAttribute('Date'))

# Извлечение данных по валютам
currency = doc.getElementsByTagName("Valute")

with open("CurrentCurrencyCource.xls", "w") as out:
    # out.write(date)
    # out.write(head)
    for rate in currency:
        sid = rate.getAttribute("ID")
        charcode = rate.getElementsByTagName("CharCode")[0]
        name = rate.getElementsByTagName("Name")[0]
        value = rate.getElementsByTagName("Value")[0]
        nominal = rate.getElementsByTagName("Nominal")[0]
        result = "{0}\t{1}\t{2}\n".format(sid, charcode.firstChild.data,
                                       value.firstChild.data)
        out.write(result)

