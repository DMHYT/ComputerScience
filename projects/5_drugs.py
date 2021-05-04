import tkinter as tk
import tkinter.messagebox as mb

drugs = []
def load_list():
    from urllib.request import urlopen
    from json import loads
    global drugs
    drugs = loads(urlopen("https://raw.githubusercontent.com/dariusk/corpora/master/data/medicine/drugs.json").read().decode('utf-8'))['drugs']
load_list()
drugs = sorted(drugs, reverse=False)

mainw = tk.Tk()
mainw.title("Drugs Database")
mainw.resizable(0, 0)
mainw.wm_attributes("-topmost", 1)

label = tk.Label(mainw, text="Введите название лекарства", font=('Helvetica', 14))
label.grid(row=0, column=0, columnspan=2, sticky='nsew')
entry_listener = tk.StringVar()
entry_listener.set("")
entry = tk.Entry(mainw, textvariable=entry_listener, font=('Helvetica', 14))
entry.grid(row=1, column=1, sticky='nsew')

sx = tk.Scrollbar(mainw, orient='horizontal')
sx.grid(row=3, column=1, sticky='ew')
sy = tk.Scrollbar(mainw, orient='vertical')
sy.grid(row=1, column=0, rowspan=2, sticky='ns')
box = tk.Listbox(mainw, xscrollcommand=sx.set, yscrollcommand=sy.set, width=40, height=20, font=('Helvetica', 14))
box.grid(row=2, column=1, sticky='nsew')

def update_box(*args):
    box.delete(0, 'end')
    if len(entry.get()) == 0:
        for drug in drugs:
            box.insert('end', drug)
        return
    for drug in drugs:
        if drug.startswith(entry.get()):
            box.insert('end', drug)
    if len(box.get(0, 'end')) == 0:
        box.insert('end', "Результаты по запросу " + entry.get() + " не найдены!")

update_box()

entry_listener.trace('w', update_box)

mainw.mainloop()