# Tkinter基础 Button bg 设置按钮的背景颜色
import tkinter as tk
from tkinter import Button
class App():
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.testButton = tk.Button(frame, text = "hello", fg = "red", bg = "blue", command = self.testPrint)
        self.testButton.pack()

    def testPrint(self):
        print("test")



root = tk.Tk()
app = App(root)
root.mainloop()