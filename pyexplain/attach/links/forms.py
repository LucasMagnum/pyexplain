# coding: utf-8

from django import forms

from .models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('name', 'url', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3})
        }