from django.contrib.auth.decorators import login_required 
from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel
# Create your views here.

# CRUD
def post_model_list_view(request):
    qs = PostModel.objects.all()
    context ={
    "object_list": qs
    }
    template = "blog/list-view.html"

    return render(request, template, context)


@login_required(login_url='/login/')
def login_required_view(request):
    print(request.user)
    qs = PostModel.objects.all()
    context ={
    "object_list": qs
    }

    if request.user.is_authenticated:
        template = "blog/list-view.html"
    else:
        template = "blog/list-view-public.html"

    return render(request, template, context)