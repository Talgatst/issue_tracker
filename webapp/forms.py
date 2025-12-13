from django import forms
from webapp.models import Issue, Type
from webapp.validators import validate_summary_capital, validate_description_english


class IssueForm(forms.ModelForm):
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=False)

    summary = forms.CharField(validators=[validate_summary_capital])
    description = forms.CharField(
        widget=forms.Textarea,
        required=False,
        validators=[validate_description_english]
    )

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'types', 'status']
