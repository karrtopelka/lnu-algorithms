# Max Plotitsyn's program for implementation of Selection Sort


# Function to do selection sort
def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Driver code to test above
array = [64, 25, 12, 22, 11]
array_two = ["m", "a", "w", "x", "g"]

selection_sort(array)
print("Sorted array:")
for k in range(len(array)):
    print("%d" % array[k])

print()

selection_sort(array_two)
print("Sorted array two:")
for k in range(len(array_two)):
    print("%s" % array_two[k])

