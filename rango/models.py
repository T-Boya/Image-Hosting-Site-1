from django.db import models
from django.template.defaultfilters import slugify

class Tag(models.Model):
    name = models.CharField(max_length=128, unique = True)
    views = models.IntegerField(default = 0)
    likes = models.IntegerField(default = 0)
    slug = models.SlugField(unique=True, blank = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Location(models.Model):
    title = models.CharField(max_length=128, unique = True)

class Photo(models.Model):
    # tag = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    location = models.CharField(max_length=128)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title