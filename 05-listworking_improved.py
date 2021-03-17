# Улучшенная схема 05-listworking.py
# Украшен интерфейс, добавлены идеальные неизменные размеры окна,
# полосы прокрутки для Listbox'а, cделана
# обработка исключения ValueError в случае введения пользователем
# некорректных данных, также программа теперь может принимать не
# только целые числа int, но и действительные числа float,
# в случае некорректного ввода вылезет messagebox с ошибкой.
# Перед подсчётом цен Listbox очищается, если он не пустой 
# (Дарья Владимировна, добавьте это в основу 0_0)

import tkinter as tk
import tkinter.messagebox as mb

mainw = tk.Tk()
mainw.title("Изменение цены")
mainw.geometry("405x205")
mainw.minsize(width=405, height=205)
mainw.maxsize(width=405, height=205)

label1 = tk.Label(mainw, text="Введите начальную цену", background='dimgrey', foreground='lightskyblue', borderwidth=5)
label1.grid(row=0, column=0, sticky='s')

entry = tk.Entry(mainw, background='lightskyblue', borderwidth=5)
entry.grid(row=1, column=0, sticky='nsew')

label2 = tk.Label(mainw, text="Рассчёт изменения цены", background='dimgrey', foreground='lightskyblue', borderwidth=5)
label2.grid(row=0, column=1, sticky='nsew')

scrollX = tk.Scrollbar(mainw, orient='horizontal')
scrollX.grid(row=3, column=1, sticky='ew')

scrollY = tk.Scrollbar(mainw, orient='vertical')
scrollY.grid(row=1, column=2, rowspan=2, sticky='ns')

box = tk.Listbox(mainw, width=40, xscrollcommand=scrollX.set, yscrollcommand=scrollY.set, background='peachpuff', foreground='red', borderwidth=5)
box.grid(row=1, column=1, rowspan=2)

scrollX.config(command=box.xview)
scrollY.config(command=box.yview)

def count_price_changing():
    if len(box.get(0, 'end')) > 0:
        box.delete(0, 'end')
    try:
        k = float(entry.get())
        for i in range(4):
            z = round(k * 1.1, 2)
            st = "Цена на " + str(i + 1) + " неделе составляет " + str(z) + " грн."
            box.insert('end', st)
            k = z
    except ValueError:
        mb.showerror("ОШИБКА", "Цена должна быть числового типа!")

buttonCount = tk.Button(mainw, text="Рассчитать", command=count_price_changing, background='lavenderblush')
buttonCount.grid(row=2, column=0, sticky='nsew')

mainw.mainloop()