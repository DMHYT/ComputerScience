# Улучшенная схема 09-sorting_common
# Украшения интерфейса, проверка корректности ввода,
# а также выбор пользователя между Bubble Sort и Quick Sort
# с помощью кнопок Radiobutton.

import tkinter as tk
import tkinter.messagebox as mb

mainw = tk.Tk()
mainw.title("BUBBLE SORT AND QUICK SORT")
mainw.minsize(width=275, height=185)
mainw.maxsize(width=275, height=185)
mainw.geometry("275x185")

sx = tk.Scrollbar(mainw, orient='horizontal')
sx.grid(row=6, column=1, sticky='ew')
sy = tk.Scrollbar(mainw, orient='vertical')
sy.grid(row=0, column=0, rowspan=6, sticky='ns')
box = tk.Listbox(mainw, xscrollcommand=sx.set, yscrollcommand=sy.set, background='peachpuff', foreground='red')
box.grid(row=0, column=1, rowspan=6)
sx.config(command=box.xview)
sy.config(command=box.yview)

entry = tk.Entry(mainw, background='lightskyblue', borderwidth=5)
entry.grid(row=0, column=2, sticky='nsew')

labelMode = tk.Label(mainw, text="Выберите алгоритм", background='dimgrey', foreground='lightskyblue', borderwidth=5)
labelMode.grid(row=1, column=2, sticky='nsew')
# Целочисленная переменная для Radiobutton'ов, сделаем так, что если
# пользователь выбрал Bubble Sort, она будет равна 0, если Quick Sort, то 1
mode = tk.IntVar()
radioBubble = tk.Radiobutton(mainw, text="Bubble Sort", variable=mode, value=0, background='peachpuff')
radioBubble.grid(row=2, column=2, sticky='nsew')
radioQuick = tk.Radiobutton(mainw, text="Quick Sort", variable=mode, value=1, background='peachpuff')
radioQuick.grid(row=3, column=2, sticky='nsew')

def append_item():
    # Позволяем пользователю вводить только целые числа
    try:
        box.insert('end', int(entry.get()))
    except ValueError:
        mb.showerror("ОШИБКА", "Вводные данные должны быть целочисленного типа!")
    entry.delete(0, 'end')

# Переписываем оба алгоритма

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

def quick_sort(lst):
    if len(lst) > 1:
        pivot = lst[0]
        less = [i for i in lst if i < pivot]
        equal = [i for i in lst if i == pivot]
        greater = [i for i in lst if i > pivot]
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return lst

def sort_box():
    array = []
    for item in box.get(0, 'end'):
        array.append(int(item))
    box.delete(0, 'end')
    # Проверяем значение переменной Radiobutton'ов
    # и применяем к списку соответствующий алгоритм
    if mode.get() == 0:
        bubble_sort(array)
    else:
        array = quick_sort(array)
    for item in array:
        box.insert('end', item)

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item, background='lavenderblush')
buttonAdd.grid(row=4, column=2, sticky='nsew')

buttonSort = tk.Button(mainw, text="Сортировать", command=sort_box, background='lavenderblush')
buttonSort.grid(row=5, column=2, sticky='nsew')

mainw.mainloop()