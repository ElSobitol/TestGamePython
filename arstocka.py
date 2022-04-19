import time
import pygame
pygame.init()
pygame.mixer.music.load('arstocka.mp3')# Загрузка музыки в проект
pygame.mixer.music.set_volume(0.2)#громкость
pygame.mixer.music.play(-1)#Включаем музыку при запуске окна программы
print('Игра - Papers, Please. \nВам будет необходимо отвечать на вопросы\n системы в качестве инспектора')

time.sleep(3)
loading = 'Поздравляем! Вы выиграли конкурс на должность инспектора!'
for i in range(57):
    print(loading[i], sep=' ', end=' '); time.sleep(0.2)#Задаем интервал для печатания нужного текста
time.sleep(1)
marquee = '\nИсправно служите во благо родины! СЛАВА АРСТОЦКЕ!'
for i in range(50):
    print(marquee[i], sep=' ', end=' '); time.sleep(0.2)
time.sleep(1.1) 
#День первый - начало работы
print('\n Ваш первый день работы, Инспектор!')
day1 = '\n Инспектор! Пропускайте только тех, кто имеет \n документы АРСТОЦКИ! \nВсем иностранцам - отказ!'
for i in range(94):
    print(day1[i], sep=' ', end=' '); time.sleep(0.2)

def Next():
    return input('\nСледующий! Ваши документы!')
def say_speech(speech):
    print(speech)
def Document(speech):
    speech = speech.lower()
    if "арстоцка" in speech:
        say_speech("\n Слава Арстоцке! Добро пожаловать!")
    elif "импор" or "колечия" or "орбистан" or "оф" or "республия" or "антегрия" in speech:
        say_speech("Иностранцы не допускаются на территорию АРСТОЦКИ!")
    else:
        return Next()


while True:
    name = Next()
    Document(name)