from django.shortcuts import render
from app.forms import PlayerForm

# Create your views here.


def home(request):
    return render(request, "home.html", {"page": "Home"})


def new_player(request):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, "home.html", {"page": "Home"})
    else:
        return render(request, "new_player.html", {"page": "New Player", "form": form})
