from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    Projects = Project.objects.all()
    return render(request, 'portfolio/home.html',{'Projects':Projects})
def all_blogs(request):
    return render(request,'blog/all_blogs.html')
