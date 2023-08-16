#اصلی
 
from django.contrib import admin
from django.urls import path,include
from news_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('news/',include("news_app.urls"))
]
