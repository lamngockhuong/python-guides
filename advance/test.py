import numpy as np
import matplotlib.pyplot as plt

# Tính toán x và y để lấy 1 số cặp điểm trên đồ thị hình sin và cosin
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Vẽ đồ thị theo các điểm dữ liệu dùng matplotlib

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')  # nhãn trục x
plt.ylabel('y axis label')  # nhãn trục y
plt.title('Sine and Cosine')  # set tiêu đề
plt.legend(['Sine', 'Cosine'])  # Hiển thị chú thích của đồ thị
plt.show()
