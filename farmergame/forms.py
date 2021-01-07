from django import forms
from django.shortcuts import get_object_or_404

from .models import Farm, Animal, OwnAnimal

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name','animals','money']
        
    animals = forms.ModelMultipleChoiceField(
        queryset=Animal.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )


class TradeAnimalsForm(forms.Form):
    
    def __init__(self, farm_pk, *args, **kwargs):
        super(TradeAnimalsForm,self).__init__(*args, **kwargs)
        self.owned_animals = Farm.objects.get(pk=farm_pk).ownanimal_set.all().order_by('animal__buy_price')
    
        for owned_animal in self.owned_animals:
            field_name = str(owned_animal.pk)
            self.fields[field_name] = forms.IntegerField(initial=owned_animal.nr_owned)
            self.fields[field_name].label = "Number of %ss" %owned_animal.animal.species