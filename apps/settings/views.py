from django.shortcuts import render
from apps.settings.models import Settings
# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    return render(request, "index.html", locals())

def about(request):
    return render(request, "about.html", locals())

def team(request):
    return render(request, "team.html", locals())

def gallery(request):
    return render(request, "gallery.html", locals())

def news(request):
    return render(request, "news.html", locals())

def post(request):
    return render(request, "post.html", locals())

def contact(request):
    return render(request, "contact.html", locals())
