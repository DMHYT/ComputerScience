import tkinter as tk
import tkinter.messagebox as mb
from math import sqrt

class QuadraticEquation:

    a = None
    b = None
    c = None
    discr = None
    fr = None
    sr = None

    def set(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        self.discr = float(pow(self.b, 2) - 4 * self.a * self.c)

    def first_root(self):
        self.fr = (-self.b - sqrt(self.discr)) / (2 * self.a)

    def second_root(self):
        self.sr = (-self.b + sqrt(self.discr)) / (2 * self.a)

    def solve(self):
        self.set(float(entrya.get()), float(entryb.get()), float(entryc.get()))
        self.discriminant()
        if self.discr > 0:
            self.first_root()
            self.second_root()
        elif self.discr == 0:
            self.first_root()

    def detailed_solve(self):
        self.solve()
        disc = "D = b^2 - 4ac = " + str(self.b) + "^2 - 4 * " + str(self.a) + " * " + str(self.c) + " = " + str(self.discr) + (" > 0" if self.discr > 0 else (" < 0 -> НЕТ КОРНЕЙ" if self.discr < 0 else " = 0")) + ";\n"
        if self.discr < 0:
            pass
        elif self.discr > 0:
            disc += "x1 = (-b - sqrt(D)) / 2a = (" + str(-self.b) + " - sqrt(" + str(self.discr) + ")) / 2 * " + str(self.a) + " = " + str(self.fr) + ";\n"
            disc += "x2 = (-b + sqrt(D)) / 2a = (" + str(-self.b) + " + sqrt(" + str(self.discr) + ")) / 2 * " + str(self.a) + " = " + str(self.sr) + ";"
        else:
            disc += "x1 = (-b - sqrt(D)) / 2a = (" + str(-self.b) + " - sqrt(" + str(self.discr) + ")) / 2 * " + str(self.a) + " = " + str(self.fr) + ";\n"
        mb.showinfo("Решение через дискриминант", disc)
        if self.discr > 0:
            vieta = "По теореме Виета,\nx1 + x2 = -b,\nx1 * x2 = c;\nОтсюда следует,\nx1 + x2 = " + str(-self.b) + ",\nx1 * x2 = " + str(self.c) + ";\n"
            vieta += "x1 = " + str(self.fr) + ", x2 = " + str(self.sr) + ";"
            mb.showinfo("Решение по теореме Виета", vieta)
        else:
            vieta = "Невозможно решить данное уравнение по теореме Виета,\nт.к. оно не имеет корней или имеет только один корень!"
            mb.showwarning("Решение по теореме Виета", vieta)


equation = QuadraticEquation()

mainw = tk.Tk()
mainw.title("Калькулятор квадратных уравнений")
mainw.resizable(0, 0)
mainw.wm_attributes("-topmost", 1)

labelEquation = tk.Label(mainw, text='x^2 + x + 1 = 0', font=('Helvetica', 14))
labelEquation.grid(row=0, column=0, columnspan=3)

def updateEquation(*args):
    a = 1
    b = 1
    c = 1
    try:
        a = float(entrya.get())
        b = float(entryb.get())
        c = float(entryc.get())
    except ValueError:
        pass
    a = int(a) if float(a).is_integer() else float(a)
    b = int(b) if float(b).is_integer() else float(b)
    c = int(c) if float(c).is_integer() else float(c)
    eq = (str(a) if a != 1 and a != 0 else "") + ("x^2" if a != 0 else "") + " "
    eq += (("+ " + ("x" if b == 1 else (str(b) + "x" if b > 1 else "- " + str(-b) + "x"))) + " " if b != 0 else "")
    eq += (("+ " + str(c) if c > 0 and c != 0 else "- " + str(-c)) if c != 0 else "")
    eq += " = 0"
    labelEquation['text'] = eq
    equation.set(a, b, c)

a_listener = tk.StringVar()
a_listener.set("1")
a_listener.trace('w', updateEquation)

b_listener = tk.StringVar()
b_listener.set("1")
b_listener.trace('w', updateEquation)

c_listener = tk.StringVar()
c_listener.set("1")
c_listener.trace('w', updateEquation)

entrya = tk.Entry(mainw, textvariable=a_listener, font=('Helvetica', 14))
entrya.grid(row=2, column=0)

entryb = tk.Entry(mainw, textvariable=b_listener, font=('Helvetica', 14))
entryb.grid(row=2, column=1)

entryc = tk.Entry(mainw, textvariable=c_listener, font=('Helvetica', 14))
entryc.grid(row=2, column=2)

labelEnter = tk.Label(mainw, text="Введите коэффициенты", font=('Helvetica', 14))
labelEnter.grid(row=1, column=0, columnspan=3)

labelResult = tk.Label(mainw, text="Корни: ", font=('Helvetica', 14))
labelResult.grid(row=4, column=0, columnspan=3, sticky='nsew')

def solve():
    equation.solve()
    labelResult['text'] = "Корни: " + ((str(equation.fr) + ", " + str(equation.sr) if equation.fr != None else "НЕТ КОРНЕЙ!"))

buttonSolve = tk.Button(mainw, text="Решить", font=('Helvetica', 14), command=solve)
buttonSolve.grid(row=3, column=0, columnspan=3, sticky='nsew')

buttonDetailedSolve = tk.Button(mainw, text="Подробное решение", font=('Helvetica', 14), command=equation.detailed_solve)
buttonDetailedSolve.grid(row=5, column=0, columnspan=3, sticky='nsew')

mainw.mainloop()