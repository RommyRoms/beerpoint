# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class BeerTable(models.Model):
    class Meta():
        db_table = 'beer_table'
    beer_name = models.CharField(verbose_name=' Название пива', max_length= 250)
    beer_maker = models.CharField(verbose_name='Произв', max_length=250)
    beer_country = models.CharField(verbose_name='Страна', max_length=250)
    beer_calory = models.IntegerField(verbose_name='Калории')
    beer_part_suslo = models.DecimalField(verbose_name='Часть сухих веществ', max_digits=4, decimal_places=1)
    beer_part_alco = models.DecimalField(verbose_name='Количество алкоголя от объема', max_digits=3, decimal_places=1)
    beer_another = models.TextField(verbose_name='Доп. информация')
    beer_date_public = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s %s %s %s %s %s %s %s" %(self.beer_name, self.beer_maker, self.beer_country, self.beer_calory, self.beer_part_suslo, self.beer_part_alco, self.beer_another, self.beer_date_public)