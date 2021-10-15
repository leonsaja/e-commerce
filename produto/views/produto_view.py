from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from produto.models import Categoria, Produto


class ProdutoDetailView(DetailView):
    queryset = Produto.disponivel.all()


class ProdutoListView(ListView):
    categoria = None
    paginate_by = 6

    def get_queryset(self):
        queryset = Produto.disponivel.all()
        categoria_slug = self.kwargs.get("slug")
        if categoria_slug:
            self.categoria = get_object_or_404(Categoria, slug=categoria_slug)

            queryset = queryset.filter(categoria=self.categoria)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produto_list'] = self.get_queryset()
        context["categoria"] = self.categoria
        context["categorias"] = Categoria.objects.all()
        return context
