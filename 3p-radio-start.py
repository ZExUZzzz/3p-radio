from yandex_music import Client # API для обращения к яндекс-музыке/радио
from math import floor # Математические операции
from random import random # Рандом по объектам
from random import randint # Рандом по цифрам
from time import sleep # Останока кода
from radio import Radio # Модуль радио radio.py (должен быть в папке с приложением)
import os # Модуль работы с ОС
import pyglet # Выполняет роль плеера


if not (os.path.exists('conf.ini')):
    config_file = open('conf.ini', 'w')
    config_file.close()

with open('conf.ini', 'r') as file: #Читаем файл
    lines = file.read().splitlines() # read().splitlines() - чтобы небыло пустых строк
conf_dict = {}

for line in lines: # Проходимся по каждой строчке
    key,value = line.split('=') # Разделяем ключ от значения через равно (radio = genre:station)
    conf_dict.update({key:value})	 # Добавляем в словарь

station = None
radio_types = {
    'activity' : 'Занятие',
    'author' : 'Авторы',
    'epoch' : 'Эпоха',
    'genre' : 'Жанр',
    'local' : 'Музыка городов',
    'mood' : 'Настроение',
    'personal' : 'Персональное',
    'user' : 'Пользовательское'
}

def select_station(d_station, k_station):
        global station
        while True:
            os.system("cls")
            print('Выбор радиостанции.')
            print('Выберите тип станции: \n'
                  '1. Занятие\n'
                  '2. Авторы\n'
                  '3. Эпоха\n'
                  '4. Жанр\n'
                  '5. Музыка городов\n'
                  '6. Настроение\n'
                  '7. Персональное\n'
                  '8. "Моя волна"')
            input_type = int(input())
            if input_type == 8:
                with open('.\\stations\\'+os.listdir('.\\stations')[input_type-1], 'r', encoding='UTF-8') as file:  # Читаем файл
                    lines = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк
                input_station = 1
                for line in lines:  # Проходимся по каждой строчке
                    key, value = line.split('=')  # Разделяем ключ от значения через равно (radio = genre:station)
                    conf_dict.update({key: value})  # Добавляем в словарь
                return (os.listdir('.\\stations')[input_type-1][:-4] + ':' + list(conf_dict.values())[(input_station - 1)],
                        list(conf_dict.keys())[(input_station - 1)])
                break
            if input_type == 7:
                with open('.\\stations\\'+os.listdir('.\\stations')[input_type-1], 'r', encoding='UTF-8') as file:  # Читаем файл
                    lines = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк
                input_station = 1
                for line in lines:  # Проходимся по каждой строчке
                    key, value = line.split('=')  # Разделяем ключ от значения через равно (radio = genre:station)
                    conf_dict.update({key: value})  # Добавляем в словарь
                return (os.listdir('.\\stations')[input_type-1][:-4] + ':' + list(conf_dict.values())[(input_station - 1)],
                        list(conf_dict.keys())[(input_station - 1)])
                break
            if input_type == 1:
                with open('.\\stations\\'+os.listdir('.\\stations')[input_type-1], 'r', encoding='UTF-8') as file:  # Читаем файл
                    lines = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк
                print('Выбран тип "Занятие". Выбор станции:\n'
                      '1. '+lines[0]+'\n'
                      '2. '+lines[1]+'\n'
                      '3. '+lines[2]+'\n'
                      '4. '+lines[3]+'\n'
                      '5. '+lines[4]+'\n'
                      '6. '+lines[5]+'\n'
                      '7. '+lines[6]+'\n'
                      '8. '+lines[7]+'\n'
                      '9. '+lines[8]+'\n'
                      '10. '+lines[9]+'\n')
                input_station = int(input())
                for line in lines:  # Проходимся по каждой строчке
                    key, value = line.split('=')  # Разделяем ключ от значения через равно (radio = genre:station)
                    conf_dict.update({key: value})  # Добавляем в словарь
                return (os.listdir('.\\stations')[input_type-1][:-4] + ':' + list(conf_dict.values())[(input_station - 1)],
                        list(conf_dict.keys())[(input_station - 1)])
                break
            if input_type == 2:
                with open('.\\stations\\'+os.listdir('.\\stations')[1], 'r', encoding='UTF-8') as file:  # Читаем файл
                    lines = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк
                print('Выбран тип "Автор". Выбор станции:\n'
                      '1. '+lines[0]+'\n'
                      '2. '+lines[1]+'\n'
                      '3. '+lines[2]+'\n'
                      '4. '+lines[3]+'\n'
                      '5. '+lines[4]+'\n'
                      '6. '+lines[5]+'\n')
                input_station = int(input())
                for line in lines:  # Проходимся по каждой строчке
                    key, value = line.split('=')  # Разделяем ключ от значения через равно (radio = genre:station)
                    conf_dict.update({key: value})  # Добавляем в словарь
                return (os.listdir('.\\stations')[input_type-1][:-4] + ':' + list(conf_dict.values())[(input_station - 1)],
                        list(conf_dict.keys())[(input_station - 1)])
            if input_type == 3:
                with open('.\\stations\\'+os.listdir('.\\stations')[input_type-1], 'r', encoding='UTF-8') as file:  # Читаем файл
                    lines = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк
                print('Выбран тип "Эпоха". Выбор станции:\n'
                      '1. '+lines[0]+'\n'
                      '2. '+lines[1]+'\n'
                      '3. '+lines[2]+'\n'
                      '4. '+lines[3]+'\n'
                      '5. '+lines[4]+'\n'
                      '6. '+lines[5]+'\n'
                      '7. '+lines[6]+'\n'
                      '8. '+lines[7]+'\n')
                input_station = int(input())
                for line in lines:  # Проходимся по каждой строчке
                    key, value = line.split('=')  # Разделяем ключ от значения через равно (radio = genre:station)
                    conf_dict.update({key: value})  # Добавляем в словарь
                return (os.listdir('.\\stations')[input_type-1][:-4] + ':' + list(conf_dict.values())[(input_station - 1)],
                        list(conf_dict.keys())[(input_station - 1)])
                break
            if input_type == 4:
                with open('.\\stations\\'+os.listdir('.\\stations')[input_type-1], 'r', encoding='UTF-8') as file:  # Читаем файл
                    lines = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк
                print('Выбран тип "Жанр". Выбор станции:\n'
                      '1. '+lines[0]+'\n'
                      '2. '+lines[1]+'\n'
                      '3. '+lines[2]+'\n'
                      '4. '+lines[3]+'\n'
                      '5. '+lines[4]+'\n'
                      '6. '+lines[5]+'\n'
                      '7. '+lines[6]+'\n'
                      '9. '+lines[8]+'\n'
                      '10. '+lines[9]+'\n'
                      '11. '+lines[10]+'\n'
                      '12. '+lines[11]+'\n'
                      '13. '+lines[12]+'\n'
                      '14. '+lines[13]+'\n'
                      '15. '+lines[14]+'\n'
                      '16. '+lines[15]+'\n'
                      '17. '+lines[16]+'\n'
                      '18. '+lines[17]+'\n'
                      '19. '+lines[18]+'\n'
                      '20. '+lines[19]+'\n'
                      '21. '+lines[20]+'\n'
                      '22. '+lines[21]+'\n'
                      '23. '+lines[22]+'\n')
                input_station = int(input())
                for line in lines:  # Проходимся по каждой строчке
                    key, value = line.split('=')  # Разделяем ключ от значения через равно (radio = genre:station)
                    conf_dict.update({key: value})  # Добавляем в словарь
                return (os.listdir('.\\stations')[input_type-1][:-4] + ':' + list(conf_dict.values())[(input_station - 1)],
                        list(conf_dict.keys())[(input_station - 1)])
                break
            if input_type == 5:
                with open('.\\stations\\'+os.listdir('.\\stations')[input_type-1], 'r', encoding='UTF-8') as file:  # Читаем файл
                    lines = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк
                print('Выбран тип "Музыка городов". Выбор станции:\n'
                      '1. '+lines[0]+'\n'
                      '2. '+lines[1]+'\n'
                      '3. '+lines[2]+'\n'
                      '4. '+lines[3]+'\n'
                      '5. '+lines[4]+'\n')
                input_station = int(input())
                for line in lines:  # Проходимся по каждой строчке
                    key, value = line.split('=')  # Разделяем ключ от значения через равно (radio = genre:station)
                    conf_dict.update({key: value})  # Добавляем в словарь
                return (os.listdir('.\\stations')[input_type-1][:-4] + ':' + list(conf_dict.values())[(input_station - 1)],
                        list(conf_dict.keys())[(input_station - 1)])
                break
            if input_type == 6:
                with open('.\\stations\\'+os.listdir('.\\stations')[input_type-1], 'r', encoding='UTF-8') as file:  # Читаем файл
                    lines = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк
                print('Выбран тип "Настроение". Выбор станции:\n'
                      '1. '+lines[0]+'\n'
                      '2. '+lines[1]+'\n'
                      '3. '+lines[2]+'\n'
                      '4. '+lines[3]+'\n'
                      '5. '+lines[4]+'\n'
                      '6. '+lines[5]+'\n'
                      '7. '+lines[6]+'\n'
                      '9. '+lines[8]+'\n'
                      '10. '+lines[9]+'\n'
                      '11. '+lines[10]+'\n'
                      '12. '+lines[11]+'\n'
                      '13. '+lines[12]+'\n'
                      '14. '+lines[13]+'\n'
                      '15. '+lines[14]+'\n'
                      '16. '+lines[15]+'\n'
                      '17. '+lines[16]+'\n'
                      '18. '+lines[17]+'\n'
                      '19. '+lines[18]+'\n'
                      '20. '+lines[19]+'\n')
                input_station = int(input())
                for line in lines:  # Проходимся по каждой строчке
                    key, value = line.split('=')  # Разделяем ключ от значения через равно (radio = genre:station)
                    conf_dict.update({key: value})  # Добавляем в словарь
                return (os.listdir('.\\stations')[input_type-1][:-4] + ':' + list(conf_dict.values())[(input_station - 1)],
                        list(conf_dict.keys())[(input_station - 1)])
                break

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def station_select():
    global conf_dict
    if ('station' in conf_dict and 'to_adv' in conf_dict):
        with open('.\\stations\\' + conf_dict['station'].split(':')[0] + '.lst', 'r',
                  encoding='UTF-8') as file:  # Читаем файл
            search_station = {}
            lines = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк
        for line in lines:  # Проходимся по каждой строчке
            key, value = line.split('=')  # Разделяем ключ от значения через равно (radio = genre:station)
            search_station.update({key: value})  # Добавляем в словарь
        print('Обнаружена конфигурация:\n-Текущее радио: ' + radio_types[conf_dict['station'].split(':')[0]]
              + ' - ' + get_key(search_station, conf_dict['station'].split(':')[1]))
        print('-Количество песен до рекламы: ' + conf_dict['to_adv'])
        print('Желаете сменить настройки? 0 - работать с текущими параметрами, 1 - сменить конфигурацию')
        answer = 2
        while (answer != 1 or answer != 0):
            try:
                answer = int(input())
                if (answer == 1 or answer == 0):
                    if answer == 1: conf_dict = {}
                    break
            except:
                None
            os.system("cls")
            print('Введено не число или не верное число, 0 - работать с текущими параметрами, 1 - сменить конфигурацию')

station_select()

while not ('station' in conf_dict or 'to_adv' in conf_dict):
    temp_conf = open('conf.ini', 'w+')
    temp_conf.seek(0)
    print('Настройка конфигурации, необходимо выбрать параметры работы радио')
    sleep(0.5)
    station = select_station(station, station)
    c_station = station[1]
    station = 'station=' + station[0] + '\n'
    sleep(0.5)
    to_adv = -1
    print('Введите количество песен до рекламы. 0 - воспроизводить только рекламу')
    try:
        while to_adv < 0:
            to_adv = int(input())
            if to_adv >= 0:
                break
            print('Введено неверное значение. Введите количество песен до рекламы. 0 - воспроизводить только рекламу')
    except:
        print('Введено неверное значение. Введите количество песен до рекламы. 0 - воспроизводить только рекламу')
    to_adv = 'to_adv=' + str(to_adv)
    to_write = [station, to_adv]
    temp_conf.writelines(to_write)
    temp_conf.close()
    with open('conf.ini', 'r') as file:
        lines = file.read().splitlines()
    conf_dict = {}
    for line in lines:
        key, value = line.split('=')
        conf_dict.update({key: value})
    os.system("cls")
    station_select()

# Создаём папки для радио и рекламы, если они отсутствуют
if not (os.path.exists('radio')):
    os.mkdir('radio')
if not (os.path.exists('adv')):
    os.mkdir('adv')

static_genre = conf_dict['station']
to_adv = int(conf_dict['to_adv'])

adv_count = 0 # Внутренняя переменная для подсчёта сколько песен для включения рекламы
files = os.listdir(path='.\\adv') # Дополнительная переменная для указания папки с рекламой
dict_adv = os.listdir(path='.\\adv') # Словарь, харнящий в себе список рекламных треков
with open('token.txt', 'r', encoding='Windows-1251') as token_temp:
    tmp_token = token_temp.read()
#try:
client = Client(tmp_token).init() # Инициализация яндекс-музыки и подключение к аккаунту по токену
#except:
#    os.system('cls')
#    print('Ошибка доступа к яндексу. Сохраните ваш токен в файле token.txt')
#    sleep(8)
#    exit()
# Метод получения станции для проигрывания. По умолчанию выводит случайную станцию, в данной реализации - станцию из текстового документа
_stations = client.rotor_stations_list()
_station_random_index = floor(len(_stations) * random())
_station = _stations[_station_random_index].station
_station_id = static_genre
_station_from = _station.id_for_from
# Запуск клиента радио
radio = Radio(client)
# Получаем первый трек для радио
print(_station_id)
print(to_adv)

with open('.\\stations\\' + conf_dict['station'].split(':')[0] + '.lst', 'r',
          encoding='UTF-8') as file:  # Читаем файл
    search_station = {}
    lines = file.read().splitlines()  # read().splitlines() - чтобы небыло пустых строк
for line in lines:  # Проходимся по каждой строчке
    key, value = line.split('=')  # Разделяем ключ от значения через равно (radio = genre:station)
    search_station.update({key: value})  # Добавляем в словарь

try:
    first_track = radio.start_radio(_station_id, _station_from)
except:
    os.system('cls')
    print('Ошибка доступа к яндексу. Сохраните ваш токен в файле token.txt или перезагрузите программу')
    sleep(8)
    exit()
try_track_dict = first_track
print('Инициализация радио...')
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
            print("Сейчас играет радио: " + radio_types[conf_dict['station'].split(':')[0]]
              + ' - ' + get_key(search_station, conf_dict['station'].split(':')[1]))
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