# Простой вспомогательный скрипт для теста алгоритмов обработки списков, а точнее Listbox
# Способ использования:
# 1) Переместить скрипт в одну директорию с вашей программой
# 2) Прописать в вашей программе "from listbox_filler import Window as FillerWindow"
# 3) После всего кода вашего окна, и ДО непрерывного его отображения, написать:
# "FillerWindow(ваш Listbox)"
# 4) Запустить свою программу. Вместе с вашим окном вылезет и окно этого скрипта.
# 5) Ввести диапазон значений чисел и их количество, которое будет вставлено в Listbox.
# 6) Нажать на кнопку "ВСТАВИТЬ". Числа появятся в соответствующем Listbox'е в вашем окне.

import tkinter as tk
import tkinter.messagebox as mb
from random import randint

class Window(tk.Tk):
    
    def createWidgets(self):
        self.labelDiapason = tk.Label(self, text="Укажите диапазон значений")
        self.labelDiapason.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.labelFrom = tk.Label(self, text="ОТ")
        self.labelFrom.grid(row=1, column=0, sticky='nsew')
        self.labelTo = tk.Label(self, text="ДО")
        self.labelTo.grid(row=1, column=1, sticky='nsew')
        self.entryFrom = tk.Entry(self)
        self.entryFrom.grid(row=2, column=0, sticky='nsew')
        self.entryTo = tk.Entry(self)
        self.entryTo.grid(row=2, column=1, sticky='nsew')
        self.labelCount = tk.Label(self, text="Количество значений: ")
        self.labelCount.grid(row=3, column=0, sticky='nsew')
        self.entryCount = tk.Entry(self)
        self.entryCount.grid(row=3, column=1, sticky='nsew')

    def __put__(self):
        try:
            self.box.delete(0, 'end')
            for i in range(int(self.entryCount.get())):
                self.box.insert('end', randint(int(self.entryFrom.get()), int(self.entryTo.get())))
        except ValueError:
            mb.showerror("ОШИБКА", "Вы ввели некорректные данные!")

    def createButton(self):
        self.button = tk.Button(self, text="ВСТАВИТЬ", command=self.__put__)
        self.button.grid(row=4, column=0, columnspan=2, sticky='nsew')

    def __init__(self, box):
        tk.Tk.__init__(self)
        self.box = box        
        self.title("Listbox Filler")
        self.minsize(width=250, height=105)
        self.maxsize(width=250, height=105)
        self.geometry("250x105")
        self.createWidgets()
        self.createButton()
        self.mainloop()