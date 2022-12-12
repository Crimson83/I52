import tkinter as tk
import random
import time
def gencarte():
    cart=[]
    #id=tk.Canvas(root,width=1080,height=720,bg='white')
    for i in range(30):
        cart.append([])
        for j in range(20):
            rand=random.randrange(5)
            if(rand!=1):
                cart[i].append(0)
            else:
                cart[i].append(1)
    return cart#id

def create_can_carte(carte):
    """
    Creation carte version rectangle sur Canvas
    """
    k=10
    for i in range(len(carte)):
        y=10
        for j in range(len(carte[i])):
            if(carte[i][j]):
                can.create_rectangle(k,y,k+10,y+10,fill='black',tags='MUR')
            else:
                can.create_rectangle(k,y,k+10,y+10,fill='white',tags='LAND')
            y+=10
        k+=10

def presMur(x,y):
    global carte
    return carte[y][x]

def movebot(event=None):
    """
    déplacement aléatoire du Robot
    """
    global id
    x,y=can.coords(id)[0],can.coords(id)[1]
    rand=random.randrange(1)
    x1=0
    y1=0
    list=['D','H','B','G']
    if(list[rand]=='H' and y>10):
        y1=-10
    elif(list[rand]=='D' and x<=290):
        x1=10
    elif(list[rand]=='B' and y<=190):
        y1=10
    elif(list[rand]=='G' and x>10):
        x1=-10
    can.move(id,x1,y1)
    can.after(100,movebot)

carte=gencarte()
print(carte)
root=tk.Tk()
root.title("La Guerre Des Robots")
can=tk.Canvas(root,width=1080,height=720,bg='white')
can.pack()
create_can_carte(carte)
global id
id=can.create_rectangle(10,10,20,20,fill='red',tags=("Joueur1","Joueur"))
can.after(100,movebot)
root.mainloop()