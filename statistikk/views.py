from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
# Create your views here.
from .models import Datasett, Sammenligning


def index(request):
    return HttpResponse("Hello, world. You're at the statistikk index.")

class DatasettView(generic.DetailView):
    model = Datasett
    template_name = 'statistikk/datasett.html'

class SammenligningView(generic.DetailView):
    model = Sammenligning
    template_name= 'statistikk/sammenligning.html'
