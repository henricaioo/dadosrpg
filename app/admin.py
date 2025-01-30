from .models import *
from django.contrib import admin

class PersonagemInline(admin.TabularInline):
    model = Personagem
    extra = 1 # Número de livros adicionais para adicionar no admin

class PessoasAdmin(admin.ModelAdmin):
    list_display = ('nome',)# Campos que serão exibidos na listagem
    search_fields = ('nome',)# Campos que serão pesquisados
    inlines = [PersonagemInline]# Adiciona a tabela de livros no admin de gêneros



class AtributoInline(admin.TabularInline):
    model = PersonagemAtributo
    extra = 1 # Número de livros adicionais para adicionar no admin

class PericiaInline(admin.TabularInline):
    model = PersonagemPericia
    extra = 1 # Número de livros adicionais para adicionar no admin

class ItemInline(admin.TabularInline):
    model = PersonagemItem
    extra = 1 # Número de livros adicionais para adicionar no admin

class PersonagemAdmin(admin.ModelAdmin):
    list_display = ('nome',)# Campos que serão exibidos na listagem
    search_fields = ('nome',)# Campos que serão pesquisados
    inlines = [AtributoInline, PericiaInline, ItemInline ]# Adiciona a tabela de livros no admin de gêneros

class CampanhaInline(admin.TabularInline):
    model = PersonagemCampanha
    extra = 1 # Número de livros adicionais para adicionar no admin

class CampanhaAdmin(admin.ModelAdmin):
    list_display = ('nome',)# Campos que serão exibidos na listagem
    search_fields = ('nome',)# Campos que serão pesquisados
    inlines = [CampanhaInline]# Adiciona a tabela de livros no admin de gêneros

admin.site.register(Pessoa, PessoasAdmin)
admin.site.register(Personagem, PersonagemAdmin)
admin.site.register(Campanha, CampanhaAdmin)
admin.site.register(PersonagemCampanha)
admin.site.register(Item)
admin.site.register(Pericia)
admin.site.register(Atributo)
admin.site.register(PersonagemAtributo)
admin.site.register(PersonagemPericia)
admin.site.register(PersonagemItem)
