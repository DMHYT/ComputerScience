import tkinter as tk

mainw = tk.Tk()
mainw.title("Кислотность почв")
mainw.geometry("610x200")

box1 = tk.Listbox(mainw, width=40, height=10)
box1.grid(row=0, column=0, rowspan=3)

entry = tk.Entry(mainw)
entry.grid(row=0, column=1)

box2 = tk.Listbox(mainw, width=40, height=10)
box2.grid(row=0, column=2, rowspan=3)

array = []

def append_item():
    k = entry.get()
    size = box1.size()
    string = "Кислотность на " + str(size + 1) + " участке составляет " + k
    box1.insert('end', string)
    entry.delete(0, 'end')
    array.append(k)

def count_environments():
    box2.delete(0, 'end')
    acidic = 0
    neutral = 0
    alcaline = 0
    for i in range(len(array)):
        if float(array[i]) < 7:
            acidic += 1
        elif float(array[i]) == 7:
            neutral += 1
        else:
            alcaline += 1
    box2.insert('end', "Кислые почвы на " + str(acidic) + " участках")
    box2.insert('end', "Нейтральные почвы на " + str(neutral) + " участках")
    box2.insert('end', "Щелочные почвы на " + str(alcaline) + " участках")

def clear_all():
    box1.delete(0, 'end')
    box2.delete(0, 'end')
    array.clear()

buttonAdd = tk.Button(mainw, text="Добавить", command=append_item)
buttonAdd.grid(row=1, column=1)

buttonCount = tk.Button(mainw, text="Посчитать", command=count_environments)
buttonCount.grid(row=2, column=1)

buttonClear = tk.Button(mainw, text="Очистить всё", command=clear_all)
buttonClear.grid(row=3, column=1)

mainw.mainloop()