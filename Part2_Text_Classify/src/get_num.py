# -*- coding: utf-8 -*-
import os


def get_has_num():
    file_path = '../data_cls_re'
    in_file_list = os.listdir(file_path)
    for file_name in in_file_list:
        in_file = open(file_path +"/"+ file_name, 'r', encoding='utf-8')
        data = in_file.readline().split(",")[1]



        data_temp = data.split(" ")
        word_in_file_stat = {}
        for word in data_temp:
            print(word)


if __name__ == '__main__':
    get_has_num()
