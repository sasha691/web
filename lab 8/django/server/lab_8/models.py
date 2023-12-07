from django.db import models

# Create your models here.
class Race(models.Model):
    race = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.race}"
    
class Profession(models.Model):
    profession = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.profession}"

class Player(models.Model):
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    rase = models.ForeignKey(Race, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    birthday = models.DateField()
    banned = models.BooleanField()
    level = models.IntegerField()
    def __str__(self):
        return f"id: {self.pk}; name: {self.name}; title: {self.title}; rase: {self.rase}; profession: {self.profession}; level: {self.level}"