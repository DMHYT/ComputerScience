import tkinter as tk
import tkinter.messagebox as mb
from urllib.request import urlopen
from json import loads


class CurrencyExchangeWindow(tk.Tk):

    currency = 'USD'
    menu = None
    cm = None

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Обмен валют")
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
        self.mainloop()
        
    def __update_box__(self):
        key = self.selected_currency.get()
        self.box.delete(0, 'end')
        if self.menu != None:
            self.menu.destroy()
        if self.cm != None:
            self.cm.destroy()
        self.currency = key
        dataname = self.__get_dict_with_base__()
        self.label['text'] = "Курс валюты " + key + "\n(" + dataname[1] + ")"
        data = {k: v for k, v in sorted(dataname[0].items(), key=lambda item: item[0])}
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.cm = tk.Menu(self.menu)
        self.menu.add_cascade(label="Выбрать валюту", menu=self.cm)
        self.cm.add_command(label="Подтвердить", command=self.__update_box__)
        self.cm.add_separator()
        for k in data:
            self.box.insert('end', str(data[k]['Name']) + " (" + str(k) + ") - " + str(round(data[k]['Value'], 2)))
            self.cm.add_radiobutton(label=(k + " (" + data[k]['Name'] + ")"), value=k, variable=self.selected_currency)

    def __get_dict_with_base__(self):
        key = self.selected_currency.get()
        data = loads(urlopen('https://www.cbr-xml-daily.ru/daily_json.js').read().decode('utf-8'))
        valute = data['Valute']
        for k in valute:
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
            newvalute['RUB'] = {'Name': 'Российский рубль', 'Value': 1 / neededvalue * 100}
            for k in newvalute:
                newvalute[k]['Value'] /= neededvalue
            return (newvalute, valute[key]['Name'])


if __name__ == "__main__":
    CurrencyExchangeWindow()