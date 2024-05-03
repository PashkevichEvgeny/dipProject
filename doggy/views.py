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
    # paginate_by = 2
    template_name = template_name
    queryset = Animal.objects.order_by("-pk").all()


class AnimalDetailView(DetailView):
    model = Animal
