import pandas as pd
import matplotlib.pyplot as plt
import pyodbc

# Kết nối tới SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-G9HNNUG;DATABASE=thpt24;UID=sa;PWD=1')

# Truy vấn dữ liệu từ bảng
query = """
SELECT ma_ngoai_ngu
FROM diem_thi_thpt_2024
"""
df = pd.read_sql(query, conn)

# Đóng kết nối
conn.close()

# Thống kê số thí sinh thi ngoại ngữ và không thi ngoại ngữ
num_tester_foreign_lang = df['ma_ngoai_ngu'].notna().sum()
num_non_tester_foreign_lang = df['ma_ngoai_ngu'].isna().sum()

# Dữ liệu cho biểu đồ tròn
labels = ['Thi Ngoại Ngữ', 'Không Thi Ngoại Ngữ']
sizes = [num_tester_foreign_lang, num_non_tester_foreign_lang]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)

# Tạo biểu đồ tròn
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Phân phối số thí sinh thi và không thi ngoại ngữ')
plt.axis('equal')  # Đảm bảo biểu đồ tròn
plt.show()
