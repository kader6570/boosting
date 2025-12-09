from django.urls import path
from .views import Acceuil
from django.views.generic import TemplateView
urlpatterns = [
    path('',Acceuil.as_view(),name="acceuil"),
    path('success',TemplateView.as_view(template_name='success.html')),
]