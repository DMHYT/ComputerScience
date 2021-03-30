# Улучшенная схема 07-listworking.py
# Как обычно, украшение интерфейса и обработка исключений.
# Но сразу к самому интересному:
# В Python есть встроенные функции min и max, которые
# позволяют найти наименьшее и наибольшее значение соответственно,
# в итерируемом объекте (массиве / списке).
# И какой смысл вообще что-то выдумывать, если эти функции сделают всё за нас?

import tkinter as tk
import tkinter.messagebox as mb

mainw = tk.Tk()
mainw.title("MIN / MAX")
mainw.minsize(width=275, height=185)
mainw.maxsize(width=275, height=185)
mainw.geometry("275x185")

sx = tk.Scrollbar(mainw, orient='horizontal')
sx.grid(row=6, column=1, sticky='ew')
sy = tk.Scrollbar(mainw, orient='vertical')
sy.grid(row=0, column=0, rowspan=6, sticky='ns')
box = tk.Listbox(mainw, background='peachpuff', foreground='red', xscrollcommand=sx.set, yscrollcommand=sy.set)
box.grid(row=0, column=1, rowspan=6)
sx.config(command=box.xview)
sy.config(command=box.yview)

labelMax = tk.Label(mainw, background='dimgrey', foreground='lightskyblue', borderwidth=5)
labelMax.grid(row=0, column=2, sticky='nsew')

labelMin = tk.Label(mainw, background='dimgrey', foreground='lightskyblue', borderwidth=5)
labelMin.grid(row=1, column=2, sticky='nsew')

labelDiff = tk.Label(mainw, background='dimgrey', foreground='lightskyblue', borderwidth=5)
labelDiff.grid(row=2, column=2, sticky='nsew')

entry = tk.Entry(mainw, background='lightskyblue', borderwidth=5)
entry.grid(row=3, column=2, sticky='nsew')

def append_item():
    try:
        box.insert('end', int(entry.get()))
    except ValueError:
        mb.showerror("ОШИБКА", "Вводные данные могут быть только целочисленного типа")
    entry.delete(0, 'end')

def count_minmax():
    array = []
    for item in box.get(0, 'end'):
        array.append(int(item))
    # И лишних 5 строк кода улетучиваются)))
    maxValue = max(array)
    minValue = min(array)
    labelMax['text'] = "Наибольшее значение: " + str(maxValue)
    labelMin['text'] = "Наименьшее значение: " + str(minValue)
    labelDiff['text'] = "Разница: " + str(maxValue - minValue)

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item, background='lavenderblush')
buttonAdd.grid(row=4, column=2, sticky='nsew')

buttonCount = tk.Button(mainw, text="Посчитать", command=count_minmax, background='lavenderblush')
buttonCount.grid(row=5, column=2, sticky='nsew')

mainw.mainloop()