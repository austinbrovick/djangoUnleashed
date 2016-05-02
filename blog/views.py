from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Post

class PostList(View):
    template_name = 'blog/post_list.html'
    def get(self, request, template_name=None): # get refers to the Http method used to access it
        return render(request, self.template_name, {'post_list':Post.objects.all()})

# def post_list(request):
#     return render(request, 'blog/post_list.html', {'post_list':Post.objects.all()})


def post_detail(request, year, month, slug, parent_template=None):
    post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
    return render(request, 'blog/post_detail.html', {'post':post, 'parent_template':parent_template}),
