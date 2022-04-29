from django import forms
from .models import Category, Request


class RequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)

        for field in self.Meta.fields:
            if field == "img":
                continue
            self.fields[field].required = True

    class Meta:
        model = Request
        fields = ["title", "description", "img", "category"]
