
from os import lstat
import tkinter as tk
import random
import time
import numpy as np
global lst
lst=[]
# Create a window object
# window = tk.Tk()
# window.columnconfigure([0,1,2,3,4,5,6,7,8], minsize=50, weight=1)
# window.rowconfigure(0,minsize=50,weight=1)
# WIDTH = 800
# HEIGHT = 500
SIZE = 600
def clear():
    canvas.delete("all")
    hole=canvas.create_oval(-50,250 ,50,350, fill="black")
    hole=canvas.create_oval(650,250 ,550,350, fill="black")
def add_balls():
    num=int(entry.get())
    for i in range(num):
        ball = balls(canvas ,random.randint(100,400),random.randint(100,400),random.randint(-10,10),random.randint(-10,10))
        lst.append(ball)
        ball.move_ball()
        ball.bounce()
        # ball.bouncebetween(lst)
        ball.deleting()

def add_ball():
    ball = balls(canvas ,random.randint(20,580),random.randint(20,580),random.randint(-10,10),random.randint(-10,10))
    ball.move_ball()
    ball.bounce()
    ball.deleting()
    lst.append(ball)
class balls():
    color = ["red", "orange", "yellow", "green", "blue", "violet"]
    def __init__(self, canvas,x1,y1,vx,vy):
        global R
        R=10
        self.vx=vx
        self.vy=vy
        self.x1 = x1
        self.y1=y1
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1-R, self.y1-R,self.x1+R,self.y1+R, fill=random.choice(self.color))

    def __str__(self):
        return self.ball

    def move_ball(self):
        self.canvas.move(self.ball, self.vx,self.vy)
        self.canvas.after(30, self.move_ball)
    def bouncebetween(self,other):
        for i in lst:
            A=[(canvas.coords(self.ball)[0]-canvas.coords(other.ball)[0]),
            (canvas.coords(self.ball)[1]-canvas.coords(other.ball)[1])]
            if ((A[0])**2+(A[1])**2)**0.5<=2*R:
                self.vx,self.vy,other.vx,other.vy=other.vx,other.vy,self.vx,self.vy
    def bounce(self):

        if canvas.coords(self.ball)[0]<=0 or canvas.coords(self.ball)[2]>=SIZE:
            self.vx=-self.vx
        if canvas.coords(self.ball)[1]<=0 or canvas.coords(self.ball)[3]>=SIZE:
            self.vy=-self.vy
        self.canvas.after(30,self.bounce)

    def deleting(self):
        if canvas.coords(self.ball)[0]<=50 and canvas.coords(self.ball)[1]>=250 and canvas.coords(self.ball)[3]<=350:
            canvas.delete(self.ball)
        if canvas.coords(self.ball)[2]>=550 and canvas.coords(self.ball)[1]>=250 and canvas.coords(self.ball)[3]<=350:
            canvas.delete(self.ball)
        canvas.after(30,self.deleting)
            
            
# initialize root Window and canvas
window= tk.Tk()
window.title("Ball")
frame1=tk.Frame(master=window,height=SIZE,width=SIZE)
frame1.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
frame2=tk.Frame(master=window,height=100,width=100)
frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

canvas = tk.Canvas(master=frame1, width = SIZE, height = SIZE)
canvas.pack()
global hole
hole=canvas.create_oval(-50,250 ,50,350, fill="black")
hole=canvas.create_oval(650,250 ,550,350, fill="black")


btn=tk.Button(master=frame2,text="Initialize",command=add_balls)
btn_reset=tk.Button(master=frame2,text="reset",command=clear)
btn_anotherball=tk.Button(master=frame2,text="add more balls",command=add_ball)
number_objects=tk.Label(text="Enter number of objects")
entry=tk.Entry()
entry.insert(0,"10")
number_objects.pack()
entry.pack()


btn.grid( sticky="nsew")
btn_reset.grid( sticky="nsew")
btn_anotherball.grid( sticky="nsew")
for ball in lst:
    if canvas.coords(ball)[0]<=0 and canvas.coords(ball)[3]<=400 and canvas.coords(ball)[1]>=0:
        canvas.delete(ball) 

window.mainloop()
