from django.forms import ModelForm
from .models import Organization, Key


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = ('name',)


class KeyForm(ModelForm):
    class Meta:
        model = Key
        fields = '__all__'
