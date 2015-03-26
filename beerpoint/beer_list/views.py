# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import BeerTable
from django.shortcuts import get_object_or_404
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


"""
1. Вытягиваем все объекты с мускла
2. Делаем рандом по главной странице для всех напитков
3. выводим 6 штук
"""

def choose_all_beers(request):
    beers = BeerTable.objects.all().order_by('-beer_date_public')
    return render_to_response('beers.html', {"beers": beers})

"""
1. При нажатии на ссылку открываеться название пива и через регулярное выражение выбираем id пива.
2. Если нету id в базе вызываем 404
3. Если есть выводим через айти страницу определенного пива
"""
def detail_beer(request, beer_id):
    kind = get_object_or_404(BeerTable, pk=beer_id)
    return render_to_response('beer.html', {'kind': kind})

