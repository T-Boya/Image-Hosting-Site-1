from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Tag, Location, Photo
from rango.forms import TagForm, PhotoForm
from django.forms.formsets import formset_factory

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
        # photos = Photo.objects.filter(tag=tag)
        photos = Photo.objects.all()
        context_dict['photos'] = photos
        context_dict['tag'] = tag
    except Tag.DoesNotExist:
        context_dict['photos'] = None
        context_dict['tag'] = None

    return render(request, 'rango/tag.html', context_dict)

# def add_tag(request):
#     form = TagForm()
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
#         else:
#             print(form.errors)
#     return render(request, 'rango/add_tag.html', {'form': form})

def add_photo(request):
    PhotoFormSet = formset_factory(PhotoForm, extra=0,
                                    min_num=1, validate_min=True)
    if request.method == 'POST':
        form = TagForm(request.POST)
        formset = PhotoFormSet(request.POST)
        if all([form.is_valid(), formset.is_valid()]):
            poll = form.save()
            for inline_form in formset:
                if inline_form.cleaned_data:
                    choice = inline_form.save(commit=False)
                    choice.question = poll
                    choice.save()
            return render(request, 'rango/index.html', {})
    else:
        form = TagForm()
        formset = PhotoFormSet()

    return render(request, 'rango/add_photo.html', {'form': form,
                                                   'formset': formset})