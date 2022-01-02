from django import forms
from django.forms import ModelForm, TextInput, IntegerField

from .models import Offer, Truck


class OfferForm(ModelForm):
    class Meta:
        model = Offer
        labels = {'senderID': 'Transportator'}
        fields = ['senderID', 'truckID', 'freight_type', 'date', 'price_per_km']

    def __init__(self, user, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        self.fields['truckID'].queryset = Truck.objects.filter(ownerId=user)
    # senderID = forms.IntegerField(widget=forms.TextInput())
    # truckID = forms.IntegerField()
    # freight_type = forms.CharField(max_length=20)
    # date = forms.DateField()
    # price_per_km = forms.FloatField()
