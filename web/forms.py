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


class RequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)

        placeholders = ["Product you want", "Description of the item"]

        for index, field in enumerate(self.Meta.fields):
            self.fields[field].widget.attrs.update(
                {"class": "text-input, text-input-75"}
            )

            if index < 2:
                self.fields[field].widget.attrs.update(
                    {"placeholder": placeholders[index]}
                )

            if field == "img":
                continue
            self.fields[field].required = True

    class Meta:
        model = Request
        fields = ["title", "description", "img", "category"]


class DonationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)

        placeholders = ["Product you have to give away", "Description of the item"]

        for index, field in enumerate(self.Meta.fields):
            self.fields[field].widget.attrs.update(
                {"class": "text-input, text-input-75"}
            )

            if index < 2:
                self.fields[field].widget.attrs.update(
                    {"placeholder": placeholders[index]}
                )

            self.fields[field].required = True

    class Meta:
        model = Donation
        fields = ["title", "description", "img", "category"]
