from django.urls import path
from .views import IndexView, CategoryView

app_name = 'main' #=> main:index
urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Bosh sahifa uchun
    path('<str:category_name>/category', CategoryView.as_view(), name='category'),  # Kategoriya sahifasi uchun
]