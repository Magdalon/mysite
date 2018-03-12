from django.contrib import admin
from .models import Country, Leadership

# Register your models here.
#admin.site.register(Country)
#admin.site.register(Leadership)
#admin.site.register(Person)
#admin.site.register(Leadership_result)
class LeadershipInline(admin.TabularInline):
    model = Leadership
    extra = 3

class CountryAdmin(admin.ModelAdmin):
    inlines = [LeadershipInline]
    search_fields = ['country_name']
admin.site.register(Country, CountryAdmin)
