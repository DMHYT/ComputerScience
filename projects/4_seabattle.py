import tkinter as tk
import tkinter.messagebox as mb
from time import sleep
from random import choice, randrange, randint

mainw = tk.Tk()
app_running = True
size_canvas_x = 500
size_canvas_y = 500
s_x = s_y = 8
step_x = size_canvas_x // s_x
step_y = size_canvas_y // s_y
size_canvas_x = step_x * s_x
size_canvas_y = step_y * s_y
txt_len_middle = "* Human vs Computer"
size_font_x = 10
len_txt_x = len(txt_len_middle)*size_font_x
delta_menu_x = len_txt_x // step_x + 1
menu_x = step_x * delta_menu_x
menu_y = 40
ships = s_x // 2
ship_len1 = s_x // 5
ship_len2 = s_x // 3
ship_len3 = s_x // 2
enemy_ships1 = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]
enemy_ships2 = [[0 for i in range(s_x + 1)] for i in range(s_y + 1)]
list_ids = []  
points1 = [[-1 for i in range(s_x)] for i in range(s_y)]
points2 = [[-1 for i in range(s_x)] for i in range(s_y)]
boom = [[0 for i in range(s_x)] for i in range(s_y)]
ships_list = []
player_1_turn = False
is_vs_ai = False
add_to_label = add_to_label2 = ""

def on_closing():
    global app_running
    if mb.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        app_running = False
        mainw.destroy()

mainw.protocol("WM_DELETE_WINDOW", on_closing)
mainw.title("Морской бой")
mainw.resizable(0, 0)
mainw.wm_attributes("-topmost", 1)
canvas = tk.Canvas(mainw, width=size_canvas_x + menu_x + size_canvas_x, height=size_canvas_y + menu_y, bd=0, highlightthickness=0)
canvas.create_rectangle(0, 0, size_canvas_x, size_canvas_y, fill="white")
canvas.create_rectangle(size_canvas_x + menu_x, 0, size_canvas_x + menu_x + size_canvas_x, size_canvas_y, fill="lightyellow")
canvas.pack()
mainw.update()

def draw_table(offset_x=0):
    for i in range(0, s_x + 1):
        canvas.create_line(offset_x + step_x * i, 0, offset_x + step_x * i, size_canvas_y)
    for i in range(0, s_y + 1):
        canvas.create_line(offset_x, step_y * i, offset_x + size_canvas_x, step_y * i)

draw_table()
draw_table(size_canvas_x + menu_x)

t0 = tk.Label(mainw, text="Игрок №1", font=("Helvetica", 16))
t0.place(x=size_canvas_x // 2 - t0.winfo_reqwidth() // 2, y=size_canvas_y + 3)
t1 = tk.Label(mainw, text="Игрок №2"+add_to_label, font=("Helvetica", 16))
t1.place(x=size_canvas_x + menu_x + size_canvas_x // 2 - t1.winfo_reqwidth() // 2, y=size_canvas_y + 3)
t3 = tk.Label(mainw, text="@@@@@@@", font=("Helvetica", 16))
t3.place(x=size_canvas_x + menu_x//2 - t3.winfo_reqwidth() // 2, y= size_canvas_y)

def show_ships(num):
    for i in range(0, s_x):
        for j in range(0, s_y):
            if (enemy_ships1 if num == 1 else enemy_ships2)[j][i] > 0:
                offset_x = size_canvas_x + menu_x if num == 2 else 0
                list_ids.append(canvas.create_rectangle(offset_x + i * step_x, j * step_y, offset_x + i * step_x + step_x, j * step_y + step_y, fill=('green' if (points1 if num == 1 else points2)[j][i] != -1 else 'red')))

show_ships_1 = lambda:show_ships(1)
show_ships_2 = lambda:show_ships(2)

def restart():
    global list_ids, points1, points2, boom, enemy_ships1, enemy_ships2
    for el in list_ids:
        canvas.delete(el)
    list_ids = []
    generate_ships_list()
    enemy_ships1 = generate_enemy_ships()
    enemy_ships2 = generate_enemy_ships()
    points1 = [[-1 for i in range(s_x)] for i in range(s_y)]
    points2 = [[-1 for i in range(s_x)] for i in range(s_y)]
    boom = [[0 for i in range(s_x)] for i in range(s_y)]

buttonShow1 = tk.Button(mainw, text="Показать корабли\nигрока №1", font=('Helvetica', 14), command=show_ships_1)
buttonShow1.place(x=size_canvas_x + menu_x // 2 - buttonShow1.winfo_reqwidth() // 2, y=10)
buttonShow2 = tk.Button(mainw, text="Показать корабли\nигрока №2", font=('Helvetica', 14), command=show_ships_2)
buttonShow2.place(x=size_canvas_x + menu_x // 2 - buttonShow2.winfo_reqwidth() // 2, y=10+buttonShow1.winfo_reqheight()+5)
buttonRestart = tk.Button(mainw, text="Начать заново", font=('Helvetica', 14), command=restart)
buttonRestart.place(x=size_canvas_x + menu_x // 2 - buttonRestart.winfo_reqwidth() // 2, y=10+buttonShow1.winfo_reqheight()+buttonShow2.winfo_reqheight()+10)

def change_rb():
    global is_vs_ai, add_to_label, add_to_label2
    is_vs_ai = rb_var.get()
    add_to_label = " (ИИ)" if is_vs_ai else ""
    add_to_label2 = " (прицеливается)" if is_vs_ai else ""

rb_var = tk.BooleanVar()
rb1 = tk.Radiobutton(mainw, text="Игрок vs ИИ", variable = rb_var, value=1, command=change_rb, font=('Helvetica', 14))
rb2 = tk.Radiobutton(mainw, text="Игрок vs Игрок", variable = rb_var, value=0, command=change_rb, font=('Helvetica', 14))
rb1.place(x=size_canvas_x + menu_x // 2 - rb1.winfo_reqwidth() // 2, y=10 + buttonShow1.winfo_reqheight() + buttonShow2.winfo_reqheight() + buttonRestart.winfo_reqheight() + 15)
rb2.place(x=size_canvas_x + menu_x // 2 - rb2.winfo_reqwidth() // 2, y=10 + buttonShow1.winfo_reqheight() + buttonShow2.winfo_reqheight() + buttonRestart.winfo_reqheight() + rb1.winfo_reqheight() + 20)
if is_vs_ai:
    rb1.select()

def mark_player_turn(player_1):
    t0.configure(bg=('white' if player_1 else 'red'), text="Игрок №1"+add_to_label2)
    t1.configure(bg=('red' if player_1 else 'white'), text="Игрок №2"+add_to_label)
    t3.configure(text="Ход игрока №"+("2" if player_1 else "1" + add_to_label))
    t0.place(x=size_canvas_x//2-t0.winfo_reqwidth()//2, y=size_canvas_y+3)
    t1.place(x=size_canvas_x+menu_x+size_canvas_x//2-t1.winfo_reqwidth()//2, y=size_canvas_y+3)
    t3.place(x=size_canvas_x+menu_x//2-t3.winfo_reqwidth()//2, y=size_canvas_y)

mark_player_turn(player_1_turn)

def draw_point(x, y, offset_x=None):
    if enemy_ships1[y][x] == 0:
        list_ids.append(canvas.create_oval(offset_x + x * step_x, y * step_y, offset_x + x * step_x + step_x, y * step_y + step_y, fill='red'))
        list_ids.append(canvas.create_oval(offset_x + x * step_x + step_x // 3, y * step_y + step_y // 3, offset_x + x * step_x + step_x - step_x // 3, y * step_y + step_y - step_y // 3, fill='white'))
    if enemy_ships1[y][x] > 0:
        list_ids.append(canvas.create_rectangle(offset_x + x * step_x, y * step_y + step_y // 2 - step_y // 10, offset_x + x * step_x + step_x, y * step_y + step_y // 2 + step_y // 10, fill='blue'))
        list_ids.append(canvas.create_rectangle(offset_x + x * step_x + step_x // 2 - step_x // 10, y * step_y, offset_x + x * step_x + step_x // 2 + step_x // 10, y * step_y + step_y, fill='blue'))

draw_point_1 = lambda x, y:draw_point(x, y, offset_x=0)
draw_point_2 = lambda x, y:draw_point(x, y, offset_x=size_canvas_x+menu_x)

def check_winner(num):
    win = True
    for i in range(0, s_x):
        for j in range(0, s_y):
            if (enemy_ships1 if num == 1 else enemy_ships2)[j][i] > 0:
                if (points1 if num == 1 else points2)[j][i] == -1:
                    win = False
    return win

check_winner_1 = lambda:check_winner(1)
check_winner_2 = lambda:check_winner(2)

def on_win(num):
    winner = "Победа игрока №" + str(num) + add_to_label
    winner_add = "Все корабли игрока №" + str(num) + " уничтожены"
    points1 = [[10 for i in range(s_x)] for i in range(s_y)]
    points2 = [[10 for i in range(s_x)] for i in range(s_y)]
    list_ids.append(canvas.create_rectangle(step_x * 3, step_y * 3, size_canvas_x + menu_x + size_canvas_x - step_x * 3, size_canvas_y - step_y, fill="blue"))
    list_ids.append(canvas.create_rectangle(step_x * 3 + step_x // 2, step_y * 3 + step_y // 2, size_canvas_x + menu_x + size_canvas_x - step_x * 3 - step_x // 2, size_canvas_y - step_y - step_y // 2, fill="yellow"))
    list_ids.append(canvas.create_text(step_x * 10, step_y * 5, text=winner, font=("Arial", 50), justify='center'))
    list_ids.append(canvas.create_text(step_x * 10, step_y * 6, text=winner_add, font=("Arial", 25), justify='center'))

on_win_1 = lambda:on_win(1)
on_win_2 = lambda:on_win(2)

def ai_turn():
    global points1, points2, player_1_turn
    mainw.update()
    sleep(1)
    player_1_turn = False
    ip_x = randint(0, s_x-1)
    ip_y = randint(0, s_y-1)
    while not points1[ip_y][ip_x] == -1:
        ip_x = randint(0, s_x-1)
        ip_y = randint(0, s_y-1)
    points1[ip_y][ip_x] = 7
    draw_point_1(ip_x, ip_y)
    if check_winner_2():
        on_win_2()

def add_to_all(event):
    global points1, points2, player_1_turn
    _type = 0
    if event.num == 3:
        _type = 1
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    ip_x = mouse_x // step_x
    ip_y = mouse_y // step_y
    if ip_x < s_x and ip_y < s_y and player_1_turn:
        if points1[ip_y][ip_x] == -1:
            points1[ip_y][ip_x] = _type
            player_1_turn = False
            draw_point_1(ip_x, ip_y)
            if check_winner_1():
                player_1_turn = True
                on_win_1()
    if ip_x >= s_x + delta_menu_x and ip_x <= s_x + s_x + delta_menu_x and ip_y < s_y and not player_1_turn:
        if points2[ip_y][ip_x - s_x - delta_menu_x] == -1:
            points2[ip_y][ip_x - s_x - delta_menu_x] = _type
            player_1_turn = True
            draw_point_2(ip_x - s_x - delta_menu_x, ip_y)
            if check_winner_2():
                player_1_turn = False
                on_win_2()
            elif is_vs_ai:
                mark_player_turn(player_1_turn)
                ai_turn()
    mark_player_turn(player_1_turn)

canvas.bind_all("<Button-1>", add_to_all)
canvas.bind_all("<Button-3>", add_to_all)

def generate_ships_list():
    global ships_list
    ships_list = []
    for i in range(0, ships):
        ships_list.append(choice([ship_len1, ship_len2, ship_len3]))

def generate_enemy_ships():
    global ships_list
    enemy_ships = []
    sum_1_all_ships = sum(ships_list)
    sum_1_enemy = 0
    while sum_1_enemy != sum_1_all_ships:
        enemy_ships = [[0 for i in range(s_x + 1)] for i in
                       range(s_y + 1)]
        for i in range(0, ships):
            len = ships_list[i]
            horizont_vertikal = randrange(1, 3)
            primerno_x = randrange(0, s_x)
            if primerno_x + len > s_x:
                primerno_x = primerno_x - len
            primerno_y = randrange(0, s_y)
            if primerno_y + len > s_y:
                primerno_y = primerno_y - len
            if horizont_vertikal == 1:
                if primerno_x + len <= s_x:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y][primerno_x - 1] + \
                                               enemy_ships[primerno_y][primerno_x + j] + \
                                               enemy_ships[primerno_y][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j + 1] + \
                                               enemy_ships[primerno_y + 1][primerno_x + j] + \
                                               enemy_ships[primerno_y - 1][primerno_x + j]
                            if check_near_ships == 0:
                                enemy_ships[primerno_y][primerno_x + j] = i + 1
                        except Exception:
                            pass
            if horizont_vertikal == 2:
                if primerno_y + len <= s_y:
                    for j in range(0, len):
                        try:
                            check_near_ships = 0
                            check_near_ships = enemy_ships[primerno_y - 1][primerno_x] + \
                                               enemy_ships[primerno_y + j][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j + 1][primerno_x - 1] + \
                                               enemy_ships[primerno_y + j][primerno_x + 1] + \
                                               enemy_ships[primerno_y + j][primerno_x - 1]
                            if check_near_ships == 0:
                                enemy_ships[primerno_y + j][primerno_x] = i + 1
                        except Exception:
                            pass
        sum_1_enemy = 0
        for i in range(0, s_x):
            for j in range(0, s_y):
                if enemy_ships[j][i] > 0:
                    sum_1_enemy = sum_1_enemy + 1
    return enemy_ships


generate_ships_list()
enemy_ships1 = generate_enemy_ships()
enemy_ships2 = generate_enemy_ships()

while app_running:
    if app_running:
        mainw.update_idletasks()
        mainw.update()
    sleep(0.005)