from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[ 
    re_path('^$', views.images, name = 'Images'),
     re_path('^$', views.news_of_day, name = 'newsToday'),
]

if settings.DEBUG:
     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)