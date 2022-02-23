import django_filters
from django_filters import DateFilter, CharFilter
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

from .models import *


class KeyFilter(django_filters.FilterSet):
    key = CharFilter(field_name='key', lookup_expr='icontains', label='Ключ:')

    class Meta:
        model = Key
        fields = ('key', 'org_id')
        widgets = {
            'key': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 200px; margin: 1000px 50px 120px 130px;',
                'placeholder': 'Key'
                }),
            'org_id': forms.Select(attrs={
                'class': "form-control form-control-sm",
                'style': 'max-width: 200px; margin: 1000px 50px 120px 130px;',
                'placeholder': 'org_id'
                })
        }

    def __init__(self, *args, **kwargs):
        super(KeyFilter, self).__init__(*args, **kwargs)
        self.filters['key'].label = "Ключ"

        self.filters['org_id'].label = "Организация"
        self.filters['org_id'].extra.update(
            {'empty_label': 'Все организации'})
