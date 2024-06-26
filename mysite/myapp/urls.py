from django.urls import path
from myapp.views import BuscketDeleteView, OrderListView, create_charge,TourListView, TourDetailView, PrivateTourListView, GroupTourListView, BuscketCreateView 
from myapp.views import GroupTourCzechListView, GroupTourEuropeListView,PrivateTourCzechListView, PrivateTourEuropeListView
from myapp.views import ServicesView, AboutView, BuscketListView, ContactsView, payment

app_name= 'myapp'

urlpatterns = [
    path('home/', TourListView.as_view(), name='home'),
    path('tours/', TourListView.as_view(), name='tours'),
    path('services/', ServicesView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('private_tour_list/', PrivateTourListView.as_view(), name='private_tour_list'),
    path('private_tour_czech/', PrivateTourCzechListView.as_view(), name='private_tour_czech'),
    path('private_tour_europe/', PrivateTourEuropeListView.as_view(), name='private_tour_europe'),
    path('group_tour_list/', GroupTourListView.as_view(), name='group_tour_list'),
    path('group_tour_czech/', GroupTourCzechListView.as_view(), name='group_tour_czech'),
    path('group_tour_europe/', GroupTourEuropeListView.as_view(), name='group_tour_europe'),
    path('detail/<int:pk>/', TourDetailView.as_view(), name='detail'),
    path('buscket_create/<int:tour_pk>/', BuscketCreateView.as_view(), name='buscket_create'),
    path('buscket/', BuscketListView.as_view(), name='buscket'),
    path('buscket-delete/<int:pk>/', BuscketDeleteView.as_view(), name='buscket-delete'),
    path('create-charge/', create_charge, name='create-charge'),
    path('checkout_session/', payment, name='checkout'),
    path('profile/', OrderListView.as_view(), name='profile'),

]

