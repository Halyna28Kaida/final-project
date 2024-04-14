from django.urls import path
from myapp.views import TourListView, TourDetailView, PrivateTourListView, GroupTourListView, BuscketCreateView
from myapp.views import GroupTourCzechListView, GroupTourEuropeListView,PrivateTourCzechListView, PrivateTourEuropeListView
from myapp.views import ServicesView, AboutView, BuscketListView

app_name= 'myapp'

urlpatterns = [
    path('home/', TourListView.as_view(), name='home'),
    path('tours/', TourListView.as_view(), name='tours'),
    path('services/', ServicesView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
    path('private_tour_list/', PrivateTourListView.as_view(), name='private_tour_list'),
    path('private_tour_czech/', PrivateTourCzechListView.as_view(), name='private_tour_czech'),
    path('private_tour_europe/', PrivateTourEuropeListView.as_view(), name='private_tour_europe'),
    path('group_tour_list/', GroupTourListView.as_view(), name='group_tour_list'),
    path('group_tour_czech/', GroupTourCzechListView.as_view(), name='group_tour_czech'),
    path('group_tour_europe/', GroupTourEuropeListView.as_view(), name='group_tour_europe'),
    path('detail/<int:pk>/', TourDetailView.as_view(), name='detail'),
    path('buscket_create/<int:pk>/', BuscketCreateView.as_view(), name='buscket_create'),
    path('buscket/', BuscketListView.as_view(), name='buscket'),
]

