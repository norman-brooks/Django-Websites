
from django.db import models




TYPE_CHOICES = {
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Ms','Ms'),
}

class Profile(models.Model):
    Title = models.CharField(max_length=5, blank=True, choices=TYPE_CHOICES)
    First_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Last_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Email = models.EmailField(max_length=300, default="", blank=True, )
    Username= models.CharField(max_length=100, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.Last_Name