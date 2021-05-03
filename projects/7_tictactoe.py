import tkinter as tk
import tkinter.messagebox as mb
from time import sleep
from random import randint


mainw = tk.Tk()
app_running = True
size_canvas_x = size_canvas_y = 240
s_x = s_y = 3 # НЕ МЕНЯТЬ, WIP
step_x = size_canvas_x // s_x
step_y = size_canvas_y // s_y
size_canvas_x = step_x * s_x
size_canvas_y = step_y * s_y
txt_len_middle = "* Игрок vs Игрок"
size_font_x = 10
len_txt_x = len(txt_len_middle) * size_font_x
delta_menu_x = len_txt_x // step_x + 1
menu_x = step_x * delta_menu_x
crosses = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]
noughts = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]
list_ids = []
is_cross_turn = True
is_vs_ai = False
icon_tag = []

def on_closing():
    global app_running
    if mb.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        app_running = False
        mainw.destroy()

mainw.protocol("WM_DELETE_WINDOW", on_closing)
mainw.title("Крестики-нолики")
mainw.resizable(0, 0)
mainw.wm_attributes("-topmost", 1)
cvs = tk.Canvas(mainw, width=size_canvas_x + menu_x, height=size_canvas_y, bd=0, highlightthickness=0)
cvs.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill='white')
cvs.pack()
mainw.update()

def draw_table():
    for i in range(0, s_x + 1):
        cvs.create_line(step_x * i, 0, step_x * i, size_canvas_y)
    for i in range(0, s_y + 1):
        cvs.create_line(0, step_y * i, size_canvas_x, step_y * i)
draw_table()

def change_var():
    global is_vs_ai
    is_vs_ai = is_vs_ai_var.get()

is_vs_ai_var = tk.BooleanVar()
rb1 = tk.Radiobutton(mainw, text="Игрок vs ИИ", variable=is_vs_ai_var, value=1, command=change_var)
rb2 = tk.Radiobutton(mainw, text="Игрок vs Игрок", variable=is_vs_ai_var, value=0, command=change_var)
rb1.place(x=size_canvas_x+menu_x//2-rb1.winfo_reqwidth()//2, y=40)
rb2.place(x=size_canvas_x+menu_x//2-rb2.winfo_reqwidth()//2, y=60)
if is_vs_ai:
    rb1.select()

def mark_turn(is_cross):
    icon_tag = 0
    # if is_cross:
    #     crosses[y][x] = 1
    #     list_ids.append(cvs.create_line(, fill='red', width=5))
    #     list_ids.append(cvs.create_line(, fill='red', width=5))
    # else:
    #     noughts[y][x] = 1
    #     list_ids.append(cvs.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill='blue'))
    #     list_ids.append(cvs.create_oval(x * step_x + step_x // 3, y * step_y + step_y // 3, x * step_x + step_x - step_x // 3, y * step_y + step_y - step_y // 3, fill='white'))
mark_turn(is_cross_turn)

def restart():
    global list_ids, crosses, noughts
    for el in list_ids:
        cvs.delete(el)
    list_ids = []
    crosses = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]
    noughts = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]
    is_cross_turn = True

buttonRestart = tk.Button(mainw, text="Начать заново", command=restart)
buttonRestart.place(x=size_canvas_x+menu_x//2-buttonRestart.winfo_reqwidth()//2, y=10)

def cut_combinations(lst):
    result = []
    for i in range(3, len(lst) + 1):
        j = 0
        while len(lst[j:len(lst)-1]) >= 2:
            result.append(lst[j:j+i])
            j += 1
    return result

# def create_diagonal_up_line(x, y):
#     global s_x, s_y
#     result = []
#     for xx in range(s_x):
#         if s_x - xx + x < s_x and s_y - xx + y < s_y:
#             result.append((s_x - xx + x, s_y - xx + y))
#     return result

# def create_diagonal_up_lines():
#     global s_x, s_y
#     result = []
#     result.append(create_diagonal_up_line(0, 0))
#     offset = 1
#     while s_x - offset >= 0:
#         line = create_diagonal_up_line(s_x - offset, 0)
#         if len(line) >= 3:
#             result.append(line)
#         offset += 1
#     offset = 1
#     while s_x - offset >= 1:
#         line = create_diagonal_up_line(s_x - offset, offset)
#         if len(line) >= 3:
#             result.append(line)
#         offset += 1
#     return result

# def create_diagonal_down_line(x, y):
#     global s_x, s_y
#     result = []
#     for xx in range(s_x):
#         if x + xx < s_x and y + xx < s_y:
#             result.append((x + xx, y + xx))
#     return result

# def create_diagonal_down_lines():
#     global s_x, s_y
#     result = []
#     result.append(create_diagonal_down_line(0, 0))
#     offset = 1
#     while offset < s_y - 2:
#         line = create_diagonal_down_line(0, offset)
#         if len(line) >= 3:
#             result.append(line)
#         offset += 1
#     offset = 1
#     while offset < s_x - 2:
#         line = create_diagonal_down_line(offset, 0)
#         if len(line) >= 3:
#             result.append(line)
#         offset += 1
#     return result

horizontal = [cut_combinations([(i, j) for i in range(s_y)])[0] for j in range(s_x)]
vertical = [cut_combinations([(i, j) for j in range(s_y)])[0] for i in range(s_x)]
diagonal_up = [[(0, 0), (1, 1), (2, 2)]]
diagonal_down = [[(2, 0), (1, 1), (0, 2)]]
# for k,v in enumerate():
#     for item in v:
#         diagonal_up.append(item)
# for k,v in enumerate():
#     for item in v:
#         diagonal_down.append(item)
# print(horizontal)
# print(vertical)
# print(diagonal_up)
# print(diagonal_down)
all_combinations = horizontal + vertical + diagonal_up + diagonal_down
# print(all_combinations)
# print(len(all_combinations))

def draw_win_line(x1, y1, x2, y2):
    xx1 = x1 * step_x + step_x // 2
    yy1 = y1 * step_y + step_y // 2
    xx2 = x2 * step_x + step_x // 2
    yy2 = y2 * step_y + step_y // 2
    list_ids.append(cvs.create_line(xx1, yy1, xx2, yy2, fill='green', width=8))

def draw_win_lines(is_cross, suitables):
    for suitable in suitables:
        draw_win_line(suitable[0][0], suitable[0][1], suitable[len(suitable)-1][0], suitable[len(suitable)-1][1])

def check_winner(is_cross):
    win = False
    suitables = []
    for combination in all_combinations:
        thiscomb = True
        for vector in combination:
            if (crosses if is_cross else noughts)[vector[1]][vector[0]] == 0:
                thiscomb = False
        if thiscomb:
            if not win: win = True
            suitables.append(combination)
    draw_win_lines(is_cross, suitables)
    return win

check_winner_cross = lambda:check_winner(True)
check_winner_nought = lambda:check_winner(False)

def on_win(is_cross):
    mb.showinfo("Конец игры", "Победили " + ("крестики!" if is_cross else "нолики!"))
    restart()
    # TODO

on_win_cross = lambda:on_win(True)
on_win_nought = lambda:on_win(False)

def draw(x, y, is_cross):
    global crosses, noughts
    if crosses[y][x] == 0 or noughts[y][x] == 0:
        if is_cross:
            crosses[y][x] = 1
            list_ids.append(cvs.create_line(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill='red', width=5))
            list_ids.append(cvs.create_line(x * step_x + step_x, y * step_y, x * step_x, y * step_y + step_y, fill='red', width=5))
        else:
            noughts[y][x] = 1
            list_ids.append(cvs.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill='blue'))
            list_ids.append(cvs.create_oval(x * step_x + step_x // 3, y * step_y + step_y // 3, x * step_x + step_x - step_x // 3, y * step_y + step_y - step_y // 3, fill='white'))

draw_cross = lambda x, y:draw(x, y, True)
draw_nought = lambda x, y:draw(x, y, False)

def ai_turn():
    global is_cross_turn, crosses, noughts
    mainw.update()
    sleep(1)
    is_cross_turn = True
    ip_x = randint(0, s_x - 1)
    ip_y = randint(0, s_y - 1)
    while not crosses[ip_y][ip_x] == 0 or not noughts[ip_y][ip_x] == 0:
        ip_x = randint(0, s_x - 1)
        ip_y = randint(0, s_y - 1)
    noughts[ip_y][ip_x] = 1
    draw_nought(ip_x, ip_y)
    
def add_to_all(event):
    global is_cross_turn, crosses, noughts
    _type = 0
    if event.num == 3:
        _type = 1
    mouse_x = cvs.winfo_pointerx() - cvs.winfo_rootx()
    mouse_y = cvs.winfo_pointery() - cvs.winfo_rooty()
    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y
    if ip_x < s_x and ip_y < s_y:
        if crosses[ip_y][ip_x] == 0 and noughts[ip_y][ip_x] == 0:
            if is_cross_turn:
                is_cross_turn = False
                draw_cross(ip_x, ip_y)
                # print(check_winner_cross())
                if check_winner_cross():
                    is_cross_turn = True
                    on_win_cross()
                if is_vs_ai:
                    mark_turn(is_cross_turn)
                    ai_turn()
            else:
                is_cross_turn = True
                draw_nought(ip_x, ip_y)
                # print(check_winner_nought())
                if check_winner_nought():
                    is_cross_turn = False
                    on_win_nought()
    
    mark_turn(is_cross_turn)

cvs.bind_all("<Button-1>", add_to_all)
cvs.bind_all("<Button-3>", add_to_all)

while app_running:
    if app_running:
        mainw.update_idletasks()
        mainw.update()
    sleep(0.005)