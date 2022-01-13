#
# author: SaleJuice
# lab: lima lab
#
import matplotlib.pyplot as plt

# 1: export figure as pdf files
# 0: not
exportFlag = 0

# variables of figure
# var1
var1=[40.36,43.45,43.91,45.6,46.84,47.01,47.58,48.53,49.52,49.28,50.62,51.17,52.04,52.83,52.2,53.25,54.06,54.75,55.59,56.43,57.37,58.3,59.02]
var1Color = "green"
var1Label = "Load bearing (kg)"
# var2
var2=[28.34,26.05,25.98,25.8,25.4,25.37,24.81,24.68,24.25,24.09,23.75,23.49,23.11,22.75,22.53,22.6,22.23,21.91,21.53,21.15,20.73,20.27,20]
var2Color = "orange"
var2Label = "Length (mm)"
# var3
var3=[6.322,2.881,2.926,2.764,2.829,3.159,2.804,3.238,3.229,3.547,3.165,2.854,3.043,2.864,2.876,2.485,2.496,2.259,2.377,2.258,2.363,2.314,2]
var3Color = "grey"
var3Label = "Thickness (mm)"
# var4
var4=[4.001,4.554,4,4.467,4.112,4.026,4,4.182,4,4,4.155,4,4,4,4,4.328,4,4,4,4,4,4,4]
var4Color = "brown"
var4Label = "Width (mm)"

# legend of figure
# location
legLocation = "upper left"
# size
legSize = 11

# x,y labels of figure
xLabel = "Iteration"
yLabel = "Mechanical parameters"

# check length of input variables
assert len(var1) == len(var2)
assert len(var1) == len(var3)
assert len(var1) == len(var4)

# process
fig, ax = plt.subplots(figsize=(6, 3.5))
plt.subplots_adjust(bottom=0.15)
ax.plot(var1, color = var1Color, label = var1Label)
ax.plot(var2, color = var2Color, label = var2Label)
ax.plot(var3, color = var3Color, label = var3Label)
ax.plot(var4, color = var4Color, label = var4Label)
ax.legend(loc = legLocation, prop={'size': legSize})
plt.xlabel(xLabel, fontsize=15)
plt.ylabel(yLabel, fontsize=15)
plt.grid()
plt.show()
if exportFlag == 1:
    fig.savefig("boo.pdf")