import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

# Kết nối tới SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-G9HNNUG;DATABASE=thpt24;UID=sa;PWD=1')

# Truy vấn dữ liệu từ bảng
query = "SELECT toan FROM diem_thi_thpt_2024"
df = pd.read_sql(query, conn)

# Đóng kết nối
conn.close()

# Trực quan hóa điểm môn Toán từ 0 đến 10, bao gồm các giá trị lẻ với thang logarit
plt.figure(figsize=(10, 6))
plt.hist(df['toan'], bins=50, range=(0, 10), edgecolor='black', log=True)
plt.title('Phân phối điểm môn Toán (Thang logarit)')
plt.xlabel('Điểm')
plt.ylabel('Số lượng thí sinh (log)')
plt.grid(True)
plt.show()
