from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import JeuForm
from . import models


def index(request):
    return render(request, 'projetYasser/index.html')

def formulaire(request):
    return render(request, 'projetYasser/formulaire.html')

def affiche(request):
    nom=request.GET["nom"] 
    prenom=request.GET["prenom"] # récupère la valeur du paramètre nom du formulaire
    return render(request,'projetYasser/affiche.html',{"nom":nom, "prenom": prenom}) # passe cette valeur à la vue au travers du dictionnaire de contexte

def main(request):
    return render(request, 'projetYasser/main.html')

def test(request):
    jeux = JeuForm(request)
    return render(request, 'projetYasser/test.html',{"jeux" : jeux})

def ajout(request):
    if request.method == "POST":
        form = JeuForm(request)
        if form.is_valid():
            Jeu = form.save()
            return render(request, "projetYasser/affiche.html", {"Jeu" : Jeu})
        else:
            return render(request, "projetYasser/ajout.html", {"form": form})
    else :
        form = JeuForm()
        return render(request, "projetYasser/ajout.html", {"form": form})
    
def traitement(request):
    jform = JeuForm(request.POST)
    if jform.is_valid():
        Jeu = jform.save()
        return render(request, "projetYasser/traitement.html", {"Jeu" : Jeu})
    else:
        return render(request, "projetYasser/ajout.html",{"form": jform})
    
def read(request, id):
    Jeu = models.Jeu.objects.get(pk=id) # méthode pour récupérer les donnéesdans la base avec un id donnée
    return render(request,"projetYasser/traitement.html",{"Jeu": Jeu})

def update(request, id):
    jform = JeuForm(request.POST)
    if jform.is_valid():
        Jeu = jform.save(commit=False) # création d'un objet Livre avec les données du formulaire mais sans l'enregistrer dans la base.
        Jeu.id = id; # modification de l'id de l'objet
        Jeu.save() # mise à jour dans la base puisque l'id du Livre existe déja.
        return HttpResponseRedirect(f"/projetYasser/")
    else:
        return render(request, "projetYasser/update.html", {"form": jform, "id": id})   