from django.contrib import admin
from django.db import models
# Register your models here.
from .models import Datasett, Data, Sammenligning

class DataInline(admin.TabularInline):
    model = Data
    extra = 11

class DatasettAdmin(admin.ModelAdmin):
    inlines = [DataInline]

admin.site.register(Datasett, DatasettAdmin)
admin.site.register(Sammenligning)
