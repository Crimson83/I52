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
