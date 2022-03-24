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

file = open("companies", "r")
file_2016 = open("companies_2016", "r")
while True:
    if not file.readline():
        break
    for j in range(len(companies)):
        company = file.readline()[:-1]
        n = file.readline()[:-1]
        companies[company][0] = int(n)
        for i in range(5):
            companies[company][1].append(list(map(float, file.readline()[:-1].split())))
while True:
    if not file_2016.readline():
        break
    for j in range(len(companies_2016)):
        company = file_2016.readline()[:-1]
        n = file_2016.readline()[:-1]
        companies_2016[company][0] = int(n)
        for i in range(5):
            companies_2016[company][1].append(list(map(float, file_2016.readline()[:-1].split())))
file.close()
file_2016.close()

def capitalization(companies, month):
    companies2 = {}
    for company in companies:
        companies2[company] = companies[company][0] * companies[company][1][month][-1]
    return companies2

def evgeniy(companies2):
    total = 0
    for i in companies2.values():
        total += i
    k = []
    for i in companies2.values():
        k.append(i / total)
    return k

def buy(k, companies, money, month):
    actions = {}
    i = 0
    for company in companies.keys():
        actions[company] = (money * k[i])/companies[company][1][month][0]
        i += 1
    return actions

def sale(arr_buy, month):
    names = list(arr_buy.keys())
    actions = list(arr_buy.values())
    n = 0
    for i in range(len(names)):
        n += companies[names[i]][1][month][0] * actions[i]
    return n

money_file = open("money", "a")
money = [10000000]
n = 10000000
n = 10000000
for i in range(5):
    if i == 0:
        h = capitalization(companies_2016, -1)
        arr = evgeniy(h)
        b = buy(arr, companies, n, i)
    elif i == 4:
        h = capitalization(companies, i)
        arr = evgeniy(h)
        s = sale(b, i)
        money.append(s)
    else:
        h = capitalization(companies, i)
        arr = evgeniy(h)
        s = sale(b, i)
        money.append(s)
        b = buy(arr, companies, n, i)
money_file.write(" ".join(list(map(str, money)))+"\n")
money_file.close()
print(s)
