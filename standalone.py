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
