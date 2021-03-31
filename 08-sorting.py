# ыыыыы
import tkinter as tk

# ыыыыы...

mainw = tk.Tk()
mainw.title("Сортировка")
mainw.geometry("255x170")

box = tk.Listbox(mainw)
box.grid(row=0, column=0, rowspan=3)

entry = tk.Entry(mainw)
entry.grid(row=0, column=1)

def append_item():
    box.insert('end', int(entry.get()))
    entry.delete(0, 'end')

# Функция для кнопки сортировки
def sort_box():
    # Перекидываем содержимое Listbox'а в новый список
    array = []
    for item in box.get(0, 'end'):
        array.append(item)
    # Создаём сортированный список функцией sorted
    sorted_list = sorted(array, reverse=False)
    # Очищаем Listbox
    box.delete(0, 'end')
    # И закидываем в него рассортированные элементы
    for i in range(len(sorted_list)):
        box.insert('end', sorted_list[i])

# ыыыыы

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item)
buttonAdd.grid(row=1, column=1)

buttonSort = tk.Button(mainw, text="Рассортировать", command=sort_box)
buttonSort.grid(row=2, column=1)

mainw.mainloop()