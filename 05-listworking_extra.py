# Дополнительное задание к уроку "Алгоритмы работы списков. Изменение цены"
# Задача: добавить к основному домашнему заданию возможность
# выбора пользователем количества пройденных недель и стороны времени
# (в будущем или в прошлом), а также в последний элемент Listbox'a записывать,
# насколько меньше или больше стала итоговая сумма, по сравнению с начальной
# Окно сделано в виде класса, наследованного от tkinter.Tk, вместо элемента в
# Listbox'е изменение суммы записывается в лейбл под ним.

# Импорт
import tkinter as tk
import tkinter.messagebox as mb

# Класс
class Stonks(tk.Tk):

    # Поле для цены, изменённой вычислениями
    newPrice = None

    # Самое утомительное - простые виджеты, которых очень много!

    def createLabelsAndEntries(self):
        self.labelEnter = tk.Label(self, text="Введите начальную цену", background='dimgrey', foreground='lightskyblue', borderwidth=5)
        self.labelEnter.grid(row=0, column=0, sticky='nsew')
        self.entryPrice = tk.Entry(self, background='lightskyblue', borderwidth=5)
        self.entryPrice.grid(row=1, column=0, sticky='nsew')
        self.labelChooseMode = tk.Label(self, text="Выберите направление подсчётов", background='dimgrey', foreground='lightskyblue', borderwidth=5)
        self.labelChooseMode.grid(row=2, column=0, sticky='nsew')
        self.labelCount = tk.Label(self, text="Рассчёт изменения цены", background='dimgrey', foreground='lightskyblue', borderwidth=5)
        self.labelCount.grid(row=0, column=1, sticky='nsew')
        self.labelWeeks = tk.Label(self, text="Введите количество недель", background='dimgrey', foreground='lightskyblue', borderwidth=5)
        self.labelWeeks.grid(row=5, column=0, sticky='nsew')
        self.entryWeeks = tk.Entry(self, background='lightskyblue', borderwidth=5)
        self.entryWeeks.grid(row=6, column=0, sticky='nsew')
        self.labelDifference = tk.Label(self, background='gold', foreground='forestgreen', borderwidth=5, height=2)
        self.labelDifference.grid(row=6, column=1, sticky='nsew', rowspan=2)

    def createListboxAndScrolls(self):
        self.scrollX = tk.Scrollbar(self, orient='horizontal')
        self.scrollX.grid(row=5, column=1, sticky='ew')
        self.scrollY = tk.Scrollbar(self, orient='vertical')
        self.scrollY.grid(row=1, column=2, rowspan=4, sticky='ns')
        self.box = tk.Listbox(self, xscrollcommand=self.scrollX.set, yscrollcommand=self.scrollY.set, width=40)
        self.box.grid(row=1, column=1, rowspan=4, sticky='nsew')
        self.scrollX.config(command=self.box.xview)
        self.scrollY.config(command=self.box.yview)

    # Создадим две радиокнопки для выбора пользователем направления подсчётов
    def createRadioButtons(self):
        # Создаём поле в классе типа tk.IntVar - специальный класс,
        # используемый для хранения данных из Checkbutton и Radiobutton (в данном случае именно целочисленных)
        self.futureOrPast = tk.IntVar()
        # Создаём радиокнопки, указываем в них нашу переменную в параметре variable,
        # и выставляем значение, которое кнопка будет возвращать, если именно она выбрана пользователем.
        # Я сделал 0 для будущего и 1 для прошлого
        self.buttonFuture = tk.Radiobutton(self, text="Будущее", variable=self.futureOrPast, value=0, background='peachpuff')
        self.buttonFuture.grid(row=3, column=0, sticky='nsew')
        self.buttonPast = tk.Radiobutton(self, text="Прошлое", variable=self.futureOrPast, value=1, background='peachpuff')
        self.buttonPast.grid(row=4, column=0, sticky='nsew')

    # Саме цикаве - функция подсчётов)))
    def __count__(self):
        # Как и в прошлые разы, перед операцией очищаем Listbox, если он не пустой
        if self.box.size() > 0:
            self.box.delete(0, 'end')
        # Обрабатываем ValueError. В поле для цены пользователь сможет ввести int и float,
        # а в поле для количества недель только int
        try:
            # Конвертируем в нужные типы из строки
            price = float(self.entryPrice.get())
            weeks = int(self.entryWeeks.get())
            # Устанавливаем начальную цену в поле
            self.newPrice = price
            # Такой же цикл, как в основном задании
            for i in range(weeks):
                # Только здесь проверяем направление, и либо умножаем, либо делим на 1.1
                # Используем метод get класса IntVar, также округляем значение до сотых
                if self.futureOrPast.get() == 0:
                    self.newPrice = round(self.newPrice * 1.1, 2)
                elif self.futureOrPast.get() == 1:
                    self.newPrice = round(self.newPrice / 1.1, 2)
                # Вставляем текст в Listbox
                self.box.insert('end', "Цена на " + str(i + 1) + " неделе составляет " + str(self.newPrice) + " грн.")
            # Используем тернарный оператор чтобы проверить, больше новая цена начальной или меньше,
            # и устанавливаем значением переменной слово, которое будет вставлено в строку - увеличилась или уменьшилась
            changes = "увеличилась" if self.newPrice > price else "уменьшилась"
            # Изменяем текст нижнего лейбла, обращаясь к полю 'text'
            # Для выведения разницы придётся использовать небольшую многоножку из функций:
            # округление до сотых, получение абсолютного значения и переведение в строку
            self.labelDifference['text'] = "За " + str(weeks) + " недель цена " + changes + " на\n" + str(abs(round(self.newPrice - price, 2))) + " грн."
        except ValueError:
            # Говорим пользователю, шо хтось накосячив 0_0
            mb.showerror("ОШИБКА", "Значение цены может быть только числового типа!\nКоличество недель может быть только целочисленного типа")

    # Создаём кнопку с ранее написанной функцией
    def createButton(self):
        self.buttonCount = tk.Button(self, text="Рассчитать", command=self.__count__)
        self.buttonCount.grid(row=7, column=0, sticky='nsew')

    # В конструкторе всё как в прошлые разы: инициализация суперкласса,
    # заголовок и идеальные неизменные размеры окна, вызов создания всех виджетов,
    # ну и запуск непрерывного отображения окна на экране
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Stonks")
        self.geometry("465x285")
        self.minsize(width=465, height=285)
        self.maxsize(width=465, height=285)
        self.createLabelsAndEntries()
        self.createListboxAndScrolls()
        self.createRadioButtons()
        self.createButton()
        self.mainloop()

# В запуске программы просто создаём экземпляр класса, даже без переменной
if __name__ == "__main__":
    Stonks()

# Спасибо за внимание)))