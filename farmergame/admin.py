from django.contrib import admin
from . import models as md

class OwnAnimalInline(admin.TabularInline):
    model = md.OwnAnimal




class FarmAdmin(admin.ModelAdmin):
    model = md.Farm
    inlines = (OwnAnimalInline,)

class AnimalAdmin(admin.ModelAdmin):
    model = md.Animal
    inlines = (OwnAnimalInline,)

class AnnualCropAdmin(admin.ModelAdmin):
    model = md.AnnualCrop


# Register your models here.
admin.site.register(md.Farm, FarmAdmin)
admin.site.register(md.Animal, AnimalAdmin)
admin.site.register(md.AnnualCrop, AnnualCropAdmin)

