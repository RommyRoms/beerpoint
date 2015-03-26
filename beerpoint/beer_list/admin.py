# -*- coding: utf-8 -*-
from django.contrib import admin
from models import BeerTable
# Register your models here.

class BeerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('beer_name', ('beer_country', 'beer_maker'))
        }),
        ('Advanced options', {
            'fields': ('beer_calory', ('beer_part_suslo', 'beer_part_alco'), 'beer_another')
        }),
    )
    list_display = ('beer_name', 'beer_country', 'beer_maker', 'beer_calory', 'beer_part_suslo', 'beer_part_alco', 'beer_date_public')
    search_fields = ['beer_name']
admin.site.register(BeerTable, BeerAdmin)





