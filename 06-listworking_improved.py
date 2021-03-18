# Улучшенная схема 06-listworking.py
# Сделана проверка на корректность введённых пользователем данных,
# включая проверку на то, что введённое значение >=0 и <=14,
# а также идеальные неизменные размеры окна
# (Дарья Владимировна, добавьте эти обе вещи на постоянной основе 0_0)
# Также вместо цикла со счётчиком в диапазоне длины массива,
# сделан цикл с пробегом по всем элементам, 
# и вместо трёх переменных для сред использован словарь.
# Ну и конечно же, улучшение интерфейса)))

import tkinter as tk
import tkinter.messagebox as mb

mainw = tk.Tk()
mainw.title("Кислотность почв")
mainw.geometry("655x190")
mainw.minsize(width=655, height=190)
mainw.maxsize(width=655, height=190)

# Добавляем полосы прокрутки к двум боксам, на этот раз отдельно,
# потому что я заметил, что они достаточно багано работают,
# когда привязываешь их сразу к нескольких боксам

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
    # Делаем обработку ValueError (в какой уже раз #_#)
    try:
        k = float(entry.get())
        entry.delete(0, 'end')
        # Если введённое значение за гранью возможного, бросаем ошибку
        # и завершаем функцию ключевым словом return
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
    # Словарь вместо трёх переменных
    envs = {'acidic': 0, 'neutral': 0, 'alcaline': 0}
    # Более удобный и читабельный цикл
    for item in array:
        if float(item) < 7:
            envs['acidic'] += 1
        elif float(item) == 7:
            envs['neutral'] += 1
        else:
            envs['alcaline'] += 1
    box2.insert('end', "Кислые почвы на " + str(envs.get('acidic')) + " участках")
    box2.insert('end', "Нейтральные почвы на " + str(envs.get('neutral')) + " участках")
    box2.insert('end', "Щелочные почвы на " + str(envs.get('alcaline')) + " участках")

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