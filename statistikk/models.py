from django.db import models
import numpy
import scipy.stats
import mystat
import statistics
# Create your models here.

class Datasett(models.Model):
    app_label = 'statistikk'
    '''TODO'''
    person_name = models.CharField(max_length=200)
    data_description = models.TextField()
    def __str__(self):
        return self.person_name
    enhet = models.CharField(max_length=200,default='minutter')

    def median(self):
        data = list(self.data_set.values_list('value',flat=True))
        return format(numpy.median(data), '.3g')

    def gjennomsnitt(self):
        data = list(self.data_set.values_list('value',flat=True))
        return format(numpy.mean(data), '.3g')

    def typetall(self):
        data = list(self.data_set.values_list('value',flat=True))
        return [format(f, '.3g') for f in mystat.typetall(data)]

    def variasjonsbredde(self):
        data = list(self.data_set.values_list('value',flat=True))
        return format(max(data) - min(data), '.3g')

    def kvartilbredde(self):
        data = list(self.data_set.values_list('value',flat=True))
        return format(numpy.subtract.reduce(numpy.percentile(data, [75, 25])), '.3g')

    def Q1(self):
        data = list(self.data_set.values_list('value',flat=True))
        return 0

    def Q3(self):
        data = list(self.data_set.values_list('value',flat=True))
        return 0

    def varians(self):
        data = list(self.data_set.values_list('value',flat=True))
        return format(statistics.pvariance(data), '.4g')

    def standardavvik(self):
        data = list(self.data_set.values_list('value',flat=True))
        return format(statistics.pstdev(data), '.3g')

    def beregn(self):
        print("here!")

    def gjennomsnittshastighet(self):
        data = list(self.data_set.values_list('value',flat=True))
        return format(600/numpy.mean(data), '.3g')


class Data(models.Model):
    app_label = 'statistikk'
    dataset = models.ForeignKey(Datasett, on_delete=models.CASCADE)
    value = models.IntegerField()
    def __str__(self):
        return str(self.value)
