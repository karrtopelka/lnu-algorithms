# Програма Макса Плотіцина з поясненням роботи selection sort


# Функція selection sort
def selection_sort(arr):
    # пройти всі елементи масиву
    for i in range(len(arr)):
        # знайти мінімальний елемент з несортованого масиву
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        # поміняти місцями знайдений мінімальний елемент з першим елементом
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Код щоб перевірити
array = [64, 25, 12, 22, 11]
array_two = ["m", "a", "w", "x", "g"]

selection_sort(array)
print("Sorted array:")
for k in range(len(array)):
    print("%d" % array[k])

print('\n')

selection_sort(array_two)
print("Sorted array two:")
for k in range(len(array_two)):
    print("%s" % array_two[k])
