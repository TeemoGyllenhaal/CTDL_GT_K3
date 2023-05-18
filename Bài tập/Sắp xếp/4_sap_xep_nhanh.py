# Hàm quick_sort(arr) dùng để sắp xếp một mảng arr sử dụng thuật toán quick sort
def quick_sort(arr):
    # Nếu độ dài mảng arr là 1 hoặc nhỏ hơn, hàm sẽ trả về mảng đó
    if len(arr) <= 1:
        return arr
    # Nếu độ dài mảng arr lớn hơn 1, hàm sẽ chọn một phần tử đầu tiên làm pivot
    # và phân chia mảng arr thành hai mảng con left và right
    # một mảng chứa các phần tử nhỏ hơn pivot và một mảng chứa các phần tử lớn hơn hoặc bằng pivot
    # Hàm đệ quy sử dụng thuật toán quick sort để sắp xếp các mảng con left và right
    # và sau đó ghép kết quả lại với phần tử pivot giữa chúng để tạo thành một mảng đã sắp xếp
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in arr[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [pivot] + quick_sort(right)

arr = input("Nhập một dãy số, các số cách nhau bởi khoảng trắng: ").split()
arr = [int(x) for x in arr]  # chuyển đổi chuỗi thành mảng số
sorted_arr = quick_sort(arr) # để sắp xếp mảng arr và lưu kết quả vào biến sorted_arr
print("Dãy số đã sắp xếp:", sorted_arr)

