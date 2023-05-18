# khai báo thư viện
import networkx as nx
import matplotlib.pyplot as plt

# Yêu cầu nhập số đỉnh và số cạnh
n = int(input("Nhập số đỉnh: "))
m = int(input("Nhập số cạnh: "))

# Tạo đồ thị
G = nx.Graph()

# Thêm các đỉnh vào đồ thị
# tạo vòng lặp duyệt từ 1 đến n đỉnh trong đó i là số hiện tại của vòng lặp tương ứng với tên của đỉnh được thêm vào đồ thị
for i in range(1, n+1):
    G.add_node(i)

# Thêm các cạnh vào đồ thị
# tạo vòng lặp duyệt từ 1 đến m cạnh trong đó j là số hiện tại của vòng lặp tương ứng với các cạnh của đồ thị 
for j in range(1, m+1):
    # yêu cầu người dùng nhập 2 số nguyên u và v là đỉnh đầu và đỉnh cuối của cạnh 
    # hàm split tách chuỗi nhập vào bằng dấu cách
    # hàm map chuyển đổi các phần thành số nguyên 
    u, v = map(int, input("Nhập cạnh thứ %d nằm giữa 2 đỉnh : " % j).split())
    # Sau đó, đỉnh u và v được thêm vào đồ thị G bằng cách sử dụng hàm add_edge(u, v) của đối tượng G
    G.add_edge(u, v)

# Hiển thị đồ thị

plt.figure()
plt.title("đô thị vô hướng")
nx.draw(G, with_labels=True)
plt.show()


