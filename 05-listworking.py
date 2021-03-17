# Импортируем tkinter (неужели это всё ещё нужно повторять? 0_0)
import tkinter as tk

# Создаём окно
mainw = tk.Tk()
mainw.title("Изменение цены")
mainw.geometry("400x200")

# Первая надпись
label1 = tk.Label(mainw, text="Введите начальную цену")
label1.grid(row=0, column=0)

# Поле ввода
entry = tk.Entry(mainw)
entry.grid(row=1, column=0)

# Вторая надпись
label2 = tk.Label(mainw, text="Рассчёт изменения цены")
label2.grid(row=0, column=1)

# Listbox, делаем параметр width 40 или больше,
# чтобы он получился не высоким, а длинным, как в образце
box = tk.Listbox(mainw, width=40)
box.grid(row=1, column=1, rowspan=2)

# Функция подсчёта цены в первые 4 недели
# (напомню, каждую неделю цена увеличивается на 10%)
def count_price_changing():
    # Берём ввод пользователя
    k = int(entry.get())
    # Цикл со счётчиком в диапазоне от 0 до 3
    for i in range(4):
        # Умножаем цену на 1.1, то есть, прибавляем 10%,
        # функцией round округляем до сотых (2 цифры после запятой, второй аргумент)
        z = round(k * 1.1, 2)
        # Вносим результат в Listbox
        st = "Цена на " + str(i + 1) + " неделе составляет " + str(z) + " грн."
        box.insert('end', st)
        # Присваиваем цене увеличенное значение
        k = z

# Создаём кнопку
buttonCount = tk.Button(mainw, text="Рассчитать", command=count_price_changing)
buttonCount.grid(row=2, column=0)

# Запускаем
mainw.mainloop()

# Скушна 0_0
# Предлагаю глянуть improved и extra версии)))