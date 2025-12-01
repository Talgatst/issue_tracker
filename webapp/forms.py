from django import forms
from webapp.models import Issue, Type


class IssueForm(forms.ModelForm):
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=False)

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'types', 'status']
