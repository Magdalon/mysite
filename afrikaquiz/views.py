from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from random import sample

# Create your views here.

from afrikaquiz.models import *

ALTERNATIVE_COUNT = 4

class IndexView(generic.ListView):
    template_name = 'afrikaquiz/index.html'
    context_object_name ='latest_question_list'

    def get_queryset(self):
        return Country.objects.all()

def result(request, iso, pid):
    country = get_object_or_404(Country,iso=iso)
    correct_person = country.get_leader()
    selected_person = Person.objects.get(pk=pid)
    alternativer = Leadership_result.objects.filter(country=country).order_by('-votes')
    return render(request, 'afrikaquiz/result.html', { 'country':country, 'selected_person': selected_person, 'correct_person': correct_person, 'alternativer': alternativer})

def longest(request):
    leadership = Leadership.objects.filter(end__isnull=True).order_by('start')
    return render(request, 'afrikaquiz/longest.html', {'leadership':leadership})

def detail(request, iso):
    country = get_object_or_404(Country,iso=iso)
    title = country.get_title()
    alternatives = country.get_alternatives(ALTERNATIVE_COUNT)
    return render(request, 'afrikaquiz/detail.html', { 'alternatives':alternatives, 'country': country, 'title':title})

def random(request):
    country = sample(list(Country.objects.all()), 1)[0]
    title = country.get_title()
    alternatives = country.get_alternatives(ALTERNATIVE_COUNT)
    return render(request, 'afrikaquiz/detail.html', { 'alternatives':alternatives, 'country': country, 'title':title})

def vote(request, iso):
    country = get_object_or_404(Country,iso=iso)
    alternatives = country.get_alternatives(ALTERNATIVE_COUNT)
    try:
        selected_person = Person.objects.get(pk=request.POST['choice'])
    except (KeyError, Person.DoesNotExist):
        #Redisplay the question voting form
        return render(request, 'afrikaquiz/detail.html', { 'alternatives':alternatives, 'country': country, 'error_message':"You didn't select a choice."})
    else:
        lr = Leadership_result.objects.get_or_create(country=country,person=selected_person)[0]
        lr.votes += 1
        lr.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('afrikaquiz:result',args=(iso,selected_person.id)))
