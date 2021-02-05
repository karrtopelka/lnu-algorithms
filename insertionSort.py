# Max Plotitsyn's program for implementation of Insertion Sort


# Function to do insertion sort
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Driver code to test above
array = [12, 11, 13, 5, 6]
array_two = ["m", "a", "w", "x", "g"]
array_three = []

insertion_sort(array)
print("Sorted array:")
for k in range(len(array)):
    print("%d" % array[k])

print()

insertion_sort(array_two)
print("Sorted array two:")
for k in range(len(array_two)):
    print("%s" % array_two[k])
