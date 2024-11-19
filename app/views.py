from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from app.models import Groups, Notifications
from app.forms import (
    GroupForm,
    JoinGroupForm,
    RemoveForm,
    ViewGroupsForm,
    DeleteGroupsForm,
    EditGroupForm,
    AcceptJoinForm,
)

# from app.forms import PlayerForm

# Create your views here.


def home(request):
    form = ViewGroupsForm(request.GET)
    if form.is_valid():
        groups = Groups.objects.filter(game_version=form.cleaned_data["game_version"])
        groups = list(groups)
        if form.cleaned_data["hide"]:
            for i in groups:
                if request.user.username in i.members:
                    groups.remove(i)
        return render(
            request,
            "feed.html",
            {
                "page": "Home",
                "groups": groups,
                "form": form,
                "site": request.get_host(),
            },
        )
    else:
        return render(request, "feed.html", {"form": form})


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
    if request.method == "POST":
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            group = Groups(
                group_description=form.cleaned_data["group_description"],
                group_pic=form.cleaned_data["group_pic"],
                group_name=form.cleaned_data["group_name"],
                members=[request.user.username],
                game_version=form.cleaned_data["game_version"],
            )
            group.save()
            return redirect("home")
    else:
        form = GroupForm()
    return render(request, "add_group.html", {"form": form})


def edit_group(request, id):
    form = EditGroupForm(request.POST or None)
    if form.is_valid():
        group = Groups.objects.get(id=id)
        if group.members[0] == request.user.username:
            if form.cleaned_data["group_description"]:
                group.group_description = form.cleaned_data["group_description"]
            if form.cleaned_data["group_pic"]:
                group.group_pic = form.cleaned_data["group_pic"]
            if form.cleaned_data["group_name"]:
                group.group_name = form.cleaned_data["group_name"]
            if form.cleaned_data["game_version"]:
                group.game_version = form.cleaned_data["game_version"]
            group.save()
            return redirect("home")
        else:
            return redirect("home")
    else:
        return render(request, "edit_group.html", {"form": form})


def delete_group(request, id):
    form = DeleteGroupsForm(request.POST or None)
    if form.is_valid():
        group = Groups.objects.get(id=id)
        if (
            form.cleaned_data["confirmation"].lower() == "i understand."
            and group.members[0] == request.user.username
        ):
            group.delete()
            return redirect("home")
        elif form.cleaned_data["confirmation"].lower() != "i understand.":
            return redirect("home")
        else:
            return redirect("home")
    else:
        return render(request, "delete_group.html", {"form": form})


def groups_account_view(request, id):
    group = Groups.objects.get(id=id)
    return render(
        request,
        "group_account.html",
        {"group": group, "site": request.get_host()},
    )


def notifications(request):
    try:
        notis = Notifications.objects.get(user=request.user.username).notification[1:]
        print(len(notis))
    except Notifications.DoesNotExist:
        notis = Notifications(user=request.user.username)
        notis.save()
        notis = Notifications.objects.get(user=request.user.username).notification[1:]
    return render(
        request,
        "notifications.html",
        {"notifications": notis},
    )


def join_group(request, id):
    form = JoinGroupForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data["confirm"]:
            group = Groups.objects.get(id=id)
            if request.user.username not in group.members:
                for i in group.members:
                    try:
                        member = Notifications.objects.get(user=i)
                    except Notifications.DoesNotExist:
                        member = Notifications(user=i)
                    member.notification.append(
                        [
                            User.objects.get(username=i).id,
                            group.id,
                            group.members,
                            f"{request.user.username} would like to join {group.group_name}.",
                            request.user.id,
                        ]
                    )
                    member.save()
        return redirect("home")
    else:
        return render(request, "join_group.html", {"form": form})


def accept(request, group_id, user_id):
    form = AcceptJoinForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data["confirm"]:
            group = Groups.objects.get(id=group_id)
            if request.user.username == group.members[0]:
                if User.objects.get(id=user_id).username not in group.members:
                    group.members.append(User.objects.get(id=user_id).username)
                notif = Notifications.objects.get(user=request.user.username)
                for i in notif.notification:
                    if i:
                        if i[4] == user_id and i[1] == group_id:
                            notif.notification.remove(i)
                group.save()
                notif.save()
        return redirect("notifications")
    else:
        return render(request, "accept.html", {"form": form})


def remove(request, group_id, username):
    form = RemoveForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data["confirm"]:
            group = Groups.objects.get(id=group_id)
            if (
                request.user.username == group.members[0]
                or request.user.username == username
            ):
                if username in group.members:
                    group.members.remove(username)
            group.save()
        return redirect("home")
    else:
        return render(request, "remove.html", {"form": form, "username": username})


def reject(request, group_id, user_id):
    group = Groups.objects.get(id=group_id)
    if request.user.username == group.members[0]:
        notif = Notifications.objects.get(user=request.user.username)
        for i in notif.notification:
            if i:
                if i[4] == user_id and i[1] == group_id:
                    notif.notification.remove(i)
        notif.save()
    return redirect("home")


def real_home(request):
    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "home.html")
