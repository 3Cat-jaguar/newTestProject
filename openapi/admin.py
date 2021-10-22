from django.contrib import admin
from .models import api_table


@admin.register(api_table)
class ApiTableAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'item_name',
        'kind_name',
        'rank',
        'unit',
        'date',
        'today_price',
        'average_price',
<<<<<<< HEAD
        'created_at',
=======
>>>>>>> c7f241e13ed46a372b85f4ccc6086d82f4459977
    )

