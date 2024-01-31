
from django.contrib import admin
from django.urls import path, re_path, include
from firstapp import views
from firstapp import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('trips/', views.cruisetrips_list),
    re_path(r'^api/firstapp/([0-9])$', views.cruisetrip_detail),
]