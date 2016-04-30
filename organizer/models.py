from __future__ import unicode_literals

from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=31,
                            unique=True) # no repeat names
    slug = models.SlugField(max_length=31,
                            unique=True, # no repeat slugs
                            help_text='A label for URL config.') # used when we autogenerate forms later on


    def __str__(self):
        return self.name.title()

    class Meta:
        ordering = ['name']

    # django will look for the Meta class in the Tag class and then search for known options, affecting the behavior of Tag instances or groups of Tag instances


class Startup(models.Model):
    name = models.CharField(max_length=31,
                            db_index=True)
    slug = models.SlugField(max_length=31,
                            unique=True,
                            help_text='A label for URL config')
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'



class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published') # the verbose_name parameter can be passed as the first unnamed argument
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup) # one startup can have many newslinks


    def __str__(self):
        return "{}:{}".format(self.startup, self.title)

    class Meta:
        verbose_name = 'news article' # rather than displaying as news link, django will display as news article
        # verbose_name_plural for specifications on plurals
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'


# default ordering is ['-order_date']
