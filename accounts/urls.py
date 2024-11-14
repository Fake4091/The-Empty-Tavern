from django.urls import path

from .views import SignUpView, delete_account

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("delete_account/", delete_account, name="delete_account"),
]
