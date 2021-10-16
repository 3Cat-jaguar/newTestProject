from django.db import models


class api_table(models.Model):
    category = models.CharField(max_length=30, default='100')
    item_name = models.CharField(max_length=30)
    kind_name = models.CharField(max_length=30)
    rank = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    today_price = models.CharField(max_length=30)
    average_price = models.CharField(max_length=30)
