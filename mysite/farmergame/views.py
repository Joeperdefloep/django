from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.forms import modelformset_factory


from .models import Animal, Farm, OwnAnimal


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
        #create an instance of BuyAnimalsForm and populate it 
        try:
            return HttpResponse("list: %s" % request.POST['desired_amount'])
        except (KeyError):
            return HttpResponse(str(KeyError))
        return HttpResponseRedirect(reverse('farmergame:',args=(farm.id,)))
    else:
        return render(request, 'farmergame/buy_animals.html', {'farm': farm, 'formset': formset})
        
def view_farm(request, pk):
    """view the farm"""
    farm = get_object_or_404(Farm, pk=pk)
    return HttpResponse("Looking at Farm: %s" %farm.farm_name)