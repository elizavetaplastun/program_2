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
companies_names = []
for company in companies.keys():
    companies_names.append(company)
file = open("companies", "r")
file_2016 = open("companies_2016", "r")
corel_2016 = [[None for j in range(len(companies.keys()))] for k in range(len(companies.keys()))]
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


def corel(companies, corel_matrix, company_names):
    for i in range(len(companies.keys())):
        for j in range(len(companies.keys())):
            if i == j:
                corel_matrix[i][j] = None
            else:
                company_name_1 = company_names[i]
                company_name_2 = company_names[j]
                arr = []
                for f in range(5):
                    actions_1 = companies[company_name_1][1][f]
                    actions_2 = companies[company_name_2][1][f]
                    n = len(actions_1)
                    xy = 0
                    for k in range(n):
                        xy += actions_1[k] * actions_2[k]
                    x2 = 0
                    for k in range(n):
                        x2 += actions_1[k] ** 2
                    y2 = 0
                    for k in range(n):
                        y2 += actions_1[k] ** 2
                    x = sum(actions_1)
                    y = sum(actions_2)
                    r = (n * xy - x * y) / (((n * x2 - x ** 2) ** 0.5) * ((n * y2 - y ** 2) ** 0.5))
                    if type(r) != complex:
                        arr.append(r)
                if len(arr) != 0 and sum(arr):
                    corel_matrix[i][j] = sum(arr) / len(arr)

    return corel_matrix


def anatol(corel_matrix, names):
    for i in range(len(corel_matrix)):
        for j in range(len(corel_matrix)):
            if corel_matrix[i][j] == None:
                corel_matrix[i][j] = 900000
            if corel_matrix[i][j] < 0:
                corel_matrix[i][j] *= -1
    companies_names = []
    min_arr = []
    arr = []
    for i in range(len(corel_matrix)):
        m = min(corel_matrix[i])
        index_min = corel_matrix[i].index(m)
        min_arr.append([m, i, index_min])
        arr.append(m)
    arr.sort()
    arr_2 = []
    for n in arr:
        for i in min_arr:
            if n == i[0]:
                arr_2.append(i)
    for k in arr_2:
        if k[1] not in companies_names:
            companies_names.append(k[1])
        if k[2] not in companies_names:
            companies_names.append(k[2])
    companies_names.sort()
    for i in range(len(names)):
        for j in range(len(companies_names)):
            if i == companies_names[j]:
                companies_names[j] = names[i]
    for company in companies_names:
        if companies[company][1][0][0] > companies[company][1][-1][-1]:
            companies_names.remove(company)
    return companies_names[:6]


def buy(arr, n, count):
    k = n / len(arr)
    actions = {}
    for company in arr:
        actions[company] = int(k // companies[company][1][count][0])
    return actions


def sale(arr_buy, day):
    names = list(arr_buy.keys())
    actions = list(arr_buy.values())
    n = 0
    for i in range(len(names)):
        n += companies[names[i]][1][day][0] * actions[i]
    return n


n = 10000000
for i in range(5):
    if i == 0:
        h = corel(companies_2016, corel_2016, companies_names)
        arr = anatol(h, companies_names)
        b = buy(arr, n, i)
    elif i == 4:
        h = corel(companies_2016, corel_2016, companies_names)
        arr = anatol(h, companies_names)
        s = sale(b, i)
    else:
        h = corel(companies_2016, corel_2016, companies_names)
        arr = anatol(h, companies_names)
        s = sale(b, i)
        b = buy(arr, s, i)
print(s)
