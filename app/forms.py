from django import forms
from django.contrib.auth.models import User
from app.models import Groups

# from app.models import Player


class GroupForm(forms.Form):
    users = []
    for i in User.objects.all():
        users.append((i, i.username))

    group_description = forms.CharField()
    group_pic = forms.ImageField()
    group_name = forms.CharField(max_length=100)
    game_version = forms.ChoiceField(choices=Groups.GAME_VERSIONS)


class ViewGroupsForm(forms.Form):
    game_version = forms.ChoiceField(choices=Groups.GAME_VERSIONS)


# class PlayerForm(forms.ModelForm):
#    class Meta:
#        model = Player
#        exclude = ["user"]
