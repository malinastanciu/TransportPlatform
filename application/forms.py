from django import forms


class OfferForm(forms.Form):
    senderID = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'intField'}))
    truckID = forms.IntegerField()
    freight_type = forms.CharField(max_length=20)
    date = forms.DateField()
    price_per_km = forms.FloatField()