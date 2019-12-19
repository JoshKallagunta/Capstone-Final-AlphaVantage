from django.db import models

# Create your models here.

#First model used to create the app.. 
class Stock(models.Model):
    name = models.CharField(max_length=200)
    viewed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}, viewed? {self.viewed}'


# Model for the Track Stock feature 
# includes a dropdown of values used in the API call 
# returns a string of symbol and interval information      
class FindStock(models.Model):

    INTERVAL_CHOICES = (
        ('5min', '5 MIN'),
        ('15min', '15 MIN'),
        ('30min', '30 MIN'),
        ('60min', '60 MIN'),
    )

    Symbol = models.CharField(max_length=200)
    Interval = models.CharField(max_length=5, choices=INTERVAL_CHOICES, default='5min')


    def __str__(self):
        return 'Stock ticker: {} with {} interval'.format(self.Symbol, self.Interval)


#Model for the View Stocks     
class ViewStock(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return 'Saved house name: {}'.format(self.name)
    
