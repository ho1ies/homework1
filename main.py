# -*- encoding:utf-8 -*-
from tkinter import *
Str = ('~','|','&','↺','1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '.', '0', '/', '=')

class Calculator:
     def __init__(self, master):
         self.master = master
         self.Interface()

#程序事件处理
     def ButtonClick(self,var):
         # 获取文本框中的内容
         textcontent = self.content.get()
         # 判断点击消息，将textcontent设置为要计算的式子，并在文本框显示
         if var.widget['text'] in '0123456789.+-*/&|~':
             textcontent += var.widget['text']
             self.content.set(textcontent)
         # 使用eval计算textcontent，并在文本框显示
         elif var.widget['text'] == '=':
             self.content.set(eval(textcontent))
         # 清除文本框的内容
         elif var.widget['text'] == '↺':
             textcontent = ''
             self.content.set(textcontent)

# 程序界面接口
     def Interface(self):
         # 设置文本框显示的字符串
         self.content = StringVar(self.master, '')
         # 创建Entry组件
         self.module = Entry(relief=SUNKEN, font=('Arial',25), width=26,textvariable=self.content)
         self.module.pack(side=TOP, pady=10)
         # Grad布局
         fra = Frame(self.master)
         fra.pack(side=TOP)
         # 创建Button组件
         for i in range(len(Str)):
             botton = Button(fra,text=Str[i], font=('Arial',25),width=6)
             botton.grid(row=i//4,column=i%4)
             botton.bind('<Button-1>',self.ButtonClick)

if __name__ == '__main__':
     root = Tk()
     root.title('计算器')
     Calculator(root)
     root.mainloop()