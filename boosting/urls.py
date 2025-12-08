from django.urls import path
from .views import Acceuil
urlpatterns = [
    path('',Acceuil.as_view(),name="acceuil")
]