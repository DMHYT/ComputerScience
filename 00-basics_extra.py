# Дополнительное задание к уроку "Основы Python"
# Задача: создать тест из трёх вопросов, с подсчётом баллов
# Схема улучшена, добавлена оценка в процентах в конце,
# и обработка ZeroDivisionError, в случае деления на ноль в вычислении процента

# Инициализируем переменную для баллов
score = 0
# Используя тернарный оператор, добавляем один балл
# в каждом вопросе в случае правильного ответа от пользователя
score = score + 1 if int(input("Сколько будет 2+2?")) == 4 else score
score = score + 1 if int(input("Сколько будет 8*9?")) == 72 else score
score = score + 1 if int(input("Сколько будет 999-888?")) == 111 else score

# Если вы боитесь этого оператора или ещё в нём не разобрались, 
# можете сделать на каждый вопрос банальную конструкцию if else
# (использовал def для того, чтобы этот показательный код не запустился, если я этого не захочу)
def anotherOne():
    if int(input("Сколько будет 2+2?")) == 4:
        score += 1  # прибавляем к переменной 1
    else:
        pass # просто пропускаем блок кода


# Создаём переменную для результата в процентах
percentscore = 0

# Находим результат в процентах делением счёта на количество всех вопросов (в нашем случае 3)
# И так как счёт может быть ноль, а при делении на ноль Python на нас разозлится,
# делаем обработку исключения ZeroDivisionError, в случае его появления просто присваиваем переменной значение 0
try:
    percentscore = score / 3
except ZeroDivisionError:
    percentscore = 0

# Так как у нас должна получиться десятичная дробь <= 1,
# умножаем переменную на 100, в итоге получаем значение в процентах
percentscore *= 100

# В данный момент наш счёт в процентах типа float
# Превращаем его в тип int, соответствующей функцией
percentscore = int(percentscore)

# Наконец выводим результат в консоль )))
print("Ваш результат: " + str(score) + "/3 баллов (" + str(percentscore) + "%)")

# Спасибо за внимание :-)