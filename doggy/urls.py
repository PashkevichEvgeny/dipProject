from django.urls import path

from . import views

app_name = 'doggy'


urlpatterns = [
    path("", views.AnimalListView.as_view(), name="index"),
    path("<int:pk>/", views.AnimalDetailView.as_view(), name="detail"),
]