from django import forms
from .models import Tag, Startup, NewsLink
from django.core.exceptions import ValidationError



class SlugCleanMixin:
    # mixin class for slug cleaning method
    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug man not be "create".')
        return new_slug


class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__' # fields = ['name', 'slug']

    def save(self):
        new_tag = Tag.objects.create(name=self.cleaned_data['name'], slug=self.cleaned_data['slug'])
        return new_tag

    def clean_name(self):
        return self.cleaned_data['name'].lower()

class NewsLinkForm(forms.ModelForm):
    class Meta:
        model = NewsLink
        fields = '__all__'

class StartupForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'





    # name = forms.CharField(max_length=31)
    # slug = forms.SlugField(max_length=31, help_text='A label for URL config')



# model fields vs form fields
# both
    # may represent their data in HTML output
    # associated with a python type
# a model field knows how to represent data in a database whereas form fields do not
# a form field is associated with a Django widget which is nothing more than an HTML field element

