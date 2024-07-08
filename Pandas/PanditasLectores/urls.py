from django.urls import path
from . import views

urlpatterns = [
    path('registro_grupo/', views.registro_grupo, name='registro_grupo'),
    path('lista_grupo/', views.registro_grupo, name='lista_grupo'),
]