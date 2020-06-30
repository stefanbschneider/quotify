from django.urls import path

from . import views


app_name = 'quotes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # show quote
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # functions: like, random quote
    path('<int:quote_id>/like/', views.like, name='like'),
    path('random/', views.rand_quote, name='random'),
    # create, update, delete
    path('add/', views.QuoteCreate.as_view(), name='add'),
    path('<int:pk>/edit/', views.QuoteUpdate.as_view(), name='edit'),
    path('<int:pk>/delete/', views.QuoteDelete.as_view(), name='delete'),
]
