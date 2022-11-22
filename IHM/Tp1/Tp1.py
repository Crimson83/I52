import re
def gestfich(chemin,option):
    try:
        file=open(chemin,option); #ouverture fichier
        if(file==None): #pas de fichier
            print(errno) #affiche l'erreur
            os.strerror(errno)
        else:
            print(file.read())
            file.close()
    except FileNotFoundError: #fichier non trouvé
        print("Fichier non Trouvé")
        exit()
    except PermissionError: #pas permisssion
        print("Pas les droits {} sur le fichier".format(option))
        exit()

def parser(nom,option):
    Dico={} #Creation du dico
    with(open(nom,option))as file: #ouverture du fichier dans file
        lignes=file.readlines() #lecture des lignes
        for i in range(1,len(lignes)): #on prend la ligne i
            tmp=re.split('\t|\n',lignes[i]) #on sépare la ligne en mot
            cle=tmp[-2]#on recup la clé
            tmp=re.split(' |\t|\n',lignes[i]) #reséparation
            rvb=[0,0,0]
            k,x=0,0
            while(x<3):
                while(tmp[k]==""):
                    k+=1
                rvb[x]=tmp[k] #on récupére les valeurs rgb
                x+=1
                k+=1
            rgb=(rvb[0],rvb[1],rvb[2])  #creation tuple rgb
            if cle not in Dico: #si la clé n'est pas dans le dico
                cont=True #condition d'ajout
                for j in Dico: #pour chaque clée du dico
                    if(Dico[j]==rgb): #si le code rgb est déjà dans le dico on ne rajoute pas la ligne
                        cont=False
                if(cont):
                    Dico.update({cle:rgb}) #ajout dans le dico
    return Dico


def convers(dico):
    """
    conversion de dico en liste
    """
    l=[] #creation liste
    for j in dico:
        l+=[j]
        #ajouter saut indice
        #l+=j #ajout clé
    l.sort()  #tri
    return l


#chemin="/etc/X11/rgb.txt"
#option=str(input("Option d'ouverture du fichier :"))
#gestfich(chemin,option)
#dic={}
#dic=parser(chemin,option)
#print(convers(dic))
