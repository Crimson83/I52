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
