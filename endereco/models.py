from django.db import models

# Create your models here.
class lugar(models.Model):
    cep_lugar        = models.CharField(max_length=8)
    uf_lugar         = models.CharField(max_length=2, blank=True)
    distrito_lugar   = models.CharField(max_length=50, blank=True)
    logradouro_lugar = models.TextField(blank=True)

    def __str__(self):
        return self.cep_lugar