from django.shortcuts import render
from app.models import Groups
from app.forms import GroupForm, ViewGroupsForm

# from app.forms import PlayerForm

# Create your views here.


def home(request):
    form = ViewGroupsForm(request.GET)
    if form.is_valid():
        groups = Groups.objects.filter(game_version=form.cleaned_data["game_version"])
        return render(
            request, "home.html", {"page": "Home", "groups": groups, "form": form}
        )
    else:
        return render(request, "home.html", {"page": "Home", "form": form})


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
            group_description=form.cleaned_data["group_description"],
            group_pic=form.cleaned_data["group_pic"],
            group_name=form.cleaned_data["group_name"],
            members=[request.user],
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
