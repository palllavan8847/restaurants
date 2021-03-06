# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-04 15:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_id', models.CharField(blank=True, max_length=45, null=True, unique=True)),
                ('country_code', models.CharField(blank=True, max_length=45, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
                ('locality', models.CharField(blank=True, max_length=45, null=True)),
                ('locality_verbose', models.CharField(blank=True, max_length=45, null=True)),
                ('longitude', models.CharField(blank=True, max_length=45, null=True)),
                ('latitude', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'restaurant',
            },
        ),
        migrations.CreateModel(
            name='RestaurantDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(blank=True, max_length=45, null=True)),
                ('cuisines', models.CharField(blank=True, max_length=45, null=True)),
                ('average_cost_for_two', models.CharField(blank=True, max_length=45, null=True)),
                ('currency', models.CharField(blank=True, max_length=45, null=True)),
                ('has_table_booking', models.CharField(blank=True, max_length=45, null=True)),
                ('has_online_delivery', models.CharField(blank=True, max_length=45, null=True)),
                ('aggregate_rating', models.CharField(blank=True, max_length=45, null=True)),
                ('rating_color', models.CharField(blank=True, max_length=45, null=True)),
                ('rating_text', models.CharField(blank=True, max_length=45, null=True)),
                ('votes', models.CharField(blank=True, max_length=45, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant', to_field='restaurant_id')),
            ],
            options={
                'db_table': 'restaurant_detail',
            },
        ),
    ]
