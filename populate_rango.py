import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workspace.settings')
print("0 complete")
import django
print("1 complete")
django.setup()
print("2 complete")
from rango.models import Tag, Photo
print("3 complete")

def populate():
    python_photos = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/"} ]
    django_photos = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/"},
        {"title":"How to Tango with Django",
         "url":"http://www.tangowithdjango.com/"} ]
    other_photos = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask",
         "url":"http://flask.pocoo.org"} ]
    tags = {"Python": {"photos": python_photos},
            "Django": {"photos": django_photos},
            "Other Frameworks": {"photos": other_photos} }

    for tag, tag_data in tags.items():
        c=add_tag(tag)
        for p in tag_data["photos"]:
            add_photo(c, p['title'], p["url"])
    
    for c in Tag.objects.all():
        for p in Photos.objects.filter(Tag=c):
            print("- {0} - {1}".format(str(c), str(p)))
    
print("4 complete")

def add_photo(tag, title, url, views=0):
    p = Photo.objects.get_or_create(tag=tag, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

print("5 complete")
def add_tag(name):
    c = Tag.objects.get_or_create(name=name)[0]
    c.save()
    return c
print("6 complete")

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()