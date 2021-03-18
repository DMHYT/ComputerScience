# Дополнительное задание к уроку "Алгоритмы обработки списков"
# Задача, добавить к основному домашнему заданию отдельный Listbox,
# на котором будет показан каждый элемент с количеством его повторений в списке
# Окно сделано в виде класса, наследованного от tkinter.Tk,
# Для сохранения количества повторений каждого элемента использован словарь,
# также возвращена кнопка удаления элемента из предыдущего урока,
# и добавлена кнопка очистки обеих Listbox'ов

# Импортируем библиотеки
import tkinter as tk
import tkinter.messagebox as mb

# Создаём класс окна, наследуемый от tkinter.Tk
class ListboxElementCounter(tk.Tk):

    # Как и в прошлый раз, разделим создание виджетов по функциям
    # Сначала, основной Listbox с полосами прокрутки к нему
    def createMainListbox(self):
        self.scrollY = tk.Scrollbar(self, orient='vertical')
        self.scrollY.grid(column=1, row=1, rowspan=4, sticky='ns')
        self.scrollX = tk.Scrollbar(self, orient='horizontal')
        self.scrollX.grid(column=2, row=5, sticky='ew')
        self.listbox = tk.Listbox(self, font='Helvetica', bg='black', fg='lightskyblue', yscrollcommand=self.scrollY.set, xscrollcommand=self.scrollX.set)
        self.listbox.grid(row=1, column=2, rowspan=4, sticky='nsew')
        self.scrollY.config(command=self.listbox.yview)
        self.scrollX.config(command=self.listbox.xview)

    # Поле ввода
    def createEntry(self):
        self.entry = tk.Entry(self)
        self.entry.grid(row=1, column=3, sticky='ew')

    # Теперь отдельно функции кнопок, первые две списываем с прошлого урока

    def __append_item_to_listbox__(self):
        entry_text = self.entry.get()
        # Если поле ввода пустое, не добавляем элемент в Listbox
        if len(entry_text) == 0:
            mb.showerror("ОШИБКА", "Не удалось получить введённые данные!")
            return
        self.listbox.insert('end', entry_text)
        self.entry.delete(0, 'end')
    
    def __delete_item_from_listbox__(self):
        try:
            select = self.listbox.curselection()
            self.listbox.delete(select)
        except tk.TclError:
            mb.showerror("ОШИБКА", "Вы не выбрали элементы для удаления!")
    
    # Теперь создаём Listbox для отсортированных количеств повторений каждого элемента
    def createSortedListbox(self):
        self.scrollYSorted = tk.Scrollbar(self, orient='vertical')
        self.scrollYSorted.grid(column=5, row=1, rowspan=4, sticky='ns')
        self.scrollXSorted = tk.Scrollbar(self, orient='horizontal')
        self.scrollXSorted.grid(column=4, row=5, sticky='ew')
        self.listboxSorted = tk.Listbox(self, font='Helvetica', bg='black', fg='lightskyblue', yscrollcommand=self.scrollYSorted.set, xscrollcommand=self.scrollXSorted.set)
        self.listboxSorted.grid(row=1, column=4, rowspan=4, sticky='nsew')
        self.scrollYSorted.config(command=self.listboxSorted.yview)
        self.scrollXSorted.config(command=self.listboxSorted.xview)

    # Та самая функция сортировки
    def __sort_items_counts__(self):
        # Очищаем сортированный Listbox перед операцией, если он не пустой
        if self.listboxSorted.size() > 0:
            self.listboxSorted.delete(0, 'end')
        # Создаём словарь
        sortedDict = dict()
        # Перекидываем элементы Listbox'а в новосозданный список, для удобства
        items = []
        for item in self.listbox.get(0, 'end'):
            items.append(item)
        # Делаем пробег циклом по списку элементов
        for item in items:
            # Используем метод словаря get, возвращает элемент, если он найден 
            # по данному ключу, и None, если элемента нет
            if sortedDict.get(item) != None:
                # Если элемент найден, прибавляем к нему 1
                # (все элементы в этом словаре будут целыми числами, 
                # обозначающими количество повторения определённого элемента Listbox'а)
                sortedDict[item] = sortedDict[item] + 1
            else:
                # Если элемент не найден, создаём его и присваиваем значение 1,
                # то есть, мы уже нашли 1 элемент, равный item
                sortedDict[item] = 1
        # Делаем пробег циклом по парам из ключа и значения, словаря 
        # (представляет собой список из двух элементов)
        for item in sortedDict.items():
            # Вписываем в Listbox запись формата: "элемент" - количество_раз.
            self.listboxSorted.insert('end', "\"" + item[0] + "\" - " + str(item[1]) + ".")
    
    # Теперь простенькая функция, очищающая оба Listbox'а
    def __clear_all__(self):
        self.listbox.delete(0, 'end')
        self.listboxSorted.delete(0, 'end')

    # Наконец функция создания всех кнопок
    def createButtons(self):
        self.button_append = tk.Button(self, text="Добавить", command=self.__append_item_to_listbox__)
        self.button_append.grid(row=2, column=3, sticky='nsew')
        self.button_delete = tk.Button(self, text="Удалить", command=self.__delete_item_from_listbox__)
        self.button_delete.grid(row=3, column=3, sticky='nsew')
        self.button_sort = tk.Button(self, text="Рассортировать", command=self.__sort_items_counts__)
        self.button_sort.grid(row=4, column=3, sticky='nsew')
        self.button_clear = tk.Button(self, text="Очистить всё", command=self.__clear_all__)
        self.button_clear.grid(row=5, column=3, sticky='nsew')

    # И в конструкторе создаём окно, указываем идеальные неизменные размеры,
    # функциями создаём все виджеты и запускаем непрерывное отображение
    def __init__(self):
        tk.Tk.__init__(self)
        self.minsize(width=530, height=225)
        self.maxsize(width=530, height=225)
        self.title("ListboxElementCounter")
        self.geometry("530x225")
        self.createMainListbox()
        self.createEntry()
        self.createSortedListbox()
        self.createButtons()
        self.mainloop()

# Дописываем запуск программы
if __name__ == "__main__":
    # Просто создаём экземпляр класса
    window = ListboxElementCounter()

# Спасибо за внимание)))