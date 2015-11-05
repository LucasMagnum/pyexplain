# coding: utf-8

from django import forms

from .models import Example


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = ('name', 'code')
        widgets = {
            'code': forms.Textarea(attrs={'rows': 5})
        }
