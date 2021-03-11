# Импортируем tkinter
import tkinter as tk

# Объявляем окно
main = tk.Tk()
main.title("Количество одинаковых элементов в списке")
main.geometry("300x300")

# Создаём и отображаем на нём Listbox
box = tk.Listbox(main)
box.pack()

# Поле ввода
entry = tk.Entry(main)
entry.pack()

# И текст Label
quantity = tk.Label(main)
quantity.pack()

# Копируем функцию добавления элемента в Listbox
# из предыдущего урока
def add_item():
    box.insert(tk.END, entry.get())
    entry.delete(0, tk.END)

# Создаём функцию, которая будет считать количество элементов в Listbox,
# которые равны самому первому элементу
def count_equal_elements():
    # Создаём список
    array = []
    # Циклом заполняем его всеми элементами Listbox'а
    for item in box.get(0, tk.END):
        array.append(item)
    # Создаём переменную подсчёта
    # Ставим 1, так как мы будем приравнивать все элементы к первому,
    # который у нас уже имеется
    k = 1
    # Создаём цикл со счётчиком в диапазоне от нуля до максимального индекса в нашем списке
    # (так как элементы считаются с нуля, максимальный индекс будет на 1 меньше длины списка)
    for i in range(len(array) - 1):
        # Если взятый элемент равен первому
        if array[i + 1] == array[0]:
            # Прибавляем 1 к переменной-счётчику
            k += 1
    # Обращаясь к полю лейбла 'text',
    # вставляем туда полученное количество
    quantity['text'] = str(k)

# Создаём кнопки

addButton = tk.Button(main, text="Добавить", command=add_item)
addButton.pack()

countButton = tk.Button(main, text="Посчитать", command=count_equal_elements)
countButton.pack()

# Вызываем непрерывное отображение окна
main.mainloop()