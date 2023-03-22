from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('dashboard/', views.createSurvivor, name='dashboard'),
    path('customers/', views.updateUser, name='customers'),
    path('orders/', views.deleteSurvivor, name='orders'),
    path('login/', views.views, name='views'),
    path('transacoes/', views.transacoes, name='transacoes'),
    path('antecipacao/', views.antecipacao, name='antecipacao'),
    path('futurepay/', views.futurepay, name='futurepay'),
    path('profile/', views.profile, name='profile')

] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)