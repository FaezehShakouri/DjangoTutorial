from django.db import models

class Favorite(models.Model):
    word = models.CharField(max_length=20)
    weight = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.word

    def save(self, *args, **kwargs):
        if not self.weight:
            self.weight = len(str(self.word))
        super(Favorite, self).save(*args, **kwargs)
    

class CustomUser(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    favorites = models.ManyToManyField(Favorite)

    def __str__(self) -> str:
        return self.username



