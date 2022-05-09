from django.urls import path
from django.contrib.auth import views as auth_views

from web.forms import MyResetPasswordForm, MySetPasswordForm
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("ask/", views.post_request, name="post_request"),
    path("donate/", views.post_donation, name="post_donation"),
    path("<str:type>/<int:id>", views.item, name="item"),
    path("close/<str:type>/<int:id>", views.close_item, name="close_item"),
    # Register, login and password reset
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="web/password_reset.html", form_class=MyResetPasswordForm
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="web/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset_/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="web/password_reset_form.html", form_class=MySetPasswordForm
        ),
        name="password_reset_confirm",
    ),  # userid encrypted, token to check password is valid
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="web/password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
]
