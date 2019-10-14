from django.db import models


class Food(models.Model):
    food_name = models.CharField(max_length=60)
    #TODO: FALTA COLOCAR TIPO DE MEDIDA AQUI (medida caseira)
    #TODO: FALTA COLOCAR QUANTIDADE DA MEDIDA CASEIRA
    measure = models.FloatField(default=0) # in grams
    calories = models.FloatField(default=0) # calories per measure
    proteins = models.FloatField(default=0) # proteins per measure
    carbohydrates = models.FloatField(default=0) # carbohydrates per measure
    lipids = models.FloatField(default=0) # lipids per measure
    #TODO: COLOCAR GRUPO ALIMENTAR
