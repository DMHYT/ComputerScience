# Импорт
import tkinter as tk

# Окно
mainw = tk.Tk()
mainw.title("Кислотность почв")
mainw.geometry("610x200")

# Два Listbox'а и поле ввода

box1 = tk.Listbox(mainw, width=40, height=10)
box1.grid(row=0, column=0, rowspan=3)

entry = tk.Entry(mainw)
entry.grid(row=0, column=1)

box2 = tk.Listbox(mainw, width=40, height=10)
box2.grid(row=0, column=2, rowspan=3)

# Список для значений кислотности, введённых пользователем
array = []

# Функция добавления участка
def append_item():
    # Получаем данные из поля ввода
    # и количество элементов в Listbox'е
    k = entry.get()
    size = box1.size()
    # Вставляем элемент в Listbox, очищаем поле ввода,
    # добавляем значение кислотности в список
    string = "Кислотность на " + str(size + 1) + " участке составляет " + k
    box1.insert('end', string)
    entry.delete(0, 'end')
    array.append(k)

# Функция подсчёта
def count_environments():
    # Чистим второй Listbox перед операцией
    box2.delete(0, 'end')
    # Создаём переменные для количества участков
    # с кислой, нейтральной и щелочной почвой соответственно
    acidic = 0
    neutral = 0
    alcaline = 0
    # Делаем проверку всех значений кислотности, и в случае
    # истинности условия прибавляем 1 к одной из переменных
    for i in range(len(array)):
        if float(array[i]) < 7:
            acidic += 1
        elif float(array[i]) == 7:
            neutral += 1
        else:
            alcaline += 1
    # Вставляем полученные данные во второй Listbox
    box2.insert('end', "Кислые почвы на " + str(acidic) + " участках")
    box2.insert('end', "Нейтральные почвы на " + str(neutral) + " участках")
    box2.insert('end', "Щелочные почвы на " + str(alcaline) + " участках")

# Функция для кнопки, которая очищает оба Listbox'а и массив со значениями
def clear_all():
    box1.delete(0, 'end')
    box2.delete(0, 'end')
    array.clear()

# Кнопки

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item)
buttonAdd.grid(row=1, column=1)

buttonCount = tk.Button(mainw, text="Посчитать", command=count_environments)
buttonCount.grid(row=2, column=1)

buttonClear = tk.Button(mainw, text="Очистить всё", command=clear_all)
buttonClear.grid(row=3, column=1)

# Непрерывное отображение окна на экране
mainw.mainloop()