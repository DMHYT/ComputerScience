# ВАРИАНТ С АЛГОРИТМОМ 'BUBBLE SORT'

import tkinter as tk

mainw = tk.Tk()
mainw.title("BUBBLE SORT")
mainw.geometry("250x160")

box = tk.Listbox(mainw)
box.grid(row=0, column=0, rowspan=3)

entry = tk.Entry(mainw)
entry.grid(row=0, column=1)

def append_item():
    box.insert('end', entry.get())
    entry.delete(0, 'end')

# Делаем алгоритм сортировки Bubble Sort,
# функция аргументом принимает список и ничего не возвращает,
# но при этом изменяет содержимое данного списка
def bubble_sort(lst):
    # Нам нужно будет повторить операцию столько раз, сколько элементов в списке
    for i in range(len(lst)):
        # Далее делаем цикл, который закончится на предпоследнем элементе
        for j in range(len(lst) - 1):
            # Пусть n - возможный индекс элемента списка
            # Здесь j = n - 1, j + 1 = n
            # Сравниваем два рядом стоящих элемента
            if lst[j] > lst[j + 1]:
                # Если первый больше второго, меняем их местами
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Сортируем Listbox
def sort_box():
    # Перекидываем элементы в новый список и чистим бокс
    array = []
    for item in box.get(0, 'end'):
        array.append(int(item))
    box.delete(0, 'end')
    # Вызываем сортировку по этому списку
    bubble_sort(array)
    # И закидываем отсортированные элементы обратно в Listbox
    for item in array:
        box.insert('end', item)

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item)
buttonAdd.grid(row=1, column=1)

buttonSort = tk.Button(mainw, text="Сортировать", command=sort_box)
buttonSort.grid(row=2, column=1)

mainw.mainloop()