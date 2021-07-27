from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView

from .models import *

from django.db.models import F


class board_of_trustees(ListView):
    model = Sovet
    template_name = 'sovet/popsovet.html'
    context_object_name = 'postpops'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context

class get_one_board_of_trustees(DetailView):
    model = Sovet
    template_name = 'sovet/popdetails.html'
    context_object_name = 'postpop'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        sovet = Sovet.objects.get(slug=slug)
        chlen = Chelensoveta.objects.filter(sovet=sovet)
        context['chlen'] = chlen
        self.object.views = F('views') + 1
        self.object.save()
        # self.object.refresh_from_db()
        return context


