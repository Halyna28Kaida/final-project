
from datetime import datetime
from django.http import HttpRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView, CreateView
from myapp.models import Order, Tour, Buscket
from myapp.utils import GetTourTypeMixin
from myapp.forms import BuscketCreateForm, OrderCreateForm
from django.conf import settings
import stripe
from django.db.models import Sum

from users.models import TuristUserNew



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
    




    def get_min_day_value(self):
        return datetime.today().strftime("%Y-%m-%d")

    def form_valid(self, form):
        tour_instance = Tour.objects.get(pk=self.kwargs['tour_pk'])
        if not self.request.user.is_authenticated:
            return redirect(reverse('users:login'))
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
        context = super().get_context_data(**kwargs)
        tour = Tour.objects.get(pk=self.kwargs['tour_pk'])
    
        context.update({
            'available_places': tour.available_places(),
            'form': self.get_form(),
            'tour_name': tour.name,
            'tour_type': tour.tour_type,
            'tour_pk': tour.pk,

            'min_day_value': self.get_min_day_value() 
        })
        return context
    

    

class BuscketListView(ListView):
    model = Buscket
    template_name = 'buscket.html'
    context_object_name = "buscket"
    extra_context = {'create_form': OrderCreateForm}

    def get_queryset(self):
        user = self.request.user
        queryset = Buscket.objects.filter(buyer=user)
        return queryset
    

class BuscketDeleteView(View):

    def get(self,request, pk):
        obj = Buscket.objects.get(pk=pk)
        obj.delete()
        return redirect('myapp:buscket')




stripe.api_key = settings.STRIPE_SECRET_KEY


def payment(request):
    user = request.user
    context = {'stripe_public_key': settings.STRIPE_PUBLISHABLE_KEY, 
               'amount': Buscket.objects.filter(buyer=user).total_summ()}
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
            buscket = Buscket.objects.get(buyer=user, tour=tour)
            total_persons = Buscket.objects.filter(tour=tour, buyer=user).aggregate(
                total=Sum('person_quantity')
            )['total']

            if total_persons:
                tour.place_quantity -= total_persons
                tour.save()

            order = Order.objects.create(buyer=user, email=user.email, amount=buscket.get_summ(), tour=tour,
                                         date=buscket.date, time=buscket.time, 
                                         person_quantity=buscket.person_quantity)

            buscket.delete()

    except stripe.error.StripeError as e:

        return render(request, 'failed.html', {'message': str(e)})

    return render(request, 'success.html', {'total_summ': total_summ})


class OrderListView(ListView):
    model = Order
    template_name = 'profile.html'
    context_object_name = "order"

    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(buyer=user)
        return queryset
    
