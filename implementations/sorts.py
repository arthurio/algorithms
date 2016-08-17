# Algorithm         Time Complexity                                Space Complexity
#                   Best          Average         Worst            Worst
# ----------------------------------------------------------------------------------
# Quicksort         O(n log(n))   O(n log(n))     O(n^2)           O(log(n))
# Mergesort         O(n log(n))   O(n log(n))     O(n log(n))      O(n)
# Timsort           O(n)          O(n log(n))     O(n log(n))      O(n)
# Heapsort          O(n log(n))   O(n log(n))     O(n log(n))      O(1)
# Bubble Sort       O(n)          O(n^2)          O(n^2)           O(1)
# Insertion Sort    O(n)          O(n^2)          O(n^2)           O(1)
# Selection Sort    O(n^2)        O(n^2)          O(n^2)           O(1)
# Tree Sort         O(n log(n))   O(n log(n))     O(n^2)           O(n)
# Shell Sort        O(n log(n))   O(n(log(n))^2)  O(n(log(n))^2)   O(1)
# Bucket Sort       O(n+k)        O(n+k)          O(n^2)           O(n)
# Radix Sort        O(nk)         O(nk)           O(nk)            O(n+k)
# Counting Sort     O(n+k)        O(n+k)          O(n+k)           O(k)
# Cubesort          O(n)          O(n log(n))     O(n log(n))      O(n)


def insertion_sort(array):
    current_index = 1

    # Loop through whole array
    while current_index < len(array):
        # Get element
        current_element = array[current_index]
        # Position the current element in the sorted side
        i = current_index - 1
        # Loop through sorted side from right to left
        while i >= 0:
            # If the element of the sorted side is greater than our element, move it to the right
            if array[i] > current_element:
                # Move element to the right
                array[i + 1] = array[i]
                # Keep going
                i = i - 1
            else:  # We found the element's place
                # stop going through sorted side
                break

        # place the element
        array[i + 1] = current_element

        # Move up the list
        current_index += 1


def quicksort(array):
    quicksort_recursion(array, 0, len(array) - 1)


def quicksort_recursion(array, li, ri):
    if li < ri:
        pivot_index = quicksort_partition(array, li, ri)
        quicksort_recursion(array, li, pivot_index - 1)
        quicksort_recursion(array, pivot_index + 1, ri)


def quicksort_partition(array, li, ri):
    # The pivot will always be the right most element
    current_index = li
    # We scan the elements between left most index and the index of the pivot
    while current_index <= ri:
        # If the element is smaller or equal than the pivot
        if array[current_index] <= array[ri]:
            # swap with the element right most of the delimiter
            array[li], array[current_index] = array[current_index], array[li]
            # If the current_index is not on the pivot
            if current_index != ri:
                # Move index of delimiter by one to the right
                li += 1
        current_index += 1

    return li


# Fake in place for now
def merge_sort_in_place(array):
    sorted_array = merge_sort(array)
    for i, value in enumerate(sorted_array):
        array[i] = value


def merge_sort(array):
    if len(array) <= 1:
        return array

    left_array = merge_sort(array[:len(array) / 2])
    right_array = merge_sort(array[len(array) / 2:])
    return merge(left_array, right_array)


def merge(left_array, right_array):
    merged_array = []
    while len(left_array) + len(right_array) != 0:
        if not left_array:
            merged_array.append(right_array.pop(0))
            continue
        if not right_array:
            merged_array.append(left_array.pop(0))
            continue
        if left_array[0] < right_array[0]:
            merged_array.append(left_array.pop(0))
            continue
        merged_array.append(right_array.pop(0))

    return merged_array


def bubble_sort(array):
    is_sorted = True
    i = 1
    while True:
        if i >= len(array):
            if is_sorted:
                break
            is_sorted = True
            i = 1
            continue

        if array[i - 1] > array[i]:
            array[i - 1], array[i] = array[i], array[i - 1]
            is_sorted = False

        i += 1
