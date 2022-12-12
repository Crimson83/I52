import tkinter as tk
import random
import time
def gencarte():
    """
    generation aléatoire carte avec environ 20% de mur
    """
    cart=[]
    #id=tk.Canvas(root,width=1080,height=720,bg='white')
    for x in range(30):
        cart.append([])
        for y in range(20):
            rand=random.randrange(5)
            if(rand!=1):
                cart[x].append(0)
            else:
                cart[x].append(1)
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
                can.create_rectangle(k,y,k+10,y+10,fill='white',tags='SOL')
            y+=10
        k+=10

def movebot(event=None):
    """
    déplacement aléatoire du Robot
    """
    x,y=can.coords(id)[0],can.coords(id)[1]
    rand=random.randrange(4)
    x=int(x//10)
    y=int(y//10)
    #print(x,y)
    x1=0
    y1=0
    list=['H','B','G','D']
    #print(list[rand])
    #print("Position x:",x,"y:",y)
    if(list[rand]=='H' and y>1):
        if(presMur(x,y-1)):
            y1=-10
            #print(y1)
    elif(list[rand]=='D' and x<=29):
        if(presMur(x+1,y)):
            x1=10
            #print(x1)
    elif(list[rand]=='B' and y<=19):
        if(presMur(x,y+1)):
            y1=10
            #print(y1)
    elif(list[rand]=='G' and x>1):
        if(presMur(x-1,y)):
            x1=-10
            #print(x1)
    can.move(id,x1,y1)
    #print("on bouge x:",x1," y:",y1)
    #can.after(100,movebot) récursif déplacement enchainé pour tests

def presMur(x,y):
    """
    il y a t-il un mur au coordonnées passées en paramètres
    """
    global carte
    return not(carte[x-1][y-1])

def placebot(NumJ):
    """
    Placement aléatoire d'un robot sur la carte
    (on le place random)
    """
    global carte
    global PlayerList
    x=random.randrange(30)
    y=random.randrange(20)
    place=False
    while(place==False):
        if(carte[x][y]==0):
            id=can.create_rectangle(x*10+10,y*10+10,x*10+20,y*10+20,fill=ListCoul[NumJ],tags=(NumJ,"Joueur"))
            PlayerList[NumJ]=[x,y,id]
            place=True
        else:
            x=random.randrange(30)
            y=random.randrange(20)



global carte
global PlayerList
global ListCoul
ListCoul=["red","cyan","light green","gold"]
PlayerList={}
carte=gencarte()
root=tk.Tk()
root.title("La Guerre Des Robots")
can=tk.Canvas(root,width=1080,height=720,bg='white')
can.pack()
create_can_carte(carte)
#id=can.create_rectangle(10,10,20,20,fill='red',tags=("Joueur1","Joueur"))
#can.after(1,movebot)
for i in range(4):
    placebot(i)
    print(PlayerList[i][:2],PlayerList[i][2])


root.mainloop()
