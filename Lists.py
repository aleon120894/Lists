# Дан упорядоченный список книг. Добавить новую книгу, сохранив упорядоченность списка.
books = ["Forever War", "Chasm City", "Ringworld"]

books.append("Ubik")

print(books)

# Дан список состоящий чисел. Выяснить сколько раз входит ли некоторое число в список.

numbers = [1, 2, 3, 4]

print(numbers.count(1))
print(numbers.count(2))
print(numbers.count(3))
print(numbers.count(4))



# Найдите сумму четных чисел списка которые являются числом.
a = [1, 2, 3, 4, 5, 6, 7, 8]

def even_count(n):

    even = []
    for i in n:
        if i % 2 == 0:
            even.append(i)

    the_sum = 0
    for i in even:
        the_sum = the_sum + i
    return the_sum

print(even_count(a))


# Дан пустой список. Заполнить список путем ввода данных с клавиатуры. Найти наибольший элемент списка.

l = []

for i in l:
    i = input("enter a number: ")

print(l)

# Создайте объект, который мог бы описать журнал посещаимости. Измените информацию о посещаимости второму студенту в списке. Отформатиройте вывод журнала.

 journal = {
             'Ivan Tyshchenko' : [['21-02', True], ['25-02', False]],
             'Oleksii Leontiev' : [['21-02', True], ['25-02', False]],
             'Olga Shklyarova' : [['21-02', True], ['25-02', False]]
 }






# ..
# [
#    ['Ivan Tyshchenko', [['21-02', True], ['25-02', False]]],
#    ...
# ]

# Пример вывода
# `
#   Ivan Tyshchenko:
#     21-01 +
#     25-02 -
#   ...
# `