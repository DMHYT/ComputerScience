# Дополнительное задание к уроку "Алгоритмы работы списков. Кислотность почв"
# Задача: улучшить основной вариант д/з тем, что в итоговые строчки
# правого Listbox'a, помимо количества участков с определённой кислотностью почвы,
# добавлять ещё перечисление этих участков.
# Делается очень просто, добавил буквально пару строчек к improved-версии

# # # # # # # # # # # # # # # # # # # #

def main():

    import tkinter as tk
    import tkinter.messagebox as mb

    mainw = tk.Tk()
    mainw.title("Кислотность почв")
    mainw.geometry("655x190")
    mainw.minsize(width=655, height=190)
    mainw.maxsize(width=655, height=190)

    scrollX1 = tk.Scrollbar(mainw, orient='horizontal')
    scrollX1.grid(row=3, column=1, sticky='ew')
    scrollY1 = tk.Scrollbar(mainw, orient='vertical')
    scrollY1.grid(row=0, column=0, rowspan=3, sticky='ns')
    box1 = tk.Listbox(mainw, width=40, height=10, xscrollcommand=scrollX1.set, yscrollcommand=scrollY1.set, background='peachpuff', foreground='red')
    box1.grid(row=0, column=1, rowspan=3)
    scrollX1.config(command=box1.xview)
    scrollY1.config(command=box1.yview)

    scrollX2 = tk.Scrollbar(mainw, orient='horizontal')
    scrollX2.grid(row=3, column=3, sticky='ew')
    scrollY2 = tk.Scrollbar(mainw, orient='vertical')
    scrollY2.grid(row=0, column=4, rowspan=3, sticky='ns')
    box2 = tk.Listbox(mainw, width=40, height=10, xscrollcommand=scrollX2.set, yscrollcommand=scrollY2.set, background='peachpuff', foreground='red')
    box2.grid(row=0, column=3, rowspan=3)
    scrollX2.config(command=box2.xview)
    scrollY2.config(command=box2.yview)

    entry = tk.Entry(mainw, background='lightskyblue', borderwidth=5)
    entry.grid(row=0, column=2, sticky='nsew')

    array = []

    def append_item():
        try:
            k = float(entry.get())
            entry.delete(0, 'end')
            if not (k >= 0 and k <=14):
                mb.showerror("ОШИБКА", "Кислотность среды не может быть ниже 0 или выше 14!")
                return
            box1.insert('end', "Кислотность на " + str(box1.size() + 1) + " участке составляет " + str(k))
            array.append(k)
        except ValueError:
            mb.showerror("ОШИБКА", "Значение кислотности среды может быть только числового типа!")
        

    def count_environments():
        if box2.size() > 0:
            box2.delete(0, 'end')
        # Принцип работы: значением элемента словаря, вместо числа 
        # количества участков с определённой кислотностью,
        # будет список чисел - номеров этих участков,
        # ну а само количество будет выводиться, как длина этого списка
        envs = {'acidic': [], 'neutral': [], 'alcaline': []}
        # Пришлось использовать некрасивый вариант цикла
        # для наличия доступа к индексу списка, к которому прибавляем 1
        # и получаем номер участка
        for i in range(len(array)):
            if float(array[i]) < 7:
                envs['acidic'].append(i + 1)
            elif float(array[i]) == 7:
                envs['neutral'].append(i + 1)
            else:
                envs['alcaline'].append(i + 1)
        # Используем здесь прикольную конструкцию с методом join, которая выведет все элементы списка в строчку через ;
        # (мне просто захотелось, чтобы список не выводился в квадратных скобках O_O)
        box2.insert('end', "Кислые почвы на " + str(len(envs.get('acidic'))) + " участках. Участки: " + "".join(str(x) + "; " for x in envs.get('acidic')))
        box2.insert('end', "Нейтральные почвы на " + str(len(envs.get('neutral'))) + " участках. Участки: " + "".join(str(x) + "; " for x in envs.get('neutral')))
        box2.insert('end', "Щелочные почвы на " + str(len(envs.get('alcaline'))) + " участках. Участки: " + "".join(str(x) + "; " for x in envs.get('alcaline')))

    def clear_all():
        box1.delete(0, 'end')
        box2.delete(0, 'end')
        array.clear()

    buttonAdd = tk.Button(mainw, text="Добавить", command=append_item, background='lavenderblush')
    buttonAdd.grid(row=1, column=2, sticky='nsew')

    buttonCount = tk.Button(mainw, text="Посчитать", command=count_environments, background='lavenderblush')
    buttonCount.grid(row=2, column=2, sticky='nsew')

    buttonClear = tk.Button(mainw, text="Очистить всё", command=clear_all, background='lavenderblush')
    buttonClear.grid(row=3, column=2, sticky='nsew')

    mainw.mainloop()

# # # # # # # # # # # # # # # # # # # #

if __name__ == "__main__":
    main()