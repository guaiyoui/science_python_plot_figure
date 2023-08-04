import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as mfm


font_path_Linli = "./fonts/LinLibertine_R.ttf"
font_path_Linli_B = "./fonts/LinLibertine_RB.ttf"
font_path_Linli_BI = "./fonts/LinLibertine_RBI.ttf"
font_path_Linli_aBL = "./fonts/LinLibertine_aBL.ttf"
font_path_Linli_aBS = "./fonts/LinLibertine_aBS.ttf"
font_path_Linli_DR = "./fonts/LinLibertine_DR.ttf"
prop_Linli = mfm.FontProperties(fname=font_path_Linli, size=18, weight='normal')
prop_Linli_B = mfm.FontProperties(fname=font_path_Linli_B, size=32, weight='light')
prop_Linli_BI = mfm.FontProperties(fname=font_path_Linli_BI, size=32, weight='light')
prop_Linli_aBL = mfm.FontProperties(fname=font_path_Linli_aBL, size=32, weight='light')
prop_Linli_aBS = mfm.FontProperties(fname=font_path_Linli_aBS, size=32, weight='light')
prop_Linli_DR = mfm.FontProperties(fname=font_path_Linli_DR, size=32, weight='light')
mfm.fontManager.addfont(font_path_Linli_B)
plt.rcParams['font.family'] = prop_Linli_B.get_name()

# plt.xlabel('Dataset Network', fontproperties = prop_Linli_B)
# plt.ylabel('F1-score', fontproperties = prop_Linli_B)

plt.figure(num=3, figsize=(10, 5))

plt.ylim((0, 1.1))

size = 10

data_set = ['Citeseer', 'Cora', 'Facebook', 'Cornell', 'Texas', 'Washt', 'Wiscs', 'Reddit', 'Flickr', 'Friendster']
x = np.arange(size)
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)
d = np.random.random(size)
e = np.random.random(size)
f = np.random.random(size)

total_width, n = 0.8, 4
width = total_width / n
x = x - (total_width - width) / 2

# other choices: "#377D22", '#5A6A37', "#F0855B", "#75140C"
edgecolors =  ["#689FBF", "#999999"]

# /, \, |, -, +, x, o, O, ., *
plt.bar(x, a,  width=width-0.04, color='white', label='a', edgecolor=edgecolors[0],hatch='\\\\') 
plt.bar(x + width, b, width=width-0.04, color='white', label='b', edgecolor=edgecolors[0], hatch="////")
plt.bar(x + 2 * width, c, width=width-0.04, color='white', label='c', edgecolor=edgecolors[1], hatch="---")
plt.bar(x + 3 * width, d, width=width-0.04, color='white', label='d', edgecolor=edgecolors[1], hatch="XXX")


# plt.xticks(range(len(data_set)), data_set, fontsize=9, rotation=45)
plt.xticks(range(len(data_set)), data_set)

plt.xlabel('Dataset Network', fontsize=14)
plt.ylabel('F1-score', fontsize=14)

plt.legend(ncol=2)
plt.show()

plt.savefig("bar.png", dpi=600, bbox_inches='tight')
plt.savefig("bar.pdf", dpi=600, bbox_inches='tight')