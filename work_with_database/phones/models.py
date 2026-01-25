# -*- coding: utf-8 -*-
from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()