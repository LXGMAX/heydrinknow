import time
from tkinter import messagebox


numberCN = ('十二','一','二','三','四','五','六','七','八','九','十','十一')

timeNum = time.localtime().tm_hour
if timeNum > 11:
	timeNum -= 12

timeStr = str(numberCN[timeNum])
messagebox.showinfo("喂！", "喂 ！" + timeStr + "点几嚟！饮下水先！")
