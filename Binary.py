 def binary_search(array, target):
  """Performs a binary search on a sorted array to find the target element.

  Args:
    array: A sorted list of elements.
    target: The element to search for.

  Returns:
    The index of the target element in the array, or -1 if the element is not found.
  """

  low = 0
  high = len(array) - 1

  while low <= high:
    mid = (low + high) // 2

    if target == array[mid]:
      return mid
    elif target < array[mid]:
      high = mid - 1
    else:
      low = mid + 1

  return -1

# Example usage:

array = [1, 3, 5, 7, 9]
target = 7

index = binary_search(array, target)

if index == -1:
  print("The target element is not found in the array.")
else:
  print("The target element is found at index {}.".format(index))
