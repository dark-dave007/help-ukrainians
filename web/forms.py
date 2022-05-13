from django import forms
from .models import Category, Donation, Request
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "text-input",
                "placeholder": "Password",
            }
        ),
        strip=False,
    )
    new_password2 = forms.CharField(
        label="",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "text-input",
                "placeholder": "Confirm Password",
            }
        ),
    )


class MyResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        label="",
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
                "class": "text-input",
                "placeholder": "Email",
            }
        ),
    )


class FilterPostsForm(forms.Form):
    categories = forms.ModelChoiceField(
        Category.objects.all(),
        empty_label="Choose a category",
        required=False,
        widget=forms.Select(attrs={"class": "small"}),
    )
    requests = forms.BooleanField(required=False)
    donations = forms.BooleanField(required=False)


class RequestForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Product you want",
                "class": "text-input form-text-input",
            }
        ),
        required=True,
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description of the product",
                "class": "text-input form-text-input",
                "style": "resize:none;",
            }
        ),
        required=True,
    )
    img = forms.ImageField(label="Image")
    category = forms.ModelChoiceField(
        Category.objects.all(),
        label="Category",
        required=True,
        empty_label="Choose a category",
    )


class DonationForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Product you want",
                "class": "text-input form-text-input",
            }
        ),
        required=True,
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description of the product",
                "class": "text-input form-text-input",
                "style": "resize:none;",
            }
        ),
        required=True,
    )
    img = forms.ImageField(label="Image", required=True)
    category = forms.ModelChoiceField(
        Category.objects.all(),
        label="Category",
        required=True,
        empty_label="Choose a category",
    )
