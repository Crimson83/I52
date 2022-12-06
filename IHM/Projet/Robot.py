import random
class Robot:
    def __init__(self):
        self._x=0,self._y=0,self._EN=0,self._j=0,self._INV=False

    def INITROB(x,y,j,EN):
        self._x=x,self._y=y,self._j=j,self._EN=EN,self._INV=False

    def DD(self,direction):
        '''
    DEPLACEMENT HAUT BAS GAUCHE DROITE
    COUT = 5
    '''
        if(direction=='H'):
            self._y-=case
        elif(direction=='D'):
            self._x+=case
        elif(direction=='B'):
            self._y+=case
        elif(direction=='G'):
            self._x-=clist[rand]ase
        self._EN-=5

    def movebot(event=None,carte):
        """
        déplacement aléatoire du Robot
        """
        global id
        x,y=can.coords(iidd)[0],can.coords(id)[1] #recup coord
        rand=random.randrange(4)                #haut bas gauche droite
        x1=0
        y1=0
        list=['H','B','G','D']
        if(list[rand]=='H' and y>10): #verif si on est pas au bord de la carte
            if(cart[(y/10)-1][x]!=1): #verif mur au dessus
                y1=-10
        elif(list[rand]=='D' and x<290):
            if(cart[y][(x/10)+1]!=1):
                x1=10
        elif(list[rand]=='B' and y<190):
            if(cart[(y/10)+1][x]!=1):
                y1=10
        elif(list[rand]=='G' and x>10):
            if(cart[y][(x/10)-1]!=1):
                x1=-10
        can.move(id,x1,y1))
        can.after(1000,movebot)

    def MI(self):

        PLACEMENT MINE
        COUT=10
        DGT=200

        rand=random.randrange(4):
        list=['H','B','G','D']
        setmine(self._j,self._x,self._y,list[4])

    def IN(self):
        self._INV=True

    def PS(self,cible):

        DD()

    @property
    def x(self):
        return self_x
    @property
    def y(self)
        return self_y
