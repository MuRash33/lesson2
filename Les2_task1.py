age = int(input('Введите Ваш возраст: '))

def occupatiion (age):
    age = abs(int(age))

    if age <= 6:
        print('Вам пора садик!')
    elif 6 < age <= 15:
        print('Ваше место за партой в школе')
    elif 15 < age <= 20:
        print('Универ')
    elif 20 < age <= 60:
        print('Поздравляем! Вы всему научились!  Пора работать!')
    else:
        print('Здравствуй пенсия!')

result = occupatiion(age)

print(result)