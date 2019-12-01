from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel
# Create your views here.

# CRUD

def post_model_list_view(request):
    qs = PostModel.objects.all()
    print(qs)
    template = "blog/list-view.html"
    context ={
        "object_list": qs
    }
    return render(request, template, context)