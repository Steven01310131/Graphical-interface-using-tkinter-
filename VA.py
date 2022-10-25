#Tsabanakis Stefanos VA
#Tom 
from os import lstat
from re import S
import tkinter as tk
import random
import time
import numpy as np


from scipy.linalg import norm
global lst
lst=[]
SIZE = 600
def clear():
    canvas.delete("all")
    hole=canvas.create_oval(-50,250 ,50,350, fill="black")
    hole=canvas.create_oval(650,250 ,550,350, fill="black")
    lst.clear()
def speed():
    for i in lst:
        i.speed_(float(entry2.get()))
        
def add_balls():
    num=int(entry1.get())
    for i in range(num):
        ball = balls(canvas ,random.randint(100,400),random.randint(100,400),random.randint(-10,10),random.randint(-10,10))
        lst.append(ball)
        ball.move_ball()
        ball.bounce()
        
        ball.deleting()
        ball.bouncebetween()
        



def add_ball():
    ball = balls(canvas ,random.randint(20,580),random.randint(20,580),random.randint(-10,10),random.randint(-10,10))
    lst.append(ball)
    ball.move_ball()
    ball.bounce()
    
    ball.bouncebetween()
    ball.deleting()
    
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

    def vspeed(self):
        x=self.vx
        y=self.vy
        return x,y 
    def change(self,x,y):
        self.vx=x
        self.vy=y

    def move_ball(self):
        self.canvas.move(self.ball, self.vx,self.vy)
        self.canvas.after(30, self.move_ball)
    def bouncebetween(self):

        for i in range(0,len(lst)):
            if self.ball != lst[i]:
                A=[canvas.coords(self.ball)[0]-canvas.coords(lst[i].ball)[0],canvas.coords(self.ball)[1]-canvas.coords(lst[i].ball)[1]]
                if ((A[0])**2+(A[1])**2)**0.5<=2*R:

                    self.vx,self.vy,lst[i].vx,lst[i].vy=lst[i].vx,lst[i].vy,self.vx,self.vy
        self.canvas.after(30,self.bouncebetween)


    def bounce(self):# If the position canvas.coords(self.ball)[0] happens to be in the area <=5 
                    #and not approaching we will a obseve the balls sticking to the wall becauce it will 
                    # constantly be in that area so the speed will fluctuate between + and -
                    # same problem will occur in the collision of the balls were we will observe them stick to eachother

        if canvas.coords(self.ball)[0]<=5 or canvas.coords(self.ball)[2]>=SIZE-5:
            self.vx=-self.vx
        if canvas.coords(self.ball)[1]<=5 or canvas.coords(self.ball)[3]>=SIZE-5:
            self.vy=-self.vy
        self.canvas.after(30,self.bounce)

    def deleting(self):
        if canvas.coords(self.ball)[0]<=50 and canvas.coords(self.ball)[1]>=250 and canvas.coords(self.ball)[3]<=350:
            canvas.delete(self.ball)
            lst.remove(self)
        if canvas.coords(self.ball)[2]>=550 and canvas.coords(self.ball)[1]>=250 and canvas.coords(self.ball)[3]<=350:
            canvas.delete(self.ball)
            lst.remove(self)
        canvas.after(30,self.deleting)
    def speed_(self,s):
        self.vx=self.vx*s
        self.vy=self.vy*s
        self.canvas.after(30, self.speed_)
            
            
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
btn_slow=tk.Button(master=frame2,text="speed x ",command=speed)
exit_button = tk.Button(master=frame2, text="Exit", command=window.destroy)



number_objects=tk.Label(text="Enter number of objects")
number_objects.pack()
entry1=tk.Entry()
entry1.insert(0,"10")
entry1.pack()
simullationspeed=tk.Label(text="Enter a value to speed up or slowdown")
simullationspeed.pack()
entry2=tk.Entry()
entry2.insert(0,"1")
entry2.pack()



btn.grid( sticky="nsew")
btn_reset.grid( sticky="nsew")
btn_anotherball.grid( sticky="nsew")
btn_slow.grid(sticky="nsew")
exit_button.grid(sticky="nsew")

window.mainloop()
