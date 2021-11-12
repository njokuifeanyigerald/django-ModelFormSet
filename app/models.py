from django.db import models



class ModelFormSetModel(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length=200)
    department = models.TextField()

    class Meta:
        verbose_name_plural = 'data'

    def __str__(self):
        return self.email