from django.urls import path

from . import views


app_name = 'quotes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:quote_id>/like/', views.like, name='like'),
    path('random/', views.rand_quote, name='random')
]
