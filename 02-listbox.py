# Импортируем библиотеку tkinter,
# для упрощения написания кода переименовываем в tk
import tkinter as tk

# Создаём окно, указываем его заголовок и размеры
main = tk.Tk()
main.title("Списки")
main.geometry("300x300") # (длина)x(ширина)

# Создаём объект Listbox, привязываем его к окну
# и выводим на экран методом pack
box = tk.Listbox(main)
box.pack()

# Создаём поле ввода, так же сам привязываем и отображаем
entry = tk.Entry(main)
entry.pack()

# Создаём функцию добавления элемента в Listbox из поля ввода
def add_item():
    # Вставляем в конец списка то, что ввёл пользователь в entry
    box.insert(tk.END, entry.get())
    # Очищаем поле ввода
    entry.delete(0, tk.END)

# Теперь функция удаления тех элементов, которые пользователь выделит
def del_list():
    # Получаем элементы, выделенные пользователем в данный момент
    select = box.curselection()
    # Удаляем их из Listbox
    box.delete(select)

# Далее добавляем и отображаем кнопки добавления и удаления элементов Listbox
# Вставляем в них соответствующие функции, написанные ранее

addButton = tk.Button(main, text="Добавить", command=add_item)
addButton.pack()

delButton = tk.Button(main, text="Удалить", command=del_list)
delButton.pack()

# Запускаем непрерывный цикл отображения окна
main.mainloop()