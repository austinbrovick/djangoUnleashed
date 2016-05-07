from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .forms import PostForm

from .models import Post

class PostList(View):
    template_name = 'blog/post_list.html'
    def get(self, request, template_name=None): # get refers to the Http method used to access it
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return render(request, self.template_name, {'post_list':Post.objects.all()})

# def post_list(request):
#     return render(request, 'blog/post_list.html', {'post_list':Post.objects.all()})


def post_detail(request, year, month, slug, parent_template=None):
    post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
    return render(request, 'blog/post_detail.html', {'post':post, 'parent_template':parent_template}),

class PostCreate(View):
    form_class = PostForm # not invoked
    template_name = 'blog/post_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form':self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            return render(request, self.template_name, {'form': bound_form})

class PostUpdate(View):
    form_class = PostForm
    model = Post
    template_name = 'blog/post_form_update.html'

    def get_object(self, year, month, slug):
        return get_object_or_404(self.model, pub_date__year=year, pub_date__month=month, slug=slug)

    def get(self, request, year, month, slug):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#######")
        post = self.get_object(year, month, slug)
        context = {'form':self.form_class(instance=post), 'post': post}
        return render(request, self.template_name, context)
        bound_form = self.form_class(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)

    def post(self, request, year, month, slug):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$#######")
        post = self.get_object(year, month, slug)

        bound_form = self.form_class(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {'form':bound_form, 'post':post}
            return render(request, self.template_name, context)

class PostDelete(View):
    def get(self, request, year, month, slug):
        post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
        return render(request, 'blog/post_confirm_delete.html', {'post':post}),

    def post(self, request, year, month, slug):
        post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug__iexact=slug)
        post.delete()
        return redirect('blog_post_list')
