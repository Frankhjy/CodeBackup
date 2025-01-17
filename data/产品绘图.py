import matplotlib.pyplot as plt
#文字编码设置为UTF-8
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 数据准备
years = ['2019', '2020', '2021', '2022', '2023']

# 高新技术产品的海关编码
high_tech_imports = {
    '28 (无机化学品)': [1.589728e+08 , 2.365883e+08 , 3.064371e+08 , 4.342205e+08 , 3.877746e+08],
    '29 (有机化学品)': [6.486574e+09 , 6.068184e+09 , 7.099800e+09 , 6.881857e+09 , 6.350565e+09],
    '30 (药品)': [2.260654e+10 , 2.314932e+10 , 2.762393e+10 , 3.014621e+10 , 3.341933e+10],
    '38 (杂项化学品)': [1.046984e+09 , 1.267918e+09 , 1.645443e+09 , 6.894167e+09 , 7.070147e+09],
    '84 (机械设备)': [6.183108e+10 , 6.317268e+10 , 7.950280e+10 , 6.960895e+10 , 7.396797e+10],
    '85 (电机、电气设备)': [2.053439e+11 , 2.160336e+11 , 2.498469e+11 , 2.384429e+11 , 1.978927e+11],
    '88 (飞行器及零件)': [6.682712e+08 , 4.245172e+08 , 4.159886e+08 , 4.331074e+09 , 5.486194e+09],
    '90 (光学和医疗器械)': [3.469094e+10 , 3.648465e+10 , 4.147032e+10 , 4.182399e+10 , 4.133833e+10]
}

high_tech_exports = {
    '28 (无机化学品)': [5.511682e+07, 1.057695e+08, 8.369085e+07, 1.219078e+08, 4.782166e+08],
    '29 (有机化学品)': [1.836789e+10, 1.990963e+10, 2.668098e+10, 3.215534e+10, 2.410451e+10],
    '30 (药品)': [2.411620e+09, 4.584728e+09, 1.057886e+10, 4.409923e+09, 3.195751e+09],
    '38 (杂项化学品)': [1.372708e+09, 1.452519e+09, 2.135033e+09, 1.212560e+10, 5.197344e+09],
    '84 (机械设备)': [1.482675e+11, 1.605754e+11, 1.895130e+11, 1.861155e+11, 1.526174e+11],
    '85 (电机、电气设备)': [2.137410e+11, 2.224585e+11, 2.674307e+11, 3.209523e+11, 2.869153e+11],
    '88 (飞行器及零件)': [1.046452e+08, 1.407004e+08, 3.754465e+08, 6.119949e+09, 5.984412e+09],
    '90 (光学和医疗器械)': [1.974686e+10, 2.646111e+10, 3.149890e+10, 3.114448e+10, 2.981085e+10]
}

# 绘制高新技术产品进口趋势图
plt.figure(figsize=(14, 7))
for category, values in high_tech_imports.items():
    plt.plot(years, values, marker='o', label=category)
plt.title('China High-Tech Product Imports (2019-2023)')
plt.xlabel('Year')
plt.ylabel('Import Value (in Billions)')
plt.legend()
plt.grid(True)
plt.show()

# 绘制高新技术产品出口趋势图
plt.figure(figsize=(14, 7))
for category, values in high_tech_exports.items():
    plt.plot(years, values, marker='o', label=category)
plt.title('China High-Tech Product Exports (2019-2023)')
plt.xlabel('Year')
plt.ylabel('Export Value (in Billions)')
plt.legend()
plt.grid(True)
plt.show()