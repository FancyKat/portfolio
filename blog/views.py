from django.shortcuts import render
from . models import Post


def home(request):
    data = Post.objects.all()
    return render(request, "index.html", {})


def single(request, slug):
    data = Post.objects.get(slug=slug)
    return render(request, "single.html", {})


def aboutus(request):
    return render(request, "aboutus.html", {})


def chart(request):
    return render(request, "chart.html", {})


def form(request):
    return render(request, "form.html", {})


def error(request):
    return render(request, "error.html", {})
