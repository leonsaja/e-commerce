from django.urls import path
from produto.views import produto_view

app_name = "produto"

urlpatterns = [
    path("", produto_view.ProdutoListView.as_view(), name="list"),
    path("<slug:slug>/", produto_view.ProdutoDetailView.as_view(), name="detail"),
    path("categoria/<slug:slug>/",
         produto_view.ProdutoListView.as_view(), name="lista_categoria"),
]
