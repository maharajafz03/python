
array = [11,2,3,4,5,7]

# array.pop()

array.append(64)
array.insert(0, "hello")

print(array[3])
print(array)

num = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def find_max_element(num: List[int]) -> int:
    pass

from typing import List

def find_max_element(arr: List[int]) -> int:
    max_element = arr[0]  # Initialize max_element to the first element of the array
    for num in arr:
        if num > max_element:
            max_element = num
            print(max_element)

