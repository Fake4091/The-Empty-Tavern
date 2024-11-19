from django import forms
from django.contrib.auth.models import User
from app.models import Groups

# from app.models import Player


class GroupForm(forms.Form):
    group_name = forms.CharField(max_length=100)
    group_description = forms.CharField()
    group_pic = forms.ImageField()
    game_version = forms.ChoiceField(choices=Groups.GAME_VERSIONS)


class ViewGroupsForm(forms.Form):
    game_version = forms.ChoiceField(choices=Groups.GAME_VERSIONS)
    hide = forms.BooleanField(label="Hide joined groups?", required=False)


class EditGroupForm(forms.Form):
    group_name = forms.CharField(max_length=100, required=False)
    group_description = forms.CharField(required=False)
    group_pic = forms.ImageField(required=False)
    game_version = forms.ChoiceField(choices=Groups.GAME_VERSIONS, required=False)


class DeleteGroupsForm(forms.Form):
    confirmation = forms.CharField()


class JoinGroupForm(forms.Form):
    confirm = forms.BooleanField()


class AcceptJoinForm(forms.Form):
    confirm = forms.BooleanField()


class RemoveForm(forms.Form):
    confirm = forms.BooleanField()
