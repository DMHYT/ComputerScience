# Дополнительное задание к уроку "Повторение tkinter, Scrollbar и Listbox"
# Задача: добавить к основному домашнему заданию функцию
# записи данных в файл из Listbox
# Окно сделано в виде класса, наследованного от tkinter.Tk
# Также добавлена функция чтения данных из файла в Listbox,
# если этот файл уже был создан.
# При чтении данных из файла, программа спросит, очистить ли перед этим Listbox.

# Импортируем tkinter и messagebox
import tkinter as tk
import tkinter.messagebox as mb
# Также два метода из os:
# первый для получения расположения скрипта, второй для создания папки
from os import getcwd, mkdir
# И метод на проверку существования пути из os.path
from os.path import exists

# Создаём класс окна, наследуем от tkinter.Tk
class ListboxFileWriter(tk.Tk):

    # Файл, с которым мы будем работать, будет находиться по пути "путь_к_скрипту/ListboxWriter/generated.txt"
    # Такой путь мы и запишем в отдельное поле
    __file_path__ = getcwd() + "\\ListboxWriter\\generated.txt"

    # Разделим создание виджетов по функциям.
    # Сначала создадим Listbox и полосы прокрутки к нему
    def createBoxAndScrolls(self):
        # В объявлении виджетов ставим ключевое слово self вместо названия переменной окна,
        # так как мы сейчас типа находимся внутри этого окна 0_0
        self.scrollY = tk.Scrollbar(self, orient='vertical') # Одна полоса вертикальная
        # Используем параметры rowspan/columnspan и sticky,
        # чтобы полосы покрывали всё пространство под и слева от Listbox'а
        self.scrollY.grid(column=1, row=1, rowspan=3, sticky='ns')
        self.scrollX = tk.Scrollbar(self, orient='horizontal') # И другая полоса горизонтальная
        self.scrollX.grid(column=1, row=4, columnspan=3, sticky='ew')
        # Создаём сам Listbox, украшаем его, привязываем полосы прокрутки и делаем расположение
        self.listbox = tk.Listbox(self, font='Helvetica', bg='black', fg='lightskyblue', yscrollcommand=self.scrollY.set, xscrollcommand=self.scrollX.set)
        self.listbox.grid(row=1, column=2, rowspan=5, sticky='nsew')
        # А теперь наоборот, к полосам привязываем Listbox
        self.scrollY.config(command=self.listbox.yview)
        self.scrollX.config(command=self.listbox.xview)

    # Теперь функция создания поля ввода
    def createEntry(self):
        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=3, sticky='ew')

    # Перед тем, как создать кнопки, напишем для них функции
    # Первые две повторяем из основного д/з, только не забываем использовать ключевое слово self
    def __append_item_to_listbox__(self):
        self.listbox.insert('end', self.entry.get())
        self.entry.delete(0, 'end')

    def __delete_item_from_listbox__(self):
        try:
            select = self.listbox.curselection()
            self.listbox.delete(select)
        except tk.TclError:
            mb.showerror("ОШИБКА!", "Вы не выбрали элемент для удаления!")

    # Ну а теперь напишем функцию для записи элементов Listbox'a в файл
    def __write_items_to_file__(self):
        # При записи данных в файл мы также должны предусмотреть ту ситуацию, 
        # в которой ни файла, ни даже папки с ним не будет создано
        # (а такое будет, если кто-то захочет запустить скрипт у себя на компьютере в первый раз)
        # В случае отсутствия файла или папки вылезет FileNotFoundError, в блоке его обработки создадим папку, если даже её нет,
        # перевызовем функцию, и open уже сам создаст файл, дай ему только существующую папку
        try:
            # Открываем файл функцией open
            file = open(self.__file_path__, "w") # Открываем файл в режиме записи (w)
            # Делаем пробег по элементам Listbox'а, метод нашёл на StackOverflow
            for i, listbox_entry in enumerate(self.listbox.get(0, 'end')):
                # Записываем каждый в файл отдельной строкой
                file.write(str(listbox_entry))
                # Пишем перенос строки
                file.write("\n")
            mb.showinfo("ГОТОВО", "Все данные из Listbox'а успешно записаны в локальный файл!")
            file.close()
        # Если вылезает исключение
        except FileNotFoundError:
            # Проверяем наличие папки ListboxWriter функцией os.exists
            if not exists(getcwd() + "\\ListboxWriter\\"):
                # Если её нет, создаём её функцией os.mkdir
                mkdir(getcwd() + "\\ListboxWriter\\")
                # Вызываем функцию ещё раз
                self.__write_items_to_file__()
            # Других вариантов развития события быть просто не может
            else:
                mb.showerror("ОШИБКА", "Не удалось найти файл. На этом наши полномочия всё(((")

    # И напишем функцию для чтения элементов из файла и занесения их в Listbox
    def __read_items_from_file__(self):
        # Так же само обрабатываем FileNotFoundError
        try:
            # На этот раз открываем файл в режиме чтения (r)
            file = open(self.__file_path__, "r")
            # Получаем список всех строк файла методом readlines
            lines = file.readlines()
            # Вызываем YesNo окно, спрашиваем у пользователя, опустошить ли Listbox
            if mb.askyesno("ПРИМЕЧАНИЕ", "Очистить ли Listbox перед внесением в него данных из файла"):
                self.listbox.delete(0, 'end')
            # Циклом по списку строк вставляем их в Listbox
            for item in lines:
                self.listbox.insert('end', item)
            file.close()
        except FileNotFoundError:
            # Здесь просто вызываем ошибку, так как перед тем, как использовать эту функцию,
            # пользователь должен был хотя бы один раз произвести запись в файл
            mb.showError("ОШИБКА", "Вы ещё ни разу не создавали файл, или же удалили его. Не удалось прочитать данные из файла!")

    # Ну и теперь создадим сами кнопки с соответствующими функциями
    def createButtons(self):
        self.button_append = tk.Button(self, text="Добавить", command=self.__append_item_to_listbox__)
        self.button_append.grid(row=2, column=3, sticky='nsew')
        self.button_delete = tk.Button(self, text="Удалить", command=self.__delete_item_from_listbox__)
        self.button_delete.grid(row=3, column=3, sticky='nsew')
        self.button_write = tk.Button(self, text="Записать в файл", command=self.__write_items_to_file__)
        self.button_write.grid(row=4, column=3, sticky='nsew')
        self.button_read = tk.Button(self, text="Прочитать из файла", command=self.__read_items_from_file__)
        self.button_read.grid(row=5, column=3, sticky='nsew')
    
    # И наконец, в конструкторе вызовем __init__ суперкласса,
    # укажем одинаковые минимальные и максимальные размеры, чтобы они были неизменными.
    # Укажем заголовок и начальные размеры, и в завершение создадим все виджеты функциями
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(width=330, height=215)
        self.maxsize(width=330, height=215)
        self.title("ListboxFileWriter")
        self.geometry("330x215")
        self.createBoxAndScrolls()
        self.createEntry()
        self.createButtons()
        self.mainloop()


# Наконец, дописываем запуск программы, просто создаём окно
if __name__ == "__main__":
    main_window = ListboxFileWriter()

# Спасибо за внимание)))