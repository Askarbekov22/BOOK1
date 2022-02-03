from django.shortcuts import render
from django.views.generic import CreateView, ListView
from . import models, forms


class ProductListView(ListView):
    template_name = 'product/list.html'

    def get_queryset(self):
        return super().get_queryset()


class OrderCreateView(CreateView):
    template_name = 'product/order.html'
    form_class = forms.Ordercreate
    queryset = models.OrderCL.objects.all()
    success_url = '/product/'

    def form_valid(self, form):
        return super().form_valid(form=form)
