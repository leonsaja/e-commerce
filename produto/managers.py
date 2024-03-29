from django.db import models


class DisponivelProdutoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_disponivel=True)
