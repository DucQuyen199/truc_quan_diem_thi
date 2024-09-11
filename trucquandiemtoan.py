import pandas as pd
import matplotlib.pyplot as plt
import pyodbc
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-G9HNNUG;DATABASE=thpt24;UID=sa;PWD=1')
query = "SELECT sbd, toan FROM [dbo].[diem_thi_thpt_2024] WHERE toan > 9.8;"
data = pd.read_sql(query, conn)
print(data)
plt.figure(figsize=(10, 6))
plt.hist(data['toan'], bins=10, edgecolor='black')
plt.title('Phổ điểm môn Toán (>9.8)')
plt.xlabel('Điểm Toán')
plt.ylabel('Số Lượng Thí Sinh')
plt.show()
