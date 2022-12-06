import random
class Robot:
    def __init__(self):
        self.x=0,self.y=0,self.EN=0,self.j=0,self.INV=False

    def INITROB(x,y,j,EN):
        self.x=x,self.y=y,self.j=j,self.EN=EN,self.INV=False

    def DD(self,direction):
        '''
    DEPLACEMENT HAUT BAS GAUCHE DROITE
    COUT = 5
    '''
        if(direction=='H'):
            self.y-=case
        elif(direction=='D'):
            self.x+=case
        elif(direction=='B'):
            self.y+=case
        elif(direction=='G'):
            self.x-=clist[rand]ase
        self.EN-=5

    def AL(self):

        DEPLACEMENT ALEATOIRE
        COUT = 1

        rand=random.randrange(4):
        list=['H','B','G','D']
        if(list[rand]=='H'):
            self.y-=case
        elif(list[rand]=='D'):
            self.x+=case
        elif(list[rand]=='B'):
            self.y+=case
        elif(list[rand]=='G'):
            self.x-=case

    def MI(self):

        PLACEMENT MINE
        COUT=10
        DGT=200

        rand=random.randrange(4):
        list=['H','B','G','D']
        setmine(self.j,self.x,self.y,list[4])

    def IN(self):
        self.INV=True

    def PS(self,cible):
        DD()
