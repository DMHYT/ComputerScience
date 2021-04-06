# ВАРИАНТ С АЛГОРИТМОМ "QUICK SORT"

import tkinter as tk

mainw = tk.Tk()
mainw.title("QUICK SORT")
mainw.geometry("250x160")

box = tk.Listbox(mainw)
box.grid(row=0, column=0, rowspan=3)

entry = tk.Entry(mainw)
entry.grid(row=0, column=1)

def append_item():
    box.insert('end', entry.get())
    entry.delete(0, 'end')

# Делаем алгоритм сортировки Quick Sort,
# функция аргументом принимает список и возвращает новый отсортированный 
def quick_sort(lst):
    # Если в списке больше одного элемента
    if len(lst) > 1:
        # Создаём pivot, пусть это будет первый элемент списка
        pivot = lst[0]
        # Создаём три списка специальными конструкциями,
        # с условиями: равно pivot, больше pivot'а, меньше pivot'а
        less = [i for i in lst if i < pivot]
        equal = [i for i in lst if i == pivot]
        greater = [i for i in lst if i > pivot]
        # Используем рекурсию: заново вызываем функцию по элементам больше и меньше pivot'а,
        # таким образом, условная сортировка выше будет повторяться до тех пор, пока эти
        # списки не будут состоять из одного элемента
        result = quick_sort(less) + equal + quick_sort(greater)
        # Возвращаем результат
        return result
    # Если список пустой или в нём только один элемент, возвращаем его без операций
    else:
        return lst

# Сортировка Listbox'а
def sort_box():
    array = []
    for item in box.get(0, 'end'):
        array.append(int(item))
    box.delete(0, 'end')
    # Так как здесь функция не изменяет содержимое данного списка,
    # а возвращает новый, то вместо свободного вызова присваиваем
    # нашему списку то, что вернёт функция
    array = quick_sort(array)
    for item in array:
        box.insert('end', item)

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item)
buttonAdd.grid(row=1, column=1)

buttonSort = tk.Button(mainw, text="Сортировать", command=sort_box)
buttonSort.grid(row=2, column=1)

mainw.mainloop()