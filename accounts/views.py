from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from accounts.forms import DeleteAccountForm
from app.models import Notifications
from app.views import home


class SignUpView(CreateView):
    form_class = UserCreationForm()
    if form_class.is_valid():
        n = Notifications(
            user=User.objects.get(username=form_class.cleaned_data["username"]).id
        )
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def delete_account(request):
    form = DeleteAccountForm(request.POST or None)
    if form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user is not None:
            user.delete()
            return redirect(home)
        else:
            return redirect(home)
    else:
        return render(request, "registration/delete.html", {"form": form})
