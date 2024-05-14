from django.db import models

from django.db import models
class Jeu(models.Model): #déclare la classe Livre héritant de la classe Model, classede base des modèles
    nomJeu = models.CharField(max_length=100) # défini un champs de type texte de 100caractères maximum
    editeur = models.CharField(max_length = 100)
    date_parution = models.DateField(blank=True, null = True) # champs de type date,pouvant être null ou ne pas être rempli
    description = models.TextField(null = True, blank = True) # champs de type text long
    def __str__(self):
        chaine = f"le jeu {self.nomJeu}, éditer par {self.editeur}, est sortie le {self.date_parution}. La description du jeu est : {self.description}"
        return chaine

class Joueur(models.Model):
    nomJoueur = models.CharField(max_length=100)
    nomJeu = models.CharField(max_length=100)
    nomEquipe = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"Le joueur {self.nomJoueur} fait partie de l'équipe {self.nomEquipe} et joue a jeu {self.nomJeu}"