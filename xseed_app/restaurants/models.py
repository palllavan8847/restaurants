# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.CharField(max_length = 45, blank = True,null = True, unique=True)
    country_code = models.CharField(max_length = 45, blank = True,null = True)
    city = models.CharField(max_length = 200, blank = True, null = True)
    address = models.CharField(max_length = 45, blank = True, null = True)
    locality = models.CharField(max_length = 45, blank = True, null = True)
    locality_verbose = models.CharField(max_length = 45, blank = True, null = True)
    longitude = models.CharField(max_length = 45, blank = True, null = True)
    latitude = models.CharField(max_length = 45, blank = True, null = True)
    
    class Meta:
        db_table = 'restaurant'
        
    
class RestaurantDetail(models.Model):
    restaurant = models.ForeignKey(Restaurant, db_column = 'restaurant_id', to_field = 'restaurant_id')
    restaurant_name = models.CharField(max_length = 45, blank = True, null = True)
    cuisines = models.CharField(max_length = 45, blank = True, null = True)
    average_cost_for_two = models.CharField(max_length = 45, blank = True,null = True)
    currency = models.CharField(max_length = 45, blank = True, null = True)
    has_table_booking = models.CharField(max_length = 45, blank = True, null = True)
    has_online_delivery = models.CharField(max_length = 45, blank = True, null = True)
    aggregate_rating = models.CharField(max_length = 45, blank = True, null = True)
    rating_color = models.CharField(max_length = 45, blank = True, null = True)
    rating_text = models.CharField(max_length = 45, blank = True, null = True)
    votes = models.CharField(max_length = 45, blank = True,null = True)
    
    class Meta:
        db_table = 'restaurant_detail'      