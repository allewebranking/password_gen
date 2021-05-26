from django.shortcuts import render, get_object_or_404
from .models import paragr
# Create your views here.

def all_blogs(request):
    
    paragraphs= paragr.objects.all()[:5]

    return render(request, 'blog/all_blogs.html',{'paragraphs':paragraphs})

def detail(request,blog_id):
    blog = get_object_or_404(paragr, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})
