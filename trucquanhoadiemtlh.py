import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

# Kết nối tới SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-G9HNNUG;DATABASE=thpt24;UID=sa;PWD=1')

# Lấy dữ liệu
query = """
SELECT sbd, toan, vat_li, hoa_hoc, (toan + vat_li + hoa_hoc) AS tong_diem
FROM [dbo].[diem_thi_thpt_2024]
WHERE (toan + vat_li + hoa_hoc) > 29;
"""
data = pd.read_sql(query, conn)

# Hiển thị số lượng học sinh có tổng điểm > 29
so_luong_hoc_sinh = len(data)
print(f"Số lượng học sinh có tổng điểm Toán, Lý, Hóa > 29: {so_luong_hoc_sinh}")

# Vẽ biểu đồ Histogram
plt.figure(figsize=(10, 6))
plt.hist(data['tong_diem'], bins=10, edgecolor='black')
plt.title('Phổ điểm tổng của Toán, Lý, Hóa (>29)')
plt.xlabel('Tổng điểm Toán, Lý, Hóa')
plt.ylabel('Số lượng học sinh')
plt.show()
