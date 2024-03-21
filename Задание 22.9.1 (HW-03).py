import random

def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)
    return array

def binary_search(array, element, left, right):
    if left > right:
            return False
    middle = (right + left) // 2

    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
element = int(input("Введите любое число из указанного списка: "))

array = sorted(array)

print('Отсортированный список:', array)

left = int(array[0])
right = int(array[-1])

if element < left or element > right:
    print('Числа нет в списке')
else:
    print('Позиция введенного числа:', binary_search(array, element, 0, len(array) - 1))

position=binary_search(array, element, 0, len(array)-1) 
if position == len(array)-1:
    print('Позиции элементов перед и после введенного числа:', binary_search(array, element, 0, len(array)-1)-1, binary_search(array, element, 0, len(array)-1))
elif position ==0:
    print('Позиции элементов перед и после введенного числа:', binary_search(array, element, 0, len(array)-1), binary_search(array, element, 0, len(array)-1)+1)
else:
   print ('Позиции элементов перед и после введенного числа:', binary_search(array, element, 0, len(array)-1)-1, binary_search(array, element, 0, len(array)-1)+1)
