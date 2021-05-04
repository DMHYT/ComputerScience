import tkinter as tk
import tkinter.messagebox as mb
from random import choice, shuffle, randint
from time import sleep
from os import getcwd, mkdir, remove
from os.path import exists, dirname
from zipfile import ZipFile
# pip install pyttsx3
from pyttsx3 import init
# pip install requests
from requests import get
# pip install pillow
from PIL import Image
from PIL.ImageTk import PhotoImage

sound_engine = init()
sound_engine.setProperty('rate', 100)
learning_word_index = -1
current_question_number = 0
score = 0

class Word:
    
    def __init__(self, word, translation, transcription):
        self.word = word
        self.translation = translation
        self.transcription = transcription

    def play_word(self):
        global sound_engine
        sound_engine.say(self.word)
        sound_engine.runAndWait()

    def set_topic(self, topic):
        self.topic = topic


class Topic:

    def __init__(self, topic_name, translation, words):
        self.topic_name = topic_name
        self.translation = translation
        self.words = words


create_words_array = lambda l: [Word(word[0], word[1], word[2]) for word in l]

words_colors = create_words_array([["yellow", "жёлтый", "[ˈjeləʊ]"], ["green", "зелёный", "[ɡriːn]"], ["blue", "синий", "[bluː]"], ["red", "красный", "[red]"], ["orange", "оранжевый", "[ˈɔːrɪndʒ]"], ["pink", "розовый", "[pɪŋk]"], ["black", "чёрный", "[blæk]"], ["brown", "коричневый", "[braʊn]"], ["grey", "серый", "[ɡreɪ]"], ["white", "белый", "[waɪt]"], ["purple", "фиолетовый", "[ˈpɜːrpl]"]])
topic_colors = Topic("Colors", "Цвета", words_colors)

words_school = create_words_array([["book", "книжка", "[bʊk]"], ["pen", "ручка", "[pen]"], ["pencil", "карандаш", "[ˈpensl]"], ["rubber", "резинка", "[ˈrʌbər]"], ["ruler", "линейка", "[ˈruːlər]"], ["bag", "сумка", "[bæɡ]"], ["pencil case", "пенал", "[ˈpensl keɪs]"]])
topic_school = Topic("School", "Школа", words_school)

words_animals = create_words_array([["cat", "кошка", "[kæt]"], ["dog", "собака", "[dɔːɡ]"], ["parrot", "попугай", "[ˈpær.ət]"], ["rabbit", "кролик", "[ˈræb.ɪt]"], ["mouse", "мышь", "[maʊs]"], ["hamster", "хомяк", "[ˈhæm.stər]"], ["tortoise", "черепаха", "[ˈtɔːr.t̬əs]"], ["monkey", "мартышка", "[ˈmʌŋ.ki]"], ["elephant", "слон", "[ˈel.ɪ.fənt]"], ["crocodile", "крокодил", "[ˈkrɒk.ə.daɪl]"], ["bird", "птица", "[bɜːd]"], ["duck", "утка", "[dʌk]"]])
topic_animals = Topic("Animals", "Животные", words_animals)

words_home = create_words_array([["bed", "кровать", "[bed]"], ["table", "стол", "[ˈteɪbl]"], ["chair", "кресло", "[tʃeə(r)]"], ["TV", "телевизор", "[ˌtiː ˈviː]"], ["room", "комната", "[ruːm]"], ["house", "дом", "[haʊs]"]])
topic_home = Topic("Home", "Дом", words_home)

words_toys = create_words_array([["ball", "мяч", "[bɔːl]"], ["doll", "кукла", "[dɑːl]"], ["plane", "самолёт", "[pleɪn]"], ["car", "машинка", "[kɑː(r)]"], ["train", "поезд", "[treɪn]"], ["boat", "лодка", "[bəʊt]"], ["bike", "велосипед", "[baɪk]"], ["kite", "воздушный змей", "[kaɪt]"], ["teddy bear", "плюшевый мишка", "[ˈted.i beə(r)]"], ["drums", "барабаны", "[drʌms]"], ["guitar", "гитара", "[ɡɪˈtɑː]"]])
topic_toys = Topic("Toys", "Игрушки", words_toys)

words_skills = create_words_array([["run", "бегать", "[rʌn]"], ["jump", "прыгать", "[dʒʌmp]"], ["play", "играть", "[pleɪ]"], ["climb", "взбираться", "[klaɪm]"], ["swim", "плавать", "[swɪm]"], ["eat", "кушать", "[iːt]"], ["drink", "пить", "[drɪŋk]"], ["dance", "танцевать", "[dɑːns]"], ["sing", "петь", "[sɪŋ]"]])
topic_skills = Topic("Skills", "Умения", words_skills)

words_body = create_words_array([["eye", "глаз", "[aɪ]"], ["ear", "ухо", "[ɪə(r)]"], ["nose", "нос", "[nəʊz]"], ["mouth", "рот", "[maʊθ]"], ["leg", "нога", "[leɡ]"], ["hand", "рука", "[hænd]"]])
topic_body = Topic("Body parts", "Части тела", words_body)

words_food = create_words_array([["apple", "яблоко", "[ˈæp.l̩]"], ["banana", "банан", "[bəˈnɑː.nə]"], ["biscuit", "печенье", "[ˈbɪskɪt]"], ["bread", "хлеб", "[bred]"], ["juice", "сок", "[dʒuːs]"], ["milk", "молоко", "[mɪlk]"], ["egg", "яйцо", "[eɡ]"], ["cheese", "сыр", "[tʃiːz]"], ["chocolate", "шоколад", "[ˈtʃɒklət]"], ["tea", "чай", "[tiː]"], ["ice-cream", "мороженое", "[ˌaɪsˈkriːm]"], ["pizza", "пицца", "[ˈpiːt.sə]"], ["hot-dog", "хот-дог", "[hɒt dɒɡ]"]])
topic_food = Topic("Food", "Еда", words_food)

all_topics = [topic_colors, topic_school, topic_animals, topic_home, topic_toys, topic_skills, topic_body, topic_food]
for topic in all_topics:
    for word in topic.words:
        word.set_topic(topic)
all_words = words_colors + words_school + words_animals + words_home + words_toys + words_skills + words_body + words_food

def load_images():
    print("Downloading images archive from GitHub...")
    response = get("https://raw.githubusercontent.com/DMHYT/ComputerScience/main/assets/english_game/archive.zip")
    directory = getcwd() + "\\VSDumEnglish\\"
    if not exists(directory):
        mkdir(directory)
    with open(directory + "archive.zip", 'wb') as archive:
        archive.write(response.content)
    print("Archive successfully downloaded!")
    with ZipFile(directory + "archive.zip") as archive:
        archive.extractall(directory)
    print("Archive has been extracted!")
    remove(directory + "archive.zip")
    print("Archive has been removed!")
load_images()

def create_learning_screen(window):
    if mb.askokcancel("ОБУЧЕНИЕ", "Начать обучение?"):
        global all_words, learning_word_index
        window.destroy()
        learning_screen_running = True
        def on_closing_learning():
            if mb.askokcancel("Завершение работы", "Действительно ли вы хотите завершить обучение?"):
                learningw.destroy()
                create_start_screen()
        learningw = tk.Tk()
        learningw.title("Изучение слов")
        learningw.resizable(0, 0)
        learningw.protocol("WM_DELETE_WINDOW", on_closing_learning)
        learningw.wm_attributes("-topmost", 1)
        labelImage = tk.Label(learningw)
        labelImage.grid(row=0, column=0, columnspan=2, sticky='nsew')
        labelTopic = tk.Label(learningw, font=('Helvetica', 14))
        labelTopic.grid(row=1, column=0, columnspan=2, sticky='nsew')
        labelWord = tk.Label(learningw, font=('Helvetica', 14))
        labelWord.grid(row=2, column=0, columnspan=2, sticky='nsew')
        labelTranslation = tk.Label(learningw, font=('Helvetica', 14))
        labelTranslation.grid(row=3, column=0, columnspan=2, sticky='nsew')
        def update_word():
            global learning_word_index
            word = all_words[learning_word_index]
            labelTopic.configure(text="Тема: " + word.topic.topic_name + " (" + word.topic.translation + ")")
            labelWord.configure(text=word.word+" "+word.transcription)
            labelTranslation.configure(text=word.translation)
            img_name = word.word.replace(" ", "_").replace("-", "_")
            path = (getcwd() + "\\VSDumEnglish\\" + img_name + ".png").replace("\\", "/")
            image = Image.open(path)
            resize_image = image.resize((512, 288))
            img = PhotoImage(resize_image)
            labelImage.configure(image=img)
            labelImage.image = img
        def next_word():
            global learning_word_index
            learning_word_index += 1
            if learning_word_index < len(all_words):
                update_word()
            else:
                mb.showinfo("Поздравляем!", "Обучение завершено! Теперь попробуйте пройти тест по освоенному материалу!")
                learningw.destroy()
                create_start_screen()
        next_word()
        def previous_word():
            global learning_word_index
            if learning_word_index >= 1:
                learning_word_index -= 1
                update_word()
        buttonPlay = tk.Button(learningw, text="Прослушать", font=('Helvetica', 14), command=lambda:all_words[learning_word_index].play_word())
        buttonPlay.grid(row=4, column=0, columnspan=2, sticky='nsew')
        buttonPrevious = tk.Button(learningw, text="Предыдущее", font=('Helvetica', 14), command=previous_word)
        buttonPrevious.grid(row=5, column=0, sticky='nsew')
        buttonNext = tk.Button(learningw, text="Следующее", font=('Helvetica', 14), command=next_word)
        buttonNext.grid(row=5, column=1, sticky='nsew')
        while learning_screen_running:
            if learning_screen_running:
                try:
                    learningw.update_idletasks()
                    learningw.update()
                except tk.TclError:
                    pass
            sleep(0.005)

def create_test_screen(window):
    global all_words
    if mb.askokcancel("ТЕСТИРОВАНИЕ", "Запустить тестирование?"):
        window.destroy()
        test_screen_running = True
        def on_closing_test():
            if mb.askokcancel("Завершение работы", "Действительно ли вы хотите завершить тестирование? Ваши результаты не сохранятся!"):
                testw.destroy()
                create_start_screen()
        questions_count = randint(5, 50)
        questions = []
        for i in range(questions_count):
            randword = choice(all_words)
            while randword in questions:
                randword = choice(all_words)
            else:
                questions.append(randword)
        testw = tk.Tk()
        testw.title("Тестирование (Вопрос " + str(current_question_number + 1) + " из " + str(questions_count) + ")")
        testw.resizable(0, 0)
        testw.protocol("WM_DELETE_WINDOW", on_closing_test)
        testw.wm_attributes("-topmost", 1)
        labelImage = tk.Label(testw)
        labelImage.grid(row=0, column=0, sticky='nsew')
        labelWhat = tk.Label(testw, text="Что изображено на картинке?\nВыберите правильный вариант.", font=('Helvetica', 14))
        labelWhat.grid(row=1, column=0, sticky='nsew')
        radios = []
        var = tk.IntVar()
        def create_buttons():
            global current_question_number
            word = questions[current_question_number]
            img_name = word.word.replace(" ", "_").replace("-", "_")
            path = (getcwd() + "\\VSDumEnglish\\" + img_name + ".png").replace("\\", "/")
            image = Image.open(path)
            resize_image = image.resize((512, 288))
            img = PhotoImage(resize_image)
            labelImage.configure(image=img)
            labelImage.image = img
            for radio in radios:
                radio.destroy()
            radios.clear()
            words = [word]
            for i in range(4):
                randomword = choice(word.topic.words)
                while randomword in words:
                    randomword = choice(word.topic.words)
                else:
                    words.append(randomword)
            shuffle(words)
            for i in range(len(words)):
                radio = tk.Radiobutton(testw, variable=var, value=(1 if words[i] == word else -i), text=words[i].word, font=('Helvetica', 14))
                radio.grid(row=i+2, column=0, sticky='nsew')
                radios.append(radio)
        create_buttons()
        def next_word():
            global current_question_number, score
            if current_question_number + 1 < questions_count:
                current_question_number += 1
                testw.title("Тестирование (Вопрос " + str(current_question_number + 1) + " из " + str(questions_count) + ")")
                neededButton = None
                for radio in radios:
                    if radio['value'] == 1:
                        neededButton = radio
                        break
                if var.get() != 1:
                    for radio in radios:
                        if radio != neededButton:
                            radio['background'] = 'red'
                else:
                    score += 1
                neededButton['background'] = 'green'
                mb.showinfo("ИНФО", "Ответ засчитан!")
                for radio in radios:
                    radio['background'] = 'white'
                var.set(-1)
                create_buttons()
            else:
                mb.showinfo("ИНФО", "Тест завершён! Смотрите результаты!")
                mb.showinfo("Результаты теста", "Ваш результат: " + str(score) + " из " + str(questions_count) + " (" + str(round(score / questions_count * 100, 2)) + "%)")
                testw.destroy()
                create_start_screen()
        buttonConfirm = tk.Button(testw, text="Подтвердить ответ", font=('Helvetica', 14), command=next_word)
        buttonConfirm.grid(row=7, column=0, sticky='ns')
        while test_screen_running:
            if test_screen_running:
                try:
                    testw.update_idletasks()
                    testw.update()
                except tk.TclError:
                    pass
            sleep(0.005)

def create_start_screen():
    start_screen_running = True
    def on_closing_start():
        if mb.askokcancel("Завершение работы", "Действительно ли вы хотите закрыть приложение?"):
            startw.destroy()
            for word in all_words:
                remove(getcwd() + "\\VSDumEnglish\\" + word.word.replace(" ", "_").replace("-", "_") + ".png")
    startw = tk.Tk()
    startw.title("English For Beginners")
    startw.resizable(0, 0)
    startw.protocol("WM_DELETE_WINDOW", on_closing_start)
    startw.wm_attributes("-topmost", 1)
    label = tk.Label(startw, text="Выберите режим работы", font=('Helvetica', 18))
    label.grid(row=0, column=0, sticky='nsew')
    buttonStartLearning = tk.Button(startw, text="Обучение", font=('Helvetica', 14), command=lambda:create_learning_screen(startw))
    buttonStartLearning.grid(row=1, column=0, sticky='nsew')
    buttonStartTest = tk.Button(startw, text="Тестирование", font=('Helvetica', 14), command=lambda:create_test_screen(startw))
    buttonStartTest.grid(row=2, column=0, sticky='nsew')
    while start_screen_running:
        if start_screen_running:
            try:
                startw.update_idletasks()
                startw.update()
            except tk.TclError:
                pass
        sleep(0.005)

if __name__ == "__main__":
    create_start_screen()