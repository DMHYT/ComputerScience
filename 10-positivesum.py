import tkinter as tk
import tkinter.messagebox as mb

mainw = tk.Tk()
mainw.title("Сумма положительных элементов")
mainw.geometry("250x165")

box = tk.Listbox(mainw)
box.grid(row=0, column=0, rowspan=4)

entry = tk.Entry(mainw)
entry.grid(row=0, column=1)

label = tk.Label(mainw)
label.grid(row=1, column=1)

def append_item():
    box.insert('end', int(entry.get()))
    entry.delete(0, 'end')

def count_sum():
    array = []
    for item in box.get(0, 'end'):
        array.append(item)
    positive = [i for i in array if i > 0]
    summ = 0
    for item in positive:
        summ += (item)
    label['text'] = "Сумма положительных\nэлементов списка:\n" + str(summ)

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item)
buttonAdd.grid(row=2, column=1)

buttonCount = tk.Button(mainw, text="Посчитать", command=count_sum)
buttonCount.grid(row=3, column=1)

mainw.mainloop()