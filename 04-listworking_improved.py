# Улучшенная схема 04-listworking_common, объединяющая в себе два варианта
# реализации (с tkinter и без), и обрабатывающая ошибки, к которым
# уязвим код, данный в листинге
# Также добавлен момент очищения второго Listbox'a при повторе операции

import tkinter as tk
import tkinter.messagebox as mb

def window_mode():
    # От себя добавлю полосы прокрутки, общие для двух Listbox'ов,
    # и идеальные неизменные размеры окна
    mainw = tk.Tk()
    mainw.minsize(width=390, height=185)
    mainw.maxsize(width=390, height=185)
    mainw.title("Изменение значений")
    mainw.geometry("390x185")
    sx = tk.Scrollbar(mainw, orient='horizontal')
    sx.grid(column=2, row=5, columnspan=3, sticky='ew')
    sy = tk.Scrollbar(mainw, orient='vertical')
    sy.grid(column=1, row=1, rowspan=4, sticky='ns')
    box = tk.Listbox(mainw, yscrollcommand=sy.set, xscrollcommand=sx.set)
    box.grid(row=1, column=2, rowspan=3, sticky='nsew')
    sx.config(command=box.xview)
    sy.config(command=box.yview)
    entry = tk.Entry(mainw)
    entry.grid(row=1, column=3, sticky='ew')
    boxSq = tk.Listbox(mainw, yscrollcommand=sy.set, xscrollcommand=sx.set)
    boxSq.grid(row=1, column=4, rowspan=3)
    def add_item():
        entry_text = entry.get()
        # Если поле ввода пустое, не добавляем элемент в Listbox
        if len(entry_text) == 0:
            mb.showerror("ОШИБКА", "Не удалось получить введённые данные!")
            return
        box.insert('end', entry_text)
        entry.delete(0, 'end')
    def count_squares():
        # Если второй Listbox не пустой, чистим его
        if boxSq.size() > 0:
            boxSq.delete(0, 'end')
        elems = box.get(0, 'end')
        for item in elems:
            # Делаем обработку исключения ValueError
            # в случае введения пользователем НЕ числа
            try:
                k = int(item) ** 2
                boxSq.insert('end', k)
            except ValueError:
                # Просто вставляем INVALID
                boxSq.insert('end', 'INVALID')
    buttonAdd = tk.Button(mainw, text="Добавить", command=add_item)
    buttonAdd.grid(row=2, column=3, sticky='nsew')
    buttonCount = tk.Button(mainw, text="Посчитать", command=count_squares)
    buttonCount.grid(row=3, column=3, sticky='nsew')
    mainw.mainloop()

def console_mode():
    array = input("Введите список значений: ").split()
    arraySq = []
    for item in array:
        # Такую же обработку делаем в консольном режиме
        try:
            item = int(item)
            k = item ** 2
            arraySq.append(k)
        except ValueError:
            arraySq.append("INVALID")
    print("Список возведённых в квадрат значений: " + arraySq)

# Запуск программы абсолютно такой же, как в прошлом improved
if __name__ == "__main__":
    launchType = mb.askyesno("Выберите режим запуска", "Желаете запустить в окне? (если нет, запустится в консоли)")
    if launchType:
        window_mode()
    else:
        mb.showinfo("ИНФОРМАЦИЯ", "Посмотрите в консоль!")
        console_mode()