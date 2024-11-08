# функция



# циклы



# практики



# def hello():
  #  print("Всем привет!")
# hello()

# параметры
# def total_sum(num1, num2, num3):
#    result = num1 + num2 + num3
#    print(result)

# result = total_sum(num1: 80, num2: 550, num3: 900) # аргументы функции

# films = ["Фильм", "Фильм1", "Фильм2", "Фильм3"]
# print(films)
# for film in films:
#    print(film)

import random
num = random.randint(1,100)

points = 5
errorPoints = 0
print(num)

while points > errorPoints:
    answer = int(input("Ввкдите число,которое загадал компьютер: "))
    print(type(answer),answer)
    if answer > num:
        print("мое число меньше")
        errorPoints += 1
    elif answer < num:
        print("мое число больше")
        errorPoints += 1
    else:
        print("вы угадали")
        break
