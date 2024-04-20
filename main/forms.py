from django import forms
from .models import Task


class AddPostForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['description',]
        widgets = {
            'description': forms.Textarea(attrs={'cols': 50, 'rows': 5 }),
            }
        labels = {'description': 'Описание'}


class UploadFileForm(forms.Form):
    file = forms.FileField(label="Файл")