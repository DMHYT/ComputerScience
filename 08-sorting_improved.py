# Улучшенная схема 08-sorting.py
# Украшение интерфейса, пользователь может вводить, кроме целых чисел,
# также и действительные числа и строки, сортируются по отдельности

import tkinter as tk

mainw = tk.Tk()
mainw.title("Сортировка")
mainw.minsize(width=275, height=185)
mainw.maxsize(width=275, height=185)
mainw.geometry("275x185")

sx = tk.Scrollbar(mainw, orient='horizontal')
sx.grid(row=3, column=1, sticky='ew')
sy = tk.Scrollbar(mainw, orient='vertical')
sy.grid(row=0, column=0, rowspan=3, sticky='ns')
box = tk.Listbox(mainw, background='peachpuff', foreground='red', xscrollcommand=sx.set, yscrollcommand=sy.set)
box.grid(row=0, column=1, rowspan=3)
sx.config(command=box.xview)
sy.config(command=box.yview)

entry = tk.Entry(mainw, background='lightskyblue', borderwidth=5)
entry.grid(row=0, column=2, sticky='nsew')

def append_item():
    # Позволяем пользователю вводить данные
    # типов int, float и string.
    # Через обработки исключений конвертируем
    # строковой ввод в нужный тип
    try:
        box.insert('end', int(entry.get()))
    except ValueError:
        try:
            box.insert('end', float(entry.get()))
        except ValueError:
            box.insert('end', entry.get())
    entry.delete(0, 'end')

def sort_box():
    # Создаём списки отдельно для int, float и str
    ints = []
    floats = []
    strings = []
    # Проверяем тип данных каждого элемента функцией type,
    # и закидываем в соответствующий массив
    for item in box.get(0, 'end'):
        if type(item) is int:
            ints.append(item)
        elif type(item) is float:
            floats.append(item)
        else:
            strings.append(item)
    # Сортируем списки
    sorted_ints = sorted(ints, reverse=False)
    sorted_floats = sorted(floats, reverse=False)
    sorted_strings = sorted(strings, reverse=False)
    box.delete(0, 'end')
    # Закидываем по очереди в Listbox
    box.insert('end', "ЦЕЛЫЕ ЧИСЛА: ")
    for item in sorted_ints:
        box.insert('end', item)
    box.insert('end', "ДРОБНЫЕ ЧИСЛА: ")
    for item in sorted_floats:
        box.insert('end', item)
    box.insert('end', "СТРОКИ: ")
    for item in sorted_strings:
        box.insert('end', item)

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item, background='lavenderblush')
buttonAdd.grid(row=1, column=2, sticky='nsew')

buttonSort = tk.Button(mainw, text="Рассортировать", command=sort_box, background='lavenderblush')
buttonSort.grid(row=2, column=2, sticky='nsew')

mainw.mainloop()