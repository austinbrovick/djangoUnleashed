from django.shortcuts import render
from django.http.response import HttpResponse

from .models import Tag

def homepage(request):
    tag = Tag.objects.all()[0]
    # tag_list = Tag.objects.all()
    # output = "$".join([tag.name for tag in tag_list])
    # return HttpResponse(output)
    return render(request, 'organizer/tag_detail.html', {"tag" : tag})