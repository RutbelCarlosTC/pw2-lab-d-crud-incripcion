from django.urls import re_path as url
from . import views
from django.urls import path

urlpatterns = [
    #path('enrolls/',views.CategoriaListView.as_view(), name='enrolls'),
]

urlpatterns+=[
    #path('categoria/create/',views.CategoriaCreate.as_view(), name="categoria-create"),
    #path('categoria/<int:pk>/update/',views.CategoriaUpdate.as_view(), name="categoria-update"),
    #path('categoria/<int:pk>/delete/',views.CategoriaDelete.as_view(),name="categoria-delete"),
]