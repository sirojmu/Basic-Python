nums = [10, 20, 30, 40, 50]
x = 30


def binary_search(nums, x):
    low, high = 0, len(nums) - 1  # inisiasi titik low dan high
    while low <= high:
        mid = (low + high) // 2  # deklarasi titik mid
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # bila hasil tidak ditemukan
