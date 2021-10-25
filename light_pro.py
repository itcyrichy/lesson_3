'''
методами строк очистить текст от знаков препинания;
сформировать list со словами (split);
привести все слова к нижнему регистру (map);
получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
'''
with open ("text.txt", "r",encoding="utf-8") as f:
    data=f.readlines()
data=str(data)
simbol_str: str='.,[]\\n;:\'—«?»()!'
# print(simbol_str)
def replacer(text,simbol_str):
    for i in simbol_str:
        text=text.replace(str(i),'')
    return text
text=replacer(data,simbol_str)
print(text)

list_of_words=text.split()
list_of_words=list(map(str.lower,list_of_words))
print(list_of_words)
print('\n')

from collections import Counter
c=Counter(list_of_words)
slovar=dict(c)
list_of_pairs=[]

for i in slovar.items():
    list_of_pairs.append({'word':i[0],'count':i[1]})
print(list_of_pairs)
print('\n')

from operator import itemgetter
print(sorted(list_of_pairs, key=itemgetter('count'),reverse=True)[:5])
# Примитивные попытки:
# data.replace('.','').replace(',','').replace('[','').replace(']','').replace('\n','').replace('\'','').replace(';','')\
# .replace('—','').replace('?','').replace('«','').replace(':','').replace('»','')
# print(data,type(data))

print(set(list_of_words),'\n',len(set(list_of_words)))
print('\n')

import pymorphy2
morph = pymorphy2.MorphAnalyzer()
normal_forms=[]
for word in list_of_words:
    norm_form=morph.parse(word)[0]
    normal_forms.append(norm_form.normal_form)

print(normal_forms)