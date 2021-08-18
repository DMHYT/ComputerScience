import tkinter as tk
import tkinter.messagebox as mb
from urllib.request import urlopen
from json import loads

def get_dict_with_base(key):
    data = loads(urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read().decode('utf-8'))
    valute = data['Valute']
    for k in valute:
        valute[k]['Value'] = valute[k]['Value'] / valute[k]['Nominal']
        del valute[k]['ID']
        del valute[k]['NumCode']
        del valute[k]['CharCode']
        del valute[k]['Nominal']
        del valute[k]['Previous']
    if key.upper() == 'RUB':
        return (valute, "Российский рубль")
    else:
        newvalute = dict()
        neededvalue = valute[key]['Value']
        for k in valute:
            if k != key:
                newvalute[k] = valute[k]
        newvalute['RUB'] = {'Name': 'Российский рубль', 'Value': round(1 / neededvalue, 5)}
        for k in newvalute:
            if k != 'RUB':
                newvalute[k]['Value'] = round(newvalute[k]['Value'] / neededvalue, 5)
        return (newvalute, valute[key]['Name'])

class CurrenciesWindow(tk.Tk):

    currency = 'USD'
    cm = None

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Курс валют")
        self.resizable(0, 0)
        self.wm_attributes("-topmost", 1)
        self.label = tk.Label(self, text='Курс валюты ' + self.currency, font=('Helvetica', 14))
        self.label.grid(row=0, column=1, sticky='nsew')
        self.sx = tk.Scrollbar(self, orient='horizontal')
        self.sx.grid(row=2, column=1, sticky='ew')
        self.sy = tk.Scrollbar(self, orient='vertical')
        self.sy.grid(row=1, column=0, sticky='ns')
        self.box = tk.Listbox(self, width=40, height=20, xscrollcommand=self.sx.set, yscrollcommand=self.sy.set, font=('Helvetica', 14))
        self.box.grid(row=1, column=1, sticky='nsew')
        self.sx.config(command=self.box.xview)
        self.sy.config(command=self.box.yview)
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.selected_currency = tk.StringVar()
        self.selected_currency.set('USD')
        self.__update_box__()
        self.exchangemenu = tk.Menu(self)
        self.menu.add_cascade(label="Обмен", menu=self.exchangemenu)
        self.exchangemenu.add_command(label="Запустить обменник", command=self.__launch_exchanger__)
        self.selected_currency.trace('w', self.__update_box__)
        self.mainloop()
        
    def __update_box__(self, *args):
        key = self.selected_currency.get()
        self.box.delete(0, 'end')
        if self.cm != None:
            self.cm.destroy()
        self.currency = key
        dataname = get_dict_with_base(self.selected_currency.get())
        self.label['text'] = "Курс валюты " + key + "\n(" + dataname[1] + ")"
        data = {k: v for k, v in sorted(dataname[0].items(), key=lambda item: item[0])}
        self.menu.delete(0, 'end')
        self.cm = tk.Menu(self.menu)
        self.menu.add_cascade(label="Выбрать валюту", menu=self.cm)
        for k in data:
            self.box.insert('end', "1 " + str(data[k]['Name']) + " (" + str(k) + ") в " + self.selected_currency.get() + " - " + str(data[k]['Value']))
            self.cm.add_radiobutton(label=(k + " (" + data[k]['Name'] + ")"), value=k, variable=self.selected_currency)
    
    def __launch_exchanger__(self):
        ExchangeWindow(self.selected_currency.get(), self.selected_currency.get())
        try:
            self.destroy()
        except tk.TclError:
            pass

class ExchangeWindow(tk.Tk):

    currency_dict = None

    def __init__(self, currencyFrom, currencyTo):
        tk.Tk.__init__(self)
        self.selectedCurrencyFrom = tk.StringVar()
        self.selectedCurrencyTo = tk.StringVar()
        self.selectedCurrencyFrom.set(currencyFrom)
        self.selectedCurrencyTo.set(currencyTo)
        self.entryFrom_variable = tk.StringVar(self)
        self.entryTo_variable = tk.StringVar(self)
        self.title("Обмен валют")
        self.resizable(0, 0)
        self.wm_attributes("-topmost", 1)
        self.labelNameFrom = tk.Label(self, text=self.selectedCurrencyFrom.get(), font=('Helvetica', 14))
        self.labelNameFrom.grid(row=0, column=0, sticky='nsew')
        self.labelNameTo = tk.Label(self, text=self.selectedCurrencyTo.get(), font=('Helvetica', 14))
        self.labelNameTo.grid(row=0, column=1, sticky='nsew')
        self.entryValueFrom = tk.Entry(self, textvariable=self.entryFrom_variable, font=('Helvetica', 14))
        self.entryValueFrom.grid(row=1, column=0, sticky='nsew')
        self.entryFrom_variable.set("0")
        self.entryValueTo = tk.Entry(self, textvariable=self.entryTo_variable, font=('Helvetica', 14))
        self.entryValueTo.grid(row=1, column=1, sticky='nsew')
        self.entryTo_variable.set("0")
        self.entryFrom_variable.trace('w', self.__update_values_from__)
        self.entryTo_variable.trace('w', self.__update_values_to__)
        self.menuFrom = tk.Menu(self, tearoff=0)
        self.menuTo = tk.Menu(self, tearoff=0)
        self.labelNameFrom.bind_all("<Button-1>", self.show_menu_from)
        self.labelNameTo.bind_all("<Button-1>", self.show_menu_to)
        self.selectedCurrencyFrom.trace('w', self.__load_menu_contents__)
        self.selectedCurrencyTo.trace('w', self.__load_menu_contents__)
        self.__load_menu_contents__()
        self.mainloop()

    def __load_menu_contents__(self, *args):
        d = get_dict_with_base(self.selectedCurrencyFrom.get())
        self.currency_dict = {k: v for k, v in sorted(d[0].items(), key=lambda item: item[0])}
        self.currency_dict[self.selectedCurrencyFrom.get()] = {'Name': d[1], 'Value': 1}
        self.menuFrom.delete(0, 'end')
        self.menuTo.delete(0, 'end')
        for k in self.currency_dict:
            self.menuFrom.add_radiobutton(label=(k + " (" + self.currency_dict[k]['Name'] + ")"), value=k, variable=self.selectedCurrencyFrom)
            self.menuTo.add_radiobutton(label=(k + " (" + self.currency_dict[k]['Name'] + ")"), value=k, variable=self.selectedCurrencyTo)
        self.__update_labels__()
            
    def __update_labels__(self):
        print("Типа лейблы должны обновиться...")
        self.labelNameFrom['text'] = self.selectedCurrencyFrom.get()
        self.labelNameTo['text'] = self.selectedCurrencyTo.get()

    def __update_values_from__(self, *args):
        print("Типа обнова значений FROM")
        self.__update_labels__()
        val = self.entryFrom_variable.get()
        try:
            self.entryTo_variable.set(self.currency_dict[self.selectedCurrencyTo.get()]['Value'] * float(val))
        except ValueError:
            self.entryTo_variable.set("Ошибка")

    def __update_values_to__(self, *args):
        print("Типа обнова значений TO")
        self.__update_labels__()
        val = self.entryTo_variable.get()
        try:
            self.entryFrom_variable.set(1 / self.currency_dict[self.selectedCurrencyTo.get()]['Value'] * float(val))
        except ValueError:
            self.entryFrom_variable.set("Ошибка")

    def show_menu_from(self, event):
        self.menuFrom.post(0, self.labelNameFrom.winfo_reqheight())

    def show_menu_to(self, event):
        self.menuTo.post(self.labelNameFrom.winfo_reqwidth(), self.labelNameFrom.winfo_reqheight())

if __name__ == "__main__":
    CurrenciesWindow()