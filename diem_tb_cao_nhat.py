import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

# Kết nối tới SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-G9HNNUG;DATABASE=thpt24;UID=sa;PWD=1')

# Truy vấn dữ liệu từ bảng
query = """
SELECT toan, ngu_van, ngoai_ngu, vat_li, hoa_hoc, sinh_hoc, lich_su, dia_li, gdcd
FROM diem_thi_thpt_2024
"""
df = pd.read_sql(query, conn)

# Đóng kết nối
conn.close()

# Tính điểm trung bình cho từng môn
mean_scores = df.mean()

# Tạo biểu đồ cột
plt.figure(figsize=(12, 8))
mean_scores.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Điểm Trung Bình Các Môn')
plt.xlabel('Môn')
plt.ylabel('Điểm Trung Bình')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
