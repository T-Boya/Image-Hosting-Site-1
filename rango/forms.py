from django import forms
from django.forms import ModelForm
from rango.models import Tag, Photo

class TagForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
    help_text="Please enter a tag name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Tag
        fields = ('name',)

class PhotoForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the photo.")
    image = forms.FileField(label='Select an image file', help_text='Please select a photo to upload')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Photo
        exclude = ('tag',)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url
            return cleaned_data