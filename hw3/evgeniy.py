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
print(companies)
print(companies_2016)
file.close()
file_2016.close()
