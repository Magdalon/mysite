from django.db import models

from random import sample, shuffle

# Parent classes
class Result(models.Model):
    '''Placeholder'''

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Country(models.Model):
    iso = models.CharField(max_length=3,primary_key=True)
    name= models.CharField(max_length=200)
    leaders = models.ManyToManyField(Person,through='Leadership')
    def __str__(self):
        return self.iso + ": " + self.name
    def get_leader(self):
        return Leadership.objects.filter(country=self,end__isnull=True).first().person
    def get_title(self):
        return Leadership.objects.filter(country=self,end__isnull=True).first().title
    def get_alternatives(self,n):
        correct = self.get_leader()
        alternatives = [correct]
        t_wrong = list(Person.objects.exclude(pk=correct.pk))
        if len(t_wrong) < n-1: n = len(t_wrong)+1
        wrong = sample(t_wrong,max(n-1,0))
        alternatives.extend(wrong)
        shuffle(alternatives)
        return alternatives
    class Meta:
        verbose_name_plural = "countries"

class Leadership(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="president")
    start = models.DateField()
    end = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.end:
            endtext=str(self.end.year)
        else:
            endtext=""
        return self.country.name + " (" + self.country.iso + "): " + self.person.name + "(" + str(self.start.year) + " - " + endtext + ")"

class Leadership_result(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.country.name + " (" + self.country.iso + "): " + self.person.name + " (" + str(self.votes) + ")"
