# encoding:utf-8

import sys
from importlib import reload

import jieba
import re
from collections import Counter

reload(sys)


# sys.setdefaultencoding('utf-8')  # 设置默认编码为utf-8


## 计算词频的例子
def com_tf():
    f = open('data/7s.txt', encoding="utf-8")
    data = f.read()
    # data_temp =data.encode()# 转换为unicode编码形式
    data = ''.join(re.findall(u'[\u4e00-\u9fff]+', data))  # 必须为unicode类型，取出所有中文字符
    # sts = data.translate(None, string.punctuation)            # 删除英文的标点符号，中文标点不支持。

    data2 = jieba.cut(data)  # 分词
    data3 = " ".join(data2)  # 结果转换为字符串（列表转换为字符串）

    open('data/7temp.txt', 'w',encoding="utf-8").write(data3)  # 分词结果写入7temp.txt

    wlist = data3.split()  # 将分词结果按空格切割为列表（字符串的切割）
    num_dict = Counter(wlist)  # 统计词频

    # 统计结果写入result.txt(字典的遍历)
    for (k, v) in num_dict.items():
        open('data/result.txt', 'a+',encoding="utf-8").write(str(k) + ' ' + str(v) + '\n')  # 将k，v转换为str类型


if __name__ == '__main__':
    com_tf()
