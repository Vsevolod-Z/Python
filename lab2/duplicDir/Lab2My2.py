# -*- coding: utf-8 -*-
import os
import re
import hashlib
import subprocess

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

def duplic_find():
    path = 'duplicDir'
    files = os.listdir(path)
    nums = []
    for file in files:
        with open(f'{path}\{file}',"rb") as file:
            nums.append(hashlib.md5(file.read()).hexdigest())

    for i in range(len(files) - 1):
        for j in range(i + 1, len(files)):
            if nums[i] == nums[j]:
                print('Группа дубликатов:', files[i], files[j])

duplic_find()