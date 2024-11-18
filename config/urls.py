"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from app.views import (
    home,
    account_view,
    new_group,
    edit_group,
    delete_group,
    groups_account_view,
    notifications,
    join_group,
    accept,
    remove,
    reject,
    real_home,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", real_home, name="real_home"),
    path("feed", home, name="home"),
    path("notifications", notifications, name="notifications"),
    path("groups/<int:id>", groups_account_view, name="groups"),
    path("groups/remove/<int:group_id>/<str:username>", remove, name="remove"),
    path("groups/join/<int:id>", join_group, name="join_group"),
    path("groups/accept/<int:group_id>/<int:user_id>", accept, name="accept"),
    path("groups/reject/<int:group_id>/<int:user_id>", reject, name="reject"),
    path("groups/new", new_group, name="new_group"),
    path("groups/edit/<int:id>", edit_group, name="edit_group"),
    path("groups/delete/<int:id>", delete_group, name="delete_group"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/<str:username>/", account_view, name="account"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
