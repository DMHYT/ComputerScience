# Улучшенная схема 00-basics.py
# Добавлена обработка исключения ValueError 
# в случае некорректно введённых пользователем данных,
# и немного приколов)))

def intInput(question):
    inp = None
    try:
        inp = int(input(question))
    except ValueError:
        print("Некорректно введённые данные! Ввод должен быть целочисленного типа!")
        intInput(question)
    return inp

if __name__ == "__main__":
    squirrels = intInput("Сколько белок: ")
    nuts = intInput("Сколько орехов: ")
    otrum = nuts // squirrels
    zalush = nuts % squirrels
    if nuts == 0 and squirrels > 0:
        print("Белки останутся голодными. Плак-плак 0_0")
    elif otrum == 0 and nuts > 0:
        print("Ну вы и жадина! Вы собираетесь делить орехи на части?")
    elif squirrels == 0 and nuts > 0:
        print("Вы решили съесть эти орехи сами? Приятного аппетита)")
    elif otrum < 5 and squirrels > 0:
        print("Ну им же это на ползуба((( Ну ладно, как хотите.")
    else:
        print("Каждая белка получит", otrum, "орехов. Вам достанется", zalush, "орехов.", 
        "Печалька -_-" if zalush == 0 else ("Почти ничего не осталось(((" if zalush < 5 else "Вы нормально так подкрепитесь)))"))