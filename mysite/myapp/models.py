from django.db import models
from users.models import TuristUserNew


TOUR_TYPE_CHOICE = (
    (1, ("ИНДИВИДУАЛЬНЫЕ ЭКСКУРСИИ")),
    (2, ("ГРУППОВЫЕ ЭКСКУРСИИ")),
)

TOUR_TYPE_KIND_CHOICES = (
    (1, ("ЭКСКУРСИИ ПО ПРАГЕ")),
    (2, ("ЭКСКУРСИИ ПО ЧЕХИИ")),
    (3, ("ЭКСКУРСИИ ПО ЕВРОПЕ")),
)


class Tour(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    duration = models.DecimalField(max_digits=10, decimal_places=1, default=0)
    beginning = models.TimeField()
    meeting_place = models.CharField(max_length=300, blank=True, null=True)
    image = models.ImageField(default=True, upload_to="images")
    tour_type = models.IntegerField(choices=TOUR_TYPE_CHOICE, default=1)
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=True)
    sunday = models.BooleanField(default=True)
    adult_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tour_type_kind = models.IntegerField(choices=TOUR_TYPE_KIND_CHOICES, default=1)
    place_quantity = models.PositiveIntegerField(blank=True, default=1, choices=[(i, i) for i in range(1, 50)])

    def __str__(self) -> str:
        return str(self.name)
    
    def available_places(self):
        total_orders = Buscket.objects.filter(tour=self).count()
        available_places = self.place_quantity - total_orders
        return available_places
    
class BuscketQuarySet(models.QuerySet):
    def total_summ(self):
        return sum(obj.get_summ() for obj in self)
    
    def total_quantity(self):
        return sum(obj.person_quantity for obj in self)
    
    

class Buscket(models.Model):
    date = models.DateField()
    time = models.TimeField(default=None)
    buyer = models.ForeignKey(TuristUserNew, on_delete=models.CASCADE)
    prepayment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    person_quantity = models.PositiveIntegerField( blank=True)
    tour = models.ForeignKey(Tour, blank=True, null=True, on_delete=models.CASCADE)
    

    def get_summ(self):
        return self.tour.adult_price * self.person_quantity
    
    objects = BuscketQuarySet.as_manager()


    


class Order(models.Model):
    buyer = models.ForeignKey(TuristUserNew, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None, verbose_name='Пользователь')
    phone_number = models.CharField(max_length=20, null=True, verbose_name='Номер телефона')
    email = models.CharField(max_length=50, null=True, verbose_name='E-mail')
    is_paid = models.CharField(default=False, verbose_name='Оплачено')

    class Meta:
        db_table: str = 'order'
        verbose_name: str = 'Заказ'
        verbose_name_plural: str = 'Заказы'

    def __str__(self):
        return f'Заказ № {self.pk} | Покупатель {self.buyer.first_name} {self.buyer.last_name}'


class Review(models.Model):
    text = models.TextField()
    user = models.ForeignKey(TuristUserNew, blank=True, null=True, on_delete=models.CASCADE)

