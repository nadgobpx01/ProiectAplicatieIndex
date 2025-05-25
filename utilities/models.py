from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Consumption(models.Model):
    TYPE_CHOICES = [
        ('apa', 'Apă'),
        ('curent', 'Curent'),
        ('gaze', 'Gaze'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tip = models.CharField(max_length=10, choices=TYPE_CHOICES)
    furnizor = models.CharField(max_length=100)
    index_vechi = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    index_nou = models.DecimalField(max_digits=10, decimal_places=2)
    unitate_masura = models.CharField(max_length=10)  # ex: kWh, m3
    pret_unitar = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField(auto_now_add=True)

    def consum(self):
        if self.index_vechi is not None:
            return self.index_nou - self.index_vechi
        return self.index_nou

    def total_cost(self):
        return self.consum() * self.pret_unitar

    def __str__(self):
        return f"{self.get_tip_display()} - {self.furnizor} ({self.data})"
