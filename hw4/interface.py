from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame

data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
         'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]}
df2 = DataFrame(data2, columns=['Year', 'Unemployment_Rate'])


# Функции для обработки введенных данных
def Get():
    res = "Введено: {}".format(ticker.get())
    lbl_test.configure(text=res)


def GrafTest():
    x = [1, 2, 3, 4, 5]
    y = [5, 4, 3, 2, 1]
    plt.plot(x, y)
    plt.show()
    pass

def generate(df2=df2):
    global conv
    if conv:
        conv.get_tk_widget().destroy()
    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    conv = FigureCanvasTkAgg(figure2, str4)
    conv.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()
    df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
    ax2.set_title('Year Vs. Unemployment Rate')


def close():
    global conv
    if conv:
        conv.get_tk_widget().destroy()


# Структура окна
window = Tk()
window.geometry("800x600")
window.title("Аналитика акций")

conv = None

str1 = Frame(window)
str2 = Frame(window)
str3 = Frame(window)
str4 = Frame(window)


str1.pack()
str2.pack()
str3.pack()
str4.pack()


lb1 = Label(str1, text="Введите тикер ", padx=5, pady=5)
lb1.pack(side=LEFT)

lb2 = Label(str2, text="Введите временной отрезок ", padx=5, pady=5)
lb2.pack(side=LEFT)

ticker = Entry(str1, width=15)
ticker.pack(side=LEFT)

date_start = Entry(str2, width=15)
date_end = Entry(str2, width=15)
date_start.pack(side=LEFT)
date_end.pack(side=LEFT)

button = Button(str3, text="Выполнить", command=close, padx=5, pady=5)
button.pack(side=LEFT)

button1 = Button(str3, text="Построить график", command=generate, padx=5, pady=5)
button1.pack(side=LEFT)

lbl_test = Label(str3, text="Введено: ", padx=5, pady=20)
lbl_test.pack(side=LEFT)

window.mainloop()
