import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors
import os

def data_integrate():
    path = 'D:/test_edition/数据处理/data/pref(e-19_e-17_e-19)___P0(0.5_3_0.5)___La(0.005_0.02_0.005).txt'
    indexx = [i for i in range(0, 301, 3)]
    columnn = np.arange(0, 40.1, 0.5333333333334462)
    stock = []
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
        count = 0
        final = []
        for line in lines[8:]:
            value = line.split()
            if eval(value[0]) == 0:
                singleday = [round(eval(value[1]), 3)]
            else:
                singleday.append(round(eval(value[1]), 3))
            if len(singleday)==76:
                stock.append(singleday)
            count += 1
            if len(stock)==101:
                final.append(stock)
                stock = []
    return final
def data_predict(txt):  # 将txt文件转为csv文件,（弃用）
    l = []
    with open(txt) as f:
        p = f.readlines()
        for pp in p:
            l.append(pp)
    def func(x):
        return [float(i) for i in x.split()]
    lp = list(map(func, l))
    pd.DataFrame(lp).to_excel(txt+'.xlsx')
    pass
def draw():     # 将训练结果与预测结果作图显示
    
    norm = colors.Normalize(vmin=0,vmax=1.1) 
    data15 = pd.read_excel('./data/e-16.xlsx', index_col=0)
    data16 = pd.read_excel('./data/e-17.xlsx', index_col=0)
    data17 = pd.read_excel('./data/e-18.xlsx', index_col=0)
    data18 = pd.read_excel('./data/e-19.xlsx', index_col=0)
    data516 = pd.read_excel('./data/save0.txt.xlsx', index_col=0)
    data517 = pd.read_excel('./data/save1.txt.xlsx', index_col=0)
    data518 = pd.read_excel('./data/save2.txt.xlsx', index_col=0)
    data519 = pd.read_excel('./data/save3.txt.xlsx', index_col=0)
    data = [data15, data16, data17, data18, data516, data517, data518, data519]
    fig, ax = plt.subplots(2, 4)
    ax = ax.flatten()
    for i in range(8):
        ax[i].contourf(data[i], norm=norm)
    im = ax[3].contourf(data[3], norm=norm)
    ax[0].title.set_text('e-16')
    ax[1].title.set_text('e-17')
    ax[2].title.set_text('e-18')
    ax[3].title.set_text('e-19')
    ax[4].title.set_text('5e-16')
    ax[5].title.set_text('5e-17')
    ax[6].title.set_text('5e-18')
    ax[7].title.set_text('5e-19')    
    # plt.colorbar()
    fig.colorbar(im, ax=[ax[i] for i in range(8)], fraction=0.02, pad=0.05)
    plt.savefig('瓦斯压力下降预测图.png')
    plt.show()

a = np.array(data_integrate())
with open('./data/e16_e19/pref(e-19_e-17_e-19)___P0(0.5_3_0.5)___La(0.005_0.02_0.005).txt', 'w') as outfile:
    for i in a:
        np.savetxt(outfile, i, fmt='%f', delimiter=',')
        
# ？各个数量级之间的样本数不同
# draw()
pass