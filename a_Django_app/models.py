from django.db import models


class Package(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='packages', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'a_Django_app'

