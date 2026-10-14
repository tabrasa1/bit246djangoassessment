from django.urls import path
from . import views
from .views import CategoryListView

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", CategoryListView.as_view(), name="categories"),
]