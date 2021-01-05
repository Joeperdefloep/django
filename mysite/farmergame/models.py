from django.db import models

# Create your models here.
    

class Animal(models.Model):
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    buy_price = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
    benefits = models.FloatField(default=0)
    
    def __str__(self):
        return self.species + ": " + self.breed


    
    
class Farm(models.Model):


    name = models.CharField(max_length=200)
    capital = models.IntegerField(default=4000)
    animals = models.ManyToManyField(Animal, through='OwnAnimal')
    
    def __str__(self):
        return self.farm_name

class OwnAnimal(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    nr_owned = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.nr_owned) + " " + str(self.animal) + " on farm: " + str(self.farm)