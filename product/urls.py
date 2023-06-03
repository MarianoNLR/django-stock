from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    #path('/filterSearch', views.filteredSearch, name="filtered_search")   
]