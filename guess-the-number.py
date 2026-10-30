import random

all_numbers = []
for i in range(1, 21):
    all_numbers.append(i)
    
random_number = random.choice(all_numbers)

print("Привет! Давай сыграем в игру? Я загадаю число от 1 до 20, а твоя задача будет его отгадать.) Начинаем!")

for i in range (5):
    print(' ')
    print("Ваше число...")
    our_number = int(input())
    if our_number == random_number:
        print(' ')
        print("Поздравляю! Вы угадали число!")
        break
    else:
        if our_number < random_number:
            print("Это не то число. Загадано число больше вашего.")
        elif our_number > random_number:
            print("Это не то число. Загадано число меньше вашего.")
print(' ')
if our_number == random_number:
        print("Вы победили.")
else:
    print("Вы проиграли. Было загадано число", random_number)
