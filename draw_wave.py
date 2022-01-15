# _*_ coding: utf-8 _*_
# @File        : draw_wave.py
# @Time        : 2022/1/15 11:19
# @Author      : SaleJuice
# @E-Mail      : linxzh@shanghaitech.edu.cn
# @Institution : LIMA Lab, ShanghaiTech University, China
# @SoftWare    : PyCharm

import matplotlib.pyplot as plt


if __name__ == '__main__':
    while True:
        x = []
        y = []
        index = 0
        while True:
            x.append(index)  # 添加i到x轴的数据中
            y.append(uesr_data)  # 添加i的平方到y轴的数据中
            plt.clf()  # 清除之前画的图
            plt.plot(x, y)  # 画出当前x列表和y列表中的值的图形
            plt.pause(0.001)  # 暂停一段时间，不然画的太快会卡住显示不出来
            plt.ioff()  # 关闭画图窗口s
            index += 1
            break
