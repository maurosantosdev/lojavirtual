# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product, Category
from watson import search as watson
from django.views.decorators.cache import cache_page


class ProductListView(generic.ListView):

    template_name = 'catalog/product_list.html'
    paginate_by = 3

    # Pesquisando no formulario de pesquisa (Filtrando pelo título do Produto | pelo nome da Categoria | pela descrição do produto

    def get_queryset(self):
        queryset = Product.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = watson.filter(queryset, q)
        return queryset


product_list = ProductListView.as_view()


class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


category = CategoryListView.as_view()

# Cache de 60 segundos na pagina de produtos
@cache_page(60)
def product(request, slug):
    product = Product.objects.get(slug=slug)

    context = {
        'product': product,
    }
    return render(request, 'catalog/product.html', context)
