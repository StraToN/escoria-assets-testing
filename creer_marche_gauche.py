import PIL
from PIL import Image

#retourner verticalement l'image dans le fichierOriginal et écrire le résultat dans fichierAproduire
def flipVertical(fichierOriginal,fichierAproduire):
    #read the image
    im = Image.open(fichierOriginal)
    #flip image
    out = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    out.save(fichierAproduire)

#créer les fichiers pour la marche vers la gauche à partir des fichiers originaux de la marche vers la droite
def creer_marche_gauche():
    for i in range(0,12):
        fichierOriginal="marche_vers_droite/"+str(i)+".png"
        fichierAproduire="marche_vers_gauche/"+str(i)+".png"
        flipVertical(fichierOriginal,fichierAproduire)
        print("marche_vers_droite/"+str(i)+".png fait")


creer_marche_gauche()
