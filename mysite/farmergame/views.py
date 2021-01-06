from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.forms import modelformset_factory
from django.core.serializers.json import DjangoJSONEncoder
from json import dumps

from .models import Animal, Farm, OwnAnimal
from .forms import TradeAnimalsForm

class FarmListView(generic.ListView):
    """The view for the index of farms"""
    model = Farm
    template_name='farmergame/farm_list.html'
    
def trade_animals(request, pk):
    """handles the buy animals form page"""
    farm = get_object_or_404(Farm, pk=pk)
    #create a formset
    #TradeFormSet = modelformset_factory(OwnAnimal,
     #                                   fields = ('nr_owned',),
      #                                  labels = {'nr_owned':'desired number of %ss' %} )
    
    #formset = TradeFormSet(queryset=OwnAnimal.objects.filter(farm__pk=pk))
    if request.method == 'POST':
        form = TradeAnimalsForm(pk, request.POST)
        #create an instance of BuyAnimalsForm and populate it 
        if form.is_valid():
            farm = Farm.objects.get(pk=pk)
            owned_animals = farm.ownanimal_set.all()
            money = farm.capital
            
            for owned_animal in owned_animals:
                nr_change = form.cleaned_data[str(owned_animal.pk)] - owned_animal.nr_owned
                
                if nr_change > 0:
                    #we buy animals
                    print("Buying: ", nr_change, " ", owned_animal.animal.species)
                    money -= owned_animal.animal.buy_price*(nr_change)
                else:
                    print("Selling: ",-nr_change," ", owned_animal.animal.species)
                    money -=  owned_animal.animal.sell_price*(nr_change)
            
            if (money > 0):
                print("Trade successful!")
                for owned_animal in owned_animals:
                    owned_animal.nr_owned = form.cleaned_data[str(owned_animal.pk)]
                    owned_animal.save()
                
                farm.capital = money
                farm.save()
                
                return HttpResponseRedirect(reverse('farmergame:view_farm',args=(farm.id,)))
                
            return render(request, 'farmergame/buy_animals.html', {'farm': farm,
                                                                    'form': form,
                                                                    'error_message':"Not enough money! need %d more" %-money})
    else:
        form = TradeAnimalsForm(pk)
        return render(request, 'farmergame/buy_animals.html', {'farm': farm, 'form': form})
        
def view_farm(request, pk):
    """view the farm"""
    farm = get_object_or_404(Farm, pk=pk)
    dataJSON = dumps(farm.ownanimal_set.all(), cls=DjangoJSONEncoder)
    return render(request, 'farmergame/view_farm.html', {'farm':farm,
                                                         'data': dataJSOM})