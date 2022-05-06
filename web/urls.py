from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("ask", views.post_request, name="post_request"),
    path("donate", views.post_donation, name="post_donation"),
]
