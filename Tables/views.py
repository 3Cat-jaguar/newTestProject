from django.shortcuts import render
from .models import post_table


def mainpage(request):
    posts = post_table.objects.get(id=1)
    return render(request, 'index.html', {'post':posts})
