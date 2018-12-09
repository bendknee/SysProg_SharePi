from django import forms
from django.forms import ModelForm
from .models import File


class FileCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FileCreationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = File
        fields = '__all__'
