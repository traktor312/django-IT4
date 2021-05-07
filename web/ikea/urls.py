from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nabytek', views.MyListView.as_view(), name='list'),
    path('nabytek/<int:pk>', views.MyDetailView.as_view(), name='detail'),
    path('nabytek/create', views.MyCreate.as_view(), name='my-create'),
    path('nabytek/<int:pk>/update', views.MyUpdate.as_view(), name='my-update'),
    path('nabytek/<int:pk>/delete', views.MyDelete.as_view(), name='my-delete'),
]