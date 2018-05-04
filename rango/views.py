from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Tag, Location, Photo

def index (request):
    tag_list = Tag.objects.order_by('-likes')[:5]    
    context_dict = {'tags': tag_list}
    return render(request, 'rango/index.html', context=context_dict)

def rango (request):
    return HttpResponse('RRRRRRRRRRANGO!, <a href = "http://127.0.0.1:8000/rango/about/">about</a>')

def about (request):
    # return HttpResponse('None of your beeswax! <a href = "http://127.0.0.1:8000/rango/">main</a>')
        return render(request, 'rango/about.html')

def show_tag(request, tag_name_slug):
    context_dict = {}
    try:
        tag = Tag.objects.get(slug=tag_name_slug)
        photos = Photo.objects.filter(tag=tag)
        context_dict['photos'] = photos
        context_dict['tag'] = tag
    except Tag.DoesNotExist:
        context_dict['photos'] = None
        context_dict['tag'] = None

    return render(request, 'rango/tag.html', context_dict)