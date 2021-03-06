from django.db import models
from django.template.defaultfilters import slugify

class Tag(models.Model):
    name = models.CharField(max_length=128, unique = True)
    # views = models.IntegerField(default = 0)
    # likes = models.IntegerField(default = 0)
    slug = models.SlugField(unique=True, blank = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Location(models.Model):
    title = models.CharField(max_length=128, blank = True)

class Photo(models.Model):
    # location = models.ForeignKey(Location, blank = True)
    # tag = models.ManyToManyField(Tag)
    tag = models.ForeignKey(Tag)
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to = 'Stinagram/%Y/%m/%d')
    # views = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def search(cls, query):
        photo = cls.objects.filter(location__title__icontains=query)
        return photo