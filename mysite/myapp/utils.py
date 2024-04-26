from django.contrib.auth.mixins import AccessMixin
from myapp.models import Buscket, Tour

class GetTourTypeMixin(AccessMixin):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['private_tours'] = Tour.objects.filter(tour_type=1)
        context['group_tours'] = Tour.objects.filter(tour_type=2)
        context['tour_type_praha'] = Tour.objects.filter(tour_type_kind=1)
        context['tour_type_czech'] = Tour.objects.filter(tour_type_kind=2)
        context['tour_type_europe'] = Tour.objects.filter(tour_type_kind=3)
        return context
        
class GetBuscketMixin(AccessMixin):
    
    def get_queryset(self):
        user = self.request.user
        queryset = Buscket.objects.filter(buyer=user)
        return queryset
   

      
    