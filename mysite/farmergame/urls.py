from django.urls import path

from . import views

app_name='farmergame'
urlpatterns = [
    path('', views.FarmListView.as_view(), name='index'),
    path('<int:pk>/',views.view_farm, name='view_farm'),
    path('<int:pk>/buy/',views.trade_animals, name='buy_animals'),   
]
