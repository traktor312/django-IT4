from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ikea.models import Nabytek


def index(request):
    context = {
        'nadpis': 'Úvodní stránka IKEA',
        'obsah': ''
    }

    return render(request, template_name='index.html', context=context)


class MyListView(ListView):
    model = Nabytek
    context_object_name = 'nabytek_list'
    template_name = 'list.html'


class MyDetailView(DetailView):
    model = Nabytek
    context_object_name = 'nabytek'
    template_name = 'detail.html'


class MyCreate(CreateView):
    model = Nabytek
    fields = ['nazev', 'popis', 'cena', 'druh', 'foto']
    initial = {'cena': 500}


class MyUpdate(UpdateView):
    model = Nabytek
    fields = '__all__'


class MyDelete(DeleteView):
    model = Nabytek
    success_url = reverse_lazy('list')