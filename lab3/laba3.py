from Fraction import*
from Book import*
from Library import*
from AppTask3 import*
from StringFormatter import*
from StringFormatterApp import*
import wx

#1. Задан простой класс Fraction для представления дробей: 
def task1():
    frac = Fraction(7,2)
    print(-frac) # выводит -7/2
    print(~frac) # выводит 2/7
    print(frac**2) # выводит 49/4
    print(float(frac)) # выводит 3.5
    print(int(frac)) # выводит 3
#task1()

#2. Напишите классы «Книга» (с обязательными полями: название, автор,код), 
#«Библиотека» (с обязательными полями: адрес, номер) и корректно свяжите их

def task2():

    lib = Library(1, '51 Some str., NY')
    lib += Book.Book('Leo Tolstoi', 'War and Peace')
    lib += Book.Book('Charles Dickens', 'David Copperfield')
    lib += Book.Book('Чоткий Паца', 'Аугментированные люди , Которые желают  , приобрести,,,,,,,, Конечности')

    for book in lib:
        print(book._id , end = '. ')
        print(book, end = ' ')
        print(book.tag())

#task2()

#3. Создайте графическую оболочку для скрипта, написанного в ходе выполнения задания № 4 лабораторной работы № 2, в виде диалогового
#окна. Рекомендуется использовать wxPython или PyQt

def task3():

    app = wx.App()
    frame = AppTask3()
    frame.Show()
    app.MainLoop()
    del app
#task3()

#4. Напишите простой класс StringFormatter для форматирования строк
def task4():

    text = 'jfkjdsf  182фыв 3943выа 2 ad skf jns lkd f1f g56549 322.348.39.29'

    format = StringFormatter();
    print(text)
    print(format.del_word(text, 5))
    print(format.replace_digit(text))
    print(format.insert_space(text))
    print(format.sort_size(text))
    print(format.sort_alphabet(text))

#task4()

#5. Напишите скрипт с графическим интерфейсом пользователя для демонстрации работы класса StringFormatter. Разные комбинации
#отмеченных чекбоксов приводят к разным цепочкам операций форматирования задаваемой в верхнем поле строки с разными результатами

def task5():

    app = wx.App()
    frame = StringFormatterApp()
    frame.Show()
    app.MainLoop()

task5()