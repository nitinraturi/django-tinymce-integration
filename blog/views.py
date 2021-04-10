from django.shortcuts import render
from .models import *


# Create your views here.
def posts(request):
    context = {
        "articles": Blog.objects.all()
    }
    return render(request, 'home.html', context)


def post_detail(request, pk):
    article = Blog.objects.get(id=pk)
    return render(request, 'detail.html', {"article": article})
