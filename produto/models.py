from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from pages.models import DataCriacao
from produto.managers import DisponivelProdutoManager


class Categoria(DataCriacao):
    nome = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False,
                         populate_from="nome")

    class Meta:
        ordering = ("nome",)
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("produto:lista_categoria", kwargs={"slug": self.slug})


class Produto(DataCriacao):
    categoria = models.ForeignKey(
        Categoria, related_name="produtos_categoria", on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=255, blank=False, null=False)
    slug = AutoSlugField(unique=True, always_update=False,
                         populate_from="nome")
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    descricao = models.TextField(blank=False, null=False)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False)
    is_disponivel = models.BooleanField(default=True)

    objects = models.Manager()
    disponivel = DisponivelProdutoManager()

    class Meta:
        ordering = ("nome",)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse("produto:detail", kwargs={"slug": self.slug})
