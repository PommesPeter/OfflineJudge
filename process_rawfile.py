import pandas as pd
import numpy as np

import os

all_text = []

with open(os.path.join('./raw', 'mul.txt'), 'r', encoding='UTF-8') as f:
    all_text = f.readlines()
res = ""
j = 1
for i, item in enumerate(all_text):
    if item.startswith("正确答案"):
        print(i, item)

        res += (str(j) + '、')

        res += (all_text[i - 5].split('\n')[0] + ',')

        if len(item.split('：')[-1]) >= 3:
            print(item.split('：')[-1])
            res += '多选,'
            for ansc in item.split('\n')[0].split('：')[-1].split('、'):
                res += ansc
            res += ','
        else:
            res += '单选,'
            res += item.split('\n')[0].split('：')[-1] + ','

        res += (all_text[i - 4].split('\n')[0].split('.')[-1] + ',')
        res += (all_text[i - 3].split('\n')[0].split('.')[-1] + ',')
        res += (all_text[i - 2].split('\n')[0].split('.')[-1] + ',')
        res += (all_text[i - 1].split('\n')[0].split('.')[-1] + ',')
        res += '0'
        res += '\n'
        j += 1

f = open(os.path.join('./test', 'test2.csv'), 'w', encoding='UTF-8')
print(res)
f.writelines(res)
