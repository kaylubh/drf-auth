from django.db import models
from django.contrib.auth import get_user_model


class Penguin(models.Model):
    species_choices = {
        'gentoo': 'gentoo',
        'emperor': 'emperor',
        'chinstrap': 'chinstrap',
        'rockhopper': 'rockhopper',
    }
    # fields
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    species = models.CharField(max_length=64, choices=species_choices)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
