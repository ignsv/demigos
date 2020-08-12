from django import forms
from django.utils.translation import ugettext as _

from .handler import CryptoHandler
from .models import Pair, PairRecord


class CreatePairForm(forms.ModelForm):
    class Meta:
        model = Pair
        fields = ['name', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handler = CryptoHandler()

    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data['name'].split('-')) != 2:
            raise forms.ValidationError(_('You should enter pair name in XXX-YYY format'))
        else:
            if not self.handler.get_pair_current_value(*cleaned_data['name'].split('-')):
                raise forms.ValidationError(_('This pair do not exists'))
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=True)
        volume = self.handler.get_pair_current_value(*self.cleaned_data['name'].split('-'))
        PairRecord.objects.create(pair=instance, volume=volume)
        return instance
