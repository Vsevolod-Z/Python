# -*- coding: utf-8 -*-
import os
import re
import hashlib
import subprocess

#1 
#Напишите скрипт, который читает текстовый файл и выводит символы в порядке убывания частоты встречаемости в тексте. Регистр символа
#не имеет значения. Программа должна учитывать только буквенные символы (символы пунктуации, цифры и служебные символы слудет игнорировать).
def let_count():
    
    file = open('task1.txt')
    text = file.read()
    file.close()
    letters_dict = {}
    for i in text: 
        if i.isalpha():
            letters_dict[i.lower()] = text.count(i)
    for value in sorted(letters_dict.keys(), key=letters_dict.get, reverse=True):
        print(value, " meets: ", letters_dict[value])
#let_count()

#2
#Напишите скрипт, позволяющий искать в заданной директории и в ее подпапках файлы-дубликаты на основе сравнения контрольных сумм (MD5). 
#Файлы могут иметь одинаковое содержимое, но отличаться именами. Скрипт должен вывести группы имен обнаруженных файлов дубликатов. 
def duplic_find():
    i = 0
    path = 'duplicDir'
    files = os.listdir(path)
    nums = []
    for file in files:
        with open(f'{path}\{file}',"rb") as file:
            nums.append(hashlib.md5(file.read()).hexdigest())

    for i in range(len(files) - 1):
        if nums[i] != nums[i-1]:
            print('Группа дубликатов:\n',files[i])
        for j in range(i + 1, len(files)):
            
            if nums[i] == nums[j]:
                if nums[j] == nums[i-1]:
                    print()
                else:
                    print(files[j])

#duplic_find()

#3
#Задан путь к директории с музыкальными файлами (в названии которых нет номеров, а только названия песен) и текстовый файл,
#хранящий полный список песен с номерами и названиями в виде строк формата «01. Freefall [6:12]». 
#Напишите скрипт, который корректирует имена файлов в директории на основе текста списка песен

def track_name_replace():
    track_dir = 'Tracks'
    with open('track_list.txt',"r", encoding="utf-8") as t_list:
        for file in os.listdir(track_dir):
            fname = t_list.readline().rstrip()+'.mp3'
            os.rename(f'{track_dir}/{file}', f'{track_dir}/{fname}')

#track_name_replace()

#4
#Напишите скрипт, который позволяет ввести с клавиатуры имя текстового файла, найти в нем с помощью регулярных выражений все
#подстроки определенного вида, в соответствии с вариантом 
#Вариант 3: найдите все IPv4-адреса – подстроки вида «192.168.5.48»

def get_data(file_name):
    if os.path.exists(os.getcwd() + '\\' + file_name):
        with open(file_name) as file:
            text = [i for i in file]
        return text


def get_substr(text, reg):
    words = text.split(' ')
    print(words)
    substr = ['Начало']
    for i in range(len(words)):
        substr  = re.findall(reg, text)
    print(substr)
    with open('ip_new.txt',"w") as file:
        for i in range(len(substr)):
            file.write(substr[i])
            print()
            
def search_type():
    reg = r"\D(?:[0-9]{3})(?:\.[0-9]+){3}"
    with open('ip_list.txt') as file:
        text = file.read()
        print(text)
    get_substr(text,reg)
    
#search_type()

#5
#Введите с клавиатуры текст. Программно найдите в нем и выведите отдельно все слова, которые начинаются с большого латинского
#символа (от A до Z) и заканчиваются 2 или 4 цифрами, например «Petr93», «Johnny70», «Service2002». Используйте регулярные выражения

input_text = input('Введите текст: ') #text = 'Petr93 Johnny70 Service2002 djsd1234595'

def check_input(text, reg):
    for i in range(len(text)):
        parser = re.search(reg,text[i])
        count = 0
        while parser!=None:
            yield i+1,parser.regs[0][0] + count + 1, parser.group()
            count += parser.regs[0][1]
            text[i] = text[i][parser.regs[0][1]:]
            parser = re.search(reg,text[i])

reg = "[A-Z][A-Za-z]+([[0-9]{2}$|0-9]{4}$)"
[print(output_text) for i, j, output_text in check_input(input_text.split(),reg)]