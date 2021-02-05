# Програма Макса Плотіцина з поясненням роботи insertion sort


# Функція insertion sort
def insertion_sort(arr):

    # пройти через 1 до len(arr)
    for i in range(1, len(arr)):
        # перемістити елементи масиву[0..i-1], які більші за індекс, на одну позицію, випереджаючи їх поточну позицію
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Код щоб перевірити
array = [12, 11, 13, 5, 6]
array_two = ["m", "a", "w", "x", "g"]

insertion_sort(array)
print("Sorted array:")
for k in range(len(array)):
    print("%d" % array[k])

print()

insertion_sort(array_two)
print("Sorted array two:")
for k in range(len(array_two)):
    print("%s" % array_two[k])
