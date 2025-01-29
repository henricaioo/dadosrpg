from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=20, verbose_name="Nome da pessoa")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Personagem(models.Model):
    nome = models.CharField(max_length=20, verbose_name="Nome do personagem")
    aparencia = models.TextField(verbose_name="Aparência do personagem")
    historia = models.TextField(verbose_name="História do personagem")
    vida = models.CharField(max_length=20, verbose_name="Vida do personagem")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Dono do personagem")
    def __str__(self):
        return f"{self.nome}, {self.pessoa}"
    class Meta:
        verbose_name = "Personagem"
        verbose_name_plural = "Personagens"

class Campanha(models.Model):
    nome = models.CharField(max_length=20, verbose_name="Nome da campanha")
    descricao = models.TextField(verbose_name="História/descrição da campanha")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Dono da camapanha")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Campanha"
        verbose_name_plural = "Campanhas"

class PersonagemCampanha(models.Model):
    personagem = models.ForeignKey(Personagem,on_delete=models.CASCADE, verbose_name="Personagem na camapanha")
    campanha = models.ForeignKey(Campanha,on_delete=models.CASCADE, verbose_name="Campanha")
    def __str__(self):
        return f"{self.personagem}"
    
class Item(models.Model):
    nome = models.CharField(max_length=20, verbose_name="Nome do item")
    descricao = models.TextField(verbose_name="Descrição do item")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

class Pericia(models.Model):
    nome = models.CharField(max_length=20, verbose_name="Nome da perícia")
    descricao = models.TextField(verbose_name="Descrição da perícia")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Perícia"
        verbose_name_plural = "Perícias"

class Atributo(models.Model):
    nome = models.CharField(max_length=20, verbose_name="Nome do atributo")
    abreviacao = models.CharField(max_length=3, verbose_name="Abreviação do atributo")
    descricao = models.TextField(verbose_name="Descrição do atributo")
    def __str__(self):
        return f"{self.nome}"
    class Meta:
        verbose_name = "Atributo"
        verbose_name_plural = "Atributos"

class PersonagemItem(models.Model):
    personagem = models.ForeignKey(Personagem,on_delete=models.CASCADE, verbose_name="Personagem que possui o item")
    item = models.ForeignKey(Item,on_delete=models.CASCADE, verbose_name="Item")
    qtde = models.IntegerField(verbose_name = "Quantidade")
    durabilidade = models.CharField(max_length = 20, verbose_name = "Quantidade")
    def __str__(self):
        return f"{self.personagem}"
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

class PersonagemPericia(models.Model):
    personagem = models.ForeignKey(Personagem,on_delete=models.CASCADE, verbose_name="Personagem que possui a preícia")
    pericia = models.ForeignKey(Pericia,on_delete=models.CASCADE, verbose_name="Perícia")
    valor = models.IntegerField(verbose_name = "Valor")
    def __str__(self):
        return f"{self.personagem}"
    class Meta:
        verbose_name = "Perícia"
        verbose_name_plural = "Perícias"

class PersonagemAtributo(models.Model):
    personagem = models.ForeignKey(Personagem,on_delete=models.CASCADE, verbose_name="Personagem que possui a preícia")
    atributo = models.ForeignKey(Atributo,on_delete=models.CASCADE, verbose_name="Atributo")
    valor = models.IntegerField(verbose_name = "Valor")
    def __str__(self):
        return f"{self.personagem}"
    class Meta:
        verbose_name = "Atributo"
        verbose_name_plural = "Atributos"