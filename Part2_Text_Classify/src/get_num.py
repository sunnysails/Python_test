# -*- coding: utf-8 -*-
import os


def get_has_num():
    file_path = '../data_cls_re'
    in_file_list = os.listdir(file_path)
    word_in_file_stat = {}
    for file_name in in_file_list:
        in_file = open(file_path + "/" + file_name, 'r', encoding='utf-8')
        data = in_file.readline().split(",")[1]

        data_temp = data.split(" ")
        for word in data_temp:
            # print(word)
            if word not in word_in_file_stat and word != '':
                word_in_file_stat[word] = []
                word_in_file_stat[word].append(data_temp.count(word))

    out_file = open('re.txt', 'w', encoding='utf-8')
    out_file.write(str(word_in_file_stat))
    # for (k, v) in word_in_file_stat.items():
    #     print(k+v)
    #     out_file.write(v + ',' + k + ' ' + '\n')
    # out_file.close()


if __name__ == '__main__':
    get_has_num()
