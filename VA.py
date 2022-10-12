from curses import color_content
import tkinter as tk
import random

# Create a window object
# window = tk.Tk()
# window.columnconfigure([0,1,2,3,4,5,6,7,8], minsize=50, weight=1)
# window.rowconfigure(0,minsize=50,weight=1)
# WIDTH = 800
# HEIGHT = 500
# SIZE = 50
def add_balls():
    ball = balls(canvas ,20,random.randint(0,500),random.randint(0,500))
class balls():
    def __init__(self, canvas,R,x1,y1):
        self.R=R
        self.x1 = x1
        self.y1=y1
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1-self.R, self.y1-self.R,self.x1+self.R,self.y1+self.R, fill="red")
    
# initialize root Window and canvas
window= tk.Tk()
window.title("Ball")
frame1=tk.Frame(master=window,height=500,width=500)
frame1.pack()
frame2=tk.Frame(master=window,height=100,width=100)
frame2.pack()

canvas = tk.Canvas(master=frame1, width = 500, height = 500)
canvas.pack()

# create two ball objects and animate them

btn=tk.Button(master=frame2,text="add more balls",command=add_balls)
btn.grid( sticky="nsew")



# def dice():
#     result["text"]=random.randint(1,6)



# # btn_dice = tk.Button(master=window, text="Roll", command=dice)
# # result=tk.Label()
# # result.grid(row=1, column=0)




window.mainloop()
