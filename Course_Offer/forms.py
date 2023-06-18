from django import forms

from .import models

class Course_form(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = "__all__"
