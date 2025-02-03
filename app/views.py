from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass

class ItensView(View):
    def get(self, request, *args, **kwargs):
        itens = Item.objects.all()
        return render(request, 'itens.html', {'itens' : itens})
    def post(self, request):
        pass

class AtributosView(View):
    def get(self, request, *args, **kwargs):
        atributos = Atributo.objects.all()
        return render(request, 'atributos.html', {'atributos' : atributos})
    def post(self, request):
        pass

class PericiasView(View):
    def get(self, request, *args, **kwargs):
        pericias = Pericia.objects.all()
        return render(request, 'pericias.html', {'pericias' : pericias})
    def post(self, request):
        pass

class PessoasView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoas.html', {'pessoas' : pessoas})
    def post(self, request):
        pass

class CampanhasView(View):
    def get(self, request, *args, **kwargs):
        campanhas = Campanha.objects.all()
        return render(request, 'campanhas.html', {'campanhas' : campanhas})
    def post(self, request):
        pass

class PersonagensView(View):
    def get(self, request, *args, **kwargs):
        personagens = Personagem.objects.all()
        return render(request, 'personagens.html', {'personagens' : personagens})
    def post(self, request):
        pass