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
            request,
            "home.html",
            {
                "page": "Home",
                "groups": groups,
                "form": form,
                "site": request.get_host(),
            },
        )
    else:
        return render(request, "home.html", {"form": form})


def account_view(request, username):
    return render(
        request,
        "account.html",
        {
            "page": "Account",
            "username": username,
            "groups": Groups.objects.all(),
            "site": request.get_host(),
        },
    )


def new_group(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        groups = Groups.objects.filter(game_version="D&D")
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
            {
                "page": "Home",
                "groups": groups,
                "form": form,
                "site": request.get_host(),
            },
        )
    else:
        return render(request, "add_group.html", {"form": form})


# def new_player(request):
# form = PlayerForm(request.POST or None)
# if form.is_valid():
# form.save()
# return render(request, "home.html", {"page": "Home"})
# else:
# return render(request, "new_player.html", {"form": form})
