from django.db import models
import numpy
import matplotlib.pyplot as plt
import scipy.stats
import mystat
import statistics
import os
# Create your models here.

class Datasett(models.Model):
    FORMAT = '.3g'
    DETAILED_FORMAT = '.4g'
    app_label = 'statistikk'
    '''TODO'''
    person_name = models.CharField(max_length=200)
    data_description = models.TextField()
    def __str__(self):
        return self.person_name
    enhet = models.CharField(max_length=200,default='minutter')

    def data(self):
        return list(self.data_set.values_list('verdi',flat=True))

    def sortert(self):
        return sorted(self.data())

    def median(self):
        return format(numpy.median(self.data()), self.FORMAT)

    def gjennomsnitt(self):
        return mystat.gjeldende_siffer(numpy.mean(self.data()))
        #return numpy.mean(self.data())

    def typetall(self):
        return [format(f, self.FORMAT) for f in mystat.typetall(self.data())]

    def variasjonsbredde(self):
        return format(max(self.data()) - min(self.data()), self.FORMAT)

    def kvartilbredde(self):
        return format(numpy.subtract.reduce(numpy.percentile(self.data(), [75, 25],interpolation = 'nearest')), self.FORMAT)

    def Q1(self):
        return format(numpy.percentile(self.data(),25,interpolation = 'nearest'),self.FORMAT)

    def Q3(self):
        return format(numpy.percentile(self.data(),75,interpolation = 'nearest'),self.FORMAT)

    def varians(self):
        return format(statistics.pvariance(self.data()), self.DETAILED_FORMAT)

    def standardavvik(self):
        return mystat.gjeldende_siffer(statistics.pstdev(self.data()))

    def beregn(self):
        print("here!")

    def gjennomsnittshastighet(self):
        return format(600/numpy.mean(self.data()), self.FORMAT)

    def linje_url(self):
        filnavn = "images/datasett/" + str(self.pk) + ".png"
        if not os.path.exists(filnavn):
            self.generer_linje()
        print(filnavn)
        return filnavn

    def max(self):
        return max(self.data())

    def min(self):
        return min(self.data())

    def generer_linje(self, close = True):
        filnavn = "statistikk/static/images/datasett/" + str(self.pk) + ".png"
        plt.plot(range(1,len(self.data())+1),self.data(),label=self.person_name)
        plt.ylabel('tid (minutter)')
        plt.xlabel('observasjon')
        plt.savefig(filnavn)
        if close:
            plt.close()
        return filnavn

    def leggtil(name,data):
        nyttdatasett = Datasett.objects.create(person_name=name)

        for v in data:
            Data.objects.create(datasett=nyttdatasett,verdi=v)

        return nyttdatasett

class Sammenligning(models.Model):
    datasett = models.ManyToManyField(Datasett)

    def __str__(self):
        return str(self.datasett.all())

    def generer_linje(self,close = True):
            filnavn = "statistikk/static/images/sammenligning/" + str(self.pk) + ".png"
            for sett in self.datasett.all():
                plt.plot(range(1,len(sett.data())+1),sett.data(),label=sett.person_name)

            plt.ylabel('tid (minutter)')
            plt.xlabel('observasjon')
            plt.legend()
            plt.savefig(filnavn)
            if close:
                plt.close()
            return filnavn

    def linje_url(self):
        filnavn = "images/sammenligning/" + str(self.pk) + ".png"
        if not os.path.exists(filnavn):
            self.generer_linje()
        print(filnavn)
        return filnavn

    def max(self):
        storst = -99999
        person = 'Ingen'
        for datasett in self.datasett.all():
            if(datasett.max() == storst):
                person = 'Flere enn en (begge)'
            if(datasett.max()>storst):
                person=datasett.person_name
                storst = datasett.max()

        return person

    def min(self):
        minst = 99999
        person = 'Ingen'
        for datasett in self.datasett.all():
            if(datasett.min() == minst):
                person = 'Flere enn en (begge)'
            if(datasett.min()<minst):
                person=datasett.person_name
                minst = datasett.min()

        return person

    def gjennomsnitt_min(self):
        minst = 99999
        person = 'Ingen'
        for datasett in self.datasett.all():
            if(datasett.gjennomsnitt() == minst):
                person = 'Flere enn en (begge)'
            if(datasett.gjennomsnitt()<minst):
                person=datasett.person_name
                minst = datasett.gjennomsnitt()
        return person

    def standardavvik_max(self):
        verdi = -99999
        person = 'Ingen'
        for datasett in self.datasett.all():
            if(datasett.standardavvik() == verdi):
                person = 'Flere enn en (begge)'
            if(datasett.standardavvik()>verdi):
                person=datasett.person_name
                minst = datasett.gjennomsnitt()
        return person



class Data(models.Model):
    app_label = 'statistikk'
    datasett = models.ForeignKey(Datasett, on_delete=models.CASCADE)
    verdi = models.IntegerField()
    def __str__(self):
        return str(self.verdi)
