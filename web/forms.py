from django import forms
from .models import Category, Donation, Request


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
