from tkinter import *
from pygame import mixer
from yandex_music import Client # API для обращения к яндекс-музыке/радио
from math import floor # Математические операции
from random import random # Рандом по объектам
from random import randint # Рандом по цифрам
import time
from time import sleep # Останока кода
from radio import Radio # Модуль радио radio.py (должен быть в папке с приложением)
import os # Модуль работы с ОС

if os.name == 'nt':
    #pypy does not find the dlls, so we add package folder to PATH.
    pygame_dir = os.path.split(__file__)[0]
    os.environ['PATH'] = os.environ['PATH'] + ';' + pygame_dir
    #Fix for the bpo-36085 change in Python3.8 on Windows
    os.add_dll_directory(pygame_dir)

if (os.path.exists('radio\\curr_track.mp3')):
    os.remove('radio\\curr_track.mp3')
if (os.path.exists('radio\\next_track.mp3')):
    os.remove('radio\\next_track.mp3')
b_playing = False
i_timer = 0
i_mtimer = 0
is_first_time = True
track_lenght = 0
track_artist = ''
track_title = ''
n_track_lenght = 0
n_track_artist = ''
n_track_title = ''
to_ads = 5
to_ads_count = 5


class MusicPlayer:
    def __init__(self, window ):
        window.geometry('340x220'); window.title('Iris Player'); window.resizable(0,0)
        Play = Button(window, text = 'Воспроизвести',  width = 12,font = ('Times', 10), command = self.play)
        Stop = Button(window, text = 'Стоп',  width = 12, font = ('Times', 10), command = self.stop)
        DeCounter = Button(window, text = 'Сброс счёта', width = 12, font = ('Times', 10), command= self.decounter)
        Settings = Button(window, text = 'Настройки', width = 12, font = ('Times', 10))
        track_id.place(x=10,y=2);lenght_label.place(x=50,y=22);timer_label.place(x=10,y=22);to_ads_label.place(x=10,y=42)
        Play.place(x=240,y=24);Stop.place(x=240,y=64);Settings.place(x=240,y=144);DeCounter.place(x=240,y=104)
        to_ads_label.config(text=('До рекламы: ' + str(to_ads_count)), font='Times 12')
        self.music_file = False
        self.playing_state = False

    def play(self):
        global i_timer
        global i_mtimer
        global b_playing
        get_track()
        mixer.init()
        mixer.music.load('curr_track.mp3')
        i_mtimer = 0
        i_timer = 0
        mixer.music.play()
        b_playing = True


    def stop(self):
        global b_playing
        global track_lenght
        track_id.config(text=time.strftime('',time.localtime()),
                      font='Times 12')
        track_lenght = 0
        b_playing = False
        mixer.music.stop()
        mixer.music.unload()

    def decounter(self):
        global to_ads_count, to_ads
        to_ads_count = to_ads
        to_ads_label.config(text=('До рекламы: ' + str(to_ads_count)), font='Times 12')


def update_clock(): # Если музыка в данный момент играет - ведём счётчик (сколько прошло от начала воспроизведения)
    global b_playing
    global i_timer
    global i_mtimer
    global track_lenght, track_title, track_artist, to_ads_count, to_ads
    if b_playing:
        timer_label.config(text=time.strftime(get_mins(i_timer) + ':' + get_secs(i_timer),time.localtime()),
                      font='Times 12')
        lenght_label.config(text=time.strftime('/ ' + get_mins(track_lenght) + ':' + get_secs(track_lenght),time.localtime()),
                      font='Times 12')
        track_id.config(text=time.strftime(str(track_artist) + ' - ' + str(track_title),time.localtime()),
                      font='Times 12')
        i_timer+=0.1
        if i_timer >= track_lenght and track_lenght != 0:
            MusicPlayer.stop(root)
            to_ads_count-=1
            to_ads_label.config(text=('До рекламы: ' + str(to_ads_count)), font='Times 12')
            sleep(0.5)
            MusicPlayer.play(root)

    else:
        timer_label.config(text=time.strftime('00:00',time.localtime()),
                      font='Times 12')
        lenght_label.config(text=time.strftime('/ 00:00',time.localtime()),
                      font='Times 12')
    root.after(100, update_clock)
    #print('NOW:', i_timer, 'TRACK:', track_lenght)



def get_mins(sec): # Получение из секунд минут (для счётчика)
    if sec/60 >= 10:
        return str(int(sec/60))
    else:
        return '0' + str(int(sec/60))

def get_secs(sec): # Получение из секунд остаток (для счётчика)
    if sec%60 >= 10:
        return str(int(sec%60))
    else:
        return '0' + str(int(sec%60))

def get_track():
    global track_lenght, track_title, track_artist
    first_track = radio.start_radio(_station_id, _station_from)
    first_track.download('curr_track.mp3')
    track_lenght = first_track.duration_ms / 1000
    track_artist = first_track['artists'][0]['name']
    track_title = first_track['title']
    print(first_track)

'''
def get_next_track():
    global track_lenght, track_title, track_artist, n_track_artist, n_track_title, n_track_lenght, is_first_time
    next_track = radio.play_next()
    next_track.download('radio\\next_track.mp3')
    n_track_title = next_track['title']
    n_track_artist = next_track['artists'][0]['name']
    n_track_lenght = next_track.duration_ms / 1000
    print(next_track)
'''
if not (os.path.exists('conf.ini')):
    config_file = open('conf.ini', 'w')
    config_file.close()


if not (os.path.exists('radio')):
    os.mkdir('radio')
if not (os.path.exists('adv')):
    os.mkdir('adv')

static_genre = "mood:happy"

adv_count = 0 # Внутренняя переменная для подсчёта сколько песен для включения рекламы
files = os.listdir(path='.\\adv') # Дополнительная переменная для указания папки с рекламой
dict_adv = os.listdir(path='.\\adv') # Словарь, харнящий в себе список рекламных треков

with open('token.txt', 'r', encoding='Windows-1251') as token_temp:
    tmp_token = token_temp.read()

client = Client(tmp_token).init()

_stations = client.rotor_stations_list()
_station_random_index = floor(len(_stations) * random())
_station = _stations[_station_random_index].station
_station_id = static_genre
_station_from = _station.id_for_from
# Запуск клиента радио
radio = Radio(client)


root = Tk()
timer_label = Label(root, font = ('Times', 10))# create the label for timer
timer_label.pack()
lenght_label = Label(root, font = ('Times', 10))
lenght_label.pack()
track_id = Label(root, font = ('Times', 10))
track_id.pack()
to_ads_label = Label(root, font = ('Times', 12))
to_ads_label.pack()
app= MusicPlayer(root)
root.after(0, update_clock)
root.mainloop()
