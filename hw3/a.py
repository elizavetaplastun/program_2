import requests

companies = {"GAZP": [[], []], "TATN": [[], []], "SBER": [[], []], "VTBR": [[], []], "ALRS": [[], []],
             "AFLT": [[], []],
             "AFLT": [[], []], "MOEX": [[], []], "NLMK": [[], []], "CHMF": [[], []],
             "DSKY": [[], []], "POLY": [[], []],
             "YNDX": [[], []], "AFKS": [[], []],
             "LSRG": [[], []], "LSNG": [[], []], "LKOH": [[], []], "MTSS": [[], []],
             "NVTK": [[], []], "PIKK": [[], []]}
date_list = ["01-01-2016", "01-07-2016", "01-01-2017", "01-07-2017", "01-01-2018", "01-01-2019", "01-07-2019"]
url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json?iss.meta=off&marketdata.columns=SECID,ISSUECAPITALIZATION&securities.columns=SECID,SHORTNAME,ISSUESIZE"
data = requests.get(url).json()["securities"]["data"]
for i in data:
    if i[0] in companies.keys():
        companies[i[0]][0] = int(i[2])
for company in companies.keys():
    data1 = "01-01-2016"
    data2 = "31-12-2019"
    url2 = f"https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{company}.json?from={data1}&till={data2}&history.columns=TRADEDATE,SHORTNAME,OPEN&iss.meta=off"
    data = requests.get(url2).json()["history"]["data"]
    for day in data:
        if str(day[0]) in date_list:
            companies[company][1].append(int(day[2]))
print(companies)
