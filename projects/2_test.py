# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.messagebox as mb
from random import shuffle


class Variant:
    def __init__(self, text, correct=False):
        self.text = text
        self.correct = correct


class Question:
    def __init__(self, question, variants):
        self.question = question
        self.variants = variants


questions = [
    Question("Какая функция используется,\nчтобы напечатать текст в консоль?", [Variant("print", True), Variant("console.log"), Variant("cout")]),
    Question("Какая библиотека используется\nдля создания графического интерфейса?", [Variant("tkinter", True), Variant("time"), Variant("pyeel"), Variant("random")]),
    Question("Сколько библиотек можно импортировать\nв один скрипт?", [Variant("Бесконечное множество", True), Variant("Только одну"), Variant("Не более 5")]),
    Question("Какой тип данных может принимать значения\ntrue или false?", [Variant("bool", True), Variant("int"), Variant("float"), Variant("str"), Variant("dict")]),
    Question("Какой тип данных хранит\nпоследовательность символов?", [Variant("str", True), Variant("tuple"), Variant("dict"), Variant("char")]),
    Question("Какая библиотека используется\nдля генерации случайных чисел?", [Variant("random", True), Variant("tkinter.messagebox"), Variant("os"), Variant("time")]),
    Question("Какой модуль tkinter нужно использовать\nдля вывода диалоговых окон?", [Variant("messagebox", True), Variant("colorchooser"), Variant("font"), Variant("test")]),
    Question("Какая функция берёт данные\nу пользователя через консоль?", [Variant("input", True), Variant("prompt"), Variant("cin"), Variant("Entry")]),
    Question("Какой виджет tkinter мы используем для\nполучения ввода пользователя?", [Variant("Entry", True), Variant("Radiobutton"), Variant("Listbox"), Variant("Canvas")]),
    Question("Какой виджет tkinter мы используем для\nхранения табличных данных?", [Variant("Listbox", True), Variant("Canvas"), Variant("Button"), Variant("Label"), Variant("Tk")]),
    Question("Какой виджет tkinter мы используем для\nвывода какой-то надписи?", [Variant("Label", True), Variant("Listbox"), Variant("Canvas"), Variant("Checkbutton"), Variant("Entry")]),
    Question("Как импортировать библиотеку?", [Variant("Ключевое слово import название библиотеки", True), Variant("Ключевое слово IMPORT название библиотеки"), Variant("Функция require(название библиотеки)"), Variant("Ключевое слово #include <название библиотеки>")]),
    Question("Укажите среди перечисленных оператор\n\"НЕ РАВНО\"", [Variant("!=", True), Variant("=="), Variant("%"), Variant("//")]),
    Question("Выберите вариант с правильными операторами\n\"НЕ\", \"ИЛИ\", \"И\"", [Variant("not, or, and", True), Variant("*, |, &"), Variant("!, ||, &&")]),
    Question("Что выведет данный код?\nprint(\"2+1\")", [Variant("2+1", True), Variant("3"), Variant("21"), Variant("Ошибка")]),
    Question("Укажите среди перечисленных оператор\nостатка от деления", [Variant("%", True), Variant("//"), Variant("**"), Variant("^")]),
    Question("Укажите среди перечисленных оператор\nделения без остатка", [Variant("//", True), Variant("%"), Variant("<>"), Variant("^")]),
    Question("Что выведет данный код?\nprint(str(2+1))", [Variant("\"3\"", True), Variant("3"), Variant("2+1"), Variant("21"), Variant("ОШИБКА")]),
    Question("Что выведет данный код?\nprint(25//7)", [Variant("3", True), Variant("3.5714285714285716"), Variant("4"), Variant("25//7")]),
    Question("Что выведет данный код?\nprint(float(1))", [Variant("1.0", True), Variant("1"), Variant("\"1\""), Variant("True")]),
    Question("Что выведет данный код?\nprint(bool(1))", [Variant("True", True), Variant("False"), Variant("1.0"), Variant("\"1\"")]),
    Question("Что выведет данный код?\nprint(bool(0))", [Variant("False", True), Variant("True"), Variant("0.0"), Variant("\"0\"")]),
    Question("Что выведет данный код?\nprint(bool(999))", [Variant("True", True), Variant("False"), Variant("999.0"), Variant("\"999\"")]),
    Question("Какой метод tkinter.messagebox\nвыведет окно с ошибкой?", [Variant("showerror", True), Variant("showwarning"), Variant("showinfo"), Variant("_show")]),
    Question("Какой метод tkinter.messagebox\nвыведет окно с предупреждением?", [Variant("showwarning", True), Variant("showerror"), Variant("showinfo"), Variant("_show")]),
    Question("Какой метод tkinter.messagebox\nвыведет окно с информацией?", [Variant("showinfo", True), Variant("showwarning"), Variant("showerror"), Variant("_show")]),
    Question("В каком поле виджета tkinter.Label\nхранится сама надпись?", [Variant("text", True), Variant("background"), Variant("foreground")]),
    Question("Из перечисленного выберите метод,\nкоторый НЕ является методом списка", [Variant("join", True), Variant("append"), Variant("clear"), Variant("insert")]),
    Question("Что выведет данный код?\nprint(int(\"ЫЫЫЫЫ\"))", [Variant("Ошибка", True), Variant("\"ЫЫЫЫЫ\""), Variant("0"), Variant("None")]),
    Question("Какая функция используется для округления числа?", [Variant("round", True), Variant("pow"), Variant("str"), Variant("sorted")]),
    Question("Какая функция используется для\nпереведения чего-то в строку?", [Variant("str", True), Variant("float"), Variant("bool"), Variant("pow"), Variant("sorted")]),
    Question("Какой виджет tkinter создаёт кнопку с флажком\n и можно выделить несколько таких кнопок?", [Variant("Checkbutton", True), Variant("Radiobutton"), Variant("Button"), Variant("Entry")]),
    Question("Какой виджет tkinter создаёт кнопку-переключатель\n и можно выделить только одну такую кнопку?", [Variant("Radiobutton", True), Variant("Checkbutton"), Variant("Button"), Variant("Entry")]),
    Question("Какой виджет tkinter создаёт кнопку с\nпользовательской командой?", [Variant("Button", True), Variant("Radiobutton"), Variant("Checkbutton"), Variant("Entry")]),
    Question("Какой виджет tkinter создаёт полотно,\nна котором можно рисовать линии, фигуры и т.д.?", [Variant("Canvas", True), Variant("Listbox"), Variant("Entry"), Variant("Button")]),
    Question("Какой класс tkinter мы используем\nдля создания главного окна?", [Variant("Tk", True), Variant("Canvas"), Variant("Entry"), Variant("messagebox")]),
    Question("Установите соответствие между вызванными\nокнами и последовательностями названий\nimport tkinter.messagebox as mb\nmb.showinfo()\nmb.showerror()\nmb.showwarning()", [Variant("Информация, ошибка, предупреждение", True), Variant("Ошибка, информация, предупреждение"), Variant("Предупреждение, информация, ошибка"), Variant("Предупреждение, ошибка, информация")]),
    Question("Что выведет данный код?\nprint(not False and True or False)", [Variant("True", True), Variant("False"), Variant("Ошибка")]),
    Question("Какая из ниже перечисленных функций\nсортирует итерируемые объекты (списки)?", [Variant("sorted", True), Variant("max"), Variant("min"), Variant("sum")]),
    Question("Какая из ниже перечисленных функций\nвычисляет сумму элементов списка?", [Variant("sum", True), Variant("sorted"), Variant("max"), Variant("min")]),
    Question("Какого из ниже перечисленных типов данных\nНЕ существует в Python?", [Variant("object", True), Variant("str"), Variant("bool"), Variant("list"), Variant("dict")]),
    Question("Какой из ниже перечисленных типов данных\nНЕ является числовым?", [Variant("list", True), Variant("int"), Variant("float"), Variant("complex")]),
    Question("Какая функция из библиотеки random возвращает\nодин случайный элемент данного списка?", [Variant("choice", True), Variant("shuffle"), Variant("random"), Variant("randint")]),
    Question("Какое ключевое слово используется\nв Python для создания функции?", [Variant("def", True), Variant("class"), Variant("str"), Variant("for")]),
    Question("Какое из ниже перечисленных ключевых слов\nне касается циклов?", [Variant("if", True), Variant("for"), Variant("while"), Variant("in")]),
    Question("Какая функция возвращает список чисел\nв указанном диапазоне?", [Variant("range", True), Variant("pow"), Variant("sum"), Variant("sorted")]),
    Question("Какое ключевое слово в Python заменяет\nконструкцию else if из других языков?", [Variant("elif", True), Variant("else"), Variant("elf"), Variant("elseif")]),
    Question("Какое исключение вылезет, если\nне импортировать нужную библиотеку,\nили же обратиться к несуществующей переменной?", [Variant("NameError", True), Variant("ModuleNotFoundError"), Variant("ValueError"), Variant("ZeroDivisionError")]),
    Question("Какое исключение вылезет, если\nимпортировать несуществующую библиотеку?", [Variant("ModuleNotFoundError", True), Variant("NameError"), Variant("ValueError"), Variant("ZeroDivisionError")]),
    Question("Какое исключение вылезет при делении на ноль?", [Variant("ZeroDivisionError", True), Variant("ModuleNotFoundError"), Variant("NameError"), Variant("ValueError")])
]

class QuestionDialog(tk.Tk):

    buttonConfirm = None

    def __init__(self, qcount):
        tk.Tk.__init__(self)
        self.resizable(0, 0)
        self.wm_attributes("-topmost", 1)
        self.score = 0
        shuffle(questions)
        self.qs = questions[0:min(qcount, 50)]
        self.currentq = -1
        self.chosen = tk.IntVar()
        self.chosen.set(-1)
        self.label = tk.Label(self, font=('Helvetica', 14))
        self.label.grid(row=0, column=0, sticky='nsew')
        self.buttons = []
        self.update()
        self.mainloop()

    def __button_func__(self):
        neededButton = None
        for button in self.buttons:
            if button['value'] == 1:
                neededButton = button
                break
        if self.chosen.get() != 1:
            for button in self.buttons:
                if button != neededButton:
                    button['background'] = 'red'
        else:
            self.score += 1
        neededButton['background'] = 'green'
        mb.showinfo("ИНФО", "Ответ засчитан!")
        for button in self.buttons:
            button['background'] = 'white'
        self.chosen.set(-1)
        self.update()

    def update(self):
        if self.currentq + 1 < len(self.qs):
            self.currentq += 1
            self.title("ВОПРОС (" + str(self.currentq + 1) + " из " + str(len(self.qs)) + ")")
            q = self.qs[self.currentq]
            self.label['text'] = q.question
            self.label.grid(row=0, column=0, columnspan=len(q.variants), sticky='nsew')
            shuffle(q.variants)
            self.variants = [item for item in q.variants]
            for button in self.buttons:
                button.destroy()
            if self.buttonConfirm != None:
                self.buttonConfirm.destroy()
            self.buttons.clear()
            for i in range(len(q.variants)):
                self.buttons.append(tk.Radiobutton(self, text=q.variants[i].text, font=('Helvetica', 14), variable=self.chosen, value=(1 if q.variants[i].correct else -i)))
                self.buttons[i].grid(row=1+i, column=0, sticky='nsew')
            self.buttonConfirm = tk.Button(self, text="Подтвердить ответ", font=('Helvetica', 14), command=self.__button_func__)
            self.buttonConfirm.grid(row=len(q.variants)+1, column=0, sticky='nsew')
        else:
            mb.showinfo("ИНФО", "Тест завершён! Смотрите результаты!")
            EndWindow(self.score, len(self.qs))
            self.destroy()


class StartWindow(tk.Tk):

    def __start_test__(self):
        try:
            if int(self.entryCount.get()) < 5 or int(self.entryCount.get()) > 50:
                mb.showwarning("ВНИМАНИЕ", "Вопросов должно быть не менее 5 и не более 50!")
                return
            mb.showinfo("ИНФО", "Удачи в прохождении теста!")
            count = int(self.entryCount.get())
            self.destroy()
            QuestionDialog(count)
        except ValueError:
            mb.showerror("ОШИБКА", "Введённое количество вопросов должно быть целочисленного типа!")
            return

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("ТЕСТ")
        self.resizable(0, 0)
        self.wm_attributes("-topmost", 1)
        self.label = tk.Label(self, text="Тест по информатике\nпо теме \"Python\"\nВведите количество вопросов:", font=('Helvetica', 14))
        self.label.grid(row=0, column=0, sticky='nsew')
        self.entryCount = tk.Entry(self, font=('Helvetica', 14))
        self.entryCount.grid(row=1, column=0, sticky='nsew')
        self.buttonStart = tk.Button(self, text="Начать", font=('Helvetica', 14), command=self.__start_test__)
        self.buttonStart.grid(row=2, column=0, sticky='nsew')
        self.mainloop()


class EndWindow(tk.Tk):

    def __init__(self, score, maxscore):
        tk.Tk.__init__(self)
        self.title("Результаты теста")
        self.resizable(0, 0)
        self.wm_attributes("-topmost", 1)
        self.label = tk.Label(self, text="Ваш результат: " + str(score) + " из " + str(maxscore) + " баллов! (" + str(score / maxscore * 100) + "%)", font=('Helvetica', 14))
        self.label.grid(row=0, column=0, sticky='nsew')
        self.buttonOneMoreTime = tk.Button(self, text="Пройти ещё раз", font=('Helvetica', 14), command=self.__launch_new_test__)
        self.buttonOneMoreTime.grid(row=1, column=0, sticky='nsew')
        self.buttonEnd = tk.Button(self, text="Завершить", font=('Helvetica', 14), command=self.destroy)
        self.buttonEnd.grid(row=2, column=0, sticky='nsew')

    def __launch_new_test__(self):
        self.destroy()
        StartWindow()


if __name__ == "__main__":
    StartWindow()