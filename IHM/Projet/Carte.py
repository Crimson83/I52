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

def set_sur_carte(x,y,carte):
    """
    essaie de placer le robot sur une case
    sinon regarde cases adjacentes
    """
    n=1
    if(not(presMur(x,y,carte))):
        while(n<30):
            #print(n)
            if(presMur((x-n),y,carte)):
                return x-n,y
            elif(presMur(x,y-n,carte)):
                return x,y-n
            elif(presMur(x+n,y,carte)):
                return x+n,y
            elif(presMur(x,y+n,carte)):
                return x,y+n
            elif(presMur(x-n,y-n,carte)):
                return(x-n,y-n)
            elif(presMur(x+n,y+n,carte)):
                return(x+n,y+n)
            elif(presMur(x+n,y-n,carte)):
                return(x+n,y-n)
            elif(presMur(x-n,y+n,carte)):
                return(x-n,y+n)
            n+=1
    if(n>=30):
        return
    else:
        return x,y

def place_joueur(nbrJ,carte,PlayerList):
    """
    place les joueurs sur la carte
    le paterne de placement diffère selon le nombre de joueurs
    """
    x1,y1=2,10
    x1,y1=(set_sur_carte(x1,y1,carte))
    PlayerList[0]=can.create_rectangle(x1*10,y1*10,x1*10+10,y1*10+10,fill='cyan',tags=('Joueur1','Joueur'))
    if(nbrJ==2):
        x2,y2=28,10
        x2,y2=(set_sur_carte(x2,y2,carte))
        PlayerList[1]=can.create_rectangle(x2*10,y2*10,x2*10+10,y2*10+10,fill='red',tags=('Joueur2','Joueur'))
    elif(nbrJ==3):
        x2,y2=28,18
        x3,y3=28,5
        x2,y2=(set_sur_carte(x2,y2,carte))
        x3,y3=(set_sur_carte(x3,y3,carte))
        PlayerList[1]=can.create_rectangle(x2*10,y2*10,x2*10+10,y2*10+10,fill='red',tags=('Joueur2','Joueur'))
        PlayerList[2]=can.create_rectangle(x3*10,y3*10,x3*10+10,y3*10+10,fill='light green',tags=('Joueur3','Joueur'))
    elif(nbrJ==4):
        x2,y2=28,10
        x3,y3=15,5
        x4,y4=15,18
        x2,y2=(set_sur_carte(x2,y2,carte))
        x3,y3=(set_sur_carte(x3,y3,carte))
        x4,y4=(set_sur_carte(x4,y4,carte))
        PlayerList[1]=can.create_rectangle(x2*10,y2*10,x2*10+10,y2*10+10,fill='red',tags=('Joueur2','Joueur'))
        PlayerList[2]=can.create_rectangle(x3*10,y3*10,x3*10+10,y3*10+10,fill='light green',tags=('Joueur3','Joueur'))
        PlayerList[3]=can.create_rectangle(x4*10,y4*10,x4*10+10,y4*10+10,fill='gold',tags=('Joueur4','Joueur'))
    elif(nbrJ==5):
        x2,y2=12,5
        x3,y3=20,7
        x4,y4=20,23
        x5,y5=12,15
        x2,y2=(set_sur_carte(x2,y2,carte))
        x3,y3=(set_sur_carte(x3,y3,carte))
        x4,y4=(set_sur_carte(x4,y4,carte))
        x5,y5=(set_sur_carte(x5,y5,carte))
        PlayerList[1]=can.create_rectangle(x2*10,y2*10,x2*10+10,y2*10+10,fill='red',tags=('Joueur2','Joueur'))
        PlayerList[2]=can.create_rectangle(x3*10,y3*10,x3*10+10,y3*10+10,fill='light green',tags=('Joueur3','Joueur'))
        PlayerList[3]=can.create_rectangle(x4*10,y4*10,x4*10+10,y4*10+10,fill='gold',tags=('Joueur4','Joueur'))
        PlayerList[4]=can.create_rectangle(x5*10,y5*10,x5*10+10,y5*10+10,fill='purple',tags=('Joueur5','Joueur'))
    elif(nbrJ==6):
        x2,y2=12,2
        x3,y3=18,2
        x4,y4=28,10
        x5,y5=18,18
        x6,y6=12,18
        x2,y2=(set_sur_carte(x2,y2,carte))
        x3,y3=(set_sur_carte(x3,y3,carte))
        x4,y4=(set_sur_carte(x4,y4,carte))
        x5,y5=(set_sur_carte(x5,y5,carte))
        x6,y6=(set_sur_carte(x6,y6,carte))
        PlayerList[1]=can.create_rectangle(x2*10,y2*10,x2*10+10,y2*10+10,fill='red',tags=('Joueur2','Joueur'))
        PlayerList[2]=can.create_rectangle(x3*10,y3*10,x3*10+10,y3*10+10,fill='light green',tags=('Joueur3','Joueur'))
        PlayerList[3]=can.create_rectangle(x4*10,y4*10,x4*10+10,y4*10+10,fill='gold',tags=('Joueur4','Joueur'))
        PlayerList[4]=can.create_rectangle(x5*10,y5*10,x5*10+10,y5*10+10,fill='purple',tags=('Joueur5','Joueur'))
        PlayerList[5]=can.create_rectangle(x6*10,y6*10,x6*10+10,y6*10+10,fill='brown',tags=('Joueur6','Joueur'))
    else:
        print("Nombre en paramètres supérieur à 6 ou inférieur à 2")

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
    x=int(x//10)-1
    y=int(y//10)-1
    #print(x,y)
    x1=0
    y1=0
    list=['H','B','G','D']
    #print(list[rand])
    #print("Position x:",x,"y:",y)
    if(list[rand]=='H'):
        if(presMur(x,y-1)):
            y1=-10
            #print(y1)
    elif(list[rand]=='D'):
        if(presMur(x+1,y)):
            x1=10
            #print(x1)
    elif(list[rand]=='B'):
        if(presMur(x,y+1)):
            y1=10
            #print(y1)
    elif(list[rand]=='G'):
        if(presMur(x-1,y)):
            x1=-10
            #print(x1)
    can.move(id,x1,y1)
    #print("on bouge x:",x1," y:",y1)
    #can.after(100,movebot) récursif déplacement enchainé pour tests

def presMur(x,y,carte):
        """
        il y a t-il un mur au coordonnées passées en paramètres
        """
        if(x<0 or x>=30 or y<0 or y>=20):
            return 0
        return not(carte[x][y])

ListCoul=["red","cyan","light green","gold"]
PlayerList=[0]*6
carte=gencarte()
root=tk.Tk()
root.title("La Guerre Des Robots")
can=tk.Canvas(root,width=1080,height=720,bg='white')
can.pack()
create_can_carte(carte)
#id=can.create_rectangle(10,10,20,20,fill='red',tags=("Joueur1","Joueur"))
#can.after(1,movebot)
i=int(input("Combien de joueurs voulez-vous ?: "))
print("il y a :",i," joueurs")
place_joueur(i,carte,PlayerList)

root.mainloop()
