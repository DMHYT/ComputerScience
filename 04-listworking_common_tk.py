# Импортируем tkinter
import tkinter as tk

# Создаём окно
mainw = tk.Tk()
mainw.title("Изменение значений")
mainw.geometry("400x400")

# Listbox
box = tk.Listbox(mainw)
box.grid(row=0, column=0, rowspan=3)

# Поле ввода
entry = tk.Entry(mainw)
entry.grid(row=0, column=1)

# Второй Listbox для квадратов значений
boxSq = tk.Listbox(mainw)
boxSq.grid(row=0, column=2, rowspan=3)

# Списываем функцию добавления элемента
def add_item():
    box.insert('end', entry.get())
    entry.delete(0, 'end')

# Функция подсчёта квадратов значений
def count_squares():
    # Получаем список элементов Listbox'а
    elems = box.get(0, 'end')
    # array = [] зачем этот список в листинге???
    # Делаем пробег по элементам
    for i in range(len(elems)):
        # Создаём переменную, в которой переведённый в целое число
        # элемент Listbox'a возводим в квадрат
        k = int(elems[i]) ** 2
        # Вставляем полученное значение во второй Listbox
        boxSq.insert('end', k)

# Создаём две кнопки

buttonAdd = tk.Button(mainw, text="Добавить", command=add_item)
buttonAdd.grid(row=1, column=1)

buttonCount = tk.Button(mainw, text="Посчитать", command=count_squares)
buttonCount.grid(row=2, column=1)

# И запускаем непрерывное отображение
mainw.mainloop()