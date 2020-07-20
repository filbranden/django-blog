from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Post

def index(request):
    context = {
        'posts': Post.objects.all(),
    }
    template = loader.get_template("blog/index.html")
    return HttpResponse(template.render(context, request))
