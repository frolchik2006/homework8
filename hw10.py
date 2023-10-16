# Задача 44:
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?

import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = [{'whoAmI': item} for item in lst]

for entry in data:
    print(entry)

encoded_data = []
for entry in data:
    encoded_entry = {f'whoAmI_{entry["whoAmI"]}': 1}
    encoded_data.append(encoded_entry)

for entry in encoded_data:
    print(entry)