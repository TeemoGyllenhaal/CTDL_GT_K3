import random

def sinh_so_ngau_nhien(n):
    lst = []
    for i in range(n):
        random_number = random.randint(0, 100)
        lst.append(random_number)
    return lst

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left_arr = lst[:mid]
        right_arr = lst[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0

        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i] < right_arr[j]:
                lst[k] = left_arr[i]
                i += 1
            else:
                lst[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            lst[k] = left_arr[i]
            i += 1
            k = k + 1

        while j < len(right_arr):
            lst[k] = right_arr[j]
            j += 1
            k = k + 1

def main():
    lst = sinh_so_ngau_nhien(10)
    print("Mang ban dau la:", lst)
    merge_sort(lst)
    print("Mang sau khi sap xep la:", lst)

if __name__ == "__main__":
    main()

