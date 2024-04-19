
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView, CreateView
from myapp.models import Tour, Buscket
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
    model = Buscket
    template_name = 'buscket_create.html'
    form_class = BuscketCreateForm
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('myapp:buscket')

    def form_valid(self, form):
        tour_instance = Tour.objects.get(pk=self.kwargs['tour_pk'])
        form.instance.tour = tour_instance
        form.instance.buyer = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        tour_instance = Tour.objects.get(pk=self.kwargs['tour_pk'])
        max_quantity = tour_instance.place_quantity
        beginning = tour_instance.beginning
        kwargs['max_quantity'] = max_quantity
        kwargs['beginning'] = beginning
        return kwargs

    def get_context_data(self, **kwargs):
        context={}
        context = super().get_context_data(**kwargs)
        tour = Tour.objects.get(pk=self.kwargs['tour_pk'])      
        available_places = tour.available_places()
        context['available_places'] = available_places 
        context['form'] = self.get_form() 
        context['tour_name'] = tour.name
        context['tour_type'] = tour.tour_type
        context['tour_pk'] = tour.pk
        return context
    

class BuscketListView(ListView):
    model = Buscket
    template_name = 'buscket.html'
    context_object_name = "buscket"

    def get_queryset(self):
        user = self.request.user
        queryset = Buscket.objects.filter(buyer=user)
        return queryset
    



class BuscketDeleteView(View):

    def get(self,request, pk):
        obj = Buscket.objects.get(pk=pk)
        obj.delete()
        return redirect('myapp:buscket')

