from django.shortcuts import render
from .models import post_table


def mainpage(request):
    posts = post_table.objects.all()
    return render(request, 'index.html', {'post':posts})
