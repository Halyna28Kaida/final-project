
from django.http import HttpRequest, HttpResponseNotFound, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView, CreateView
from myapp.models import Order, Tour, Buscket
from myapp.utils import GetTourTypeMixin
from myapp.forms import BuscketCreateForm
from django.conf import settings
import stripe
from django.db.models import Sum



class TourListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'home.html'
    paginate_by = 3
    context_object_name = "buscket"
 
    

class ServicesView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'services.html'
    context_object_name = "buscket"
    


class AboutView(ListView):
    model = Tour
    template_name = 'about.html'
    context_object_name = "buscket"

class ContactsView(ListView):
    model = Tour
    template_name = 'contacts.html'
    context_object_name = "buscket"

class PrivateTourListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'private_tour_list.html'
    context_object_name = "buscket"


class PrivateTourCzechListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'private_tour_czech.html'
    context_object_name = "buscket"


class PrivateTourEuropeListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'private_tour_europe.html'
    context_object_name = "buscket"


class GroupTourListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'group_tour_list.html'
    context_object_name = "buscket"


class GroupTourEuropeListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'group_tour_europe.html'
    context_object_name = "buscket"


class GroupTourCzechListView(GetTourTypeMixin, ListView):
    model = Tour
    template_name = 'group_tour_czech.html' 
    context_object_name = "buscket"   

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
    context_object_name = "buscket"

    def form_valid(self, form):
        tour_instance = Tour.objects.get(pk=self.kwargs['tour_pk'])
        form.instance.tour = tour_instance
        form.instance.buyer = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        tour_instance = Tour.objects.get(pk=self.kwargs['tour_pk'])
        place_quantity = tour_instance.place_quantity
        beginning = tour_instance.beginning
        kwargs['place_quantity'] = place_quantity
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
    
    # def get_context_data(self, **kwargs): 
    #     context = super(BuscketListView, self).get_context_data(**kwargs)
    #     context["stripe_publishable_key"] = settings.STRIPE_PUBLISHABLE_KEY
    #     return context
    


class BuscketDeleteView(View):

    def get(self,request, pk):
        obj = Buscket.objects.get(pk=pk)
        obj.delete()
        return redirect('myapp:buscket')




stripe.api_key = settings.STRIPE_SECRET_KEY


def payment(request):
    context = {'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY}
    return render(request, 'checkout.html', context)


def create_charge(request):
    user = request.user 
    token = request.POST['stripeToken']

    try:
        total_summ = Buscket.objects.filter(buyer=user).total_summ()

        charge = stripe.Charge.create(
            amount=int(total_summ * 100),
            currency='eur',
            description='Example charge',
            source=token,
        )

    
        tours = Tour.objects.filter(buscket__buyer=user) 
        for tour in tours:
            total_persons = Buscket.objects.filter(tour=tour, date=request.POST['date']).aggregate(
                total=Sum('person_quantity')
            )['total']

            if total_persons:
                tour.place_quantity -= total_persons
                tour.save()

        Buscket.objects.filter(buyer=user).delete()
    except stripe.error.StripeError as e:

        # Handle error
        return render(request, 'failed.html', {'message': str(e)})

    return render(request, 'success.html')

