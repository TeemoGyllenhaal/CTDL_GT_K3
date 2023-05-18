import matplotlib.pyplot as plt
import networkx as nx
import pprint
def nhap_ma_tran_ke():
    N = int(input("Nhập số đỉnh của đồ thị: "))

    adj = [[0] * (N + 1) for _ in range(N + 1)]  # Khởi tạo ma trận kề kích thước (N+1) x (N+1)

    M = int(input("Nhập số cạnh của đồ thị: "))
    print("Nhập các cạnh của đồ thị (u, v):")
    for i in range(M):
        u, v = map(int, input().split())
        adj[u][v] += 1  # Tăng số cạnh từ u đến v (Hàng u cột v) (Giá trị 0 -> 1)

    return adj

def ve_do_thi(ma_tran_ke):
    G = nx.DiGraph()  # Tạo đồ thị có hướng

    N = len(ma_tran_ke) - 1

    for u in range(1, N + 1):
        for v in range(1, N + 1):
            if ma_tran_ke[u][v] > 0:
                G.add_edge(u, v)  # Thêm cạnh từ u đến v

    # Vẽ đồ thị
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, arrows=True)
    plt.show()

# Chạy ví dụ
ma_tran_ke = nhap_ma_tran_ke()
pprint.pprint(ma_tran_ke)
ve_do_thi(ma_tran_ke)