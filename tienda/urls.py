from django.urls import path
from .views import ProductoListView, ProductoCreateView,ProductoDeleteView, ProductoUpdateView,CategoriaListView, CategoriaCreateView, CategoriaDeleteView

urlpatterns=[
    # <---------------urls de producto------------>
    path('', ProductoListView, name='producto-list'),
    path('producto/create/', ProductoCreateView, name='producto-create'),
    path('producto/delete/<int:id>', ProductoDeleteView, name='producto-delete'),
    path('producto/update/<int:id>', ProductoUpdateView, name='producto-update'),
    # <---------------urls de categoria------------>
    path('categoria/', CategoriaListView, name='categoria-list'),
    path('categoria/create/', CategoriaCreateView, name='categoria-create'),
    path('categoria/delete/<int:id>', CategoriaDeleteView, name='categoria-delete'),
]