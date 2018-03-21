## Setter opp Django
import os, sys
sys.path.insert(0, 'C:/Users/magopda/Dropbox/Documents/django/mysite/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mysite.settings')
import django
django.setup()

## Setter opp matematikkverktøy
import math, stat, numpy, scipy

## Laster inn modeller
from statistikk.models import *

debug = False
if debug:
    o = Datasett.objects.first()
    o.generer_linje()
    o.linje_url()

    o1 = Datasett.objects.first()
    o2 = Datasett.objects.last()
    s = Sammenligning.objects.first()
    s.datasett.add(o1)
    s.datasett.add(o2)
    s.generer_linje()
    s.linje_url()