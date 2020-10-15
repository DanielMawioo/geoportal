from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.data, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shamba/update-payment/',views.update_payment, name='payment'),
    path('data/', views.data, name='data'),
    path('registershamba/', views.registershamba, name='registershamba'),
    path('discardshamba/', views.discardshamba, name='discardshamba'),
    path('changeowner/', views.changeowner, name='changeowner'),
    path('statistics/', views.statistics, name='statistics'),
]
