# входные данные: список лосей, и городов где они проживают. таким образом: лось валера москва
# выходные данные: две диаграммы, первая по именам лосей, вторая по городам
import matplotlib.pyplot as plt

file = open("1.txt", "r")
names = {}
cities = {}
while True:
    line = file.readline()
    if not line:
        break
    else:
        line = line.split()
        if line[1] not in names.keys():
            names[line[1]] = 1
        else:
            names[line[1]] += 1
        if line[2] not in cities.keys():
            cities[line[2]] = 1
        else:
            cities[line[2]] += 1
file.close()
plt.pie(names)
plt.legend(names.keys())
plt.show()