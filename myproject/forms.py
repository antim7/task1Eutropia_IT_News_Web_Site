from django.contrib.auth.forms import forms
from myproject.models import Createnews

class NewsForm(forms.ModelForm):
    class Meta:
        model = Createnews
        fields = [
            'NewsId',
            'Title',
            'NewsDetails',
            'Coverimage',
        ]