Creer

# models.py
from django.db import models

class VotreModele(models.Model):
    champ1 = models.CharField(max_length=100)
    champ2 = models.IntegerField()

# views.py
from django.shortcuts import render, redirect
from .models import VotreModele
from .forms import VotreModeleForm

def creer_vue(request):
    if request.method == 'POST':
        form = VotreModeleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste')
    else:
        form = VotreModeleForm()
    return render(request, 'creer.html', {'form': form})

# creer.html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Créer</button>
</form>

Read
# views.py
from django.shortcuts import render
from .models import VotreModele

def liste_vue(request):
    objets = VotreModele.objects.all()
    return render(request, 'liste.html', {'objets': objets})

# liste.html
<ul>
    {% for objet in objets %}
        <li>{{ objet.champ1 }}, {{ objet.champ2 }}</li>
    {% endfor %}
</ul>


Update
# views.py
from django.shortcuts import render, redirect
from .models import VotreModele
from .forms import VotreModeleForm

def mettre_a_jour_vue(request, id):
    objet = VotreModele.objects.get(id=id)
    if request.method == 'POST':
        form = VotreModeleForm(request.POST, instance=objet)
        if form.is_valid():
            form.save()
            return redirect('liste')
    else:
        form = VotreModeleForm(instance=objet)
    return render(request, 'mettre_a_jour.html', {'form': form})

# mettre_a_jour.html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Mettre à jour</button>
</form>


Delete


# views.py
from django.shortcuts import render, redirect
from .models import VotreModele

def supprimer_vue(request, id):
    objet = VotreModele.objects.get(id=id)
    objet.delete()
    return redirect('liste')
