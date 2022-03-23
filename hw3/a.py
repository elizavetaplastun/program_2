
from urllib.request import urlopen

companies = {"Газпром": [[89, 678], [7, 900]], "Татнефть": [], "Сбербанк": [], "ВТБ": [], "Алроса": [], "Аэрофлот": [],
             "РусГидро": [], "Московская Биржа": [], "НЛМК": [], "Северсталь": [], "Детский Мир": [], "Полиметалл": [],
             "Яндекс": [], "АФК": [],
             "Система": [], "Группа ЛСР": [], "Ленэнерго": [], "Лукойл": [], "МТС": [], "Новатэк": [], "ПИК": []}

company = "GAZP"
data = "2016-01-01"
url = f"http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{company}.json?iss.json=extended&from={data}"
text = str(urlopen(url).read())
t = text.split()
print(t)