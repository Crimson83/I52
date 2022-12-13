import random
def gencarte():
    """
    generation aléatoire carte avec environ 20% de mur
    """
    carte=[]
    for x in range(30):
        carte.append([])
        for y in range(20):
            rand=random.randrange(10)
            if(rand!=1):
                carte[x].append(0)
            else:
                carte[x].append(1)
    return carte

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
                print(x-n,y)
                return
            elif(presMur(x,y-n,carte)):
                print(x,y-n)
                return
            elif(presMur(x+n,y,carte)):
                print(x+n,y)
                return
            elif(presMur(x,y+n,carte)):
                print(x,y+n)
                return
            elif(presMur(x-n,y-n,carte)):
                print(x-n,y-n)
                return
            elif(presMur(x+n,y+n,carte)):
                print(xnbr+n,y+n)
                return
            elif(presMur(x+n,y-n,carte)):
                print(x+n,y-n)
                return
            elif(presMur(x-n,y+n,carte)):
                print(x-n,y+n)
                return
            n+=1
    if(n>=30):
        print('Crash')
    else:
        print(x,y)

def place_joueur(nbrJ,carte):
    """
    place les joueurs sur la carte
    le paterne de placement diffère selon le nombre de joueurs
    """
    x1,y1=5,10
    set_sur_carte(x1,y1,carte)
    if(nbrJ==2):
        x2,y2=25,10
        set_sur_carte(x2,y2,carte)
    elif(nbrJ==3):
        x2,y2=25,15
        x3,y3=25,5
        set_sur_carte(x2,y2,carte)
        set_sur_carte(x3,y3,carte)
    elif(nbrJ==4):
        x2,y2=25,10
        x3,y3=15,5
        x4,y4=15,15
        set_sur_carte(x2,y2,carte)
        set_sur_carte(x3,y3,carte)
        set_sur_carte(x4,y4,carte)
    elif(nbrJ==5):
        x2,y2=12,5
        x3,y3=20,7
        x4,y4=20,23
        x5,y5=12,15
        set_sur_carte(x2,y2,carte)
        set_sur_carte(x3,y3,carte)
        set_sur_carte(x4,y4,carte)
        set_sur_carte(x5,y5,carte)
    elif(nbrJ==6):
        x2,y2=12,5
        x3,y3=18,5
        x4,y4=25,10
        x5,y5=18,15
        x6,y6=12,15
        set_sur_carte(x2,y2,carte)
        set_sur_carte(x3,y3,carte)
        set_sur_carte(x4,y4,carte)
        set_sur_carte(x5,y5,carte)
        set_sur_carte(x6,y6,carte)
    else:
        print("Nombre en paramètres supérieur à 6 ou inférieur à 2")

def presMur(x,y,carte):
    """
    il y a t-il un mur au coordonnées passées en paramètres
    """
    if(x<0 or x>=30 or y<0 or y>=20):
        return 0
    else:
        return not(carte[x][y])

carte=gencarte()
i=2
while(i<7):
    print("il y a :",i," joueurs")
    place_joueur(i,carte)
    i+=1
