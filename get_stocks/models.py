from django.db import models

# Create your models here.

class Stock(models.Model):
    name = models.CharField(max_length=200)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, viewed? {self.viewed}'

        
class FindStock(models.Model):

    Symbol = models.CharField(max_length=200)
    Interval = models.CharField(max_length=200)


    def __str__(self):
        return 'Stock ticker: {} with {} interval'.format(self.Symbol, self.Interval)


    
class ViewStock(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return 'Saved house name: {}'.format(self.name)
    
    