# Каждый ученик в классе изучает либо английский, либо французский, либо оба этих языка.
# У классного руководителя есть списки учеников, изучающих английский и французский языки.
# Помогите ему выяснить, сколько учеников в классе изучают только один язык.

# Входные данные:
# Для каждого ученика известны: Имя Фамилия и список изучаемых языков

# Для решения задачи подберите наиболее удобную структуру.
# Выведите: учеников, изучающих только один язык

import collections

scholars = [
    {"name": "John", "surname": "Doe", "langs": ["en", "fr"]},
    {"name": "Jim", "surname": "Doe", "langs": ["en"]},
    {"name": "Peter", "surname": "Doe", "langs": ["fr"]},
    {"name": "Eugene", "surname": "Donovan", "langs": ["en", "fr"]}

]

a1 = filter(lambda x: len(x["langs"]) == 2, scholars)
print(list(a1))
# for i in range(num_of_scholar):
#     scholar =
