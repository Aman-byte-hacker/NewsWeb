from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndiaNews,name="IndiaNews"),
    path('tech/',views.tech,name="tech"),
    path('tech',views.tech,name="tech"),
    path('entertainment/',views.entertainment,name="entertainment"),
    path('sports/',views.sport,name="sport"),
    path('science/',views.science,name="science"),
    path('health/',views.health,name="health")

    
]
