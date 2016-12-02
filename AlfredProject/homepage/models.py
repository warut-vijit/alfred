from django.db import models
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return "User "+self.id+': '+str(self.name)


class Balance(models.Model):
    user_from = models.PositiveSmallIntegerField()
    user_to = models.PositiveSmallIntegerField()
    amount = models.FloatField()

    def __str__(self):
        return str(self.user_from)+" owes "+str(self.user_to)+" $"+str(self.amount)


class Venue(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return "Venue "+self.id+": "+str(self.name)


class FoodRequest(models.Model):
    venue = models.PositiveSmallIntegerField()
    poster = models.PositiveSmallIntegerField()
    item = models.CharField(max_length=40)
    cost = models.FloatField()

    def __str__(self):
        return "Order: "+str(self.item)+" from "+str(self.venue)+" by "+str(self.poster)+" for "+str(self.cost)
