# В improved-версии задания 03-listworking, в первую очередь,
# мы объединим два способа реализации в одну программу, а также
# в целом улучшим работу, простоту кода программы и интерфейс

# Импортируем нужные библиотеки
import tkinter as tk
import tkinter.messagebox as mb

# Разделим два способа по функциям
# Создаём две функции и просто списываем туда два задания

def window_mode():
    # От себя добавлю идеально подобранные и неизменные размеры окна,
    # красивое расположение виджетов, и полосы прокрутки
    mainw = tk.Tk()
    mainw.title("Количество одинаковых элементов в списке")
    mainw.minsize(width=330, height=215)
    mainw.maxsize(width=330, height=215)
    mainw.geometry("330x215")
    sx = tk.Scrollbar(mainw, orient='horizontal')
    sx.grid(column=2, row=5, sticky='ew')
    sy = tk.Scrollbar(mainw, orient='vertical')
    sy.grid(column=1, row=1, rowspan=4, sticky='ns')
    box = tk.Listbox(mainw, font='Helvetica', bg='black', fg='lightskyblue', yscrollcommand=sy.set, xscrollcommand=sx.set)
    box.grid(row=1, column=2, rowspan=4, sticky='nsew')
    sx.config(command=box.xview)
    sy.config(command=box.yview)
    entry = tk.Entry(mainw)
    entry.grid(row=1, column=3, sticky='ew')
    quantity = tk.Label(mainw)
    quantity.grid(row=2, column=3, sticky='nsew')
    def add_item():
        entry_text = entry.get()
        # Если поле ввода пустое, не добавляем элемент в Listbox
        if len(entry_text) == 0:
            mb.showerror("ОШИБКА", "Не удалось получить введённые данные!")
            return
        box.insert('end', entry_text)
        entry.delete(0, 'end')
    def count_equal_elements():
        array = []
        for item in box.get(0, 'end'):
            array.append(item)
        k = 1
        for i in range(len(array) - 1):
            if array[i + 1] == array[0]:
                k += 1
        quantity['text'] = "Элемент: \n" + str(array[0]) + ",\n количество: " + str(k)
    addButton = tk.Button(mainw, text="Добавить", command=add_item)
    addButton.grid(row=3, column=3, sticky='nsew')
    countButton = tk.Button(mainw, text="Посчитать", command=count_equal_elements)
    countButton.grid(row=4, column=3, sticky='nsew')
    mainw.mainloop()

def console_mode():
    array = input("Введите элементы списка: ").split()
    k = 1
    for i in range(len(array) - 1):
        if array[i + 1] == array[0]:
            k += 1
    print("Первый элемент, \"" + array[0] + "\", повторяется " + str(k) + " раз.")

# Дописываем запуск программы
if __name__ == "__main__":
    # Вызываем yesno, если True, запускаем окно, в противном случае запускаем программу в консоли
    launchType = mb.askyesno("Выберите режим запуска", "Желаете запустить в окне? (Если нет, запустится в консоли)")
    if launchType:
        window_mode()
    else:
        mb.showinfo("ИНФОРМАЦИЯ", "Посмотрите в консоль!")
        console_mode()