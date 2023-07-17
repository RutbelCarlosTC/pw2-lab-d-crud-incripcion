from django.urls import re_path as url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
]
urlpatterns += [
    path('enrolls/',views.EnrollListView.as_view(), name='enrolls'),
]

urlpatterns+=[
    path('enroll/create/',views.EnrollCreate.as_view(), name="enroll-create"),
    path('enroll/<int:pk>/update/',views.EnrollUpdate.as_view(), name="enroll-update"),
    path('enroll/<int:pk>/delete/',views.EnrollDelete.as_view(),name="enroll-delete"),
]