from django.contrib import admin
from django.urls import include,path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('itens/', ItensView.as_view(), name='itens'),
    path('atributos/', AtributosView.as_view(), name='atributos'),
    path('pericias/', PericiasView.as_view(), name='pericias'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
    path('campanhas/', CampanhasView.as_view(), name='campanhas'),
    path('personagens/', PersonagensView.as_view(), name='personagens'),
]
