# Ой а чо это мы тут делаем? Догадайтесь сами,
# мне уже надоело это повторять 0_0
import tkinter as tk

# Всё по стандарту

mainw = tk.Tk()
mainw.title("MIN / MAX")
mainw.geometry("300x200")

box = tk.Listbox(mainw)
box.grid(row=0, column=0, rowspan=6)

labelMax = tk.Label(mainw)
labelMax.grid(row=0, column=1)

labelMin = tk.Label(mainw)
labelMin.grid(row=1, column=1)

labelDiff = tk.Label(mainw)
labelDiff.grid(row=2, column=1)

entry = tk.Entry(mainw)
entry.grid(row=3, column=1)

# Эта штука здесь уже какой раз О_О
def append_item():
    box.insert('end', entry.get())
    entry.delete(0, 'end')

# А оце новенькое
# По правде говоря, мне абсолютно не понравился этот листинг,
# потому что это малоэффективно. Советую глянуть в реализацию
# в improved версии, те кто не понимают в чём прикол,
# будут приятно удивлены
def count_minmax():
    # Список, в который перекинем все элементы Listbox'а
    array = []
    for item in box.get(0, 'end'):
        array.append(int(item))
    # Итак, переменные для обозначения минимального и максимального значения.
    # Вместо того, чтобы ставить в эти переменные какие бы то ни было числа,
    # просто всунем и туда, и туда, первый элемент Listbox'а.
    minValue = array[0]
    maxValue = array[0]
    # Переменная для разницы между минималкой и максималкой
    diff = 0
    # Цикл по элементам Listbox'а
    for i in range(len(array)):
        # Если элемент больше максималки, присвоить ей его значение
        if array[i] > maxValue:
            maxValue = array[i]
        # Если элемент меньше максималки, присвоить ей его значение
        if array[i] < minValue:
            minValue = array[i]
    # Вычисляем разницу
    diff = maxValue - minValue
    # Выводим всё в лейблы
    labelMax['text'] = "Наибольшее значение: " + str(maxValue)
    labelMin['text'] = "Наименьшее значение: " + str(minValue)
    labelDiff['text'] = "Разница: " + str(diff)

# Кнопки

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item)
buttonAdd.grid(row=4, column=1)

buttonCount = tk.Button(mainw, text="Посчитать", command=count_minmax)
buttonCount.grid(row=5, column=1)

# Отображение
mainw.mainloop()