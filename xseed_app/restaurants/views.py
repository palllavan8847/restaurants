# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core import serializers
from django.forms.models import model_to_dict
from django.db.models import Q
from django.contrib.auth import authenticate, login as elogin
from models import Restaurant, RestaurantDetail
import json

# Create your views here.

def restaurant_serialize(queryset):
    restaurant_list = [ model_to_dict(obj) for obj in queryset ]
    return {'all_restaurants': restaurant_list}

def login(request):
    if request.user.is_authenticated():
        return render(request, 'restaurants.html', restaurant_serialize(RestaurantDetail.objects.all()))
    if request.POST:
        data = request.POST
        username = data.get('username', '')
        password = data.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                elogin(request, user)
                return render(request, 'restaurants.html', restaurant_serialize(RestaurantDetail.objects.all()))
            else:
                return render(request, 'login.html', {'message': "User is not active"})
        else:
            return render(request, 'login.html', {'message': "Invalid username or password"})
    return render(request, 'login.html', {})

def search_restaurants(request):
    data = request.GET.get('search')
    if not data:
        return render(request, 'restaurants.html', restaurant_serialize(RestaurantDetail.objects.all()))
    return render(request, 'restaurants.html', restaurant_serialize(RestaurantDetail.objects.filter(restaurant_name__icontains = data)))

def search_cuisines(request):
    data = request.GET.get('search')
    if not data:
        return render(request, 'restaurants.html', restaurant_serialize(RestaurantDetail.objects.all()))
    cuisine_list = data.split(',')
    query_obj = Q()
    for query in cuisine_list:
        query_obj = query_obj | Q(cuisines__icontains = query)
    return render(request, 'restaurants.html', restaurant_serialize(RestaurantDetail.objects.filter(query_obj)))