from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Tag, Location, Photo
from rango.forms import TagForm, PhotoForm

def base (request):
    tag_list = Tag.objects.order_by('-likes')[:5]    
    context_dict = {'tags': tag_list}
    return render(request, 'rango/index.html', context=context_dict)

def index (request):
    tag_list = Tag.objects.order_by('-likes')[:5]
    for tag in tag_list:
        photos = Photo.objects.filter(tag=tag)
        photo_list = photos.order_by('-views')[:3]  
        # photo_list = Photo.objects.order_by('-views')[:3]  
        context_dict = {'tags': tag_list, 'photos' : photo_list}
    return render(request, 'rango/index.html', context=context_dict)

def show_tag(request, tag_name_slug):
    context_dict = {}
    try:
        tag = Tag.objects.get(slug=tag_name_slug)
        # photos = Photo.objects.filter(tag=tag)
        photos = Photo.objects.all()
        context_dict['photos'] = photos
        context_dict['tag'] = tag
    except Tag.DoesNotExist:
        context_dict['photos'] = None
        context_dict['tag'] = None
    return render(request, 'rango/tag.html', context_dict)

def add_tag(request):
    form = TagForm()
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'rango/add_tag.html', {'form': form})

def add_photo(request, tag_name_slug):
    try:
        tag = Tag.objects.get(slug=tag_name_slug)
    except Tag.DoesNotExist:
        tag = None
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            # if tag:
            photo = form.save(commit=False)
            photo.tag = tag
            photo.views = 0
            photo.save()
            return show_tag(request, tag_name_slug)
    else:
        print(form.errors)
    context_dict = {'form':form, 'tag':tag}
    return render(request, 'rango/add_photo.html', context_dict)

def view_photos(request):
    photo_list = Photo.objects.all() 
    context_dict = {'photos' : photo_list}
    return render(request, 'rango/view_photos.html', context=context_dict)

def search(request):
    return render(request, 'rango/search.html',)

# def about (request):
#     # return HttpResponse('None of your beeswax! <a href = "http://127.0.0.1:8000/rango/">main</a>')
#         return render(request, 'rango/about.html')
