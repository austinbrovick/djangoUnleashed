from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from organizer.models import Startup, Tag  # importing tables

class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63,
                            help_text='A label for URL config',
                            unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField('date_published',
                                auto_now_add=True) # field will automatically be set to the date when this instance is intially created
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')


    def __str__(self):
        return "{} on {}".format(self.title, self.pub_date.strftime('%Y-%m-%d'))


    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'


    def get_absolute_url(self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return reverse('blog_post_detail', kwargs={'year':self.pub_date.year, 'month': self.pub_date.month, 'slug': self.slug})

# posts have many tags, tags can be on many posts
# there can be many posts about startups and one post can be about many startups

# given a post instance p, the tags associated with this post are accessible via p.tags, as defined by the preceding model. However, given a tag instance t, we had not explicitly defined a variable to access Post objects. Thanks to the related_name option, we may now access the list of blog posts related to the tag t via the blog_posts attribute, as in t.blog_posts.
#         if we do not set it, Django atomatically creates the other side of the relation for us. In the case of the Tag model, Django would have createda post_set attribute, allwoing access via t.post_set in our example.

