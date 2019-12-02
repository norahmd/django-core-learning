from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import PostModel
from .forms import PostModelForm
from django.contrib import messages
# Create your views here.

# CRUD

def post_model_create_view(request):
    # if request.method == "POST":
    #     print(request.POST)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)
    form = PostModelForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Created a new blog post!")
        context = {
        "form": PostModelForm()
        }
        # return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
   
    template = "blog/create-view.html"
    return render(request, template, context)

def post_model_update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    context = {
        "object": obj,
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, "Update blog post!")
        return HttpResponseRedirect("/blog/{num}".format(num=obj.id))
   
    template = "blog/update-view.html"
    return render(request, template, context)


def post_model_detail_view(request, id=None):
    print("norah hello there")
    obj = get_object_or_404(PostModel, id=id)
    context ={
        "object": obj,
    }
    template = "blog/detail-view.html"
    return render(request, template, context)


def post_model_list_view(request):
    qs = PostModel.objects.all()
    print("hi there")
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