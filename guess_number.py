from random import randint

number = randint(1, 100)
print('!!!!Угадайте число от 1 до 100')

def main():
    while True:
        quest = int(input('Введите свое число: '))

        if quest < number:
            print('Ваше число меньше загаданного')
        
        elif quest > number:
            print('Ваше число больше загаданного')

        elif quest == number:
            break


main()

print('Вы угадали!!!!! Вы молодец')