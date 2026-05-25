import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 系統中可使用的樣式  >>> plt.style.available

# plt.style.use("seaborn-v0_8")
plt.style.use('seaborn-v0_8-colorblind')
# 設定支援繁體中文的字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # Windows 微軟正黑體
# 或 macOS 使用：['Heiti TC'] 或 ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示為方塊

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("平方數", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", labelsize=14)

plt.show()
