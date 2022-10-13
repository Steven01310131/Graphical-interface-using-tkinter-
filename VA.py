
import tkinter as tk
import random
import time


# Create a window object
# window = tk.Tk()
# window.columnconfigure([0,1,2,3,4,5,6,7,8], minsize=50, weight=1)
# window.rowconfigure(0,minsize=50,weight=1)
# WIDTH = 800
# HEIGHT = 500
# SIZE = 50
def add_balls():
    num=int(entry.get())
    for i in range(num):
        ball = balls(canvas ,random.randint(5,20),random.randint(0,980),random.randint(0,980),random.randint(-10,10),random.randint(-10,10))
        ball.move_ball()
        ball.bounce()
        
class balls():
    color = ["red", "orange", "yellow", "green", "blue", "violet"]
    def __init__(self, canvas,R,x1,y1,vx,vy):
        self.R=R
        self.vx=vx
        self.vy=vy
        self.x1 = x1
        self.y1=y1
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1-self.R, self.y1-self.R,self.x1+self.R,self.y1+self.R, fill=random.choice(self.color))

    def move_ball(self):
        self.canvas.move(self.ball, self.vx,self.vy)
        self.canvas.after(10, self.move_ball)

    def bounce(self):            
        if canvas.coords(self.ball)[0]<=0 or canvas.coords(self.ball)[2]>=1000:
            self.vx=-self.vx
        if canvas.coords(self.ball)[1]<=0 or canvas.coords(self.ball)[3]>=1000:
            self.vy=-self.vy
        self.canvas.after(10,self.bounce)

# initialize root Window and canvas
window= tk.Tk()
window.title("Ball")
frame1=tk.Frame(master=window,height=2000,width=2000)
frame1.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)
frame2=tk.Frame(master=window,height=100,width=100)
frame2.pack(fill=tk.BOTH,side=tk.LEFT,expand=True)

canvas = tk.Canvas(master=frame1, width = 1000, height = 1000)
canvas.pack()

# create two ball objects and animate them

btn=tk.Button(master=frame2,text="add more balls",command=add_balls)
btn_reset=tk.Button(master=frame2,text="reset",command=lambda:canvas.destroy())
number_objects=tk.Label(text="Enter number of objects")
entry=tk.Entry()
entry.insert(0,"100")
number_objects.pack()
entry.pack()


btn.grid( sticky="nsew")
btn_reset.grid( sticky="nsew")

window.mainloop()
