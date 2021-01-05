from django import forms
from .models import Farm, Animal

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['farm_name','animals','capital']
        
    animals = forms.ModelMultipleChoiceField(
        queryset=Animal.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )


class TradeAnimalForm(forms.Form):
    amount = forms.IntegerField()


