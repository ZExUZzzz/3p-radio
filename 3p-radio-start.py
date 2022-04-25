from yandex_music import Client # API для обращения к яндекс-музыке/радио
from math import floor # Математические операции
from random import random # Рандом по объектам
from random import randint # Рандом по цифрам
from time import sleep # Останока кода
from radio import Radio # Модуль радио radio.py (должен быть в папке с приложением)
import os # Модуль работы с ОС
import pyglet # Выполняет роль плеера


'''
#def initialization():


if not (os.path.exists('conf.ini')):
    config_file = open('conf.ini', 'w')
    config_file.close()
'''
with open('conf.ini', 'r+') as file: #Читаем файл
    lines = file.read().splitlines() # read().splitlines() - чтобы небыло пустых строк

conf_dict = {}

for line in lines: # Проходимся по каждой строчке
  key,value = line.split('=') # Разделяем ключ от значения через равно (radio = genre:station)
  conf_dict.update({key:value})	 # Добавляем в словарь

if not ('radio' in conf_dict or 'to_adv' in conf_dict):
    print('Конфигурация не обнаружена, необходимо выбрать параметры работы радио')
    sleep(1)
    print('Введите радиостанцию в виде тип:станция: ')
    station = input()
    conf_dict.update()
else:
    print('Конфигурация обнаружена, радио:', conf_dict['radio'] + '\n Песен до рекламы', conf_dict['to_adv'])

'''
conf_dict['radio'] = 'mood:genre'
conf_dict['to_adv'] = '5'
with open('conf.ini', 'r+') as file:
    for key, value in conf_dict.items():
        file.write(f'{key}= {value}\n')
'''
print(conf_dict)

# Создаём папки для радио и рекламы, если они отсутствуют
if not (os.path.exists('radio')):
    os.mkdir('radio')
if not (os.path.exists('adv')):
    os.mkdir('adv')

with open('genre.txt', 'r', encoding='Windows-1251') as genre_temp: # Считываем жанр для радио
    static_genre = genre_temp.read()
with open('to_adv.txt', 'r', encoding='Windows-1251') as adv_temp: # Считываем количество песен до рекламы
    to_adv = int(adv_temp.read())
adv_count = 0 # Внутренняя переменная для подсчёта сколько песен для включения рекламы
files = os.listdir(path='.\\adv') # Дополнительная переменная для указания папки с рекламой
dict_adv = os.listdir(path='.\\adv') # Словарь, харнящий в себе список рекламных треков
with open('token.txt', 'r', encoding='Windows-1251') as token_temp:
    tmp_token = token_temp.read()

client = Client(tmp_token).init() # Инициализация яндекс-музыки и подключение к аккаунту по токену

# Метод получения станции для проигрывания. По умолчанию выводит случайную станцию, в данной реализации - станцию из текстового документа
_stations = client.rotor_stations_list()
_station_random_index = floor(len(_stations) * random())
_station = _stations[_station_random_index].station
_station_id = static_genre
_station_from = _station.id_for_from
# Запуск клиента радио
radio = Radio(client)
# Получаем первый трек для радио
try:
    first_track = radio.start_radio(_station_id, _station_from)
except:
    print('Ошибка доступа к яндексу. Сохраните ваш токен в файле token.txt')
    sleep(8)
first_track.download('radio\\curr_track.mp3') #Скачивание первого трека для начала воспроизведения
is_first_time = True
while True:
    if (os.path.exists('radio\\curr_track.mp3')):
        if ((adv_count < to_adv) or (len(dict_adv) == 0)):
            os.system("cls")
            if is_first_time == False:
                os.remove('radio\\curr_track.mp3')
                os.rename('radio\\next_track.mp3', 'radio\\curr_track.mp3')
            music = pyglet.media.load('radio\\curr_track.mp3', streaming=False)
            sleep(3)
            player = music.play()
            from threading import Timer
            t = Timer(player.source.duration, player.next_source)
            t.start()
            if len(dict_adv) == 0: print("В папке adv не обнаружено треков. Будет воспроизводиться только радио")
            print("Сейчас играет радио:", _station_id)
            try:
                print('Исполнитель:', try_track_dict['artists'][0]['name'])
                print('Трек:', try_track_dict['title'])
            except:
                print('Название песни не найдено')
            print('Длительность:', player.source.duration, 'с')
            if not len(dict_adv) == 0: print('До рекламы осталось', to_adv - adv_count, 'песня(ен)')
            adv_count = adv_count + 1
            next_track = radio.play_next()
            try_track_dict = next_track
            next_track.download('radio\\next_track.mp3')
            is_first_time = False
            try:
                sleep(player.source.duration)
            except AttributeError:
                print('Не удалось получить время трека')
        else:
            os.system("cls")
            adv_count = 0
            if to_adv == 0: print('Значение "треков до рекламы" в to_adv.txt установлено на 0. Будет воспроизводиться только реклама')
            try:
                random_adv = dict_adv[randint(0, len(dict_adv) - 1)]
            except ValueError:
                print('Ошибка значения треков до рекламы. Установите целое положительное значение в файле to_adv.txt')
            music = pyglet.media.load('adv\\'+random_adv, streaming=False)
            sleep(3)
            player = music.play()
            print("Сейчас играет реклама")
            from threading import Timer
            t = Timer(player.source.duration, player.next_source)
            t.start()
            print('Длительность:', player.source.duration, 'с')
            next_track = radio.play_next()
            next_track.download('radio\\next_track.mp3')
            try:
                sleep(player.source.duration)
            except AttributeError:
                print('Не удалось получить время трека')
    else:
        first_track.download('radio\\curr_track.mp3')
        sleep(5)