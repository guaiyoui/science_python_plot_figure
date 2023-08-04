import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as mfm

font_path_Linli_B = "./fonts/LinLibertine_RB.ttf"
prop_Linli_B = mfm.FontProperties(fname=font_path_Linli_B, size=32, weight='light')
mfm.fontManager.addfont(font_path_Linli_B)
plt.rcParams['font.family'] = prop_Linli_B.get_name()

fig, ax = plt.subplots() # 创建图实例
x = np.linspace(0,2,100) # 创建x的取值范围

edgecolors =  ["#689FBF", "#999999", "#377D22", '#5A6A37', "#F0855B", "#75140C", "#E06661"]

y1 = x
ax.plot(x, y1, c=edgecolors[0], label='linear') # 作y1 = x 图，并标记此线名为linear
y2 = x ** 2
ax.plot(x, y2, c=edgecolors[6],label='quadratic') #作y2 = x^2 图，并标记此线名为quadratic
# y3 = x ** 3
# ax.plot(x, y3, label='cubic') # 作y3 = x^3 图，并标记此线名为cubic
ax.set_xlabel('x label') #设置x轴名称 x label
ax.set_ylabel('y label') #设置y轴名称 y label
ax.set_title('Simple Plot') #设置图名为Simple Plot
ax.legend() #自动检测要在图例中显示的元素，并且显示

plt.show()
plt.savefig("line.png", dpi=600, bbox_inches='tight')
plt.savefig("line.pdf", dpi=600, bbox_inches='tight')
