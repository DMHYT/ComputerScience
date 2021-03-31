# Дополнительное задание к уроку "Алгоритмы обработки списков. Сортировка"
# Задача: реализовать сложную сортировку: брать у пользователя
# ввод фамилии и имени ученика через пробел, либо же его года рождения, в другом поле ввода,
# также пользователь должен выбрать, нажав на кнопку, по чём сортировать, по ФИ или по году.
# Если по ФИ, должна произойти сортировка по первым буквам фамилии, если они совпадают, по первым буквам имени.
# Если по году, то если года нескольких учеников совпадают, произвести сортировку по ФИ.
# Задание выполнил достаточно красиво, по мере выполнения узнал немного нового)

# Импортируем библиотеки: сам tkinter,
# messagebox для выведения всплывающих окон с ошибками,
# а также метод itemgetter из библиотеки operator,
# он нам понадобится при использовании функции sorted
import tkinter as tk
import tkinter.messagebox as mb
from operator import itemgetter

# Окно
mainw = tk.Tk()
mainw.title("Школьный журнал (alpha)")
mainw.minsize(width=405, height=255)
mainw.maxsize(width=405, height=255)
mainw.geometry("405x255")

# Listbox с полосами прокрутки
sx = tk.Scrollbar(mainw, orient='horizontal')
sx.grid(row=9, column=1, sticky='ew')
sy = tk.Scrollbar(mainw, orient='vertical')
sy.grid(row=0, column=0, rowspan=9, sticky='ns')
box = tk.Listbox(mainw, background='peachpuff', foreground='red', xscrollcommand=sx.set, yscrollcommand=sy.set, width=35)
box.grid(row=0, column=1, rowspan=9, sticky='nsew')
sx.config(command=box.xview)
sy.config(command=box.yview)

# Надписи и поля ввода ФИ и года рождения
labelName = tk.Label(mainw, text="Введите фамилию и имя", background='dimgrey', foreground='lightskyblue', borderwidth=5)
labelName.grid(row=0, column=2, sticky='nsew')
entryName = tk.Entry(mainw, background='lightskyblue', borderwidth=5)
entryName.grid(row=1, column=2, sticky='nsew')
labelYear = tk.Label(mainw, text="Введите год рождения", background='dimgrey', foreground='lightskyblue', borderwidth=5)
labelYear.grid(row=2, column=2, sticky='nsew')
entryYear = tk.Entry(mainw, background='lightskyblue', borderwidth=5)
entryYear.grid(row=3, column=2, sticky='nsew')

labelChoice = tk.Label(mainw, text="Выберите режим сортировки", background='dimgrey', foreground='lightskyblue', borderwidth=5)
labelChoice.grid(row=4, column=2, sticky='nsew')
# Radiobutton'ы для выбора режима сортировки
choice = tk.IntVar()
radioName = tk.Radiobutton(mainw, text='Фамилия и имя', variable=choice, value=0, background='peachpuff')
radioName.grid(row=5, column=2, sticky='nsew')
radioYear = tk.Radiobutton(mainw, text='Год рождения', variable=choice, value=1, background='peachpuff')
radioYear.grid(row=6, column=2, sticky='nsew')

# Функция добавления элемента в Listbox будет не такая, как обычно
def append_item():
    # Сделаем несколько проверок, а именно:
    # наличие ввода ФИ, наличие ввода года рождения, и именно два слова в поле ввода ФИ
    if len(entryName.get()) == 0:
        mb.showerror("ОШИБКА", "Вы не ввели фамилию и имя!")
        return
    if len(entryYear.get()) == 0:
        mb.showerror("ОШИБКА", "Вы не ввели год рождения")
        return
    if len(str(entryName.get()).split()) != 2:
        mb.showerror("ОШИБКА", "Вам необходимо ввести имя и фамилию соответственно через пробел!")
        return
    # Создаём переменную для года, и обработкой ValueError проверяем корректность его ввода
    year = None
    try:
        year = int(entryYear.get())
    except ValueError:
        mb.showerror("ОШИБКА", "Год рождения должен быть целочисленного типа!")
        return
    # Вставляем в Listbox строку вида: "Имя Фамилия Год"
    box.insert('end', entryName.get() + " " + str(year))
    # Очищаем оба поля ввода
    entryName.delete(0, 'end')
    entryYear.delete(0, 'end')

# И сердце этой программы - функция сортировки
# Вместо того, чтобы сразу начать объяснять строчки кода, было бы удобнее
# для начала набросать алгоритм пошагово:
# 1) Получаем список элементов Listbox'а и очищаем его
# 2) Сортируем всё в алфавитном порядке, и если выбран режим сортировки по ФИ, завершаем работу
# 3) Если выбран режим сортировки по годам, начинаем c создания специального списка, его
# элементами будут кортежи из двух элементов: строковое ФИ и числовой год. Наполняем его
# циклом по элементам, разрезая строку на три части и создавая кортеж из двух.
# 4) Создаём конечный список кортежей сдвоенной сортировкой: первая по ФИ, вторая по году.
# 5) Наконец вставляем всё в Listbox
def sort_box():
    # По стандарту для удобства закидываем содержимое Listbox'а в отдельный список
    array = []
    for item in box.get(0, 'end'):
        array.append(item)
    # Уже здесь очищаем Listbox
    box.delete(0, 'end')
    # Сортируем список в алфавитном порядке
    sorted_first = sorted(array, reverse=False)
    # Если выбрана сортировка по ФИ, вставляем все элементы обратно в Listbox и на этом всё
    if choice.get() == 0:
        for item in sorted_first:
            box.insert('end', item)
    # Если же выбрана сортировка по году...
    else:
        # Создаём список для кортежей с ФИ и годом каждого ученика
        tuples = []
        # Цикл по отсортированному по алфавиту списку
        for item in sorted_first:
            # Разрезаем строку, получается список из трёх строк: фамилия, имя и год
            split = str(item).split()
            # Добавляем новый кортеж в список
            tuples.append(
                tuple([
                    split[0] + " " + split[1], # Соединяем фамилию с именем
                    int(split[2]) # Конвертируем в число
                ])
            )
        # Конечная сортировка
        finally_sorted = sorted(
            sorted(
                # Внутри сортируем кортежи по алфавиту, используем itemgetter,
                # вводим индекс ФИ в кортеже (0)
                tuples, reverse=False, key=itemgetter(0)
            ),
            # Внешне сортируем по годам в порядке возрастания,
            # itemgetter по второму элементу кортежа
            reverse=False, key=itemgetter(1)
        )
        # Вставляем всё в Listbox
        for item in finally_sorted:
            box.insert('end', item[0] + " " + str(item[1]))
    print("DEBUG: Сортировка прошла успешно!")

# Кнопки и запуск

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item, background='lavenderblush')
buttonAdd.grid(row=7, column=2, sticky='nsew')

buttonSort = tk.Button(mainw, text="Рассортировать", command=sort_box, background='lavenderblush')
buttonSort.grid(row=8, column=2, sticky='nsew')

mainw.mainloop()

# Спасибо за внимание)))