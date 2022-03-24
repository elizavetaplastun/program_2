import requests

companies = {"GAZP": [[], []], "TATN": [[], []], "SBER": [[], []], "VTBR": [[], []], "ALRS": [[], []],
             "AFLT": [[], []], "MOEX": [[], []], "NLMK": [[], []], "CHMF": [[], []],
             "DSKY": [[], []], "POLY": [[], []],
             "YNDX": [[], []], "AFKS": [[], []],
             "LSRG": [[], []], "LSNG": [[], []], "LKOH": [[], []], "MTSS": [[], []],
             "NVTK": [[], []], "PIKK": [[], []]}

companies_2016 = {"GAZP": [[], []], "TATN": [[], []], "SBER": [[], []], "VTBR": [[], []], "ALRS": [[], []],
                  "AFLT": [[], []], "MOEX": [[], []], "NLMK": [[], []], "CHMF": [[], []],
                  "DSKY": [[], []], "POLY": [[], []],
                  "YNDX": [[], []], "AFKS": [[], []],
                  "LSRG": [[], []], "LSNG": [[], []], "LKOH": [[], []], "MTSS": [[], []],
                  "NVTK": [[], []], "PIKK": [[], []]}
date_list_2016 = ["2016-01-01", "2016-04-01", "2016-07-01", "2016-10-01", "2016-12-01"]
date_list = ["2017-01-01", "2017-07-01", "2018-01-01", "2019-01-01", "2019-07-01"]
url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json?iss.meta=off&marketdata.columns=SECID,ISSUECAPITALIZATION&securities.columns=SECID,SHORTNAME,ISSUESIZE"
data = requests.get(url).json()["securities"]["data"]
for i in data:
    if i[0] in companies.keys():
        companies[i[0]][0] = int(i[2])
        companies_2016[i[0]][0] = int(i[2])
for company in companies_2016.keys():
    for date1 in date_list_2016:
        url2 = f"https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{company}.json?from={date1}&history.columns=TRADEDATE,SHORTNAME,OPEN&iss.meta=off"
        data = requests.get(url2).json()["history"]["data"]
        a = []
        for day in data:
            if day[2] is not None:
                a.append(day[2])
                if len(a) == 30:
                    companies_2016[company][1].append(a)
                    break
for company in companies.keys():
    for date1 in date_list:
        url2 = f"https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/{company}.json?from={date1}&history.columns=TRADEDATE,SHORTNAME,OPEN&iss.meta=off"
        data = requests.get(url2).json()["history"]["data"]
        a = []
        for day in data:
            if day[2] is not None:
                a.append(day[2])
                if len(a) == 10:
                    companies[company][1].append(a)
                    break

file = open("companies", "w")
file.write("f\n")
file_2016 = open("companies_2016", "w")
file_2016.write("f\n")
for company in companies_2016:
    file_2016.write(company + '\n')
    file_2016.write(str(companies_2016[company][0]) + "\n")
    for dates in companies_2016[company][1]:
        file_2016.write(" ".join(list(map(str, dates))) + '\n')

for company in companies:
    file.write(company + '\n')
    file.write(str(companies[company][0]) + '\n')
    for dates in companies[company][1]:
        file.write(" ".join(list(map(str, dates))) + '\n')
file.close()
file_2016.close()
