# Улучшенная схема 10-positivesum.py
# Украшение интерфейса, обработка исключения при вводе некорректных данных,
# а также применение встроенной функции sum вместо целого цикла

import tkinter as tk
import tkinter.messagebox as mb

mainw = tk.Tk()
mainw.title("Сумма положительных элементов")
mainw.minsize(width=270, height=185)
mainw.minsize(width=270, height=185)
mainw.geometry("270x185")

sx = tk.Scrollbar(mainw, orient='horizontal')
sx.grid(row=4, column=1, sticky='ew')
sy = tk.Scrollbar(mainw, orient='vertical')
sy.grid(row=0, column=0, rowspan=4, sticky='ns')
box = tk.Listbox(mainw, background='peachpuff', foreground='red', xscrollcommand=sx.set, yscrollcommand=sy.set)
box.grid(row=0, column=1, rowspan=4)
sx.config(command=box.xview)
sy.config(command=box.yview)

entry = tk.Entry(mainw, background='lightskyblue', borderwidth=5)
entry.grid(row=0, column=2, sticky='nsew')

label = tk.Label(mainw, background='dimgrey', foreground='lightskyblue', borderwidth=5)
label.grid(row=1, column=2, sticky='nsew')

def append_item():
    try:
        box.insert('end', int(entry.get()))
    except ValueError:
        mb.showerror("ОШИБКА", "Вводные данные могут быть только целочисленного типа!")
    entry.delete(0, 'end')
    

def count_sum():
    array = []
    for item in box.get(0, 'end'):
        array.append(item)
    positive = [i for i in array if i > 0]
    # Используем здесь встроенную в Python функцию sum )))
    label['text'] = "Сумма положительных\nэлементов списка:\n" + str(sum(positive))

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item, background='lavenderblush')
buttonAdd.grid(row=2, column=2, sticky='nsew')

buttonCount = tk.Button(mainw, text="Посчитать", command=count_sum, background='lavenderblush')
buttonCount.grid(row=3, column=2, sticky='nsew')

mainw.mainloop()