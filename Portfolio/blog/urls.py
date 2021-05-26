from django.urls import path
from . import  views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
app_name = 'blog'
urlpatterns = [

    path('', views.all_blogs,name="all_blogs"),
    path('admin/', admin.site.urls),
    path('<int:blog_id>/', views.detail,name="detail"),
]
