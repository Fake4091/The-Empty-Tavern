from django.shortcuts import render
from app.models import Groups
from app.forms import GroupForm

# from app.forms import PlayerForm

# Create your views here.


def home(request):
    return render(request, "home.html", {"page": "Home"})


def account_view(request, username):
    return render(
        request,
        "account.html",
        {"page": "Account", "username": username, "groups": Groups.objects.all()},
    )


def new_group(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        group = Groups(
            group_name=form.cleaned_data["group_name"],
            members=form.cleaned_data["members"],
            game_version=form.cleaned_data["game_version"],
        )
        group.save()
        return render(
            request,
            "home.html",
            {"page": "Home", "members": form.cleaned_data["members"]},
        )
    else:
        return render(request, "new_group.html", {"page": "New Group", "form": form})


# def new_player(request):
# form = PlayerForm(request.POST or None)
# if form.is_valid():
# form.save()
# return render(request, "home.html", {"page": "Home"})
# else:
# return render(request, "new_player.html", {"page": "New Player", "form": form})
