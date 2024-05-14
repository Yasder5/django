from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class JeuForm(ModelForm):
    class Meta:
        model = models.Jeu
        fields = ('nomJeu', 'editeur', 'date_parution', 'description')
        labels = {
        'nomJeu' : _('Nom du Jeu'),
        'editeur' : _('Editeur') ,
        'date_parution' : _('date de parution'),
        'description' : _('Description du Jeu')
}
    
class JoueurForm(ModelForm):
    class Meta:
        model = models.Joueur
        fields = ('nomJoueur', 'nomJeu','nomEquipe')
        label = {
            'nomJoueur' : _('Nom du joueur'),
            'nomJeu' : _('Nom du jeu'),
            'nomEquipe' : _("Nom de l'equipe E-sport")
        }