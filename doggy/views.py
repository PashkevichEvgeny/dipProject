from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Animal

template_name = 'doggy/index.html'


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        template_name=template_name,
    )


class AnimalListView(ListView):
    template_name = template_name
    queryset = Animal.objects.all()


class AnimalDetailView(DetailView):
    model = Animal
