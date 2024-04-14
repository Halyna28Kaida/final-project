from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, CreateView
from myapp.models import Order, Tour, Buscket
from myapp.utils import GetTourTypeMixin
from myapp.forms import BuscketCreateForm




class TourListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'home.html'
    paginate_by = 3


class ServicesView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'services.html'


class AboutView(TemplateView):
    model = Tour
    template_name = 'about.html'



class PrivateTourListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'private_tour_list.html'


class PrivateTourCzechListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'private_tour_czech.html'


class PrivateTourEuropeListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'private_tour_europe.html'


class GroupTourListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'group_tour_list.html'


class GroupTourEuropeListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'group_tour_europe.html'


class GroupTourCzechListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'group_tour_czech.html'    

class TourDetailView(DetailView):
    model = Tour
    template_name = 'detail.html'
    context_object_name = 'obj'

    
class BuscketCreateView(GetTourTypeMixin, CreateView):
    # model = Tour
    template_name = 'buscket_create.html'
    form_class = BuscketCreateForm
    success_url = reverse_lazy('myapp:home')
    context_object_name = 'obj'

    def get_queryset(self):
        user = self.request.user
        queryset = Buscket.objects.filter(buyer=user)
        return queryset

    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.buyer = self.request.user
        tour_pk = self.kwargs['pk']
        tour_instance = get_object_or_404(Tour, pk=tour_pk)
        obj.tour = tour_instance

        obj.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        tour_instance = Tour.objects.get(pk=self.kwargs['pk'])
        max_quantity = tour_instance.place_quantity
        beginning = tour_instance.beginning
        kwargs['max_quantity'] = max_quantity
        kwargs['beginning'] = beginning
 

        return kwargs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tour = Tour.objects.get(pk=self.kwargs['pk'])
        available_places = tour.available_places()
        context['available_places'] = available_places 
        context['form'] = self.get_form() 
        # tour_instance = tour
        tour_name = tour.name
        tour_type = tour.tour_type
        context['tour_type'] = tour_type
        context['tour_name'] = tour_name 

        return context
    


class BuscketListView(ListView):
    model = Buscket
    template_name = 'buscket.html'

    def get_queryset(self):
        buyer = self.request.user
        queryset = Buscket.objects.filter(buyer=buyer)
        return queryset

    
