# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов
list1 = gen_list(20, -10, 10)
sort(list1)
print(list1)
print(f"summax = {sum(list1[-1:-11:-1])}")
# quick_sort(a)
# print(a)
