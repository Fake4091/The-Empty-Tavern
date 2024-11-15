from django import forms
from django.contrib.auth.models import User
from app.models import Groups

# from app.models import Player


class GroupForm(forms.Form):
    group_description = forms.CharField()
    group_pic = forms.ImageField()
    group_name = forms.CharField(max_length=100)
    game_version = forms.ChoiceField(choices=Groups.GAME_VERSIONS)


class ViewGroupsForm(forms.Form):
    game_version = forms.ChoiceField(choices=Groups.GAME_VERSIONS)


class EditGroupForm(forms.Form):
    users = []
    for i in User.objects.all():
        users.append((i.username, i.username))

    members = forms.MultipleChoiceField(choices=users, required=False)
    group_description = forms.CharField(required=False)
    group_pic = forms.ImageField(required=False)
    group_name = forms.CharField(max_length=100, required=False)
    game_version = forms.ChoiceField(choices=Groups.GAME_VERSIONS, required=False)


class DeleteGroupsForm(forms.Form):
    confirmation = forms.CharField()


# class PlayerForm(forms.ModelForm):
#    class Meta:
#        model = Player
#        exclude = ["user"]
