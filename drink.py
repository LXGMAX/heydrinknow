import time
from tkinter import messagebox


number_map = ('十二','一','二','三','四','五','六','七','八','九','十','十一')

time_num = time.localtime().tm_hour % 12

messagebox.showinfo("喂！", "喂 ！" + number_map[time_num] + "点几嚟！饮下水先！")
