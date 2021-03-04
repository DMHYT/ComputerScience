# Улучшенная схема 02-listbox.py
# Сделана обработка исключения tkinter.TclError,
# в случае нажатия на кнопку удаления без выбранных элементов.
# При этой ошибке пользователю будет показан messagebox с предупреждением об ошибке.
# Использование END, LEFT, RIGHT заменено использованием строковых обозначений.
# Улучшен интерфейс, добавлены полосы прокутки для Listbox

import tkinter as tk
from tkinter import messagebox as mb

main = tk.Tk()
main.title("Списки")
# Подобраны идеальные размеры окна
main.geometry("330x215")

scrollY = tk.Scrollbar(main, orient='vertical')
scrollY.grid(column=1, row=1, rowspan=3, sticky=('n', 's'))

scrollX = tk.Scrollbar(main, orient='horizontal')
scrollX.grid(column=1, row=4, columnspan=3, sticky=('w', 'e'))

box = tk.Listbox(main, font="Helvetica", bg="black", fg="lightskyblue", yscrollcommand=scrollY.set, xscrollcommand=scrollX.set)
box.grid(row=1, column=2, rowspan=3, sticky=('n', 's', 'w', 'e'))

scrollY.config(command=box.yview)
scrollX.config(command=box.xview)

entry = tk.Entry(main)
entry.grid(row=1, column=3, sticky=('w', 'e'))

def add_item():
    box.insert('end', entry.get())
    entry.delete(0, 'end')

def del_list():
    try:
        select = box.curselection()
        box.delete(select)
    except tk.TclError:
        mb.showerror("ОШИБКА", "Вы не выбрали элемент для удаления")

addButton = tk.Button(main, text="Добавить", command=add_item)
addButton.grid(row=2, column=3, sticky=('n', 's', 'w', 'e'))

delButton = tk.Button(main, text="Удалить", command=del_list)
delButton.grid(row=3, column=3, sticky=('n', 's', 'w', 'e'))

main.mainloop()